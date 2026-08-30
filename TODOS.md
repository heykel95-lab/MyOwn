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

The \(52\) reported settings each carry three repetitions. The two
`B_combined_{t1,t2}` settings and the three surface-fixed definition-frame
settings were removed from the report. This takes the campaign from \(57\)
settings and \(171\) runs to \(52\) and \(156\); their run directories stay
in the archive and are simply not reported. The main A--D study contains
\(37\) settings and \(111\) runs. The three supporting checks in Appendix D
contain \(15\) settings and \(45\) runs.
The Case-D run that
Section 4.3.4 once recorded as excluded was re-recorded on 2026-08-19 under a
byte-identical parameter set, so the count is \(156\) of \(156\) and the chapter
says so. **Do not reintroduce an excluded-run sentence.**

The archive lives on the lab machine at
`Thesis_Final_Control/experiments/results/`, \(171\) archived run directories
(the \(156\) reported plus the fifteen no longer reported) each with
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
| Supporting initial-deviation magnitude | 4 | `P5_mag_{t1,t2}_{p000,p040}` |
| Supporting check 1: tool-axis displacement | 6 | `P3_axis_{m010,m020,m040,p010,p020,p040}` |
| Supporting check 2: intermediate tangent directions | 5 | `C_dir_{m45,p45}`, `C_fixed_{m45,p45}`, `C_fixed_t2` |

The surface-fixed `S3_surface_*` and `S2_tool_00deg` directories, the
`P2_*_{m080,p080}` directories, and the `V_*`, `S4_*`, `S5_*`, `P4_*`,
`P6_*`, `P_*`, `AXS*`, `REVS2_*` and `PROBE60_*` series are exploratory and
outside the reported \(52\).

The aborted first attempt at `P2_t1_pos_m040/r02` was moved to
`experiments/results_aborted/P2_t1_pos_m040_r02_20260817/` so no analysis script
counts it. Its `README.md` says what it was. Do not delete it and do not move it
back.

### Building on the lab machine, and the one thing it cannot check

`texlive-lang-german` is installed, so `ngerman.ldf` resolves and the document
builds. All three drivers were built on 2026-08-25 after the review
corrections, with bibtex and three passes each: no errors, no undefined
references or citations, no overfull boxes. `Thesis.pdf` and
`Professor_Draft.pdf` are 125 pages and `Review_Draft.pdf` is 129. The fifty
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

### Remaining work that can be done on this machine

None of the following needs the lab machine. Completed items have been deleted
from this list rather than annotated, so everything here is still open.

- **The pulled controller and thesis use opposite compliance-lever signs.**
  The thesis defines \(r_c=p_c-p_{\mathrm{TCP}}\). At pulled revision
  `f54b7a5`, `surface_grinding_controller/src/control/cartesian_impedance.cpp`
  instead forms \(r_c=p_{\mathrm{TCP}}-p_c\): it negates the tool-frame centre
  offset and reads `r_tcp_from_compliance_center_surface` directly. The
  terminology refactor deliberately did not change this behaviour. Reconcile
  the source, parameter overlays and Appendix A together before the controller
  is treated as the implementation of the thesis convention; the choice is
  blocked on confirmation because changing it reverses the coupled moment.

**Prose and technical (review pass 1)**

- **4** — keep the three moment concepts separate throughout, and never add
  \(m_{r_T}\) to \(m_0\) or \(m_{\mathrm{cpl},K}\). Spot-check rather than rewrite.
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

- **22** — Figure 4.1 labels and caption. Item 23, the contact-establishment figure, is done:
  it now carries \(p_{\mathrm{Tool,clearance}}\), \(p_{\mathrm{Tool},0}\),
  \(s_{\mathrm{set}}\), \(p_d\) and the TCP with its rigid offset. Item 21,
  the Figure 4.2
  calibration notation, is done: the figure now runs one band per calibration
  and its symbols match Section 4.2, and all four contact-establishment symbols are in the
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

Nothing here is blocked. The listings carry no `\Revised{}` wrappers, so no
frozen text is in the way, but both appendices carry green assessment boxes
and neither chapter has been declared revised — confirm before editing.

## The contact-establishment reference figure does not follow FIGURE_STYLE

`figures/setup_reference.tex` draws in grey, uses a `densely dotted` projection
line, and opens its node text in lower case — `surface`, `selected point at
clearance`, `commanded endpoint`. All three are ruled against: grey is not a
drawing colour, every line is solid, and node text begins with a capital. It
was left alone during the 2026-08-26 Chapter 3 restructure because that pass
was about text, and the figure is correct in content. Fix it with the other
diagrams listed under the lower-case and `\resizebox` entries below, not on its
own.

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

- **The appendix results tables are done, and the caption half of that item is
  superseded.** The column headings, the marked reference conditions, the
  dropped \(\theta_{\mathrm{dev,before}}\) column and the offset-magnitude
  comparison column are all in place, and the last generic heading,
  `Varied Entry`, became `Varied Translational Entry` on 2026-08-27. The part of
  the item that asked for a prose sentence naming varied, fixed, reference and
  response before every table **is withdrawn**: the author's appendix pass of
  2026-08-27 requires short noun-phrase captions and only the minimum
  observation, and the tables already show the reference condition in a column
  or a bold heading. The replacement rule is under *The appendices: document and
  support* in `THESIS_WRITING_GUIDE.md`.

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
into subsections, the Case-D displacement frame to be stated in Chapter 4, the
calibration consequence to be spelled out in Section 4.2, the singular-value
units to be corrected, the Figure 5.5 sign bridge, and the Section 4.5.1
rewrite. All six are done, and the rulings behind them are in
`THESIS_WRITING_GUIDE.md` and `FIGURE_STYLE.md`.

**One decision was made and then reversed, and the reversal stands.** The
direction-comparison axis was briefly shortened to `Commanded Rotation
Direction` on the grounds that its ticks are categorical, then restored to
`Commanded Rotation Direction, \(\theta_{\mathrm{cmd}}\) [°]` the same day:
uniformity of the `Descriptive Name, Symbol [Unit]` format across every axis
matters more than the categorical exception. `FIGURE_STYLE.md` carries the
reasoning on both sides so it is not re-argued.

## The other drawn diagrams still open their boxes in lower case

`FIGURE_STYLE.md` now requires every line of node text in a drawn diagram to
begin with a capital, with lines that start with a symbol left as notation. The
rule was applied to `calibration_flow`, `phase_flow_chart` and
`controller_block_diagram`. The remaining TikZ diagrams have not been through
it: `setup_schematic` (`compliance`), and any box text in
`tool_transfer_flow`, `reference_frames`,
`compliance_lever_moment`, `moment_bookkeeping`, `tool_face_plan_view` and
`case_c_direction_rule`.

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

The same wrapper is still on `controller_block_diagram`, `tool_transfer_flow`,
`setup_schematic`, `calibration_flow`, and the two appendix parameter tables.
A diagram that is *shrunk* by the wrapper has the
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

## The commanded-against-estimated wrench plot needs a log from the lab machine

Requested on 2026-08-28: a figure comparing the commanded Cartesian wrench with
the model-estimated external wrench, with the CSV it is drawn from. **It cannot
be produced away from the lab machine.** The estimate is
`external_force_x..z` / `external_moment_x..z`, written only by the current
`surface_grinding_controller` schema, and that schema exists on this machine
nowhere: `Thesis_Final_Control` here holds source only, with no `experiments/`
directory at all, and the fifty-nine log CSVs recoverable from the
`MyController` history are all the earlier development schema, which logs
`f`/`m` and `tau_raw`/`tau_limited` but carries no external-wrench column. This
is the clone limitation the archive section above already records, confirmed
against both repositories.

The generator is written and tested, so only the data is missing:
`code/python/figures/plot_commanded_vs_estimated_wrench.py` takes one log and
emits `commanded_vs_estimated_wrench.pdf` (force panel then moment panel,
magnitudes, commanded black against estimated red) and a matching CSV carrying
the raw components as well as the plotted magnitudes. Its current `--phase 2`
option selects Contact Establishment in archived logs; rename that interface
to `--state` when the generator is next updated, while retaining the old CSV
column as an input fallback. `--bias-corrected` selects the
clearance-referenced estimate.

`professoremail/` in this repository is the folder the two files are meant to
reach the professor in. It currently holds the generator, `figure_style.py` and
a README stating what is missing and the one command that fills it.

To close it: copy one `logs/surface_grinding_controller_log.csv` from a run
directory under `Thesis_Final_Control/experiments/results/` into
`professoremail/` and run the script there. Decide at that point whether the figure is for the thesis or for
the author's own checking; if it enters the thesis, the sign convention needs
stating, because the estimate opposes the commanded wrench in steady contact.

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
  tool-fixed displacement statement; Section 4.5.1, whose provenance and
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
  when the panel was added; the rest of the moved pages were not. After the appendix
compression of 2026-08-27 the document is 126 pages.
All three drivers build clean here with bibtex
and three passes each, no undefined references or citations and no overfull
boxes; `Review_Draft.tex` was rebuilt on 2026-08-25 and its soul spans still
reconstruct.
**The local builds needed
`compat=1.16`**, because the TeX Live 2019 on this machine predates the
`compat=1.18` the sources set; the file was restored afterwards and the plots
were therefore not rendered at the compat level the author's MiKTeX uses.
Rebuild there before judging any figure.

## What the Abstract-to-Conclusion consistency pass checked, and what it found

Run on 2026-08-27 over the whole document. Nine checks were made and the
findings are listed so the pass is not repeated blind.

**Clean, and needing no change.** The clearance family \(h_i\),
\(h_{\mathrm{Tool}}\), \(h_{\mathrm{clearance}}\) and
\(\varepsilon_{\mathrm{sel}}\) is used consistently and carries four
symbol-list rows; no withdrawn spelling survives anywhere
(`\varepsilon_{\mathrm{tie}}`, `\ell_i`, `h_{\mathrm{face}}`,
`n_{\mathrm{flat}}`, `\rho_c`, `R_{\mathrm{task}}`, `f_K`, `d_c`, `clr`,
`vertex` all return zero). \(p_{\mathrm{Tool}}\), \(p_{\mathrm{TCP}}\)
and \(p_c\) are never crossed, and nothing says the compliance centre moves
the force. The external wrench is `model-estimated` at all three of its
mentions and is never called measured. Grinding reads as implemented but not
entered in Chapters 1, 3, 4, 5 and 6. After removal of the definition-frame
experiment, the run counts reconcile: \(37+15=52\) settings,
\(111+45=156\) runs, \(4+6+5=15\) supporting settings and
\(12+18+15=45\) supporting runs, plus twelve pose-hold runs for \(168\).
The three `longtable` references all use literal `Table~\ref`, and no `\ref`
key in the compiled document is undefined. The only digit in the summaries is
`7-achsigen`, which names the degrees of freedom rather than measuring
anything.

**Four defects were found and fixed.** Chapter 3 pointed the reader at
Section 3.3 for the definition of \(\tau_{\mathrm{null}}\), which is
Cartesian pose hold; it now points at Section 2.8.4, where the complete torque
is derived. Chapter 5's opening named the primary quantity twice, three lines
apart, and defined it as the `current-to-reference relative rotation formed
from the measured orientations at the beginning and end of Contact Establishment` — both the
christened convention and the second measured pose that the guide rules
against. Chapter 4 said `the measured alignment rotation`. Appendix C wrote the
selection tolerance as \(10^{-4}\,\mathrm{m}\) where its home in Chapter 4
writes \(0.1\,\mathrm{mm}\). All four are corrected and the rulings are in
`THESIS_WRITING_GUIDE.md`.

## Two things the appendix compression left open

The appendix pass of 2026-08-27 cut Appendix A to its listings, deleted
Appendix B's `Evaluation Quantities` section, replaced Appendix C's damping and
compliance-centre prose with one table, and reduced each Appendix D section to
its table, figure and equations plus one observation. The rulings are in
`THESIS_WRITING_GUIDE.md` under *The appendices: document and support*. Two
items were seen during that pass and not fixed.

- **The manual-guidance rows in Appendix C were left in.** Under the principle
  that Appendix C holds only what reproduces the reported runs, the
  `Manual guidance` gain row and the `manual_guidance_damping` operating row
  are candidates for removal: every reported run started from the configured
  initial joint posture rather than from a guided pose. They were kept because
  whether manual guidance was used to seat the tool before a run could not be
  verified from this repository, and the author did not list them among the
  removals. Decide and remove or keep in one step.
- **Appendix A does not attribute its listings.** *Originality* in
  `THESIS_VOICE.md` requires an appendix listing that descends from the
  libfranka examples to say so, and `libfrankaCartesianExample` is cited only in
  Section 2.4.3. Decide whether the compliance-shift and callback excerpts
  descend from that example before adding a clause; if they do, one sentence in
  the chapter lead is the whole fix.

## Align the controller source with the state-machine terminology

The controller repository was pulled to `f54b7a5`, and the active terminology
refactor is complete. `operator_hold_states.conf` and
`contact_establishment.conf` replace the two retired parameter files. The
operator holds are explicit pre-contact and pre-grinding states, active source
and configuration use state names, new CSV files use `state`, and analysis
retains compatibility for archived files. Python syntax, shell syntax and the
schema-compatibility fixtures passed. Cppcheck completed with only the
pre-existing performance and style findings. The Makefile resolves every
renamed source before it reaches the missing lab dependency.
The real C++ build and state-transition test remain blocked on this Windows
clone because the Makefile requires the lab tree at
`/home/hm-panda/libfranka`, including `examples/examples_common.cpp`. Run that
build and a non-contact transition test on the lab machine before deleting
this entry or deploying the controller.

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

### Measure the physical surface angle independently

The controller archives provide the pose-based initial angular deviation from
the configured surface reference, and that quantity is now used for the
experimental condition. They do not provide an independent physical surface
normal for the reported campaign, and the instantaneous tool rotation relative
to the gripper was not tracked under contact load. A run-wise physical
tool--surface angle therefore cannot be reconstructed from the existing logs.

A follow-on measurement must record the physical plane normal independently of
the mounted tool and track the tool face relative to the end effector during
contact. Only then can the physical initial angle and its change replace the
pose-based reference-relative quantities in the experimental evaluation.

### Name the joints that carry the redundant motion, in Section 4.6

Requested on 2026-08-26 and still unwritten: one sentence in Section 4.6
naming the joints that carry the redundant motion. The values it needs are
below, so nothing blocks it.

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

### Decide whether the leading-feature cases carry worked numbers

Section 3.2.3 now states the corner-clearance criterion
\(h_i-h_{\mathrm{Tool}}\le\varepsilon_{\mathrm{sel}}\), the averaging, and the
principal one-, two- and four-corner outcomes, with
\Cref{fig:leading_feature_cases} drawing one panel per outcome. It does not
claim that these cases are exhaustive, because the non-zero tolerance can also
admit a three-corner group. The worked projection values that came with the
request — four corner clearances per case, such as
\(15.0\), \(13.0\), \(10.0\) and \(8.0\,\mathrm{mm}\) for the leading-corner
case — were **not** written in, because no such clearances were recorded and
*State the levels actually tested, never an illustrative sweep* rules against a
hypothetical set of numbers in the running text.

If the author wants them anyway, the defensible routes are to compute them from
the calibrated face geometry at a stated commanded orientation offset, which
makes them derived rather than invented, or to place them in the code appendix
as a worked example labelled as such. Blocked on that decision.

### The direction figure was regenerated on this machine, and its embedded font changed

`figures/MAIN_H_direction.pdf` carried the axis symbol in its glyphs, so the
\(\theta_{\mathrm{tilt}}\to\theta_{\mathrm{cmd}}\) rename could not be made in
the `.tex` alone. `make_coc_figures.py` needs no data for that figure — its four
pairs of values are written into the script — so the label was corrected at
line 199 and the figure regenerated here.

The extracted text of the new file matches the old one apart from the symbol,
and the rendered bars, ticks, legend and axes are unchanged. **One thing does
differ**: the embedded font set moved from `LMRoman7-Regular` to
`LMRoman8-Regular`, because this machine's matplotlib resolves a different
optical size for the small text. `FIGURE_STYLE.md` says a regenerated figure
differing in anything but the intended label is a signal to stop, so the
decision to install it anyway is recorded here rather than left silent. The
previous binary was kept only in this session's scratch directory; regenerate
from the script on the original machine if the older font set is wanted back.
