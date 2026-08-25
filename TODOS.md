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
reported. The main A--D study contains \(37\) settings and \(111\) runs. The
four supporting checks in Appendix D contain \(18\) settings and \(54\) runs.
The Case-D run that
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

The mapping from main cases and supporting checks to directories, which should
not be re-derived:

| Study item | Settings | Run directories |
|---|---|---|
| A | 5 | `S1_none_00deg`, `P2_{t1,t2}_{pos,neg}_p000` |
| B | 4 | `A_rot_{t1,t2}_{15,50}` |
| C | 4 | `B_trans_{t1,t2}_{0300,0800}` |
| D | 24 | `P2_{t1,t2}_{pos,neg}_{m010,m020,m040,p010,p020,p040}` |
| Supporting orientation-offset magnitude | 4 | `P5_mag_{t1,t2}_{p000,p040}` |
| Supporting check 1: definition frame | 3 | `S3_surface_00deg`, `S3_surface_t1_10deg`, `S2_tool_00deg` |
| Supporting check 2: tool-axis displacement | 6 | `P3_axis_{m010,m020,m040,p010,p020,p040}` |
| Supporting check 3: intermediate tangent directions | 5 | `C_dir_{m45,p45}`, `C_fixed_{m45,p45}`, `C_fixed_t2` |

The `P2_*_{m080,p080}` directories and the `V_*`, `S4_*`, `S5_*`, `P4_*`,
`P6_*`, `P_*`, `AXS*`, `REVS2_*` and `PROBE60_*` series are exploratory and
outside the reported \(55\).

The aborted first attempt at `P2_t1_pos_m040/r02` was moved to
`experiments/results_aborted/P2_t1_pos_m040_r02_20260817/` so no analysis script
counts it. Its `README.md` says what it was. Do not delete it and do not move it
back.

### Building on the lab machine, and the one thing it cannot check

`texlive-lang-german` is installed, so `ngerman.ldf` resolves and the document
builds. All three drivers were built on 2026-08-25 after the review
corrections, with bibtex and three passes each: no errors, no undefined
references or citations, no overfull boxes. `Thesis.pdf` and
`Professor_Draft.pdf` are 128 pages and `Review_Draft.pdf` is 132. The fifty
underfull hboxes in the final pass are loose lines in the narrow description
column of the symbol list and predate this work.
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

## Final examiner-level review: the standing work list

A complete final review was requested before supervisor submission, in two
passes — technical/notation first, then language, figures, captions and
layout. The items below are what that review has not yet reached. They are
ordered as the review specification numbered them, so an item can be matched
back to its specification.

The full specification, items 1 to 76, has been received; nothing further is
outstanding from the author on that front.

### Verified during the review and needing no change

- **`p_CoC` and `r_eff` in Appendix B are consistent** with
  \(r_c=p_c-p_{\mathrm{TCP}}\): the appendix gives
  \(p_c=p_{\mathrm{TCP}}+r_c\) and \(r_{\mathrm{eff}}=p_{\mathrm{Tool}}-p_c\). `r_eff` is a
  CSV column only and stays a data identifier, per item 49.

### Settled at source, and binding on the remaining figure work

- **The lever and the plotted centre position are now one signed quantity.**
  \(r_c\) was redefined on 2026-08-24 as \(p_c-p_{\mathrm{TCP}}\), \(d_c\)
  was removed from the thesis, and the coupling moment became
  \(m_{\mathrm{cpl},K}=r_c\times f_K\). The supporting intermediate-direction
  vectors flipped sign with the
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

- **The two configuration branches now carry the same sign.** Both define
  \(r_c=p_c-p_{\mathrm{TCP}}\). Confirmed in
  `Thesis_Final_Control/surface_grinding_controller`:
  `src/control/cartesian_impedance.cpp` forms
  \(r_c=R_{\mathrm{EE}}\,\texttt{compliance\_center\_offset\_ee}\) on the
  tool-frame branch and
  \(r_c=R_{\mathrm{base,surface}}\,\texttt{compliance\_lever\_surface}\)
  on the surface-frame branch, and `params/setup.conf` documents both in the
  same words.

  **The earlier "opposite in sign" reading is withdrawn**, and so is the
  parameter name it quoted. The tool-frame negation went on 2026-08-24 with
  `Define the compliance lever from the TCP to the centre`, and the
  surface-frame key was renamed from `r_tcp_from_compliance_center_surface` to
  `compliance_lever_surface` on 2026-08-25 with `Command the surface-frame
  lever as r_c`, which dropped its negation at all four read sites and negated
  the value in every setup overlay to leave the same physical lever. The old
  key is no longer read; a missing key falls back to zero.

### Remaining work that can be done on this machine

None of the following needs the lab machine. Completed items have been deleted
from this list rather than annotated, so everything here is still open.

**Prose and technical (review pass 1)**

- **4** — keep the three moment concepts separate throughout, and never add
  \(m_{r_T}\) to \(m_0\) or \(m_{\mathrm{cpl},K}\). Spot-check rather than rewrite.
- **48** — Appendix C must state the two configuration branches
  (`compliance_center_offset_ee` in end-effector axes,
  `compliance_lever_surface` in surface axes) rather than calling both "centre
  displacement". Both now define \(r_c=p_c-p_{\mathrm{TCP}}\), so the wording
  no longer has a sign difference to explain, only a frame difference. The rule
  is already recorded in `THESIS_WRITING_GUIDE.md`; only the appendix wording
  remains.
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

- **A.4** — Figure 3.1 still shows `spring wrench`, `tau_task` and `c(q,qdot)`.
  Correct to the Cartesian impedance wrench, \(\tau_{\mathrm{cart}}=J^\top F\)
  and \(\tau_c\). It is a TikZ source and needs no data.
- **22, 23** — Figure 4.1 labels and caption, and the Figure 3.5 set-up
  symbols \(p_{\mathrm{Tool},0}\), \(p_{\mathrm{Tool},d}\),
  \(s_{\mathrm{set}}\), \(R_{\mathrm{clr}}\). Item 21, the Figure 4.2
  calibration notation, is done: the figure now runs one band per calibration
  and its symbols match Section 4.2, and all four set-up symbols are in the
  symbol list.
- **31, 33, 34, 37, 38** — the remaining pgfplots figures and their tables:
  Figures 5.1, 5.4 and the supporting-check figures in Appendix D are `.tex`
  sources and can be edited directly. Figure 5.4 now carries sample-standard-
  deviation error bars, and its duplicate appendix spread plot has been
  removed.
- **44** — global table-unit audit across the main results and Appendix-D
  numerical tables.
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

## The appendix listings have drifted from the controller source

Checked on 2026-08-25 against
`Thesis_Final_Control/surface_grinding_controller`. Only the four appendices
`Thesis.tex` still inputs were checked; `appendix_a` to `appendix_f` are
commented out and were left alone. Each item below is a place where the
document states something the source no longer does.

The \(r_c\) items are done and have been removed from this list: the
`lst:app_spring_wrench` listing and the paragraph above it now match the
renamed key and its dropped negation, and the superseded ruling in
`THESIS_WRITING_GUIDE.md` was replaced rather than annotated. What follows is
the drift that predates the \(r_c\) work and is still open.

The compiled Appendix A now contains only the CoC point-shift and core callback
listings. The following archived listings are inside `\iffalse` and reach no
reader; correct them if they are ever reinstated.

**`backmatter/appendix_code.tex`**

- **Listing `lst:app_desired_motion`, the set-up case.** Calls
  `setUpPush(params, phase_time - gate_grind_paused_time, ...)`. The function
  is `setupPush` and it takes `phase_time`; `gate_grind_paused_time` was
  deleted on 2026-08-13 with `Keep pressing through the grinding gate`, so the
  set-up ramp deliberately runs on the live phase clock and keeps pressing to
  the configured final penetration while the grinding gate waits. The prose
  after the listing is still correct — both gates do latch, and the frozen
  clock it describes is the *descent* clock, `gate_paused_time`, which is still
  there.
- **The paragraph after `lst:implementation_nullspace_projector`** says the
  routine "fills a diagnostics structure that carries the sampled singular
  values, the selected direction, and the projected joint velocity
  \(\dot q_{\mathrm{null}}\) into the recorded data". The present
  `computeNullspaceTorque` in `src/control/robot_support.cpp` returns a `Vec7`
  and takes no diagnostics argument, so the sentence does not describe the
  source as it now stands. **It does describe the build that recorded the
  reported null-space runs**, whose logs carry every one of those signals, so
  this is a question of which state the appendix documents and not a plain
  error. Settle that before editing it.

**`backmatter/appendix_data_logging_format.tex` documents two generations of
the log format at once, and this needs a decision rather than a correction.**
An earlier note here claimed the sigma columns had never existed and should be
deleted. **That was wrong and is withdrawn**: it came from reading the current
writer instead of the archived logs. The header of
`MAIN_NS7_baseline_20N_200mm/r01/logs/surface_grinding_controller_log.csv`
carries `sigma_current`, `sigma_plus`, `sigma_minus`, `sigma_difference`,
`sigma_direction`, `nullspace_dq_1..7`, `tau_sigma_1..7` and `tau_sigma_norm`,
which is where the reported redundant-motion and \(\sigma_{\min}\) values come
from. Those runs also spell the angular columns `alignment_error_*_deg` and
`alignment_angle_deg`.

The current `src/report/csv_logging.cpp` writes a different 99-column set: no
sigma group, the angular columns spelled `angular_deviation_*_deg`, and
`p_CoC`, `r_eff` and `t_align` added. The appendix table is the union of the
two and says so nowhere. `disturbance_torque_scale` is in the current writer
and in the null-space logs, and is documented in neither the appendix nor this
note's earlier version.

**Two things are still unverified.** Whether the archived contact runs carry
the current spelling or the older one was not checked, and neither was the
claim at the sigma row that those columns are "recorded in every mode,
including when no torque is commanded". Check both against a contact-run
header before rewriting the table.

**`backmatter/appendix_controller_parameters.tex` line 162** gives
`pause_before_set_up`. The key is `pause_before_setup`.

Nothing here is blocked. The listings carry no `\Revised{}` wrappers, so no
frozen text is in the way, but both appendices carry green assessment boxes
and neither chapter has been declared revised — confirm before editing.

## Remaining requests from the supervisor narrative review

The compression pass completed the requested Chapter-1 numerical reduction,
the Chapter-2 null-space roadmap and derivation compression, the Chapter-3
operator/tool-handling reduction, the Chapter-6 wording changes, and the
Appendix-A reduction. The following narrower requests remain:

**Chapter 4.**

- Say whether \(v_{\mathrm{ref}}\) in 4.6 comes from one nominated repetition
  of the no-null-space-torque condition or from all three. One sentence.

## Two retired appendices still carry `\approx`

`\approx` is banned document-wide and the compiled thesis now contains none —
verified by extracting the text of `Thesis.pdf` and finding zero of the glyph.
Two files are outside that count because `Thesis.tex` does not input them:
`backmatter/appendix_a_panda_example.tex` (four) and
`backmatter/appendix_c_exp1_rotated_tracking.tex` (two). They are the retired
standalone experiment appendices and reach no reader while they stay commented
out. **If any of `appendix_a` to `appendix_f` is ever reinstated, clear its
`\approx` first**, by the four routes recorded under the ban in
`THESIS_WRITING_GUIDE.md`.

## Finish the figure-label convention and redesign the appendix tables

The axis and legend convention is recorded in `FIGURE_STYLE.md` and was applied
on 2026-08-25 to the four pgfplots figures and to the five plots written by
`make_coc_figures.py` and `plot_coc_case.py`, which were regenerated and
installed. Three things remain.

- **Redesign the appendix results tables**, which is where the author chose to
  keep them on 2026-08-25 rather than restoring them to Chapter 5. Every table
  in `backmatter/appendix_additional_plots.tex` should answer, without the
  reader going back to Chapter 4: what was varied, what was held fixed, what
  the reference condition is, and what was measured. Concretely: name the
  varied parameter in its column heading rather than `Varied entry`, mark the
  reference condition in the table itself (`Case-A reference`, or the
  TCP-centred column), and give the measured response as
  `Measured Set-Up Rotation, \(\Delta\theta_i\) [°]`. Precede each table
  with one prose sentence naming varied, fixed, reference and response. The
  Case-D table additionally drops the \(\theta_{\mathrm{dev,before}}\)
  column and marks its TCP column, and the offset-magnitude table gains a
  TCP-versus-selected-CoC comparison column.

## Deferred figure work from the narrative reviews

The reviews of 2026-08-25 called these improvements rather than blockers, and
each was left as the reviewer framed it. The prose corrections they asked for
are done and are not listed here.

**The null-space generator can be run on this machine**, which an earlier note
here denied. `make_nullspace_figure.py` resolves its data from the directory
above its own, so it finds nothing under `code/python/figures/`. Stage it
instead: make a scratch directory holding `analysis/` and `experiments/`, copy
`make_nullspace_figure.py`, `make_figures.py`, `figure_style.py` and
`extract_metrics.py` into `analysis/`, and symlink `experiments/results` to
`MyController/experiments/results`. Run it from `analysis/`; it writes the
figure to `figures/` and the derived summary to `experiments/derived/`
alongside. Two checks confirm the pipeline before trusting an output: it prints
the recovered redundant axis, which must match the \(v_7\) recorded further
down this file, and `MAIN_NS_automatic_summary.csv` must reproduce the
\(\Delta\eta_{\mathrm{dist}}\) and \(\Delta\sigma_{\min,\mathrm{dist}}\)
values already in Section 5.2. Both held on 2026-08-25.

- **Figure 5.5 repeats its three-entry legend in all three panels.** One shared
  legend above the panels would return the plotting area the three copies take.
  The generator is `plot_coc_case.py`, which draws a legend per panel by
  design — its docstring says so — so this is a change to that design and not a
  parameter. It reads the run logs under
  `Thesis_Final_Control/experiments/results`, which are present on the lab
  machine, and the three trials are the ones in
  `code/python/figures/README.md`. Regeneration on this machine reproduces the
  installed files faithfully: the toolchain here is the one that made them,
  `usetex` is off in `figure_style.py`, and a regenerated file differs from its
  installed copy only in the PDF creation date. Check the result at printed
  width before installing it.
- **Figure 3.3 is the densest main-text diagram.** The suggestion is to let the
  central path dominate — orient, approach, set-up, pre-grinding gate,
  grinding — and to collect pose hold, set-up hold and manual guidance into one
  side box labelled as operator modes. It is a TikZ source and needs no data.
- **Figures 3.1 and 2.2 are small for what they carry.** Figure 3.1 would take
  about ten to fifteen per cent more width if the page allows, and Figure 2.2
  draws \(r_c\), \(f\) and \(m\) smaller than their importance to the argument.
  Appendix Figures D.4 and D.6 are the same case. Both reviews raised the
  sizing and neither called it a fault. The `\resizebox` section below governs
  how to make the change.
- **A final language and proofreading pass over the whole document**, which the
  second review put after the targeted corrections and before submission. It is
  the last two items of the review work list further up, not a separate task.

The second review also asked for the Chapter 5 null-space section to be split
into subsections, the Case-D definition frame to be stated in Chapter 4, the
calibration consequence to be spelled out in Section 4.2, the singular-value
units to be corrected, the Figure 5.5 sign bridge, and the Section 4.5.1
rewrite. All six are done, and the rulings behind them are in
`THESIS_WRITING_GUIDE.md` and `FIGURE_STYLE.md`.

**One decision was made and then reversed, and the reversal stands.** The
direction-comparison axis was briefly shortened to `Commanded Rotation
Direction` on the grounds that its ticks are categorical, then restored to
`Commanded Rotation Direction, \(\theta_{\mathrm{tilt}}\) [°]` the same day:
uniformity of the `Descriptive Name, Symbol [Unit]` format across every axis
matters more than the categorical exception. `FIGURE_STYLE.md` carries the
reasoning on both sides so it is not re-argued.

## The other drawn diagrams still open their boxes in lower case

`FIGURE_STYLE.md` now requires every line of node text in a drawn diagram to
begin with a capital, with lines that start with a symbol left as notation. The
rule was applied to `calibration_flow` when it was set, and the remaining TikZ
diagrams have not been through it: `controller_block_diagram` (`robot state`,
`phase machine`, `model`), `setup_schematic` (`compliance`), and any box text in
`phase_flow_chart`, `tool_transfer_flow`, `reference_frames`,
`compliance_lever_moment`, `moment_bookkeeping`,
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

The logs to check are on the lab machine after all. Supporting check 2 is
`P3_axis_*`,
which stops at \(40\,\mathrm{mm}\), so the exploratory run is one of the
out-of-campaign series — `S5_normal_*` reaches \(90\,\mathrm{mm}\) and
`MyController` holds `B2_pole_normal_p120` and `MAIN_I3_rcn_p120`. Identify
which one the paragraph described before quoting either number again, and note
that `MyController` is the superseded controller.

The paragraph has been removed from Chapter 5. The Limitations section of
Chapter 6 now carries the defensible part without the numbers: the lever
magnitude is bounded by the joint-torque limits, and an exploratory
displacement beyond the reported supporting-check range was stopped by one.

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
panel (a) is a few points taller than the file it replaces. The compressed
kinematics and null-space theory, the symbol list, the main Case-D figures, and
all Appendix-D tables and figures have been inspected on screen. The remaining
changed Chapter-1, Chapter-4, Chapter-6, summary, and null-space-result pages
still need the complete page-by-page read. Two specific things to retain in
that pass:

- **The Abstract and the Kurzfassung now run to two pages each** (Abstract on
  pages V--VI, Kurzfassung on VII--VIII). The one-page limit is suspended in
  `THESIS_WRITING_GUIDE.md`, so this is allowed rather than a fault, but it is
  a visible change and should be seen before submission. If the limit is
  restored, the fixed-centre definition and the direction-independence
  paragraph are the material that has to displace something older.
- No heading was left stranded by an automated scan of the compiled document,
  which is a weaker check than reading the pages.
- **The review corrections of 2026-08-25 moved a further set of pages**, and
  none has had the page-by-page read. They are: the end of Section 2.4.1, which
  gained the bridge to the compliance-centre section; Section 4.2, which gained
  the calibration-consequence paragraph; Section 4.4, which gained the
  tool-fixed definition-frame statement; Section 4.5.1, whose provenance and
  sign paragraphs were rewritten; the opening of Chapter 5 and its Case-A and
  Case-D commentary; the null-space results, now split into three subsections
  and therefore repaginated from Section 5.2 onward; the three Appendix-D
  tables that gained standard deviations; and both summaries, which lost the
  sentence carrying their only measured values. Figure D.5 was regenerated with
  a categorical \(x\)-axis label and should be looked at on the page. The
  bibliography's contents entry now names the page it starts on, so the
  contents and the appendix page numbers after it moved by one.
- **The null-space figure gained a third panel** carrying the net redundant
  displacement of all four settings, so Section 5.2 onward repaginated again
  and the document is 128 pages. The page was rendered and read at 100 dpi
  when the panel was added; the rest of the moved pages were not.

All three drivers build clean here with bibtex
and three passes each, no undefined references or citations and no overfull
boxes; `Review_Draft.tex` was rebuilt on 2026-08-25 and its soul spans still
reconstruct.
**The local builds needed
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
