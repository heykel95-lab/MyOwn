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
  \(p_g=p_{\mathrm{EE}}+R_{\mathrm{EE}}r_{g,\mathrm{EE}}\) from Chapter 3. One
  calibrated-geometry table plus a cross-reference replaces both;
- the null-space configuration is still its own subsection with its own
  equation, and should fold into the common-gain table as rows plus one
  sentence saying it was held fixed;
- the data-recording subsection still lists the logged signals a third time.
  One sentence pointing at Chapter 3 and the data-format appendix is enough;
  the run counts and the excluded run stay.

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
cannot determine the counter type of a label set inside a `longtable`, and
silently printed `Section 4.4` for a table across four labels until it was
caught by eye. Those labels now use cleveref's explicit form,
`\label[table]{...}`; any new `longtable` needs the same.
