# Open items

Work agreed but not yet carried out. Each entry says what is wrong, what the
fix is, and what is blocking it. The editorial rules behind these live in
`THESIS_WRITING_GUIDE.md`, `THESIS_VOICE.md` and `FIGURE_STYLE.md`; this file
only tracks what is outstanding.

## Waiting on the plotting code

### Figure 5.13 legend still reads "EE-inferred angular deviation"

`figures/MAIN_DQ_metric_comparison.pdf`. The term is retired everywhere else in
the thesis. It should read **"Alignment angle from end-effector pose"**.

The caption and the surrounding prose are already correct, so this is one
string inside one plot. It blocks nothing.

Blocked because the plot cannot be regenerated: no script in either repository
produces it. The scripts in `MyController/experiments/analysis/` emit the
superseded figure set (`MAIN_A_angle`, `MAIN_C_KP`, `MAIN_D_CoC`,
`MAIN_H_general_pole` and so on), and a search for the current file names and
for the legend text returns nothing. The string is not patchable in the PDF
either: it appears in none of the decompressible content streams, so a binary
edit risks corrupting the font subset.

If the plotting code is found:

- the right-hand panel can be rebuilt from `experiments/derived/metrics.csv`,
  which carries `align_before_deg`, `align_after_deg` and `align_gain_deg`;
- the left-hand panel needs the per-sample CSV log of one set-up run, and no
  run logs are present on this machine — only six calibration CSVs;
- `analysis/sgc_log.py` already provides the loader and the alignment
  calculation (`read_csv`, `phase_mask`, `setup_metrics`,
  `alignment_improvement_deg`); only the plotting was lost;
- the same reconstruction should emit the renumbered case letters, which were
  changed by hand in this repository and which no script knows about.

This applies to all thirteen current plots, not only this one.

### Run counts could not be reconciled against `metrics.csv`

Raised while looking for the plotting code, and **not established as a fault in
the thesis**. The reported figures are internally consistent: the per-case runs
sum to exactly 171, and 57 settings times 3 repetitions is 171.

`MyController/experiments/derived/metrics.csv` holds 240 rows across several
campaigns (`MAIN`, `B1`--`B4`, `A2`, `G1`--`G3`, `PILOT`), and no obvious
filter reproduces 171 or 170. Its `test_case` letters are the old scheme, and
101 rows carry none. The file sits beside the superseded plotting scripts and
is plausibly from the same stale generation.

To close it: find the 171 run directories the thesis counted, confirm the one
incomplete run, and map them onto rows in `metrics.csv`. Only if they fail to
map does anything in the thesis need revisiting.

## Chapter restructures

Both are specified in full in `THESIS_WRITING_GUIDE.md`. Neither was started,
because a restructure abandoned midway leaves a chapter worse than one not
begun.

### Chapter 3

Reorder to follow the signal path, from surface and tool geometry to the torque
sent to the robot. Delete the functional-subsystems, null-space-mode and
logged-signal tables, simplify or drop the gain-frame table, and remove the
`robot.control` listing. Add the set-up reference relations, which are the
largest omission. Add three figures: grinding-face geometry and leading-feature
selection; the three points with their two offsets; set-up reference
generation.

### Chapter 4

Stop re-explaining the controller, let the tables replace the prose that repeats
them, delete the case-grouping table, move the fallback damping matrices to the
parameter appendix, and remove the mean and standard-deviation equations.

## Before the next prose session

Read `THESIS_VOICE.md` and `THESIS_WRITING_GUIDE.md` in full. The recent prose
turns used targeted reads because of context limits, which was flagged each
time, and the restructures deserve the complete pass.
