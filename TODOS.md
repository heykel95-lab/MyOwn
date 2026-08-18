# Open items

Everything agreed but not yet done. Each entry says what is wrong, what the fix
is, and what is blocking it. This file is kept current in the same turn the
situation changes, per the rule in `AGENTS.md`. Detailed specifications live in
`THESIS_WRITING_GUIDE.md`, `THESIS_VOICE.md` and `FIGURE_STYLE.md` and are
referenced from here rather than repeated.

**A finished item is deleted from this file, not annotated as done.** Whoever
completes it removes the entry in the same turn, so that no later session — and
no other agent — repeats work that is already in the document.

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

## Chapter 3 restructure — partly done

Specified in full in `THESIS_WRITING_GUIDE.md`.

Already carried out:

- the five pseudo-equations and the process-arrow display are prose;
- the set-up reference relations are in, with the sentence explaining that the
  controller reconstructs the tool centre point target rather than commanding
  it down;
- all three figures are drawn and checked in the compiled document: the
  grinding-face geometry with the corner, edge and face-centre outcomes; the
  three points with their offsets and sum; and set-up reference generation.

Still to do:

- delete the functional-subsystems, null-space-mode and logged-signal tables,
  and simplify or drop the gain-frame table;
- remove the `robot.control` listing, which shows nothing the prose does not;
- reorder the chapter to follow the signal path, from the surface and tool
  geometry through to the torque sent to the robot.

## Chapter 4 restructure — partly done

Specified in full in `THESIS_WRITING_GUIDE.md`.

Still to do:

- the calibration section keeps the runtime relations
  \(n_T=R_{\mathrm{EE}}n_{\mathrm{EE}}\) and \(R_dn_{\mathrm{EE}}=-n_s\), which
  describe how the controller uses the calibration rather than how it was
  calibrated, and belong in Chapter 3;
- the calibrated-geometry subsection still gives the face centre, half-width
  and half-length as vector equations, and still repeats
  \(p_g=p_{\mathrm{EE}}+R_{\mathrm{EE}}r_{g,\mathrm{EE}}\) from Chapter 3. One
  calibrated-geometry table plus a cross-reference replaces both;
- the null-space configuration is still its own subsection with its own
  equation, and should fold into the common-gain table as rows plus one
  sentence saying it was held fixed;
- the data-recording subsection still lists the logged signals a third time.
  One sentence pointing at Chapter 3 and the data-format appendix is enough;
  the run counts and the excluded run stay.

## Before the next prose session

Read `THESIS_VOICE.md` and `THESIS_WRITING_GUIDE.md` in full. The recent prose
turns used targeted reads because of context limits, which was flagged each
time, and the restructures deserve the complete pass.

Write edits through a file-based script with raw strings. Inline shell scripts
twice stripped a backslash level and turned `\begin`, `\right` and `\resizebox`
into control characters, which is invisible when reading the source and only
the build catches. A quoted heredoc is not a workaround: the same script
written through `cat <<'EOF'` failed to parse at all, so write the script with
the file-writing tool and run it separately.
