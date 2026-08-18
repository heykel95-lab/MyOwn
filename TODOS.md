# Open items

Everything agreed but not yet done. Each entry says what is wrong, what the fix
is, and what is blocking it. This file is kept current in the same turn the
situation changes, per the rule in `AGENTS.md`. Detailed specifications live in
`THESIS_WRITING_GUIDE.md`, `THESIS_VOICE.md` and `FIGURE_STYLE.md` and are
referenced from here rather than repeated.

**A finished item is deleted from this file, not annotated as done.** Whoever
completes it removes the entry in the same turn, so that no later session — and
no other agent — repeats work that is already in the document.

## For the lab machine, 2026-08-19

Only one item genuinely needs the other machine. An earlier session listed far
more than this and was wrong: it treated the figure work as a data problem when
almost all of it is a drawing problem. **Chapter 5 already reports every
null-space value with its standard deviation**, and figures in this thesis are
routinely drawn from tabulated means written into the source, which is how
`make_coc_figures.py` draws the Case-H comparison. Do not go looking for logs
before checking whether the number is already in the chapter.

### Three figure items, all blocked on the same missing CSV

All three need logged per-trial CSV that is on neither this machine nor in
either repository. Each entry gives the exact source edit, so the only work on
the other machine is running the script and copying the PDF back. **Make the
source edits here first** — they are already possible — then regenerate.

**Before scripting any of this, read the tooling warning at the end of this
section.**

#### 1. Figure 5.10 y-axis — `code/python/figures/make_nullspace_figure.py`

The caption is already correct and the figure is honest as it stands, so this
is polish rather than a fault. Panel (b)'s y-axis still reads
`Final singular-value change`, which is vague and does not use the symbol the
thesis now defines.

Two label strings to change:

    line 268:  label=r"Final $\Delta\sigma_{\min}$ (mean $\pm$ SD)"
        ->     label=r"$\Delta\sigma_{\min,\mathrm{dist}}$ (mean $\pm$ SD)"

    line 274:  ax.set_ylabel(r"Final singular-value change $\Delta\sigma_{\min}$ [-]")
        ->     ax.set_ylabel(r"Change in $\sigma_{\min}$ over disturbance "
                             r"interval $\Delta\sigma_{\min,\mathrm{dist}}$ [-]")

Keep the `[-]` unit marker rather than writing `[m/rad]`: the symbol list now
states that a singular value of the mixed geometric Jacobian carries no single
physical unit and is a relative indicator under one fixed representation.

**Why it cannot run here.** Two separate reasons, and both must be solved:

- **The run identifiers do not match.** `CONDITIONS` at lines 38--42 expects

      MAIN_NS7_baseline_20N_200mm
      MAIN_NS7_damping_2p0_20N_200mm
      MAIN_NS8_ksigma_1p5_20N_200mm
      MAIN_NS8_ksigma_2p0_20N_200mm

  whereas `MyController/experiments/results/` holds the same four conditions
  under `MAIN_F7_*` and `MAIN_F8_*`. Confirm which naming the reported figure
  was generated from before renaming anything, and do not edit `CONDITIONS` to
  match the old names without checking that the runs are the same.
- **No per-cycle CSV is archived.** `MAIN_F7_baseline_20N_200mm/r01/` contains
  `terminal.log`, `params_effective/`, the calibration overlays and
  `meta.txt`, but no logged CSV. Panel (a) needs the full time history, so the
  CSV is required, not just the summary.

The script also expects `experiments/results/` and
`experiments/derived/MAIN_NS_automatic_summary.csv` **relative to its own
directory**, which resolves to `code/python/experiments/...` here. Either place
the data there or run the script beside the data.

#### 2. Figure D.2 axes — `code/python/figures/plot_setup_diagnostics.py`

The axes read \(F_{\mathrm{cmd}}\) and \(M_{\mathrm{cmd}}\), neither of which is
a thesis symbol. Do not invent a vector symbol for one appendix figure; the
\(t_1\), \(t_2\), \(n_s\) legend already names the components.

    line 112:  r"$F_{\mathrm{cmd}}$ [N]"    -> r"Commanded force component [N]"
    line 114:  r"$M_{\mathrm{cmd}}$ [N m]"  -> r"Commanded moment component [N m]"

The `f"F_cmd n ..."` and `f"M_cmd t1 ..."` strings at lines 118--119 are console
output, not figure text, and stay.

**Data needed**: its two default trials, and nothing more —

    P2_t1_pos_m040/r01   ("centre -40 mm")
    P2_t1_pos_p040/r01   ("centre +40 mm")

Those detail strings say `centre`, which is \(d_c\) and **not** \(r_c\). Do not
"correct" them to \(r_c\); see the \(d_c=-r_c\) rule above. After regenerating,
check the caption still describes both columns.

#### 3. Legends of Figures 5.2, 5.3 and D.1 — `code/python/figures/make_coc_figures.py`

These read `initial $-9.31^\circ$ about $t_1$` and similar. They are no longer
wrong, because the signed set-up-entry deviation is now defined in Section 4.5,
but four such labels crowd a legend and the exact values belong in the tables.
This is polish, not a correction.

The labels are built by `initial_label()` at line 96 and used at lines 183, 222,
233, 274, 293 and 307. Shorten to the condition alone — `+10^\circ\ t_1`,
`-10^\circ\ t_1`, `+10^\circ\ t_2`, `-10^\circ\ t_2` — by rewriting
`initial_label()` to name the commanded offset instead of the measured
deviation, rather than editing six call sites.

**Do not delete the measured value from the thesis**: it is what
Table 5.4's \(\theta_{\mathrm{dev,before}}\) column carries, and the point of
`initial_label()` was to avoid substituting the nominal command for the
orientation actually reached. Say once in the surrounding text that the
commanded offset and the measured entry deviation differ, and that the measured
values are tabulated.

**Data needed**: a `metrics.csv` containing the `P2_` rows. The copy here has
240 rows and none of them. Note the README claim that this script "needs no
data" is false — `main()` calls `load()`, which reads that file.

#### Tooling warning, learned the hard way this session

Editing these `.tex` and `.py` files through an inline shell script **silently
corrupts backslashes**. Both of these failed on this machine:

- `python - <<'PY' ... PY` — a quoted heredoc still stripped one backslash
  level, so a pattern containing `\\[-2pt]` never matched and the script
  reported a clean `AssertionError` only because it happened to assert;
- `sed -i 's/\\cref{/\\Cref{/g'` — **reported success and changed nothing.**
  That is the dangerous one, because a silent no-op looks like a completed
  edit.

Use a file-based script written by an editor, or an editing tool, and verify by
re-reading the file rather than trusting the exit status.

### Push the missing pieces to a repository while there

The reason this work stalls on the other machine is that the campaign records
were never committed anywhere. Pushing them once removes the dependency for
every future session, on any machine.

**Minimum, to close Figure D.2:**

    experiments/results/P2_t1_pos_m040/r01/
    experiments/results/P2_t1_pos_p040/r01/

including the logged CSV each contains, not only `terminal.log` and
`params_effective/`. The run directories archived so far carry the metadata but
**not** the CSV, which is exactly why the figure cannot be re-run here.

**Worth adding at the same time, so no later session is blocked again:**

- a `metrics.csv` that actually contains the `P2_` rows. The copy on this
  machine, `MyController/experiments/derived/metrics.csv`, has 240 rows and not
  one `P2_` among them, so it reproduces no reported contact figure;
- one complete null-space run CSV, which also settles the trial end time below;
- the remaining `P2_*` run directories if their size is reasonable.

**Where to push.** `Thesis_Final_Control` is the natural home, since it ran the
campaign, and it currently has no `experiments/` directory at all. Its
`.gitignore` does not exclude one. If the data goes into this thesis
repository instead, note that the figure scripts resolve their input as
`HERE/../experiments/results`, which from `code/python/figures/` means
`code/python/experiments/results/`. Nothing in `MyOwn/.gitignore` blocks CSV,
so either choice works.

**One caution.** `MyController/.gitignore` deliberately excludes the measured
plane and tool-axis calibration files, with the stated reason that the measured
coordinates are not to be published. Keep that exclusion when moving anything
across; push the run records, not the calibration coordinates.

### Worth confirming while there

- **The null-space trial end time** (item 26). The disturbance interval is
  already confirmed from `MAIN_F7_baseline_20N_200mm/r01/terminal.log`, which
  states `ramp 5.0--7.0 | hold to 8.0 | release 1.0 s` and therefore ends at
  \(9.0\,\mathrm{s}\), matching Section 4.6.2. Unknown is whether **every**
  trial ran to \(18\,\mathrm{s}\). Do not write
  `9--18 s post-disturbance observation` until checked; if the runs differ in
  length, say that instead of quoting one number.

### Also worth fixing while the data is to hand

`code/python/figures/README.md` claims `make_coc_figures.py` "needs no data ...
so it runs anywhere". That is wrong: `main()` calls `load()`, which reads
`experiments/derived/metrics.csv` and raises `FileNotFoundError`. Either
correct the claim or give the script the hardcoded-means path the README
describes.

## Final examiner-level review: the standing work list

A complete final review was requested before supervisor submission, in two
passes — technical/notation first, then language, figures, captions and
layout. The items below are what that review has not yet reached. They are
ordered as the review specification numbered them, so an item can be matched
back to its specification.

The full specification, items 1 to 76, has been received; nothing further is
outstanding from the author on that front.

### Verified during the review and needing no change

- **Figure D.3 is present and renders.** It was reported as a heading, caption
  and paragraph with no visible graphic. Built from current source it renders
  correctly, `figures/MAIN_DQ_metric_comparison.pdf` is a valid two-panel
  matplotlib PDF, it appears in the build log, and both panels are visible on
  the page. The reported fault belongs to the PDF it was seen in, not to the
  source. Do not attempt to restore it. Its legend and caption still need the
  work listed under the figure items.
- **`p_CoC` and `r_eff` in Appendix B are consistent** with
  \(r_c=p_{\mathrm{TCP}}-p_c\): the appendix gives
  \(p_c=p_{\mathrm{TCP}}-r_c\) and \(r_{\mathrm{eff}}=p_T-p_c\). `r_eff` is a
  CSV column only and stays a data identifier, per item 49.

### Settled at source, and binding on the remaining figure work

- **The plotted centre position is \(d_c=-r_c\).** The experimental plots and
  tables report the signed centre offset \(d_c=p_c-p_{\mathrm{TCP}}\), which is
  the **negative** of the lever \(r_c\) in the point-shift equations. Checked
  inside the thesis's own numbers: Table 4.4 gives
  \(r_c=[0,-40,0]\,\mathrm{mm}\) for the selected \(+10^\circ\) condition
  about \(t_1\), while the Case-D sweep shows the assisting centre for that
  same condition at \(+40\,\mathrm{mm}\) along \(t_2\). **Relabelling a
  `centre position` axis as \(r_{c,t_2}\) reverses the sign and is a factual
  error.** The rule and the symbols \(d_c\), \(d_{c,t_i}\) are recorded in
  `THESIS_WRITING_GUIDE.md` and the symbol list.

  An earlier turn inferred the opposite from
  `MyController/.../MAIN_D1_t1_rc_t2_m060`. That inference is **withdrawn**:
  `MyController` is the superseded controller and its directory naming does not
  govern the reported campaign. See `code/AGENTS.md` for which repository is
  authoritative for what.

- **The two configuration branches are opposite in sign.** Confirmed in
  `Thesis_Final_Control/surface_grinding_controller`:
  `src/control/cartesian_impedance.cpp` forms
  \(r_c=-(R_{\mathrm{EE}}\,\texttt{compliance\_center\_offset\_ee})\) on the
  tool-frame branch and
  \(r_c=R_{\mathrm{base,surface}}\,\texttt{r\_tcp\_from\_compliance\_center\_surface}\)
  on the surface-frame branch, and `params/setup.conf` documents both in the
  same words. Writing this into Appendix C is item 48 below and is not blocked.

- **The signed set-up-entry deviation is defined and applied.**
  \(\theta_{\mathrm{dev}}\) is the rotation vector taking \(n_T\) onto the flat
  target \(-n_s\); \(\theta_{\mathrm{align}}\) is its norm, so the two are the
  magnitude and the signed components of one vector. Its sign is opposite to
  the commanded orientation offset because it is the rotation still required to
  reach flat, and its magnitude falls short of the command because the
  orientation phase exits on a tolerance. Source:
  `toolSurfaceAlignmentErrorBase` and `setup_evaluation.cpp`.

### Remaining work that can be done on this machine

None of the following needs the lab machine. Completed items have been deleted
from this list rather than annotated, so everything here is still open.

**Prose and technical (review pass 1)**

- **4** — keep the three moment concepts separate throughout, and never add
  \(m_{r_T}\) to \(m_0\) or \(m_{c,K}\). Spot-check rather than rewrite.
- **17, 18** — Case-A physical-asymmetry interpretation still needs its causal
  wording softened to `consistent with`.
- **48** — Appendix C must state the two opposite-sign configuration branches
  (`compliance_center_offset_ee` defines \(p_c-p_{\mathrm{TCP}}\);
  `r_tcp_from_compliance_center_surface` defines \(r_c\)) rather than calling
  both "centre displacement". The rule is already recorded in
  `THESIS_WRITING_GUIDE.md`; only the appendix wording remains.
- **50** — Appendix B `t_align`, `align_status` and `deviation_min` must read as
  observational, not as phase-termination conditions.
- **57** — \(\tau_{\mathrm{cmd}}\) carries two definitions in Section 2.4.3.
  Reserve it for the implemented command and rename the generic form.
- **59** — Introduction citation-support audit. Check each literature-supported
  claim against its source; soften anything the source does not carry, such as
  the share of industrial deployments attributed to *torque-controlled* robots.
- **60** — related-work versus contribution boundary.
- **65, 66, 67, 68** — surface-force language, directional-asymmetry language
  (no `bias`), grinding described as implemented functionality only, and
  adaptive centre-of-compliance scheduling kept explicitly as future work.

**Figures, tables and captions (review pass 2)**

- **A.5 — the second null-space figure.** Item 29 asks for the net redundant
  displacement and the \(\Delta\sigma_{\min,\mathrm{dist}}\)/peak-error
  comparison, which the present figure does not show. **This needs no logged
  data.** Every value is already in Section 5.2 with its standard deviation:
  \(\Delta\eta_{\mathrm{dist}}\) of \(0.131\pm0.016\),
  \(0.098\pm0.004\), \((0.3\pm0.3)\times10^{-3}\) and
  \((-0.1\pm0.2)\times10^{-3}\,\mathrm{rad}\);
  \(\Delta\sigma_{\min,\mathrm{dist}}\) of \((-2.13\pm0.47)\times10^{-3}\),
  \((-1.26\pm0.10)\times10^{-3}\), \((1.95\pm0.07)\times10^{-5}\) and
  \((1.93\pm0.03)\times10^{-5}\); peak Cartesian error \(0.889\pm0.024\) and
  \(0.983\pm0.053\,\mathrm{mm}\). Draw it in `pgfplots` as a new figure
  beside the existing one, per item 29's instruction to split rather than
  crowd three panels. Read `FIGURE_STYLE.md` first. Keep the
  \(2\,\mathrm{mm}\) acceptance line on the error panel.
- **A.4** — Figure 3.1 still shows `spring wrench`, `tau_task` and `c(q,qdot)`.
  Correct to the Cartesian impedance wrench, \(\tau_{\mathrm{cart}}=J^\top F\)
  and \(\tau_c\). It is a TikZ source and needs no data.
- **Rename the plotted centre coordinate to \(d_c\).** Figure 5.4's axes read
  `Centre position along t_2 [mm]`, which is correct in value but no longer
  correct in notation now that \(d_c\) exists. The same applies to Table 4.3
  and the Case-F, Case-G and Case-H tables. **The values and signs do not
  change** — this is notation only, and \(r_c\) must not be substituted.
- **21, 22, 23** — Figure 4.2 calibration notation (Option A), Figure 4.1
  labels and caption, and the Figure 3.5 set-up symbols
  \(p_{T,0}\), \(p_{T,d}\), \(s_{\mathrm{set}}\), \(R_{\mathrm{clr}}\),
  which should also join the symbol list.
- **31, 33, 34, 37, 38** — the pgfplots figures and their tables: Figures 5.1,
  5.4, 5.7, 5.8 are `.tex` sources and can be edited directly.
- **44** — global table-unit audit across Tables 5.1 to 5.8.
- **45, 46** — Table 4.3 caption and one consistent centre convention;
  Table 4.4 component headings.
- **51, 52, 53** — panel audit for every multi-panel caption, and short
  List-of-Figures and List-of-Tables entries.
- **54** — finish the full source-level symbol inventory.
- **62, 63, 64** — one cross-reference style (`Figure 5.4`, `Table 5.4`,
  `Section 4.5`, `Equation (5.1)`), consistent capitalisation, and
  `tool centre point (TCP)` used correctly against the tool-face centre.

**Whole-document passes, last**

- **58** — Abstract and Kurzfassung claim audit, line by line, for identical
  certainty. The null-space sentence is already matched in both.
- **61** — bibliography formatting audit. Invent no missing metadata.
- **69, 70** — number consistency and one rounding policy. Do not alter
  validated values.
- **71, 72** — rebuild the auxiliary lists and re-run the warning audit after
  the figures change.
- **73, 74, 75** — page-by-page visual audit of the final PDF, a second
  complete read, and the final examiner-question check.
- **76** — only then may the thesis be called ready for supervisor review.

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

## Verify the joint-torque figures before reinstating them

Chapter 5 carried a paragraph saying that an exploratory tool-axis test at
\(120\,\mathrm{mm}\) drove the commanded sixth-joint torque to
\(21.4\,\mathrm{N\,m}\) "against its \(12\,\mathrm{N\,m}\) limit" and
aborted, while the reported sweep reached \(15.1\,\mathrm{N\,m}\) at its
final position. **As written the two are inconsistent**: if the limit is
\(12\,\mathrm{N\,m}\), a reported run cannot sit at
\(15.1\,\mathrm{N\,m}\) without explanation. There may be a real
distinction — commanded torque against the value libfranka actually applies, a
transient against a configured threshold, or rated against peak torque — but
the text did not state it, and it cannot be checked here because no run logs
are on this machine.

The paragraph has been removed from Chapter 5. The Limitations section of
Chapter 6 now carries the defensible part without the numbers: the lever
magnitude is bounded by the joint-torque limits, and an exploratory
displacement beyond the reported Case-F range was stopped by one.

To close it: confirm what the \(12\,\mathrm{N\,m}\) figure refers to and
whether the \(15.1\,\mathrm{N\,m}\) value is a commanded or an applied
torque. If both are commanded values and libfranka handles the limit, say so in
one clause and the paragraph can go back.

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

## Inspect the pages this revision moved

The contact study was rebuilt around the fixed-centre question, which changed
Chapter 1 (problem statement, scope and contributions), the introduction to
Section 4.4 and the comparison column of its case table, the case commentary
and synthesis in Chapter 5, the whole of Section 6.1 with the limitations and
future work, and both summaries. The null-space material was then reinterpreted
in the same way: the trial timeline and a second motion metric in Section 4.6,
the sigma result in Section 5.2, and the corresponding passages in Chapter 6 and
the two summaries. The null-space figure was regenerated from the logs, so its
panel (a) is a few points taller than the file it replaces. Page breaks moved with all of it, and the compiled pages have
not been read on screen. Two specific things to look at:

- **The Abstract and the Kurzfassung now run to two pages each** (Abstract on
  pages V--VI, Kurzfassung on VII--VIII). The one-page limit is suspended in
  `THESIS_WRITING_GUIDE.md`, so this is allowed rather than a fault, but it is
  a visible change and should be seen before submission. If the limit is
  restored, the fixed-centre definition and the direction-independence
  paragraph are the material that has to displace something older.
- No heading was left stranded by an automated scan of the compiled document,
  which is a weaker check than reading the pages.

The three documents build clean here — `Thesis.tex`, `Professor_Draft.tex` and
`Review_Draft.tex`, with bibtex and three passes each, no undefined references
or citations and no overfull boxes. **The local build needed
`compat=1.16`**, because the TeX Live 2019 on this machine predates the
`compat=1.18` the sources set; the file was restored afterwards and the plots
were therefore not rendered at the compat level the author's MiKTeX uses.
Rebuild there before judging any figure.

## Before the next prose session

Read `THESIS_VOICE.md` and `THESIS_WRITING_GUIDE.md` in full.

Write edits through a file-based script with raw strings, or through the
editing tool directly. Inline shell scripts twice stripped a backslash level
and turned `\begin`, `\right` and `\resizebox` into control characters, which
is invisible when reading the source and only the build catches. A quoted
heredoc is not a workaround: the same script written through `cat <<'EOF'`
failed to parse at all, so write the script with the file-writing tool and run
it separately.

Check `\Cref` output in the compiled PDF, not only in the source. cleveref
cannot handle a label set inside a `longtable` and fails in two different ways,
neither of which warns: with a plain `\label{}` it printed `Section 4.4` for a
table, and with `\label[table]{}` it fixed the type but built the number from
the section prefix, printing `Table 4.3.2` for Table 4.3 across four labels.
Those four are now referenced as literal `Table~\ref{...}`, which is right in
both respects. Any new `longtable` needs the same treatment.
