# Open items

This file contains only agreed work that remains unfinished. Completed items are
removed in the turn in which they are finished.

## Publish enough data to reproduce the figures

The run CSV files and derived contact metrics remain outside the repository.
Choose whether to publish `experiments/derived/metrics.csv` from
`Thesis_Final_Control` and one complete null-space run from `MyController`.
Preserve `MyController`'s calibration exclusion: its measured plane and
tool-axis calibration files are not to be published. If the data are placed in
this repository, the current scripts expect them below
`code/python/experiments/`.

## Verify the controller on the lab machine

The state-terminology refactor has passed the available Python, shell,
schema-compatibility, and static-analysis checks. The real C++ build and a
non-contact state-transition test still require the lab tree at
`/home/hm-panda/libfranka`, including `examples/examples_common.cpp`. Run both
before deploying the controller.

## Add a provenance warning for the video trials

The archived `V_ns*` trials used a \(40\,\mathrm{N}\) disturbance at a
\(150\,\mathrm{mm}\) offset and a faster timeline. The reported pose-hold study
used \(20\,\mathrm{N}\) at \(200\,\mathrm{mm}\). Add this distinction beside the
repository-authority rules in `code/AGENTS.md` so later analysis does not mix
the two configurations.

## Decide whether Chapter 6 carries the absolute case comparisons

The Chapter 6 revision of 2026-09-01 was asked to add the absolute values
beside the headline percentages: \(7.57^\circ\) to \(2.73^\circ\) and the
\(4.84^\circ\) reduction for Case B, and the \(0.03^\circ\) span for Case C.
They were not added, because *Results and conclusion priorities* in
`THESIS_WRITING_GUIDE.md` sends the complete absolute comparisons to Chapter 5
and keeps Chapter 6 to the headline percentages with their reference
conditions, at roughly half the length of Chapter 5. The stated problem — that
the conclusion reached its percentages before saying what they meant — was
fixed by leading each paragraph with the finding instead. Confirm whether the
absolute values should go in as well; if so, the guide rule is what has to
change first.

## Finish the Appendix C reduction

The 2026-09-01 reduction pass removed Table C.3, which duplicated Table 4.3,
and dropped the pose-hold damping and data-recording rows that Table 4.5 and
Section 4.1.3 already carry. Three requested items remain:

- Remove the `Configuration key` column from Tables C.1, C.4 and C.5. This
  overturns the standing rule under *The appendices* that a parameter, its
  configuration key and its value all belong in Appendix C, so the rule has to
  be rewritten in the same turn. It touches roughly thirty rows across three
  tables, each needing its column specification changed from three columns to
  two.
- Reduce Table C.2 to the fallback damping coefficients, dropping the stiffness
  entries that Table 4.2 and Table 4.5 already state.
- Drop the remaining Table C.5 rows that repeat Section 4.1.3 and Section 4.6.1:
  the gripper speed, the collision thresholds, and the null-space values. The
  gripper grasp force stays, because Section 6.2.3 discusses tool-mount
  compliance.

## Conditional maintenance for dormant appendices

- The retired, uncompiled files `backmatter/appendix_a_panda_example.tex` and
  `backmatter/appendix_c_exp1_rotated_tracking.tex` still contain `\approx`.
  Apply the current approximation rule before either file is reinstated.

## Follow-on physical-angle measurement

The reported logs define the contact-entry angle relative to the configured
surface reference. They do not contain an independently measured physical plane
normal or the tool face's motion relative to the end effector under load. A
follow-on experiment must record both before a run-wise physical tool--surface
angle can be evaluated.
