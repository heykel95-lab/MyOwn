#!/usr/bin/env python3
"""Summarise and plot the final automatic Case-F null-space experiment.

The point force is generated inside the controller, so this analysis uses the
logged disturbance scale rather than a cue time to define the driven interval.
It writes both the small derived table used by the thesis and a vector PDF.

The final campaign uses the clean 20 N, +200 mm records acquired after the
disturbance and inter-trial hardware gates had been fixed.
"""

import argparse
import csv
import glob
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_figures  # noqa: E402
from make_figures import (  # noqa: E402
    SERIES_BLACK,
    SERIES_RED,
    SERIES_BLUE,
    SERIES_YELLOW,
    save,
)


HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.normpath(os.path.join(HERE, ".."))
# The two repositories shelve this script at different depths. MyController
# keeps it at experiments/analysis/, so the data sits in the parent directory;
# Thesis_Final_Control keeps it at analysis/, with the data under experiments/.
# Resolve whichever layout the copy is sitting in rather than assuming one.
EXP = (os.path.join(_PARENT, "experiments")
       if os.path.isdir(os.path.join(_PARENT, "experiments"))
       else _PARENT)
RESULTS = os.path.join(EXP, "results")
SUMMARY = os.path.join(EXP, "derived", "MAIN_NS_automatic_summary.csv")

CONDITIONS = (
    ("MAIN_NS7_baseline_20N_200mm", "damping", 0.0),
    ("MAIN_NS7_damping_2p0_20N_200mm", "damping", 2.0),
    ("MAIN_NS8_ksigma_1p5_20N_200mm", "sigma", 1.5),
    ("MAIN_NS8_ksigma_2p0_20N_200mm", "sigma", 2.0),
)


def _float(row, name):
    return float(row[name])


def read_run(run_dir):
    path = os.path.join(run_dir, "surface_grinding_controller_log.csv")
    with open(path, newline="") as stream:
        rows = list(csv.DictReader(stream))

    names = (
        "time", "nullspace_speed", "sigma_current", "disturbance_scale",
        "disturbance_torque_scale", "disturbance_force_base_x",
        "disturbance_force_base_y", "disturbance_force_base_z",
        "tau_disturbance_1", "tau_disturbance_2", "tau_disturbance_3",
        "tau_disturbance_4", "tau_disturbance_5", "tau_disturbance_6",
        "tau_disturbance_7", "e_p_x", "e_p_y", "e_p_z",
        "nullspace_dq_1", "nullspace_dq_2", "nullspace_dq_3",
        "nullspace_dq_4", "nullspace_dq_5", "nullspace_dq_6",
        "nullspace_dq_7",
    )
    data = {name: np.array([_float(row, name) for row in rows])
            for name in names}

    time = data["time"]
    scale = data["disturbance_scale"]
    active = scale > 1.0e-3
    if not np.any(active):
        raise ValueError(f"no automatic disturbance in {path}")

    first, last = np.flatnonzero(active)[[0, -1]]
    driven = slice(first, last + 1)
    t_driven = time[driven]
    speed = np.abs(data["nullspace_speed"][driven])
    dt = np.diff(t_driven)
    increments = 0.5 * (speed[:-1] + speed[1:]) * dt
    cumulative = np.concatenate(([0.0], np.cumsum(increments)))

    # Same integrand as the cumulative motion, without the magnitude: the
    # trapezoidal integral of the projected joint velocity is the net
    # displacement of the redundant configuration over the driven interval.
    # It is a 7-vector; because the null space is one-dimensional at full row
    # rank it lies along +-v_7, so a single reference direction resolves every
    # run onto one signed axis (see net_displacements below).
    dq_null = np.column_stack([data[f"nullspace_dq_{joint}"][driven]
                               for joint in range(1, 8)])
    net_vector = np.sum(0.5 * (dq_null[:-1] + dq_null[1:]) * dt[:, None],
                        axis=0)

    force = np.sqrt(sum(data[f"disturbance_force_base_{axis}"] ** 2
                        for axis in "xyz"))
    tau = np.sqrt(sum(data[f"tau_disturbance_{joint}"] ** 2
                      for joint in range(1, 8)))
    task_error_mm = 1000.0 * np.sqrt(sum(data[f"e_p_{axis}"] ** 2
                                        for axis in "xyz"))

    return {
        "run_dir": run_dir,
        "relative_time": t_driven - t_driven[0],
        "cumulative_excursion": cumulative,
        "excursion_rad": float(cumulative[-1]),
        "net_vector_rad": net_vector,
        "sigma_gain": float(data["sigma_current"][-1]
                            - data["sigma_current"][0]),
        "task_error_peak_mm": float(np.max(task_error_mm)),
        "force_peak_N": float(np.max(force)),
        "disturbance_tau_peak_Nm": float(np.max(tau)),
        "torque_scale_min": float(np.min(
            data["disturbance_torque_scale"][active])),
        "nullspace_speed_peak_rad_s": float(np.max(
            np.abs(data["nullspace_speed"]))),
    }


def sample_sd(values):
    return float(np.std(values, ddof=1)) if len(values) > 1 else np.nan


def net_displacements(groups, reference_id=CONDITIONS[0][0]):
    """Resolve every run's net redundant displacement onto one signed axis.

    The redundant direction v_7 is not in the log: the controller only records
    it while the conditioning term is selecting a sign, so it is absent from
    the runs without null-space torque. It is recovered from the data instead.
    Every net displacement lies in the one-dimensional null space, so the
    reference condition -- the one in which the disturbance moves the redundant
    configuration furthest -- fixes that axis, and its own mean is the largest
    signal available for the purpose. Each run is then projected onto it, which
    keeps the sign of a displacement rather than its magnitude alone.
    """
    reference = [group for group in groups if group["run_id"] == reference_id]
    if not reference:
        raise ValueError(f"reference condition {reference_id} not loaded")
    mean_vector = np.mean([run["net_vector_rad"]
                           for run in reference[0]["runs"]], axis=0)
    axis = mean_vector / np.linalg.norm(mean_vector)
    for group in groups:
        for run in group["runs"]:
            run["net_displacement_rad"] = float(axis @ run["net_vector_rad"])
    return axis


def load_conditions():
    groups = []
    for run_id, study, gain in CONDITIONS:
        paths = sorted(glob.glob(os.path.join(RESULTS, run_id, "r*")))
        runs = [read_run(path) for path in paths]
        if runs:
            groups.append({"run_id": run_id, "study": study,
                           "gain": gain, "runs": runs})
    return groups


def write_summary(groups):
    os.makedirs(os.path.dirname(SUMMARY), exist_ok=True)
    fields = (
        "run_id", "study", "gain", "n", "provenance_status",
        "excursion_mean_rad", "excursion_sd_rad",
        "net_displacement_mean_rad", "net_displacement_sd_rad",
        "sigma_gain_mean",
        "sigma_gain_sd", "task_error_peak_mean_mm",
        "task_error_peak_sd_mm", "task_error_peak_max_mm",
        "force_peak_mean_N", "disturbance_tau_peak_mean_Nm",
        "torque_scale_min", "nullspace_speed_peak_mean_rad_s",
    )
    with open(SUMMARY, "w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields,
                                lineterminator="\n")
        writer.writeheader()
        for group in groups:
            runs = group["runs"]
            values = lambda key: np.array([run[key] for run in runs])
            excursion = values("excursion_rad")
            net = values("net_displacement_rad")
            sigma = values("sigma_gain")
            task = values("task_error_peak_mm")
            writer.writerow({
                "run_id": group["run_id"],
                "study": group["study"],
                "gain": f"{group['gain']:g}",
                "n": len(runs),
                "provenance_status": "clean-committed",
                "excursion_mean_rad": f"{np.mean(excursion):.9g}",
                "excursion_sd_rad": (f"{sample_sd(excursion):.9g}"
                                      if len(runs) > 1 else ""),
                "net_displacement_mean_rad": f"{np.mean(net):.9g}",
                "net_displacement_sd_rad": (f"{sample_sd(net):.9g}"
                                            if len(runs) > 1 else ""),
                "sigma_gain_mean": f"{np.mean(sigma):.9g}",
                "sigma_gain_sd": (f"{sample_sd(sigma):.9g}"
                                  if len(runs) > 1 else ""),
                "task_error_peak_mean_mm": f"{np.mean(task):.9g}",
                "task_error_peak_sd_mm": (f"{sample_sd(task):.9g}"
                                          if len(runs) > 1 else ""),
                "task_error_peak_max_mm": f"{np.max(task):.9g}",
                "force_peak_mean_N": f"{np.mean(values('force_peak_N')):.9g}",
                "disturbance_tau_peak_mean_Nm":
                    f"{np.mean(values('disturbance_tau_peak_Nm')):.9g}",
                "torque_scale_min": f"{np.min(values('torque_scale_min')):.9g}",
                "nullspace_speed_peak_mean_rad_s":
                    f"{np.mean(values('nullspace_speed_peak_rad_s')):.9g}",
            })
    print(f"  wrote {os.path.relpath(SUMMARY, EXP)}")


def damping_panel(ax, groups):
    colours = (SERIES_BLACK, SERIES_RED, SERIES_BLUE, SERIES_YELLOW)
    damping = [group for group in groups if group["study"] == "damping"]
    common_t = np.linspace(0.0, 4.0, 161)
    for group, colour in zip(damping, colours):
        curves = np.vstack([
            np.interp(common_t, run["relative_time"],
                      run["cumulative_excursion"])
            for run in group["runs"]
        ]) * (180.0 / np.pi)
        mean = np.mean(curves, axis=0)
        sd = (np.std(curves, axis=0, ddof=1)
              if curves.shape[0] > 1 else np.zeros_like(mean))
        # Legend: descriptive condition, then symbol = value.
        gain = group["gain"]
        if gain == 0.0:
            label = (r"No Null-Space Damping, "
                     r"$d_{\mathrm{null}}=0$")
        else:
            label = (r"Projected Damping, "
                     rf"$d_{{\mathrm{{null}}}}={gain:g}"
                     r"\,\mathrm{N\,m\,s/rad}$")
        ax.plot(common_t, mean, color=colour, marker="o", markevery=40,
                linewidth=1.25,
                markerfacecolor="white", markeredgecolor=colour,
                markeredgewidth=1.1, label=label)
        ax.fill_between(common_t, mean - sd, mean + sd, color=colour,
                        alpha=0.10, linewidth=0)
    ax.set_xlabel(r"Time, $t$ [s]")
    ax.set_ylabel(
        "Cumulative Projected\n"
        r"Null-Space Motion, $E_N$ [$^\circ$]"
    )
    ax.text(0.99, 0.03, "(a)", transform=ax.transAxes,
            ha="right", va="bottom")
    ax.margins(y=0.12)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.30), ncol=2,
              frameon=False, fontsize=8.5, handlelength=1.7,
              columnspacing=2.0, borderaxespad=0.0)
    return ax.get_legend_handles_labels()


def sigma_panel(ax, groups):
    sigma_groups = [group for group in groups if group["study"] == "sigma"]
    gains = np.array([group["gain"] for group in sigma_groups])
    sigma_means = np.array([
        np.mean([run["sigma_gain"] for run in group["runs"]])
        for group in sigma_groups
    ])
    sigma_sd = np.array([
        sample_sd([run["sigma_gain"] for run in group["runs"]])
        for group in sigma_groups
    ])
    task_means = np.array([
        np.mean([run["task_error_peak_mm"] for run in group["runs"]])
        for group in sigma_groups
    ])
    task_sd = np.array([
        sample_sd([run["task_error_peak_mm"] for run in group["runs"]])
        for group in sigma_groups
    ])

    repeated = np.array([len(group["runs"]) > 1 for group in sigma_groups])
    screening = ~repeated
    sigma_handle = ax.errorbar(
        gains[repeated], sigma_means[repeated],
        yerr=sigma_sd[repeated], color=SERIES_BLACK, marker="o",
        markerfacecolor="white", markeredgecolor=SERIES_BLACK,
        markeredgewidth=1.1, linewidth=1.25, elinewidth=1.0,
        capthick=1.0, capsize=3,
        label=r"Singular-Value Change, "
              r"$\Delta\sigma_{\min}$")
    ax.plot(gains[screening], sigma_means[screening], color=SERIES_BLACK,
            marker="D", markerfacecolor="white", markeredgewidth=1.1,
            linestyle="none")
    ax.axhline(0.0, color="0.45", linewidth=1.0)
    ax.set_xlabel(r"Conditioning Torque Magnitude, $k_\sigma$ [N m]")
    ax.set_ylabel(
        "Change in Minimum Singular\n"
        r"Value, $\Delta\sigma_{\min}$ [-]")
    ax.set_xticks(gains)
    ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0),
                        useMathText=True)
    ax.text(0.01, 0.82, "(b)", transform=ax.transAxes,
            ha="left", va="top")
    if np.any(screening):
        ax.annotate("Single-run setting\n($n=1$)",
                    xy=(gains[screening][0], sigma_means[screening][0]),
                    xytext=(gains[screening][0] - 0.2,
                            sigma_means[screening][0]),
                    fontsize=7, ha="right",
                    arrowprops={"arrowstyle": "-", "color": "0.35",
                                "linewidth": 0.8})

    task_ax = ax.twinx()
    task_handle = task_ax.errorbar(
        gains[repeated], task_means[repeated],
        yerr=task_sd[repeated], color=SERIES_RED, marker="s",
        markerfacecolor="white", markeredgecolor=SERIES_RED,
        markeredgewidth=1.1, linewidth=1.25, elinewidth=1.0,
        capthick=1.0, capsize=3,
        label=r"Maximum Cartesian Position Error, $\|e_p\|_{\max}$")
    task_ax.plot(gains[screening], task_means[screening], color=SERIES_RED,
                 marker="D", markerfacecolor="white", markeredgewidth=1.1,
                 linestyle="none")
    criterion_handle = task_ax.axhline(
        2.0, color="0.45", linewidth=1.0,
        label=r"Position-Error Limit, $\|e_p\|_{\max}=2\,\mathrm{mm}$")
    task_ax.set_ylabel(
        "Maximum Cartesian Position\n"
        r"Error, $\|e_p\|_{\max}$ [mm]",
        color=SERIES_RED,
    )
    task_ax.tick_params(axis="y", colors=SERIES_RED)
    task_ax.grid(False)

    handles = [sigma_handle, task_handle, criterion_handle]
    labels = [r"Singular-Value Change, $\Delta\sigma_{\min}$",
              r"Maximum Cartesian Position Error, $\|e_p\|_{\max}$",
              r"Position-Error Limit, $\|e_p\|_{\max}=2\,\mathrm{mm}$"]
    ax.legend(handles, labels, loc="upper center",
              bbox_to_anchor=(0.5, -0.26), ncol=2, frameon=False,
              fontsize=8.5, handlelength=1.7, columnspacing=2.0,
              borderaxespad=0.0)
    return handles, labels


NET_LABELS = (
    "No Null-Space\nTorque",
    "Projected\nDamping",
    "Conditioning\n$k_\\sigma=1.5$",
    "Conditioning\n$k_\\sigma=2.0$",
)


def _net_value_label(value):
    """Print a net displacement at the precision Section 5.2 reports.

    Three decimals throughout, matching the E_N values printed beside these in
    the same section. In radians the four values needed two formats, because
    0.0003 rounds to zero at three decimals; in degrees the smallest is 0.006
    and one format covers the range. The sign takes the typographic minus the
    tick labels use, so a printed value and an axis tick agree.
    """
    return f"{value:.3f}".replace("-", "\N{MINUS SIGN}")


def net_displacement_panel(ax, groups):
    """Draw the net displacement of all four settings.

    Plotted in degrees, as panel (a) is: the quantity is an angle in radians,
    and the two panels are read against one another, so one unit is used for
    both.

    The suppression by more than two orders of magnitude is the strongest
    result of the conditioning experiment and the other two panels do not carry
    it: panel (a) plots the cumulative motion, which is a path length, and
    panel (b) plots the singular value and the task error. The bars are printed
    with their values, as the Case-A bars are, because at a scale set by
    7.517 degrees the two conditioning bars are the height of the axis line,
    and a reader has no way to tell a suppressed value from a missing one.
    """
    order = {run_id: rank for rank, (run_id, _, _) in enumerate(CONDITIONS)}
    ordered = sorted(groups, key=lambda group: order[group["run_id"]])
    means, sds = [], []
    for group in ordered:
        values = np.degrees([run["net_displacement_rad"]
                             for run in group["runs"]])
        means.append(float(np.mean(values)))
        sds.append(sample_sd(values))
    positions = np.arange(len(ordered))

    ax.bar(positions, means, width=0.55, color=SERIES_BLUE,
           edgecolor="#1a1a1a", linewidth=0.8,
           yerr=sds, capsize=3, error_kw={"elinewidth": 1.0,
                                          "capthick": 1.0,
                                          "ecolor": "#1a1a1a"})
    ax.axhline(0.0, color="0.45", linewidth=1.0)
    ax.set_xticks(positions)
    ax.set_xticklabels(NET_LABELS[:len(ordered)])
    ax.set_ylabel(
        "Net Displacement,\n"
        r"$\Delta\eta$ [$^\circ$]")
    ax.margins(y=0.28)
    for position, mean, sd in zip(positions, means, sds):
        offset = sd if np.isfinite(sd) else 0.0
        ax.annotate(_net_value_label(mean),
                    xy=(position, mean + offset),
                    xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7.5)
    ax.text(0.99, 0.92, "(c)", transform=ax.transAxes,
            ha="right", va="top")


def make_figure(groups):
    # Stacked rather than side by side: every panel carries a long descriptive
    # axis label, and at text width two columns left the data area too small
    # to read the curves against. The third panel is shorter than the other
    # two: it holds four bars and needs no room for a legend.
    fig, axes = plt.subplots(3, 1, figsize=(5.9, 8.4),
                             gridspec_kw={"height_ratios": [1.0, 1.0, 0.8],
                                          "hspace": 0.75})
    damping_handles, damping_labels = damping_panel(axes[0], groups)
    sigma_handles, sigma_labels = sigma_panel(axes[1], groups)
    net_displacement_panel(axes[2], groups)
    handles = damping_handles + sigma_handles
    labels = damping_labels + sigma_labels
    # Each panel carries its own legend, so no figure-level legend is drawn and
    # no strip is reserved at the foot of the figure for one.
    fig._thesis_legend_bottom = 0.0
    fig.align_ylabels(axes)
    return save(fig, "MAIN_NS_nullspace_automatic.pdf")


def main():
    global RESULTS, SUMMARY

    # The thesis checkout holds the script but not the 6 GB of run records, so
    # the data directory is given on the command line when the two are not
    # side by side. Without it the layout resolution above still applies.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", default=RESULTS,
                        help="directory holding the MAIN_NS* run directories")
    parser.add_argument("--out-dir", default=make_figures.FIGURES,
                        help="directory the PDF is written to")
    parser.add_argument("--summary", default=SUMMARY,
                        help="path of the derived summary CSV")
    args = parser.parse_args()

    RESULTS = args.results
    SUMMARY = args.summary
    make_figures.FIGURES = args.out_dir

    groups = load_conditions()
    if len(groups) != len(CONDITIONS):
        found = {group["run_id"] for group in groups}
        missing = [run_id for run_id, _, _ in CONDITIONS if run_id not in found]
        raise SystemExit("missing Case-F data: " + ", ".join(missing))
    axis = net_displacements(groups)
    print("  redundant axis from "
          f"{CONDITIONS[0][0]}: {np.array2string(axis, precision=3)}")
    write_summary(groups)
    make_figure(groups)
    return 0


if __name__ == "__main__":
    sys.exit(main())
