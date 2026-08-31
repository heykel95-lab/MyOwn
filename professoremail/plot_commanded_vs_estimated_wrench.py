#!/usr/bin/env python3
"""Compare the commanded Cartesian wrench with the model-estimated one.

  python3 plot_commanded_vs_estimated_wrench.py LOG.csv [--out-dir DIR]
                                                        [--bias-corrected]
                                                        [--phase N]

Two wrenches are logged at every 1 kHz tick and they are not the same kind of
quantity:

  commanded   f_x..z, m_x..z. What the impedance law asked the arm to apply at
              the TCP, before joint torque limiting.

  estimated   external_force_x..z, external_moment_x..z. libfranka's
              O_F_ext_hat_K, the external wrench inferred from the dynamic
              model and the joint torques, expressed in the base orientation
              and referenced to stiffness frame K. It is a model estimate, not
              a force-sensor reading.

Sign: libfranka defines positive estimated components as forces and moments
applied by the robot to the environment. Magnitudes are drawn in this general
comparison, while the per-component CSV retains the signed values.

--bias-corrected swaps the estimate for force_after_contact / moment_after
_contact, which are the same signals with the values captured at the clearance
transition already subtracted. Use it when the interest is the contact wrench
rather than the total, since the estimate carries the tool weight otherwise.

Writes two files next to the log (or into --out-dir):

  commanded_vs_estimated_wrench.pdf   two panels, force then moment
  commanded_vs_estimated_wrench.csv   exactly the rows and columns plotted
"""

import argparse
import csv
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figure_style import (apply_style, shared_legend, thin,  # noqa: E402
                          SERIES_BLACK, SERIES_RED)
import matplotlib.pyplot as plt  # noqa: E402

apply_style()
# The tick formatter otherwise warns that cmr10 has no upright minus.
plt.rcParams["axes.formatter.use_mathtext"] = True

SETUP_PHASE = 2  # ControlPhase::kSetup

# Wrench ordering is force followed by moment, as the thesis states it.
COMMANDED = ("f", "m")
ESTIMATED = ("external_force", "external_moment")
ESTIMATED_BIAS_CORRECTED = ("force_after_contact", "moment_after_contact")


def load(path):
    """Return the log as a dict of float arrays, keyed by column name."""
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


def vector(log, prefix):
    """Return the three base-frame components of one logged vector."""
    missing = [f"{prefix}_{axis}" for axis in "xyz" if f"{prefix}_{axis}"
               not in log]
    if missing:
        raise SystemExit(f"log has no {', '.join(missing)}; this is not a "
                         "current-schema surface_grinding_controller log")
    return np.column_stack([log[f"{prefix}_{axis}"] for axis in "xyz"])


def magnitude(vectors):
    return np.linalg.norm(vectors, axis=1)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("log", help="a controller log CSV")
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--bias-corrected", action="store_true",
                        help="use the clearance-referenced external wrench")
    parser.add_argument("--phase", type=int, default=None,
                        help=f"keep one phase only, e.g. {SETUP_PHASE} for set-up")
    args = parser.parse_args()

    log = load(args.log)
    estimated_names = (ESTIMATED_BIAS_CORRECTED if args.bias_corrected
                       else ESTIMATED)

    time = log["time"]
    keep = np.ones(len(time), dtype=bool)
    if args.phase is not None:
        if "phase" not in log:
            raise SystemExit("log has no phase column, so --phase cannot apply")
        keep = log["phase"] == args.phase
        if not keep.any():
            raise SystemExit(f"no rows with phase == {args.phase}")

    time = time[keep]
    time = time - time[0]

    series = []
    for commanded_name, estimated_name in zip(COMMANDED, estimated_names):
        commanded = vector(log, commanded_name)[keep]
        estimated = vector(log, estimated_name)[keep]
        series.append((commanded_name, estimated_name, commanded, estimated))

    out_dir = args.out_dir or os.path.dirname(os.path.abspath(args.log))
    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.join(out_dir, "commanded_vs_estimated_wrench")

    # The CSV carries the raw components as well as the plotted magnitudes, so
    # the sign convention stays checkable against the figure.
    header = ["time"]
    table = [time]
    for commanded_name, estimated_name, commanded, estimated in series:
        for index, axis in enumerate("xyz"):
            header.append(f"{commanded_name}_{axis}")
            table.append(commanded[:, index])
        for index, axis in enumerate("xyz"):
            header.append(f"{estimated_name}_{axis}")
            table.append(estimated[:, index])
        header.append(f"{commanded_name}_norm")
        table.append(magnitude(commanded))
        header.append(f"{estimated_name}_norm")
        table.append(magnitude(estimated))
    with open(f"{stem}.csv", "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(np.column_stack(table))

    figure, axes = plt.subplots(2, 1, figsize=(5.8, 4.4), sharex=True)
    labels = ("commanded force", "commanded moment")
    estimated_labels = ("estimated external force",
                        "estimated external moment")
    units = ("Force [N]", "Moment [N m]")
    for axis, (_, _, commanded, estimated), label, estimated_label, unit in zip(
            axes, series, labels, estimated_labels, units):
        t, c, e = thin(time, magnitude(commanded), magnitude(estimated))
        axis.plot(t, c, color=SERIES_BLACK, label=label)
        axis.plot(t, e, color=SERIES_RED, label=estimated_label)
        axis.set_ylabel(unit)
    axes[-1].set_xlabel("Time [s]")
    shared_legend(figure, axes, ncol=2)
    figure.savefig(f"{stem}.pdf")
    plt.close(figure)

    print(f"wrote {stem}.pdf")
    print(f"wrote {stem}.csv  ({len(time)} rows)")


if __name__ == "__main__":
    main()
