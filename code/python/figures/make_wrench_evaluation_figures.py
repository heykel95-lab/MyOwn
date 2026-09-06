#!/usr/bin/env python3
"""Generate the three Section 5.1 controller-wrench figures.

Two evaluations are kept apart, and so are their figures.

  MAIN_WR_contact_wrench.pdf     commanded against model-estimated wrench
                                 during one Contact Establishment trial
  MAIN_WR_force_plausibility.pdf quasi-static check of the translational
                                 impedance, normal-force increment
  MAIN_WR_moment_plausibility.pdf quasi-static check of the rotational
                                 impedance, moment increment about t1

The first reads the plotted pairs written by
professoremail/plot_fn_mt1_comparison.py, which resolved the commanded wrench on
the configured surface axes and transported the libfranka estimate to the TCP.
The other two call analyse_t_mode_consistency.analyse_run, so the increments,
the baseline subtraction and the spring prediction are computed by the script
that produced the reported values rather than re-derived here. That analysis
needs a run directory shaped like the campaign archive, so this generator
assembles one from the archived parameters and the controller log committed
beside the thesis.

The combined 0-35 s plot that analysis writes is deliberately not reused: the
two tests are separated here, and each figure carries a local time reference
starting at its own test interval.
"""

import argparse
import csv
import os
import shutil
import sys
import tempfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
THESIS_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PROFESSOR_EMAIL = os.path.join(THESIS_ROOT, "professoremail")

sys.path.insert(0, HERE)
sys.path.insert(0, PROFESSOR_EMAIL)

from figure_style import (apply_style, thin,  # noqa: E402
                          SERIES_BLACK, SERIES_BLUE, SERIES_RED,
                          REFERENCE_GREY)
import matplotlib.pyplot as plt  # noqa: E402


def panel_legend(figure, axes, reserve):
    '''Place one legend directly under the last panel.

    figure_style.shared_legend anchors at the foot of the figure, which leaves
    a visible band of white between the x label and the entries once the figure
    is only a few centimetres tall. plot_coc_case.py measures the panel instead
    and puts the legend against it, so the entries read as part of the last
    panel; the same is done here, after the layout is fixed so that the
    geometry the legend is measured against is final.
    '''
    handles, labels = [], []
    for axis in axes:
        for handle, label in zip(*axis.get_legend_handles_labels()):
            if label not in labels:
                handles.append(handle)
                labels.append(label)
    figure.tight_layout(rect=(0, reserve, 1, 1))
    panel = axes[-1].get_position()
    # Two entries spread across the panel width read as two separate labels
    # rather than as one legend, so only a three-entry row is expanded.
    expand = "expand" if len(handles) > 2 else None
    figure.legend(handles, labels, loc="lower center" if expand is None
                  else "lower left", ncol=len(handles),
                  bbox_to_anchor=(panel.x0, 0.012, panel.width, 0.06),
                  mode=expand, frameon=False, fontsize=8.0,
                  handlelength=1.6, handletextpad=0.5, borderaxespad=0.0)

# The windows the reported t-mode result used, from
# professoremail/T_MODE_MANUAL_D_REPEAT_PROTOCOL.md.
WINDOWS = {
    "baseline": (0.5, 3.0),
    "force": (8.0, 13.0),
    "moment_baseline": (13.0, 17.0),
    "moment": (28.5, 31.0),
}

# Each test is drawn from the start of its own baseline to the end of its own
# stationary interval, and its time axis is reset to that start.
FORCE_TEST_START = 0.0
FORCE_TEST_END = 13.5
MOMENT_TEST_START = 13.0

DEFAULT_TMODE_RUN = os.path.abspath(os.path.join(
    THESIS_ROOT, "..", "Thesis_Final_Control", "experiments", "results",
    "T_MODE_MANUAL_D_REPEAT", "r01"))
DEFAULT_TMODE_LOG = os.path.join(
    PROFESSOR_EMAIL, "T_MODE_MANUAL_D_REPEAT_r01_controller_log.csv")
DEFAULT_WRENCH_CSV = os.path.join(
    PROFESSOR_EMAIL, "fn_mt1_commanded_vs_estimated.csv")


def read_columns(path):
    """Return a CSV as float arrays keyed by column name."""
    with open(path, newline="") as handle:
        reader = csv.DictReader(handle)
        columns = {name: [] for name in reader.fieldnames}
        for row in reader:
            for name in reader.fieldnames:
                columns[name].append(float(row[name]))
    return {name: np.asarray(values) for name, values in columns.items()}


def contact_wrench_figure(csv_path, out_path):
    """Commanded against model-estimated wrench during Contact Establishment."""
    data = read_columns(csv_path)
    t, fn_cmd, fn_est, mt1_cmd, mt1_est = thin(
        data["time"],
        data["Fn_commanded_absolute"],
        data["Fn_model_estimated_absolute"],
        data["Mt1_commanded_absolute"],
        data["Mt1_model_estimated_absolute_TCP"])

    apply_style()
    plt.rcParams["axes.formatter.use_mathtext"] = True
    figure, axes = plt.subplots(2, 1, figsize=(6.15, 4.30), sharex=True)
    for axis in axes:
        axis.axvspan(4.0, 5.0, color=REFERENCE_GREY, alpha=0.13, linewidth=0)
    axes[0].plot(t, fn_cmd, color=SERIES_BLACK, label="Commanded")
    axes[0].plot(t, fn_est, color=SERIES_RED, label="Model-estimated")
    axes[0].set_ylabel("Normal Force,\n" r"$F_n$ [N]")
    axes[0].set_title("(a)", loc="left")
    axes[1].plot(t, mt1_cmd, color=SERIES_BLACK, label="Commanded")
    axes[1].plot(t, mt1_est, color=SERIES_RED, label="Model-estimated")
    axes[1].set_ylabel("TCP Moment About $t_1$,\n" r"$M_{t_1}$ [N m]")
    axes[1].set_title("(b)", loc="left")
    axes[1].set_xlabel(r"Time, $t$ [s]")
    panel_legend(figure, axes, reserve=0.08)
    figure.savefig(out_path)
    plt.close(figure)
    return out_path


def assemble_run_directory(archive_run, log_csv, workspace):
    """Rebuild a runnable archive directory from the committed log."""
    run_dir = os.path.join(workspace, "r01")
    os.makedirs(os.path.join(run_dir, "logs"), exist_ok=True)
    shutil.copytree(os.path.join(archive_run, "params_effective"),
                    os.path.join(run_dir, "params_effective"))
    for name in ("terminal.log", "about.txt", "overlay.txt"):
        source = os.path.join(archive_run, name)
        if os.path.isfile(source):
            shutil.copy(source, os.path.join(run_dir, name))
    shutil.copy(log_csv, os.path.join(
        run_dir, "logs", "surface_grinding_controller_log.csv"))
    return run_dir


def plausibility_figure(run, keys, ylabel, xlabel, span, start, end, out_path):
    """One quasi-static comparison on a local time axis."""
    time = run["time"]
    window = (time >= start) & (time <= end)
    local = time[window] - start
    commanded, estimated, spring = (run[key][window] for key in keys)
    t, cmd, est, qs = thin(local, commanded, estimated, spring)

    apply_style()
    plt.rcParams["axes.formatter.use_mathtext"] = True
    figure, axis = plt.subplots(1, 1, figsize=(6.15, 2.55))
    axis.axvspan(span[0] - start, span[1] - start,
                 color=REFERENCE_GREY, alpha=0.13, linewidth=0)
    axis.plot(t, cmd, color=SERIES_BLACK, label="Commanded increment")
    axis.plot(t, est, color=SERIES_RED, label="Model-estimated increment")
    axis.plot(t, qs, color=SERIES_BLUE, label="Quasi-static spring prediction")
    axis.set_ylabel(ylabel)
    axis.set_xlabel(xlabel)
    axis.set_xlim(0.0, float(local[-1]))
    panel_legend(figure, [axis], reserve=0.14)
    figure.savefig(out_path)
    plt.close(figure)
    return out_path


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--wrench-csv", default=DEFAULT_WRENCH_CSV)
    parser.add_argument("--tmode-run", default=DEFAULT_TMODE_RUN)
    parser.add_argument("--tmode-log", default=DEFAULT_TMODE_LOG)
    parser.add_argument("--out-dir",
                        default=os.path.join(THESIS_ROOT, "figures"))
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    written = [contact_wrench_figure(
        args.wrench_csv,
        os.path.join(args.out_dir, "MAIN_WR_contact_wrench.pdf"))]

    from analyse_t_mode_consistency import analyse_run  # noqa: E402

    workspace = tempfile.mkdtemp(prefix="tmode_")
    try:
        run_dir = assemble_run_directory(
            args.tmode_run, args.tmode_log, workspace)
        run = analyse_run(run_dir, WINDOWS)
    finally:
        shutil.rmtree(workspace, ignore_errors=True)

    written.append(plausibility_figure(
        run,
        ("fn_commanded", "fn_estimated", "fn_spring"),
        "Normal Force Increment,\n" r"$\Delta F_n$ [N]",
        r"Time After Force-Test Start, $t_F$ [s]",
        WINDOWS["force"], FORCE_TEST_START, FORCE_TEST_END,
        os.path.join(args.out_dir, "MAIN_WR_force_plausibility.pdf")))

    written.append(plausibility_figure(
        run,
        ("mt1_commanded", "mt1_estimated", "mt1_spring"),
        "Moment Increment About $t_1$,\n" r"$\Delta M_{t_1}$ [N m]",
        r"Time After Rotation-Test Start, $t_M$ [s]",
        WINDOWS["moment"], MOMENT_TEST_START, float(run["time"][-1]),
        os.path.join(args.out_dir, "MAIN_WR_moment_plausibility.pdf")))

    for row in run["rows"]:
        print(f"{row['name']}: quasi-static {row['predicted_mean']:.3f}, "
              f"commanded {row['commanded_mean']:.3f}, "
              f"model-estimated {row['estimated_mean']:.3f}, "
              f"{row['status']}")
    for path in written:
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
