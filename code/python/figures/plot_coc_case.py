#!/usr/bin/env python3
"""Draw one centre-of-compliance case in the fixed three-panel order.

  python3 analysis/plot_coc_case.py TRIAL=DETAIL [...] --axis t1 --out NAME

Every case is read the same way, top to bottom:

  1  contact-establishment rotation   the signed current-to-reference rotation
                       over contact establishment about the investigated tangent.
  2  normal force      the controller-commanded press along n_s.
  3  alignment moment  the controller-commanded moment about the commanded
                       surface tangent.

The contact-establishment rotation is the same controller-response quantity used by every
case-comparison plot. It comes from the robot orientation error referenced at
the clearance transition and is resolved on the configured surface axes. It therefore has
no absolute flat-tool zero and is not affected by play between tool and
gripper.

The commanded wrench is used consistently for force and moment. The force is
the commanded Cartesian force resolved along the surface normal. The moment is
the commanded Cartesian moment at the TCP resolved about the selected tangent.
No model-estimated wrench is mixed into this controller-response comparison.

The normal force is negative while the tool presses. n_s points out of the
plate, so the commanded press runs along -n_s.

One shared legend identifies the compliance-centre position of each curve.
"""

import argparse
import csv
import glob
import os
import sys

import numpy as np
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract_metrics import surface_frame, read_params  # noqa: E402
from figure_style import (apply_style, reference_line,  # noqa: E402
                          thin, SERIES_COLOURS)

RESULTS = os.path.join(HERE, "..", "experiments", "results")

apply_style()

CONTACT_ESTABLISHMENT_STATE = 2

AXIS_COLUMN = {"t1": 0, "t2": 1, "n": 2}
AXIS_LABEL = {"t1": r"$t_1$", "t2": r"$t_2$", "n": r"$n$"}
# The axis rides in the subscript, so a panel names the component it carries
# rather than describing it: M_{t1} instead of "M_cmd about t1". A quantity
# without an index is a commanded one; 'ext' marks a model-estimated one.
AXIS_SUBSCRIPT = {"t1": "t_1", "t2": "t_2", "n": "n"}


def vec(row, prefix):
    return np.array([float(row[f"{prefix}_{a}"]) for a in "xyz"])


def curve_label(detail):
    """Name a curve by its compliance-centre position."""
    return detail or "centre position not specified"


def load(results, trial, axis):
    """Return time, contact-establishment rotation, commanded force and moment."""
    directory = os.path.join(results, trial)
    logs = glob.glob(os.path.join(directory, "logs", "*.csv"))
    if not logs:
        raise SystemExit(f"no log csv under {trial}")
    params = read_params(os.path.join(directory, "params_effective"))
    frame = surface_frame(float(params["surface_tilt_x_deg"]),
                          float(params["surface_tilt_y_deg"]))
    normal = frame[:, 2]
    tangent_axis = frame[:, AXIS_COLUMN[axis]]

    with open(logs[0]) as f:
        rows = [r for r in csv.DictReader(f)
                if float(r["phase"]) == CONTACT_ESTABLISHMENT_STATE]

    time, rotation, fn_cmd, m_cmd = [], [], [], []
    for row in rows:
        time.append(float(row["time"]))
        rotation.append(float(np.degrees(vec(row, "e_R")) @ tangent_axis))
        fn_cmd.append(float(normal @ vec(row, "f")))
        m_cmd.append(float(tangent_axis @ vec(row, "m")))

    t = np.array(time)
    return (t - t[0], np.array(rotation), np.array(fn_cmd), np.array(m_cmd))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("trials", nargs="+", metavar="TRIAL=DETAIL")
    p.add_argument("--axis", default="t1", choices=sorted(AXIS_COLUMN))
    p.add_argument("--out", default="COC_case")
    p.add_argument("--out-dir", default=os.path.join(HERE, "..", "figures"))
    p.add_argument("--results", default=RESULTS)
    args = p.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)

    selected = [tuple(a.split("=", 1)) for a in args.trials]
    fig, axes = plt.subplots(3, 1, figsize=(5.8, 6.2), sharex=True)

    for (trial, detail), colour in zip(selected, SERIES_COLOURS):
        label = curve_label(detail)
        t, rotation, fn_cmd, m_cmd = thin(*load(args.results, trial, args.axis))
        for ax, series in zip(axes, (rotation, fn_cmd, m_cmd)):
            ax.plot(t, series, color=colour, label=label)
        print(f"{trial:26s} gamma_{args.axis} {rotation[-1]:+6.2f} deg | "
              f"Fn_cmd {fn_cmd[-1]:7.1f} N | M_cmd {m_cmd[-1]:+6.2f} N m")

    sub = AXIS_SUBSCRIPT[args.axis]
    # A y label is set rotated, so its longest line has to fit the panel
    # height, not the figure width. The withdrawn "Set-Up Rotation About t_1,"
    # fitted on one line; "Contact-Establishment Rotation About t_1," does not,
    # and ran off the top of the figure. Each label is therefore broken so that
    # no line exceeds about twenty-three characters.
    labels = [rf"Contact-Establishment" "\n"
              rf"Rotation About ${sub}$," "\n"
              rf"$\gamma_{{{sub}}}$ [$^\circ$]",
              "Commanded Normal Force,\n" r"$F_n$ [N]",
              rf"Commanded TCP Moment" "\n"
              rf"About ${sub}$, $M_{{{sub}}}$ [N m]"]
    # The panel letters are drawn here rather than added over the PDF, so the
    # thesis includes the file directly instead of overlaying it.
    for ax, letter in zip(axes, "abc"):
        ax.text(0.012, 0.95, f"({letter})", transform=ax.transAxes,
                ha="left", va="top")
    for ax, text in zip(axes, labels):
        ax.set_ylabel(text)
        # Zero separates a flat tool from a tilted one, and a restoring moment
        # from a driving one. The press panels are left without a line.
        if "F_" not in text:
            reference_line(ax)
        ax.margins(y=0.3)
    handles, legend_labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, legend_labels, loc="lower center", ncol=len(handles),
               bbox_to_anchor=(0.5, 0.005),
               frameon=False, fontsize=7, handlelength=1.5,
               columnspacing=1.2, borderaxespad=0.2)
    axes[-1].set_xlabel(r"Time, $t$ [s]")
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    out = os.path.join(args.out_dir, f"{args.out}.pdf")
    fig.savefig(out)
    fig.savefig(out.replace(".pdf", ".png"), dpi=160)
    plt.close(fig)
    print(f"wrote {os.path.abspath(out)}")


if __name__ == "__main__":
    main()
