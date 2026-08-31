#!/usr/bin/env python3
"""Analyse t-mode quasi-static Fn and Mt1 consistency trials.

Each positional argument is an archive written by
Thesis_Final_Control/experiments/run.sh.  The archive must contain a controller
CSV, params_effective/, and a terminal.log that confirms setup-impedance hold.

The default timing matches the recorded r01 trial described in
t_mode_consistency_about.txt.  The script writes:

  t_mode_consistency.pdf          commanded, estimated and quasi-static values
  t_mode_consistency_summary.csv  one plateau result per run and component
  t_mode_consistency_results.tex  numerical section included by the email PDF
"""

import argparse
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figure_style import (apply_style, thin, SERIES_BLACK, SERIES_RED,  # noqa: E402
                          SERIES_BLUE, REFERENCE_GREY)
import matplotlib.pyplot as plt  # noqa: E402


POSE_HOLD_PHASE = 4


def read_csv(path):
    with open(path, newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit(f"{path} has no header row")
        columns = {name: [] for name in reader.fieldnames}
        for row in reader:
            for name in reader.fieldnames:
                value = row[name]
                columns[name].append(float(value) if value else np.nan)
    return {name: np.asarray(values) for name, values in columns.items()}


def read_params(directory):
    values = {}
    for root, _, files in os.walk(directory):
        for name in sorted(files):
            path = os.path.join(root, name)
            try:
                with open(path) as handle:
                    for raw in handle:
                        line = raw.split("#", 1)[0].strip()
                        if "=" not in line:
                            continue
                        key, value = line.split("=", 1)
                        key = key.strip()
                        if key in values and values[key] != value.strip():
                            raise SystemExit(
                                f"parameter {key} has conflicting values in "
                                f"{directory}")
                        values[key] = value.strip()
            except UnicodeDecodeError:
                continue
    return values


def value(params, key, cast=float):
    if key not in params:
        raise SystemExit(f"effective parameters have no {key}")
    return cast(params[key])


def find_log(run_dir):
    candidates = [
        os.path.join(run_dir, "logs", "surface_grinding_controller_log.csv"),
        os.path.join(run_dir, "surface_grinding_controller_log.csv"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            return path
    raise SystemExit(f"no controller CSV found below {run_dir}")


def vector(log, prefix):
    names = [f"{prefix}_{axis}" for axis in "xyz"]
    missing = [name for name in names if name not in log]
    if missing:
        raise SystemExit(f"log has no {', '.join(missing)}")
    return np.column_stack([log[name] for name in names])


def surface_axes(params):
    tilt_x = math.radians(value(params, "surface_tilt_x_deg"))
    tilt_y = math.radians(value(params, "surface_tilt_y_deg"))
    rx = np.array([
        [1.0, 0.0, 0.0],
        [0.0, math.cos(tilt_x), -math.sin(tilt_x)],
        [0.0, math.sin(tilt_x), math.cos(tilt_x)],
    ])
    ry = np.array([
        [math.cos(tilt_y), 0.0, math.sin(tilt_y)],
        [0.0, 1.0, 0.0],
        [-math.sin(tilt_y), 0.0, math.cos(tilt_y)],
    ])
    normal = ry @ rx @ np.array([0.0, 0.0, 1.0])
    normal /= np.linalg.norm(normal)
    hint = np.array([
        value(params, "surface_tangent1_hint_base_x"),
        value(params, "surface_tangent1_hint_base_y"),
        value(params, "surface_tangent1_hint_base_z"),
    ])
    tangent1 = hint - normal * normal.dot(hint)
    tangent1 /= np.linalg.norm(tangent1)
    return normal, tangent1


def in_window(time, bounds, label):
    selected = (time >= bounds[0]) & (time <= bounds[1])
    if selected.sum() < 100:
        raise SystemExit(
            f"{label} window {bounds[0]:g}--{bounds[1]:g} s contains only "
            f"{selected.sum()} samples")
    return selected


def mean_sd(values):
    finite = values[np.isfinite(values)]
    if len(finite) < 2:
        raise SystemExit("a result window has fewer than two finite samples")
    return float(np.mean(finite)), float(np.std(finite, ddof=1))


def verify_run(run_dir, params):
    terminal = os.path.join(run_dir, "terminal.log")
    if not os.path.isfile(terminal):
        raise SystemExit(f"{run_dir} has no terminal.log; t mode is unverified")
    with open(terminal, errors="replace") as handle:
        transcript = handle.read().lower()
    if "setup-impedance hold" not in transcript and "setup impedance hold" not in transcript:
        raise SystemExit(f"{run_dir}/terminal.log does not confirm t mode")

    required = {
        "setup_translation_surface_frame": 1,
        "setup_auto_damping": 0,
        "use_virtual_compliance_center": 0,
        "nullspace_mode": 0,
    }
    for key, expected in required.items():
        actual = int(value(params, key))
        if actual != expected:
            raise SystemExit(
                f"{run_dir}: {key}={actual}, expected {expected} for this test")


def analyse_run(run_dir, windows):
    params_dir = os.path.join(run_dir, "params_effective")
    if not os.path.isdir(params_dir):
        raise SystemExit(f"{run_dir} has no params_effective directory")
    params = read_params(params_dir)
    verify_run(run_dir, params)
    normal, tangent1 = surface_axes(params)
    log = read_csv(find_log(run_dir))

    if "phase" not in log:
        raise SystemExit("controller log has no phase column")
    keep = log["phase"] == POSE_HOLD_PHASE
    if not keep.any():
        raise SystemExit(f"{run_dir} contains no pose-hold samples")

    time = log["time"][keep]
    time = time - time[0]
    baseline = in_window(time, windows["baseline"], "force baseline")
    rotation_baseline = in_window(
        time, windows["moment_baseline"], "moment baseline")
    force_plateau = in_window(time, windows["force"], "force plateau")
    moment_plateau = in_window(time, windows["moment"], "moment plateau")

    e_n_absolute = vector(log, "e_p")[keep] @ normal
    e_t1_absolute = vector(log, "e_R")[keep] @ tangent1
    fn_commanded_absolute = vector(log, "f")[keep] @ normal
    mt1_commanded_absolute = vector(log, "m")[keep] @ tangent1
    p_ee = vector(log, "p_EE")[keep]
    external_force = vector(log, "external_force")[keep]
    external_moment = vector(log, "external_moment")[keep]

    # A pre-touch mean is more stable than the single initial sample stored in
    # force_after_contact/moment_after_contact.  Transform every raw spatial
    # wrench from the base origin to its instantaneous TCP before subtracting
    # the unloaded baseline.  This is exact when the TCP position changes.
    force_baseline = np.mean(external_force[baseline], axis=0)
    force_delta = external_force - force_baseline
    moment_tcp_raw = external_moment - np.cross(p_ee, external_force)
    moment_delta_tcp = moment_tcp_raw - np.mean(
        moment_tcp_raw[baseline], axis=0)
    fn_estimated = force_delta @ normal
    mt1_estimated_absolute = moment_delta_tcp @ tangent1

    # The operator retained the normal displacement while applying the t1
    # rotation.  Resolve rotation as an increment from the immediately
    # preceding loaded baseline.  This removes the pre-existing contact moment
    # without hiding the variation measured during the rotational hold.
    e_n = e_n_absolute - np.mean(e_n_absolute[baseline])
    e_t1 = e_t1_absolute - np.mean(e_t1_absolute[rotation_baseline])
    fn_commanded = (
        fn_commanded_absolute - np.mean(fn_commanded_absolute[baseline]))
    mt1_commanded = (
        mt1_commanded_absolute
        - np.mean(mt1_commanded_absolute[rotation_baseline]))
    mt1_estimated = (
        mt1_estimated_absolute
        - np.mean(mt1_estimated_absolute[rotation_baseline]))

    kp_n = value(params, "setup_Kp_surface_normal")
    kr_t1 = value(params, "setup_KR_tangent1")
    dp_n = value(params, "setup_Dp_surface_normal")
    dr_t1 = value(params, "setup_DR_tangent1")
    fn_spring = kp_n * e_n
    mt1_spring = kr_t1 * e_t1

    def component(name, kind, mask, noise_mask, error, command, estimate,
                  spring, stiffness, baseline_values, absolute_floor):
        achieved = mean_sd(error[mask])
        commanded = mean_sd(command[mask])
        estimated = mean_sd(estimate[mask])
        predicted = mean_sd(spring[mask])
        noise = float(np.std(baseline_values[noise_mask], ddof=1))
        law_delta = commanded[0] - predicted[0]
        estimate_delta = estimated[0] - commanded[0]
        signal_to_noise = abs(commanded[0]) / noise if noise > 0.0 else math.inf
        law_tolerance = max(0.05 * abs(commanded[0]), absolute_floor)
        agreement_tolerance = max(0.20 * abs(commanded[0]), 3.0 * noise)
        law_ok = abs(law_delta) <= law_tolerance
        resolved = signal_to_noise >= 3.0
        agreement_ok = abs(estimate_delta) <= agreement_tolerance
        if law_ok and resolved and agreement_ok:
            status = "consistent"
        elif not resolved:
            status = "inconclusive (low signal)"
        else:
            status = "not consistent"
        return {
            "name": name,
            "kind": kind,
            "achieved_mean": achieved[0],
            "achieved_sd": achieved[1],
            "stiffness": stiffness,
            "predicted_mean": predicted[0],
            "predicted_sd": predicted[1],
            "commanded_mean": commanded[0],
            "commanded_sd": commanded[1],
            "estimated_mean": estimated[0],
            "estimated_sd": estimated[1],
            "law_delta": law_delta,
            "estimate_delta": estimate_delta,
            "baseline_noise": noise,
            "signal_to_noise": signal_to_noise,
            "agreement_tolerance": agreement_tolerance,
            "status": status,
        }

    rows = [
        component("Fn", "force", force_plateau, baseline, e_n, fn_commanded,
                  fn_estimated, fn_spring, kp_n, fn_estimated, 0.05),
        component("Mt1", "moment", moment_plateau, rotation_baseline, e_t1,
                  mt1_commanded, mt1_estimated, mt1_spring, kr_t1,
                  mt1_estimated, 0.01),
    ]
    return {
        "run_dir": os.path.abspath(run_dir),
        "label": os.path.basename(os.path.normpath(run_dir)),
        "time": time,
        "fn_commanded": fn_commanded,
        "fn_estimated": fn_estimated,
        "fn_spring": fn_spring,
        "mt1_commanded": mt1_commanded,
        "mt1_estimated": mt1_estimated,
        "mt1_spring": mt1_spring,
        "kp_n": kp_n,
        "dp_n": dp_n,
        "kr_t1": kr_t1,
        "dr_t1": dr_t1,
        "rows": rows,
    }


def aggregate(runs, component_name):
    rows = [next(row for row in run["rows"] if row["name"] == component_name)
            for run in runs]
    result = dict(rows[0])
    for key in ("achieved_mean", "predicted_mean", "commanded_mean",
                "estimated_mean", "law_delta", "estimate_delta",
                "baseline_noise", "signal_to_noise"):
        values = np.asarray([row[key] for row in rows])
        result[key] = float(np.mean(values))
        result[f"{key}_between_sd"] = (
            float(np.std(values, ddof=1)) if len(values) > 1 else math.nan)
    statuses = [row["status"] for row in rows]
    result["status"] = (
        "consistent" if all(s == "consistent" for s in statuses)
        else "inconclusive" if any(s.startswith("inconclusive") for s in statuses)
        else "not consistent")
    return result


def plot_results(runs, windows, output):
    stop = min(run["time"][-1] for run in runs)
    common = np.linspace(0.0, stop, min(1200, max(400, int(stop * 50))))

    def stacked(key):
        return np.vstack([
            np.interp(common, run["time"], run[key]) for run in runs
        ])

    apply_style()
    plt.rcParams["axes.formatter.use_mathtext"] = True
    figure, axes = plt.subplots(2, 1, figsize=(6.15, 4.65), sharex=True)
    specifications = [
        (axes[0], "fn_commanded", "fn_estimated", "fn_spring",
         "Normal Force Increment,\n" r"$\Delta F_n$ [N]", windows["force"]),
        (axes[1], "mt1_commanded", "mt1_estimated", "mt1_spring",
         "Moment Increment About $t_1$,\n"
         r"$\Delta M_{t_1}$ [N m]", windows["moment"]),
    ]
    for axis, cmd_key, est_key, spring_key, ylabel, plateau in specifications:
        cmd = stacked(cmd_key)
        est = stacked(est_key)
        spring = stacked(spring_key)
        t, cmd_mean, est_mean, spring_mean = thin(
            common, cmd.mean(axis=0), est.mean(axis=0), spring.mean(axis=0))
        axis.axvspan(plateau[0], plateau[1], color=REFERENCE_GREY,
                    alpha=0.13, linewidth=0)
        axis.plot(t, cmd_mean, color=SERIES_BLACK,
                  label="Commanded increment")
        axis.plot(t, est_mean, color=SERIES_RED,
                  label="Model-estimated increment")
        axis.plot(t, spring_mean, color=SERIES_BLUE,
                  label="Quasi-static spring increment")
        axis.set_ylabel(ylabel)
        low = float(np.nanmin([cmd_mean, est_mean, spring_mean]))
        high = float(np.nanmax([cmd_mean, est_mean, spring_mean]))
        span = max(high - low, 0.1)
        axis.set_ylim(low - 0.10 * span, high + 0.55 * span)
        axis.legend(loc="upper right")
    axes[-1].set_xlabel(r"Time, $t$ [s]")
    figure.tight_layout()
    figure.savefig(output)
    plt.close(figure)


def fmt_pm(mean, sd, decimals):
    if math.isnan(sd):
        return f"{mean:.{decimals}f}"
    return f"{mean:.{decimals}f} \\ensuremath{{\\pm}} {sd:.{decimals}f}"


def latex_status(status):
    if status.startswith("inconclusive"):
        status = "inconclusive"
    return status.replace("_", r"\_")


def write_tex(path, runs, fn, mt1, windows):
    repeat_text = (
        "one trial" if len(runs) == 1
        else f"{len(runs)} repeated trials")

    with open(path, "w") as handle:
        handle.write("% Generated by analyse_t_mode_consistency.py.\n")
        handle.write(f"The comparison contains {repeat_text}. ")
        handle.write(
            "The grey band in the upper $F_n$ panel marks "
            f"{windows['force'][0]:g}--{windows['force'][1]:g}\\,s, during "
            "which the normal displacement was held stationary.  The grey "
            "band in the lower $M_{t_1}$ panel marks "
            f"{windows['moment'][0]:g}--{windows['moment'][1]:g}\\,s, during "
            "which the rotation about $t_1$ was held stationary.  Only the "
            "samples inside the corresponding grey band are used for each "
            "plateau mean and consistency check.\n\n")
        handle.write("\\begin{center}\n")
        handle.write("  \\includegraphics[width=0.92\\textwidth]{")
        handle.write("professoremail/t_mode_consistency.pdf}\n")
        handle.write("\\end{center}\n\n")
        handle.write("\\begin{center}\n")
        handle.write("\\scriptsize\n")
        handle.write("\\begin{tabular}{lrrrrl}\n")
        handle.write("\\hline\n")
        handle.write(
            "Component & Achieved & Quasi-static & Commanded & Estimated & "
            "Status \\\\\n")
        handle.write("\\hline\n")
        for result, scale, unit, decimals in (
                (fn, 1000.0, "mm", 2),
                (mt1, 180.0 / math.pi, "deg", 3)):
            if len(runs) == 1:
                achieved_sd = math.nan
                command_sd = math.nan
                estimate_sd = math.nan
                spring_sd = math.nan
            else:
                achieved_sd = result.get("achieved_mean_between_sd", math.nan)
                command_sd = result.get("commanded_mean_between_sd", math.nan)
                estimate_sd = result.get("estimated_mean_between_sd", math.nan)
                spring_sd = result.get("predicted_mean_between_sd", math.nan)
            handle.write(
                f"${result['name'].replace('Mt1', 'M_{t_1}').replace('Fn', 'F_n')}$ & "
                f"{fmt_pm(scale * result['achieved_mean'], scale * achieved_sd, decimals)} {unit} & "
                f"{fmt_pm(result['predicted_mean'], spring_sd, 3)} & "
                f"{fmt_pm(result['commanded_mean'], command_sd, 3)} & "
                f"{fmt_pm(result['estimated_mean'], estimate_sd, 3)} & "
                f"{latex_status(result['status'])} \\\\\n")
        handle.write("\\hline\n")
        handle.write("\\end{tabular}\n")
        handle.write("\\end{center}\n\n")
        if len(runs) > 1:
            handle.write(
                "\n"
                "Values after $\\pm$ are sample standard deviations across "
                "the trial-level means.\n")

        fn_law_pct = 100.0 * abs(fn["law_delta"]) / abs(fn["commanded_mean"])
        fn_est_pct = (
            100.0 * abs(fn["estimate_delta"]) / abs(fn["commanded_mean"]))
        mt_law_pct = (
            100.0 * abs(mt1["law_delta"]) / abs(mt1["commanded_mean"]))
        mt_est_pct = (
            100.0 * abs(mt1["estimate_delta"]) / abs(mt1["commanded_mean"]))
        handle.write("\n\n")
        handle.write(
            "\\textbf{Normal force $F_n$.}\n"
            "\\[\n"
            f"F_{{n,\\mathrm{{qs}}}}=K_{{p,n}}\\mathbin{{\\cdot}}e_n\n="
            f"1000\\mathbin{{\\cdot}}({fn['achieved_mean']:.6f})="
            f"{fn['predicted_mean']:.3f}\\,\\mathrm{{N}}.\n"
            "\\]\n"
            f"The commanded mean is ${fn['commanded_mean']:.3f}"
            "\\,\\mathrm{N}$.  The quasi-static difference is "
            f"${abs(fn['law_delta']):.3f}\\,\\mathrm{{N}}$ "
            f"({fn_law_pct:.2f}\\%).  The model-estimated mean is "
            f"${fn['estimated_mean']:.3f}\\,\\mathrm{{N}}$, a difference of "
            f"${abs(fn['estimate_delta']):.3f}\\,\\mathrm{{N}}$ "
            f"({fn_est_pct:.2f}\\%).\n\n")
        handle.write(
            "\\textbf{Moment $M_{t_1}$.}\n"
            "\\[\n"
            f"M_{{t_1,\\mathrm{{qs}}}}=K_{{R,t_1}}\\mathbin{{\\cdot}}e_{{R,t_1}}\n="
            f"15\\mathbin{{\\cdot}}({180.0 / math.pi * mt1['achieved_mean']:.3f}"
            f"\\pi/180)={mt1['predicted_mean']:.3f}"
            "\\,\\mathrm{N\\,m}.\n"
            "\\]\n"
            f"The commanded mean is ${mt1['commanded_mean']:.3f}"
            "\\,\\mathrm{N\\,m}$.  The quasi-static difference is "
            f"${abs(mt1['law_delta']):.3f}\\,\\mathrm{{N\\,m}}$ "
            f"({mt_law_pct:.2f}\\%).  The model-estimated mean is "
            f"${mt1['estimated_mean']:.3f}\\,\\mathrm{{N\\,m}}$, a "
            "difference of "
            f"${abs(mt1['estimate_delta']):.3f}\\,\\mathrm{{N\\,m}}$ "
            f"({mt_est_pct:.2f}\\%).\n")


def write_csv(path, runs):
    fields = [
        "run", "component", "achieved_mean", "achieved_sd", "stiffness",
        "predicted_mean", "commanded_mean", "commanded_sd",
        "estimated_mean", "estimated_sd", "command_law_difference",
        "estimated_minus_commanded", "baseline_noise", "signal_to_noise",
        "agreement_tolerance", "status",
    ]
    with open(path, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for run in runs:
            for row in run["rows"]:
                writer.writerow({
                    "run": run["run_dir"],
                    "component": row["name"],
                    "achieved_mean": row["achieved_mean"],
                    "achieved_sd": row["achieved_sd"],
                    "stiffness": row["stiffness"],
                    "predicted_mean": row["predicted_mean"],
                    "commanded_mean": row["commanded_mean"],
                    "commanded_sd": row["commanded_sd"],
                    "estimated_mean": row["estimated_mean"],
                    "estimated_sd": row["estimated_sd"],
                    "command_law_difference": row["law_delta"],
                    "estimated_minus_commanded": row["estimate_delta"],
                    "baseline_noise": row["baseline_noise"],
                    "signal_to_noise": row["signal_to_noise"],
                    "agreement_tolerance": row["agreement_tolerance"],
                    "status": row["status"],
                })


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("runs", nargs="+", help="archived t-mode run directories")
    parser.add_argument("--baseline-window", nargs=2, type=float,
                        default=(0.5, 2.5), metavar=("START", "END"))
    parser.add_argument("--force-window", nargs=2, type=float,
                        default=(9.5, 13.5), metavar=("START", "END"))
    parser.add_argument("--moment-baseline-window", nargs=2, type=float,
                        default=(18.0, 20.0), metavar=("START", "END"))
    parser.add_argument("--moment-window", nargs=2, type=float,
                        default=(24.8, 25.9), metavar=("START", "END"))
    parser.add_argument("--out-dir", default=os.path.dirname(__file__))
    args = parser.parse_args()

    windows = {
        "baseline": tuple(args.baseline_window),
        "force": tuple(args.force_window),
        "moment_baseline": tuple(args.moment_baseline_window),
        "moment": tuple(args.moment_window),
    }
    runs = [analyse_run(path, windows) for path in args.runs]
    first = runs[0]
    for run in runs[1:]:
        for key in ("kp_n", "dp_n", "kr_t1", "dr_t1"):
            if not math.isclose(run[key], first[key], rel_tol=0.0, abs_tol=1e-12):
                raise SystemExit(f"repetitions use different {key} values")

    os.makedirs(args.out_dir, exist_ok=True)
    plot_path = os.path.join(args.out_dir, "t_mode_consistency.pdf")
    csv_path = os.path.join(args.out_dir, "t_mode_consistency_summary.csv")
    tex_path = os.path.join(args.out_dir, "t_mode_consistency_results.tex")
    plot_results(runs, windows, plot_path)
    write_csv(csv_path, runs)
    fn = aggregate(runs, "Fn")
    mt1 = aggregate(runs, "Mt1")
    write_tex(tex_path, runs, fn, mt1, windows)

    print(f"wrote {os.path.abspath(plot_path)}")
    print(f"wrote {os.path.abspath(csv_path)}")
    print(f"wrote {os.path.abspath(tex_path)}")
    print(f"Fn: {fn['status']}; Mt1: {mt1['status']}")


if __name__ == "__main__":
    main()
