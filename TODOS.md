# Open items

Everything agreed but not yet done. Each entry says what is wrong, what the fix
is, and what is blocking it. This file is kept current in the same turn the
situation changes, per the rule in `AGENTS.md`. Detailed specifications live in
`THESIS_WRITING_GUIDE.md`, `THESIS_VOICE.md` and `FIGURE_STYLE.md` and are
referenced from here rather than repeated.

**A finished item is deleted from this file, not annotated as done.** Whoever
completes it removes the entry in the same turn, so that no later session — and
no other agent — repeats work that is already in the document.

## The campaign archive, and what it now supports

The \(55\) reported settings each carry three repetitions. The two
`B_combined_{t1,t2}` settings were removed from the report on 2026-08-24,
taking the campaign from \(57\) settings and \(171\) runs to \(55\) and
\(165\); their run directories stay in the archive and are simply not
reported. The Case-D run that
Section 4.3.4 once recorded as excluded was re-recorded on 2026-08-19 under a
byte-identical parameter set, so the count is \(165\) of \(165\) and the chapter
says so. **Do not reintroduce an excluded-run sentence.**

The archive lives on the lab machine at
`Thesis_Final_Control/experiments/results/`, \(171\) archived run directories
(the \(165\) reported plus the six no longer reported) each with
`logs/surface_grinding_controller_log.csv`, and
`experiments/derived/metrics.csv` carries the \(100\) `P2_` rows the contact
figure scripts read. **A clone shows neither**, because that repository's
`.gitignore` excludes `experiments/results/**/*.csv` for size and
`experiments/derived/` entirely. The twelve pose-hold trials are in the other
repository as `MyController/experiments/results/MAIN_NS{7,8}_*`, three
repetitions each, all ending at \(18.001\,\mathrm{s}\).

The mapping from case letters to directories, which should not be re-derived:

| Case | Settings | Run directories |
|---|---|---|
| A | 5 | `S1_none_00deg`, `P2_{t1,t2}_{pos,neg}_p000` |
| B | 4 | `A_rot_{t1,t2}_{15,50}` |
| C | 4 | `B_trans_{t1,t2}_{0300,0800}` |
| D | 24 | `P2_{t1,t2}_{pos,neg}_{m010,m020,m040,p010,p020,p040}` |
| E | 3 | `S3_surface_00deg`, `S3_surface_t1_10deg`, `S2_tool_00deg` |
| F | 6 | `P3_axis_{m010,m020,m040,p010,p020,p040}` |
| G | 4 | `P5_mag_{t1,t2}_{p000,p040}` |
| H | 5 | `C_dir_{m45,p45}`, `C_fixed_{m45,p45}`, `C_fixed_t2` |

The `P2_*_{m080,p080}` directories and the `V_*`, `S4_*`, `S5_*`, `P4_*`,
`P6_*`, `P_*`, `AXS*`, `REVS2_*` and `PROBE60_*` series are exploratory and
outside the reported \(55\).

The aborted first attempt at `P2_t1_pos_m040/r02` was moved to
`experiments/results_aborted/P2_t1_pos_m040_r02_20260817/` so no analysis script
counts it. Its `README.md` says what it was. Do not delete it and do not move it
back.

### The repeatability sentence in Chapter 5 cannot be reproduced

Chapter 5 states that the median within-setting standard deviation of the
signed set-up rotation was approximately \(0.04^\circ\) about \(t_1\) and
\(0.14^\circ\) about \(t_2\), and treats differences below about
\(0.1^\circ\) as scatter. **No definition tried on 2026-08-19 reproduces those
two values** from `metrics.csv`: medians over the reported settings give
\(0.015\) and \(0.058\), over the \(28\) `P2_` settings \(0.041\) and
\(0.157\), and over every archived setting \(0.016\) and \(0.054\). The
\(0.041\) is close enough to be suggestive and its partner is not.

This matters because the third repetition of `P2_t1_pos_m040` widened that
setting's own scatter, so whatever the sentence was computed from has moved a
little. **The number was left unchanged**, since changing a statistic that
cannot be reproduced would be worse than leaving it. To close it: state which
set of settings and which column the two medians came from, then recompute both
and the \(0.1^\circ\) interpretation threshold with them.

### Building on the lab machine, and the one thing it cannot check

`texlive-lang-german` is installed, so `ngerman.ldf` resolves and the document
builds. `Thesis.tex` was built on 2026-08-19 with bibtex and three passes: no
errors, no undefined references or citations, no overfull boxes, 171 pages.
Judge a build by the final pass; the earlier ones always report undefined
citations.

**`compat=1.18` cannot be used here.** This TeX Live 2019 ships pgfplots 1.16
(`2018/03/28`), and `config/packages.tex` line 39 asks for `1.18`, which fails
outright with `Sorry, 'compat=1.18' is unknown in this context`. Ubuntu 20.04
has no newer TeX Live, so no apt package fixes it: the routes are a `tlmgr`
update of pgfplots alone, or a current TeX Live installed alongside and put
first on `PATH`.

Until then a local build means lowering the line to `compat=1.16` and
**restoring it afterwards** — done and restored twice on 2026-08-19. The
consequence is that every `pgfplots` figure is rendered at 1.16 semantics
rather than the 1.18 the author's MiKTeX uses, so **the plots must be seen in a
build there before submission**. Nothing else about the document differs.

### Where the run logs should live

`Thesis_Final_Control` now tracks the text record of every archived run,
including `P2_t1_pos_m040/r02`, `results_aborted/` and the four `V_ns` video
runs. Its `.gitignore` excludes the CSVs and `derived/`, so what is published
is `terminal.log`, `params_effective/`, `about.txt` and `provenance.txt` only.

One artefact to know about: that run's `provenance.txt` records
`tree_state: dirty`, because the aborted archive had been moved aside in the
same working tree before the run started. The controller source and `params/`
were unchanged and match the campaign commit.

The wider question is whether the logs should be pushed anywhere at all, since
without them a session on another machine cannot regenerate a figure. The
smallest useful additions are `experiments/derived/metrics.csv` from
`Thesis_Final_Control` and one complete null-space run from `MyController`.
**Keep `MyController`'s calibration exclusion** in either case: its
`.gitignore` drops the measured plane and tool-axis files because those
coordinates are not to be published. `MyOwn/.gitignore` blocks no CSV, so this
repository is also a possible home, but then the scripts' `HERE/../experiments`
resolution means the data has to sit at `code/python/experiments/`.

### One figure-label edit, still open

Its input is on this machine. `make_coc_figures.py` resolves its data as
`HERE/../experiments`, so run it beside `Thesis_Final_Control/experiments/`
rather than copying the archive into this repository.

Two entries that stood here are gone. The `plot_setup_diagnostics.py` axis
labels went with the appendix section that included their figure, and the
Figure 5.10 y-axis was corrected in the pass that put the thesis symbols on
every plot axis; that figure now reads
\(\Delta\sigma_{\min,\mathrm{dist}}\) and \(E_N\).

**Make the source edits below first, then regenerate and copy the PDF back.**
Line numbers were checked on 2026-08-19.

**Editing warning.** Editing these `.tex` and `.py` files through an inline
shell script **silently corrupts backslashes**. Both of these failed here:
`python - <<'PY' ... PY`, where a quoted heredoc still stripped one backslash
level; and `sed -i 's/\\cref{/\\Cref{/g'`, which **reported success and changed
nothing**. Use a file-based script written by an editor, or an editing tool,
and verify by re-reading the file.

#### The remaining item: legends of Figures 5.2, 5.3 and D.1 — `code/python/figures/make_coc_figures.py`

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

### Correct the README claim about `make_coc_figures.py`

`code/python/figures/README.md` line 43 says the script "needs no data ... so it
runs anywhere". That is wrong: `main()` calls `load()`, which reads
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

- **The lever and the plotted centre position are now one signed quantity.**
  \(r_c\) was redefined on 2026-08-24 as \(p_c-p_{\mathrm{TCP}}\), \(d_c\)
  was removed from the thesis, and the coupling moment became
  \(m_{c,K}=r_c\times f_K\). The Case-H lever vectors flipped sign with the
  definition; the Case-D columns did not, because they already reported
  \(p_c-p_{\mathrm{TCP}}\). Both now read \(+40\,\mathrm{mm}\) for the
  selected \(+10^\circ\) condition about \(t_1\), which they did not before.
  **Labelling a `centre position` axis \(r_{c,t_2}\) is now correct.** The
  rule is recorded in `THESIS_WRITING_GUIDE.md` and the symbol list.

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
- **Rename the plotted centre coordinate to \(r_{c}\).** Figure 5.4's axes read
  `Centre position along t_2 [mm]`, which is correct in value but not in
  notation. The same applies to Table 4.3 and the Case-F, Case-G and Case-H
  tables. **The values and signs do not change**: under the redefined
  \(r_c=p_c-p_{\mathrm{TCP}}\) the plotted coordinate already is
  \(r_{c,t_i}\).
- **22, 23** — Figure 4.1 labels and caption, and the Figure 3.5 set-up
  symbols \(p_{\mathrm{Tool},0}\), \(p_{\mathrm{Tool},d}\),
  \(s_{\mathrm{set}}\), \(R_{\mathrm{clr}}\). Item 21, the Figure 4.2
  calibration notation, is done: the figure now runs one band per calibration
  and its symbols match Section 4.2, and all four set-up symbols are in the
  symbol list.
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

## The surface-plane re-seating check carries no measured values

Section 4.2.1 describes the calibration the code performs: one seated pose of
the complete tool face, with the plane normal formed from the end-effector axis
configured at the time — the nominal \(+Z_{\mathrm{EE}}\) for the stored plane —
and \(p_s=p_{\mathrm{EE}}+R_{\mathrm{EE}}r_{\mathrm{face,EE}}\).

**A repeat measurement is not expected to report a near-zero angle.** With the
calibrated tool normal now configured, the angle between the measured and the
stored normal carries the \(1.56^\circ\) between that normal and
\(+Z_{\mathrm{EE}}\). Record what the tool prints; do not treat that offset as
a fault in the stored plane, and do not overwrite `surface.conf` with the
measured values, which would stop the file describing the campaign.

The verification is defined in the text but carries no measured values, because
none is recorded anywhere in the controller repository. **Do not estimate one.**
Section 4.2.1 now names the four quantities the tool reports, in its own
notation: \(\psi_{\mathrm{plane}}\), the angle between the re-seated and the
stored normal; \(\Delta\alpha_s\) and \(\Delta\beta_s\), the same comparison per
axis; and \(\varepsilon_{\mathrm{plane}}\), the offset of the re-seated
tool-face centre from the stored plane. They map onto the tool's printed lines
as `total mismatch`, the `difference: a(x) | b(y)` row, and
`configured-plane offset`. Re-run `tools/measure_plane` with the face seated on
the plate that the stored values describe, read those four, and put them into
the paragraph after \Cref{eq:surface_plane_validation_residual}.
Should the plate have moved since the campaign, the check cannot be recovered,
and the paragraph stays as the definition of the check with that stated.

**The four hand-guided poses are correct and must not be "corrected".** The axis
in `params/tool_orientation.conf` came from the hand-guided calibration —
\(T_1\)--\(T_3\) for the fit and \(T_4\) held out — confirmed by the author on
2026-08-24. Section 4.2.2 and Figure 4.2 stay at four poses.

## The other drawn diagrams still open their boxes in lower case

`FIGURE_STYLE.md` now requires every line of node text in a drawn diagram to
begin with a capital, with lines that start with a symbol left as notation. The
rule was applied to `calibration_flow` when it was set, and the remaining TikZ
diagrams have not been through it: `controller_block_diagram` (`robot state`,
`phase machine`, `model`), `setup_schematic` (`compliance`), and any box text in
`phase_flow_chart`, `tool_transfer_flow`, `reference_frames`,
`compliance_lever_moment`, `moment_bookkeeping`, `three_points`,
`face_feature_selection`, `tool_face_plan_view` and `case_c_direction_rule`.

Capitalising a line widens its box, which can close the gap its arrows need —
that happened in `calibration_flow` and cost a column-spacing adjustment. Do
one diagram at a time and look at each in the compiled document before moving
on.

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
the text did not state it.

The logs to check are on the lab machine after all. Case F is `P3_axis_*`,
which stops at \(40\,\mathrm{mm}\), so the exploratory run is one of the
out-of-campaign series — `S5_normal_*` reaches \(90\,\mathrm{mm}\) and
`MyController` holds `B2_pole_normal_p120` and `MAIN_I3_rcn_p120`. Identify
which one the paragraph described before quoting either number again, and note
that `MyController` is the superseded controller.

The paragraph has been removed from Chapter 5. The Limitations section of
Chapter 6 now carries the defensible part without the numbers: the lever
magnitude is bounded by the joint-torque limits, and an exploratory
displacement beyond the reported Case-F range was stopped by one.

To close it: confirm what the \(12\,\mathrm{N\,m}\) figure refers to and
whether the \(15.1\,\mathrm{N\,m}\) value is a commanded or an applied
torque. If both are commanded values and libfranka handles the limit, say so in
one clause and the paragraph can go back.

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

## Later todos

Wanted, agreed, and deliberately not done yet. Nothing here blocks submission.

### Name the joints that carry the redundant motion, in Section 4.6

The chapter states that the commanded disturbance is a point force on link~3 at
\(r_p=[0,0,0.200]\,\mathrm{m}\), which is correct and matches every archived
run. It does not say which joints then move, and the answer is not the one a
reader expects: the base joint moves most.

The redundant direction for the reported posture is

    v_7 = [ 0.680, 0.008, -0.674, -0.00007, 0.236, 0.0002, -0.166 ]

printed by `make_nullspace_figure.py` when it resolves the reference axis. Over
the \(5\)--\(9\,\mathrm{s}\) disturbance interval of
`MAIN_NS7_baseline_20N_200mm/r01`, the net projected joint displacement is
\(+0.077\) and \(-0.076\,\mathrm{rad}\) at joints 1 and 3, then
\(+0.027\) at joint 5 and \(-0.019\) at joint 7 — a \(39\,\%\),
\(38\,\%\), \(13\,\%\), \(9\,\%\) split of the total motion, with joints 2, 4
and 6 contributing nothing measurable.

Joint~1 therefore carries the largest share regardless of where the disturbance
acts, because the Cartesian impedance holds the TCP and the surviving motion
has to lie along \(v_7\). One sentence saying so closes an examiner question
that the current text invites — the force is applied at link~3, yet link~1 is
what visibly swings.

The values above are computed, not estimated: recompute them from the archive
rather than copying them if the posture or \(q_{\mathrm{init}}\) ever changes.

### Record that the video trials are not the reported configuration

`Thesis_Final_Control/experiments/results/V_ns*` uses the same
`disturbance_link = 3`, but at \(40\,\mathrm{N}\) and a
\(150\,\mathrm{mm}\) offset on a faster timeline, against the reported
\(20\,\mathrm{N}\) at \(200\,\mathrm{mm}\). Nothing in either repository warns
a later session against taking a null-space number from them. The note belongs
next to the existing repository-authority rules in `code/AGENTS.md`.

### Thin the consequence links

`therefore` appears 104 times across the chapters and `because` 33, which is
the thesis's default and near-only link. The connector pass added contrast and
concession where the logic already carried them, but did not touch the
consequence links themselves. Reducing them is what would most improve the
monotony the author described; it means rewriting on the order of a hundred
sentences, so it was not started.
