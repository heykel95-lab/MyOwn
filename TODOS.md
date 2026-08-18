# Open items

Everything agreed but not yet done. Each entry says what is wrong, what the fix
is, and what is blocking it. This file is kept current in the same turn the
situation changes, per the rule in `AGENTS.md`. Detailed specifications live in
`THESIS_WRITING_GUIDE.md`, `THESIS_VOICE.md` and `FIGURE_STYLE.md` and are
referenced from here rather than repeated.

**A finished item is deleted from this file, not annotated as done.** Whoever
completes it removes the entry in the same turn, so that no later session — and
no other agent — repeats work that is already in the document.

## Chapter 3 — the last structural work on the chapter

Specified in full in `THESIS_WRITING_GUIDE.md`. The signal path is now correct;
what remains is software documentation that the chapter does not need:

- delete the functional-subsystems table, the null-space-mode table and the
  logged-signal table, and simplify or drop the gain-frame table;
- remove the `robot.control` listing, which shows nothing the prose does not.

The chapter reordering called for in the guide has been carried out and should
not be reopened.

## Chapter 4 — remaining duplication

Specified in full in `THESIS_WRITING_GUIDE.md`:

- the calibration section keeps the runtime relations
  \(n_T=R_{\mathrm{EE}}n_{\mathrm{EE}}\) and \(R_dn_{\mathrm{EE}}=-n_s\), which
  describe how the controller uses the calibration rather than how it was
  calibrated, and belong in Chapter 3;
- the calibrated-geometry subsection still gives the face centre, half-width
  and half-length as vector equations, and still repeats
  \(p_T=p_{\mathrm{TCP}}+R_{\mathrm{EE}}r_{T,\mathrm{EE}}\) from Chapter 3.
  One calibrated-geometry table plus a cross-reference replaces both;
- the null-space configuration is still its own subsection with its own
  equation, and should fold into the common-gain table as rows plus one
  sentence saying it was held fixed;
- the data-recording subsection still lists the logged signals a third time.
  One sentence pointing at Chapter 3 and the data-format appendix is enough;
  the run counts and the excluded run stay.

## Six diagrams are still sized by `\resizebox`

The three Chapter 3 diagrams were drawn at about 7--10 cm and then stretched to
the text width, which magnified their label text along with the drawing: at
figure 3.3 the symbols came out roughly twice the size of the body text and
collided with each other. They now carry a `scale=` inside the picture and are
included without `\resizebox`, so the labels keep the size they were declared
at.

The same wrapper is still on `controller_block_diagram`, `phase_flow_chart`,
`tool_transfer_flow`, `setup_schematic`, `calibration_flow`, and the two
appendix parameter tables. A diagram that is *shrunk* by the wrapper has the
opposite fault and is equally wrong. Each needs looking at in the compiled
document, and the scale factor moving inside the picture wherever the label
size is off. This is judged by eye on the page, not from the source.

## Four Chapter 5 figures still need redrawing

The Chapter 5 restructure is done in prose: the discussion now sits under the
evidence, the Cross-Case Discussion is gone, and two plots have moved to the
supporting-plots appendix. Four requested figure *redesigns* could not be made,
because no script produces any of the current plots:

- **Case A** (`MAIN_A_contact`): the x-axis labels should read
  \(+10^\circ\,t_1\), \(-10^\circ\,t_1\), \(+10^\circ\,t_2\),
  \(-10^\circ\,t_2\). The measured initial values belong in the table, not
  on the axis.
- **Case D** (`MAIN_D_sign`): split the four curves into two panels, (a) the
  \(t_1\) commands and (b) the \(t_2\) commands, on identical axis limits.
- **Case F** (`MAIN_F_toolaxis`): replace with one figure plotting the
  tangential sweep of Case D against the tool-axis sweep of Case F on the same
  axes, for the same \(+10^\circ\) \(t_1\) command, so the comparison of
  spans is visible rather than stated.
- **Case G** (`MAIN_G_magnitude`): replot against the commanded offset
  (\(5^\circ\), \(10^\circ\)) with one series for the zero lever and one
  for the selected \(40\,\mathrm{mm}\) lever, in two panels for \(t_1\)
  and \(t_2\). The present figure plots against centre position, which is not
  the question the case asks.

The prose around each already states the comparison the redrawn figure would
make, so the argument does not depend on them.

`figures/MAIN_DQ_descent.pdf` is now unused: it was Figure 5.1 and was removed
because it only showed that two time histories settle. Delete the file or keep
it for reference, but do not reinstate the figure.

## Run counts could not be reconciled against `metrics.csv`

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

## The plotting code is still missing

Not blocking anything now that the metric-comparison legend has been corrected
in the PDF itself, but it still bounds what can be changed. No script in either
repository produces any of the thirteen current plots; the scripts in
`MyController/experiments/analysis/` emit the superseded figure set. A data
series, an axis, or a case letter inside a plot cannot be changed until the code
is found. `FIGURE_STYLE.md` records what a reconstruction would need and what a
direct PDF edit can and cannot do.

## Final-pass work, once the two chapters above are closed

The structural rewriting is finished. What remains is wording consistency,
figures, captions, references, formatting, and technical sanity checks against
the checklist at the end of `THESIS_WRITING_GUIDE.md`.

## Before the next prose session

Read `THESIS_VOICE.md` and `THESIS_WRITING_GUIDE.md` in full.

Write edits through a file-based script with raw strings. Inline shell scripts
twice stripped a backslash level and turned `\begin`, `\right` and `\resizebox`
into control characters, which is invisible when reading the source and only
the build catches. A quoted heredoc is not a workaround: the same script
written through `cat <<'EOF'` failed to parse at all, so write the script with
the file-writing tool and run it separately.

Check `\Cref` output in the compiled PDF, not only in the source. cleveref
cannot handle a label set inside a `longtable` and fails in two different ways,
neither of which warns: with a plain `\label{}` it printed `Section 4.4` for a
table, and with `\label[table]{}` it fixed the type but built the number from
the section prefix, printing `Table 4.3.2` for Table 4.3 across four labels.
Those four are now referenced as literal `Table~ef{...}`, which is right in
both respects. Any new `longtable` needs the same treatment.
