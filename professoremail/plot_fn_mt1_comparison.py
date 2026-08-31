#!/usr/bin/env python3
"""Plot absolute commanded and model-estimated Contact Establishment wrench.

The commanded wrench is resolved on the configured surface normal and first
tangent.  Libfranka's O_F_ext_hat_K is the spatial wrench on stiffness frame K
expressed in the base frame.  Its base-frame moment includes the base-to-K
force lever.  With K coincident with the controller TCP, subtracting
p_TCP x f gives the local TCP moment.  Absolute and clearance-referenced
estimator values are both saved to CSV, but only the absolute estimate is
compared with the absolute command in the figure.
"""

import argparse
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figure_style import (apply_style, shared_legend, thin,  # noqa: E402
                          SERIES_BLACK, SERIES_RED, REFERENCE_GREY)
import matplotlib.pyplot as plt  # noqa: E402


CONTACT_ESTABLISHMENT_PHASE = 2


def read_log(path):
    """Return a controller log as float arrays keyed by column name."""
    with open(path, newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit(f"{path} has no header row")
        columns = {name: [] for name in reader.fieldnames}
        for row in reader:
            for name in reader.fieldnames:
                columns[name].append(float(row[name]) if row[name] else np.nan)
    return {name: np.asarray(values) for name, values in columns.items()}


def read_config(path):
    """Read key-value pairs from one effective controller configuration."""
    values = {}
    with open(path) as handle:
        for raw in handle:
            line = raw.split("#", 1)[0].strip()
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    return values


def surface_axes(config):
    """Build the configured surface normal and orthonormal first tangent."""
    tilt_x = math.radians(float(config["surface_tilt_x_deg"]))
    tilt_y = math.radians(float(config["surface_tilt_y_deg"]))
    rotation_x = np.array([
        [1.0, 0.0, 0.0],
        [0.0, math.cos(tilt_x), -math.sin(tilt_x)],
        [0.0, math.sin(tilt_x), math.cos(tilt_x)],
    ])
    rotation_y = np.array([
        [math.cos(tilt_y), 0.0, math.sin(tilt_y)],
        [0.0, 1.0, 0.0],
        [-math.sin(tilt_y), 0.0, math.cos(tilt_y)],
    ])
    normal = rotation_y @ rotation_x @ np.array([0.0, 0.0, 1.0])
    normal /= np.linalg.norm(normal)

    hint = np.array([
        float(config["surface_tangent1_hint_base_x"]),
        float(config["surface_tangent1_hint_base_y"]),
        float(config["surface_tangent1_hint_base_z"]),
    ])
    tangent1 = hint - normal * normal.dot(hint)
    tangent1 /= np.linalg.norm(tangent1)
    return normal, tangent1


def vector(log, prefix):
    names = [f"{prefix}_{axis}" for axis in "xyz"]
    missing = [name for name in names if name not in log]
    if missing:
        raise SystemExit(f"log has no {', '.join(missing)}")
    return np.column_stack([log[name] for name in names])


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("log", help="surface_grinding_controller log CSV")
    parser.add_argument("surface_config", help="effective surface.conf")
    parser.add_argument("--out-dir", default=os.path.dirname(__file__))
    args = parser.parse_args()

    log = read_log(args.log)
    config = read_config(args.surface_config)
    normal, tangent1 = surface_axes(config)

    phase_keep = log["phase"] == CONTACT_ESTABLISHMENT_PHASE
    if not phase_keep.any():
        raise SystemExit("log contains no contact-establishment samples")
    phase_indices = np.flatnonzero(phase_keep)
    time = log["time"][phase_indices]
    time -= time[0]
    active = time <= 5.0
    sample_indices = phase_indices[active]
    time = time[active]

    commanded_fn = vector(log, "f")[sample_indices] @ normal
    external_force = vector(log, "external_force")[sample_indices]
    force_bias = vector(log, "contact_force_bias")[sample_indices]
    estimated_fn_absolute = external_force @ normal
    estimated_fn_change = (external_force - force_bias) @ normal
    commanded_mt1 = vector(log, "m")[sample_indices] @ tangent1

    # O_F_ext_hat_K is the spatial wrench on K expressed in O.  Its moment
    # includes p_K x f.  The controller uses K coincident with its TCP, hence
    # p_K = p_TCP.  Shift the current and stored clearance wrenches separately
    # because their TCP positions differ.
    external_moment = vector(log, "external_moment")[sample_indices]
    moment_bias = vector(log, "contact_moment_bias")[sample_indices]
    tcp_position = vector(log, "p_EE")[sample_indices]
    bias_tcp_position = vector(log, "first_contact_tcp")[sample_indices]
    moment_tcp = external_moment - np.cross(tcp_position, external_force)
    moment_tcp_bias = moment_bias - np.cross(bias_tcp_position, force_bias)
    estimated_mt1_absolute = moment_tcp @ tangent1
    estimated_mt1_change = (moment_tcp - moment_tcp_bias) @ tangent1

    os.makedirs(args.out_dir, exist_ok=True)
    stem = os.path.join(args.out_dir, "fn_mt1_commanded_vs_estimated")
    with open(f"{stem}.csv", "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "time", "Fn_commanded_absolute",
            "Fn_model_estimated_absolute",
            "Fn_model_estimated_clearance_change",
            "Mt1_commanded_absolute",
            "Mt1_model_estimated_absolute_TCP",
            "Mt1_model_estimated_clearance_change",
        ])
        writer.writerows(np.column_stack([
            time, commanded_fn, estimated_fn_absolute, estimated_fn_change,
            commanded_mt1, estimated_mt1_absolute, estimated_mt1_change,
        ]))

    apply_style()
    plt.rcParams["axes.formatter.use_mathtext"] = True
    figure, axes = plt.subplots(2, 1, figsize=(6.15, 4.30), sharex=True)
    t, fn_cmd, fn_est, mt1_cmd, mt1_est = thin(
        time, commanded_fn, estimated_fn_absolute,
        commanded_mt1, estimated_mt1_absolute)

    for axis in axes:
        axis.axvspan(4.0, 5.0, color=REFERENCE_GREY, alpha=0.13, linewidth=0)
    axes[0].plot(t, fn_cmd, color=SERIES_BLACK, label="Commanded")
    axes[0].plot(t, fn_est, color=SERIES_RED, label="Model-estimated")
    axes[0].set_ylabel("Normal Force,\n" r"$F_n$ [N]")
    axes[0].set_title("(a)", loc="left")
    axes[1].plot(t, mt1_cmd, color=SERIES_BLACK, label="Commanded")
    axes[1].plot(t, mt1_est, color=SERIES_RED,
                 label="Model-estimated at TCP")
    axes[1].set_ylabel("Tangent-1 Moment,\n" r"$M_{t_1}$ [N m]")
    axes[1].set_title("(b)", loc="left")
    axes[1].set_xlabel(r"Time, $t$ [s]")
    shared_legend(figure, axes, ncol=2, bottom=0.15)
    figure.savefig(f"{stem}.pdf")
    plt.close(figure)
    print(f"wrote {os.path.abspath(stem)}.pdf")
    print(f"wrote {os.path.abspath(stem)}.csv ({len(time)} rows)")


if __name__ == "__main__":
    main()
