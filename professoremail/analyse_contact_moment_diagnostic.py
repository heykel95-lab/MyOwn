#!/usr/bin/env python3
"""Audit the first-plot Contact Establishment wrench bookkeeping."""

import argparse
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figure_style import (  # noqa: E402
    apply_style,
    shared_legend,
    thin,
    REFERENCE_GREY,
    SERIES_BLACK,
    SERIES_RED,
    SERIES_BLUE,
)
import matplotlib.pyplot as plt  # noqa: E402


CONTACT_ESTABLISHMENT_PHASE = 2


def read_csv(path):
    with open(path, newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit(f"{path} has no header row")
        data = {name: [] for name in reader.fieldnames}
        for row in reader:
            for name in reader.fieldnames:
                data[name].append(float(row[name]) if row[name] else np.nan)
    return {name: np.asarray(values) for name, values in data.items()}


def read_params(directory):
    values = {}
    for name in sorted(os.listdir(directory)):
        if not name.endswith(".conf"):
            continue
        with open(os.path.join(directory, name)) as handle:
            for raw in handle:
                line = raw.split("#", 1)[0].strip()
                if "=" not in line:
                    continue
                key, value = line.split("=", 1)
                values[key.strip()] = value.strip()
    return values


def value(params, key):
    if key not in params:
        raise SystemExit(f"effective parameters have no {key}")
    return float(params[key])


def vector(data, prefix):
    names = [f"{prefix}_{axis}" for axis in "xyz"]
    missing = [name for name in names if name not in data]
    if missing:
        raise SystemExit(f"controller log has no {', '.join(missing)}")
    return np.column_stack([data[name] for name in names])


def find_log(run_dir):
    for path in (
        os.path.join(run_dir, "logs", "surface_grinding_controller_log.csv"),
        os.path.join(run_dir, "surface_grinding_controller_log.csv"),
    ):
        if os.path.isfile(path):
            return path
    raise SystemExit(f"no controller CSV found below {run_dir}")


def surface_axes(params):
    ax = math.radians(value(params, "surface_tilt_x_deg"))
    ay = math.radians(value(params, "surface_tilt_y_deg"))
    rx = np.array([
        [1.0, 0.0, 0.0],
        [0.0, math.cos(ax), -math.sin(ax)],
        [0.0, math.sin(ax), math.cos(ax)],
    ])
    ry = np.array([
        [math.cos(ay), 0.0, math.sin(ay)],
        [0.0, 1.0, 0.0],
        [-math.sin(ay), 0.0, math.cos(ay)],
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


def verify(run_dir, params):
    terminal = os.path.join(run_dir, "terminal.log")
    if not os.path.isfile(terminal):
        raise SystemExit(f"{run_dir} has no terminal.log")
    transcript = open(terminal, errors="replace").read().lower()
    if "selected mode: phase sequence" not in transcript:
        raise SystemExit("terminal.log does not confirm the automatic s sequence")
    expected = {
        "setup_Kp_surface_tangent1": 2000.0,
        "setup_Kp_surface_tangent2": 2000.0,
        "setup_Kp_surface_normal": 350.0,
        "setup_KR_tangent1": 5.0,
        "setup_KR_tangent2": 5.0,
        "setup_KR_normal": 50.0,
        "tool_target_offset_tangent1_deg": 10.0,
        "tool_target_offset_tangent2_deg": 0.0,
    }
    for key, target in expected.items():
        actual = value(params, key)
        if not math.isclose(actual, target, rel_tol=0.0, abs_tol=1e-9):
            raise SystemExit(f"{key}={actual}; expected {target}")
    for axis in ("tangent1", "tangent2", "normal"):
        current = f"compliance_lever_surface_{axis}"
        archived = f"r_tcp_from_compliance_center_surface_{axis}"
        key = current if current in params else archived
        if key not in params:
            raise SystemExit(f"effective parameters have no zero-lever key for {axis}")
        if not math.isclose(value(params, key), 0.0, rel_tol=0.0, abs_tol=1e-12):
            raise SystemExit(f"{key} is non-zero; the first plot requires r_c=0")


def selected_mean(values, mask):
    finite = values[mask & np.isfinite(values)]
    if finite.size == 0:
        raise SystemExit("a diagnostic window has no finite samples")
    return float(np.mean(finite))


def selected_sd(values, mask):
    finite = values[mask & np.isfinite(values)]
    return float(np.std(finite, ddof=1)) if finite.size > 1 else math.nan


def analyse(run_dir, endpoint_bounds):
    params_dir = os.path.join(run_dir, "params_effective")
    if not os.path.isdir(params_dir):
        raise SystemExit(f"{run_dir} has no params_effective directory")
    params = read_params(params_dir)
    verify(run_dir, params)
    data = read_csv(find_log(run_dir))
    keep = data["phase"] == CONTACT_ESTABLISHMENT_PHASE
    if not keep.any():
        raise SystemExit("controller log has no Contact Establishment samples")

    normal, tangent1 = surface_axes(params)
    time = data["time"][keep]
    time -= time[0]
    endpoint = (time >= endpoint_bounds[0]) & (time <= endpoint_bounds[1])
    if endpoint.sum() < 100:
        raise SystemExit("the endpoint window contains fewer than 100 samples")

    p_tcp = vector(data, "p_EE")[keep]
    p_bias = vector(data, "first_contact_tcp")[keep]
    force_o = vector(data, "external_force")[keep]
    force_bias = vector(data, "contact_force_bias")[keep]
    moment_o = vector(data, "external_moment")[keep]
    moment_bias = vector(data, "contact_moment_bias")[keep]
    force_command = vector(data, "f")[keep]
    moment_command = vector(data, "m")[keep]
    velocity = vector(data, "pdot")[keep]
    omega = vector(data, "omega")[keep]

    # O_F_ext_hat_K is the spatial wrench on K expressed in O.  Its moment
    # includes the base-to-K force lever.  K is coincident with the controller
    # TCP here, so shift the current and stored moments at their own TCP
    # positions before taking the clearance-referenced difference.
    moment_tcp_absolute = moment_o - np.cross(p_tcp, force_o)
    moment_tcp_at_clearance = moment_bias - np.cross(p_bias, force_bias)

    fn_command_absolute = force_command @ normal
    fn_estimate_absolute = force_o @ normal
    fn_estimate_change = (force_o - force_bias) @ normal
    mt1_command_absolute = moment_command @ tangent1
    mt1_estimate_absolute = moment_tcp_absolute @ tangent1
    mt1_estimate_change = (
        moment_tcp_absolute - moment_tcp_at_clearance) @ tangent1

    start = time <= min(0.05, time[-1])
    fn_command_change = fn_command_absolute - selected_mean(
        fn_command_absolute, start)
    mt1_command_change = mt1_command_absolute - selected_mean(
        mt1_command_absolute, start)

    result = {
        "time": time,
        "fn_command_absolute": fn_command_absolute,
        "fn_estimate_absolute": fn_estimate_absolute,
        "fn_command_change": fn_command_change,
        "fn_estimate_change": fn_estimate_change,
        "mt1_command_absolute": mt1_command_absolute,
        "mt1_estimate_absolute": mt1_estimate_absolute,
        "mt1_command_change": mt1_command_change,
        "mt1_estimate_change": mt1_estimate_change,
        "speed": np.linalg.norm(velocity, axis=1),
        "rate": np.linalg.norm(omega, axis=1),
        "endpoint": endpoint,
        "normal": normal,
        "tangent1": tangent1,
        "run_dir": os.path.abspath(run_dir),
    }
    result["summary"] = {
        "fn_command_absolute": selected_mean(fn_command_absolute, endpoint),
        "fn_estimate_absolute": selected_mean(fn_estimate_absolute, endpoint),
        "fn_command_change": selected_mean(fn_command_change, endpoint),
        "fn_estimate_change": selected_mean(fn_estimate_change, endpoint),
        "mt1_command_absolute": selected_mean(mt1_command_absolute, endpoint),
        "mt1_estimate_absolute": selected_mean(mt1_estimate_absolute, endpoint),
        "mt1_command_change": selected_mean(mt1_command_change, endpoint),
        "mt1_estimate_change": selected_mean(mt1_estimate_change, endpoint),
        "mt1_clearance_absolute": selected_mean(
            moment_tcp_at_clearance @ tangent1, endpoint),
        "mt1_estimate_absolute_sd": selected_sd(mt1_estimate_absolute, endpoint),
        "speed_mean": selected_mean(result["speed"], endpoint),
        "rate_mean": selected_mean(result["rate"], endpoint),
    }
    return result


def write_samples(path, result):
    fields = [
        "time_s", "Fn_command_absolute_N", "Fn_estimate_absolute_N",
        "Fn_command_clearance_change_N", "Fn_estimate_clearance_change_N",
        "Mt1_command_absolute_Nm", "Mt1_estimate_absolute_TCP_Nm",
        "Mt1_command_clearance_change_Nm", "Mt1_estimate_clearance_change_Nm",
        "tcp_speed_m_s", "angular_speed_rad_s",
    ]
    arrays = [
        result["time"], result["fn_command_absolute"],
        result["fn_estimate_absolute"], result["fn_command_change"],
        result["fn_estimate_change"], result["mt1_command_absolute"],
        result["mt1_estimate_absolute"], result["mt1_command_change"],
        result["mt1_estimate_change"], result["speed"], result["rate"],
    ]
    with open(path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(fields)
        writer.writerows(np.column_stack(arrays))


def write_summary(path, result):
    s = result["summary"]
    with open(path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["quantity", "endpoint_mean"])
        for key, value_ in s.items():
            writer.writerow([key, value_])


def write_report(path, result, endpoint_bounds):
    s = result["summary"]
    with open(path, "w") as handle:
        handle.write("CONTACT ESTABLISHMENT MOMENT DIAGNOSTIC\n\n")
        handle.write(f"run: {result['run_dir']}\n")
        handle.write(f"endpoint window: {endpoint_bounds[0]:g}--{endpoint_bounds[1]:g} s\n")
        handle.write("r_c: [0, 0, 0] m; virtual point-shift coupling is zero\n\n")
        handle.write("Normal force at the endpoint\n")
        handle.write(f"  command, absolute: {s['fn_command_absolute']:.3f} N\n")
        handle.write(f"  estimate, absolute: {s['fn_estimate_absolute']:.3f} N\n")
        handle.write(f"  command, clearance change: {s['fn_command_change']:.3f} N\n")
        handle.write(f"  estimate, clearance change: {s['fn_estimate_change']:.3f} N\n\n")
        handle.write("Moment about t1 at the endpoint\n")
        handle.write(f"  command, absolute: {s['mt1_command_absolute']:.3f} N m\n")
        handle.write(f"  estimate at TCP, absolute: {s['mt1_estimate_absolute']:.3f} N m\n")
        handle.write(f"  clearance estimate, absolute: {s['mt1_clearance_absolute']:.3f} N m\n")
        handle.write(f"  command, clearance change: {s['mt1_command_change']:.3f} N m\n")
        handle.write(f"  estimate, clearance change: {s['mt1_estimate_change']:.3f} N m\n\n")
        handle.write(f"mean endpoint TCP speed: {1000*s['speed_mean']:.4f} mm/s\n")
        handle.write(f"mean endpoint angular speed: {math.degrees(s['rate_mean']):.4f} deg/s\n\n")
        handle.write(
            "The absolute and clearance-referenced pairs are reported "
            "separately. The model-estimated moment is the total external "
            "interaction about the TCP; the log does not independently "
            "measure a pressure centre or contact couple.\n")


def write_plot(path, result, endpoint_bounds):
    apply_style()
    figure, axes = plt.subplots(3, 1, figsize=(6.15, 6.1), sharex=True)
    values = thin(
        result["time"], result["fn_command_change"],
        result["fn_estimate_change"], result["mt1_command_absolute"],
        result["mt1_estimate_absolute"], result["mt1_command_change"],
        result["mt1_estimate_change"],
    )
    time, fn_cmd, fn_est, mt_abs_cmd, mt_abs_est, mt_delta_cmd, mt_delta_est = values
    for axis in axes:
        axis.axvspan(*endpoint_bounds, color=REFERENCE_GREY,
                    alpha=0.13, linewidth=0)
    axes[0].plot(time, fn_cmd, color=SERIES_BLACK, label="Commanded change")
    axes[0].plot(time, fn_est, color=SERIES_RED, label="Model-estimated change")
    axes[0].set_ylabel("Normal Force Change,\n" r"$\Delta F_n$ [N]")
    axes[0].set_title("(a)", loc="left")
    axes[1].plot(time, mt_abs_cmd, color=SERIES_BLACK, label="Commanded absolute")
    axes[1].plot(time, mt_abs_est, color=SERIES_BLUE,
                 label="Model-estimated absolute at TCP")
    axes[1].set_ylabel("Absolute TCP Moment,\n" r"$M_{t_1}$ [N m]")
    axes[1].set_title("(b)", loc="left")
    axes[2].plot(time, mt_delta_cmd, color=SERIES_BLACK,
                 label="Commanded change")
    axes[2].plot(time, mt_delta_est, color=SERIES_RED,
                 label="Model-estimated change")
    axes[2].set_ylabel("Moment Change,\n" r"$\Delta M_{t_1}$ [N m]")
    axes[2].set_xlabel(r"Time, $t$ [s]")
    axes[2].set_title("(c)", loc="left")
    shared_legend(figure, axes, ncol=2, bottom=0.12)
    figure.savefig(path)
    plt.close(figure)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run", help="archived P2_t1_pos_p000 sequence trial")
    parser.add_argument("--endpoint-window", nargs=2, type=float,
                        default=(4.0, 5.0), metavar=("START", "END"))
    parser.add_argument("--out-dir", default=os.path.dirname(__file__))
    args = parser.parse_args()
    bounds = tuple(args.endpoint_window)
    result = analyse(args.run, bounds)
    os.makedirs(args.out_dir, exist_ok=True)
    outputs = {
        "plot": os.path.join(args.out_dir, "contact_moment_diagnostic.pdf"),
        "samples": os.path.join(args.out_dir, "contact_moment_diagnostic_samples.csv"),
        "summary": os.path.join(args.out_dir, "contact_moment_diagnostic_summary.csv"),
        "report": os.path.join(args.out_dir, "contact_moment_diagnostic_report.txt"),
    }
    write_plot(outputs["plot"], result, bounds)
    write_samples(outputs["samples"], result)
    write_summary(outputs["summary"], result)
    write_report(outputs["report"], result, bounds)
    for output in outputs.values():
        print(f"wrote {os.path.abspath(output)}")


if __name__ == "__main__":
    main()
