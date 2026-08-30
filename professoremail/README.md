# Commanded against model-estimated wrench

This folder is meant to hold two files:

    commanded_vs_estimated_wrench.pdf
    commanded_vs_estimated_wrench.csv

**Neither could be produced on this machine, because the log they are drawn
from is not on it.**

## What is missing

The estimated wrench is `external_force_x..z` and `external_moment_x..z`,
libfranka's `O_F_ext_hat_K`. Only the current `surface_grinding_controller`
schema records it, and no file with that schema exists here:

- `Thesis_Final_Control/surface_grinding_controller` holds source only. It has
  no `experiments/` directory, so no `results/`, no `logs/`, no `derived/`.
- The 59 log CSVs recoverable from the `MyController` git history are all the
  earlier development schema. They record the commanded `f` and `m` and the
  joint torques `tau_raw` and `tau_limited`, and carry no external-wrench
  column under any name.
- A full sweep of the C: drive finds 220 CSVs, none of them a controller log.

This is the expected state away from the lab machine: that repository's
`.gitignore` excludes `experiments/results/**/*.csv` for size and
`experiments/derived/` entirely.

## How to fill the folder

Copy one log from the lab machine, from any run directory under
`Thesis_Final_Control/experiments/results/`:

    <run>/logs/surface_grinding_controller_log.csv

Put it beside this README, then run:

    python plot_commanded_vs_estimated_wrench.py surface_grinding_controller_log.csv --out-dir .

Both files appear in this folder. Useful options:

    --phase 2          restrict to the set-up phase
    --bias-corrected   use the clearance-referenced estimate
                       (force_after_contact / moment_after_contact)

## What the figure shows

Two panels, force above moment, plotting magnitudes against time. The commanded
Cartesian wrench is black; the model-estimated external wrench is red. The
accompanying CSV holds exactly the plotted rows, with the raw x, y, z
components kept alongside the magnitudes.

One caveat if the figure is ever used in the thesis rather than for checking:
the estimate is the wrench the environment applies to the robot, so in steady
contact it opposes the commanded wrench. Magnitudes are plotted so the two
curves are comparable without carrying that sign, and the caption has to say so.
