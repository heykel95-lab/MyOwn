# Open items

This file contains only agreed work that remains unfinished. Completed items are
removed in the turn in which they are finished.

## Confirm the material the new summaries dropped is carried elsewhere

The supplied Abstract and Kurzfassung of 2026-09-04 dropped three things the
previous versions carried, and each needs a home in the body or a decision that
it is not needed. One remains open.

- The rotational-stiffness interval that produced the \(64\,\%\) reduction.
  Chapter 5 reports it; confirm the Conclusion still states it, since the
  Abstract no longer does.

The third is settled: Cartesian position retention left both
summaries on 2026-09-05, and Section 5.2.2 was checked the same day — it
carries \(0.889\) and \(0.983\,\mathrm{mm}\), the largest value of
\(1.304\,\mathrm{mm}\), and the \(2\,\mathrm{mm}\) limit. Nothing was lost with
the sentence.

## Remove the duplicate TCP expansion in Chapter 2

`chapters/02_theoretical_background.tex:760` spells out `tool centre point
(TCP)`. Since 2026-09-04 Chapter 1 spells it out first, at the \(r_c\)
sentence, so the Chapter 2 parenthesis is a second introduction. The duplicate
predates the change — the old Abstract expanded TCP as well — so this is
tidying rather than a fault. Drop the parenthesis in Chapter 2 and leave the
words.

## Reconcile the Tool Orientation timeout with the run archive

Changed to \(5.0\,\mathrm{s}\) on 2026-09-02 by the author's decision, in
Table 4.3 and in
`Thesis_Final_Control/surface_grinding_controller/params/approach.conf`. The
change to the controller parameter file is committed and pushed on the
branch `nullspace-disturbance-video`, at `e4241ea`; `main` still carries
\(8.0\,\mathrm{s}\). Figure 3.3 no longer states either value: both its timeout arrows
now read `timeout` alone, under the rule in `FIGURE_STYLE.md` that a state
chart names a timeout without valuing it, so the figure is no longer a place
this decision has to be kept in step.

The reported campaign ran at \(8.0\,\mathrm{s}\): every one of the 101
archived `P2_*` runs records `approach_orient_timeout = 8.0` in its
`params_effective/approach.conf`, and those files are the record of what was
executed and are not edited. The thesis therefore states a value the archive
does not support until the campaign is repeated at \(5.0\,\mathrm{s}\).
`THESIS_WRITING_GUIDE.md` records the decision under *Cross-chapter factual
consistency* so that a consistency pass does not revert it.

Either repeat the campaign at \(5.0\,\mathrm{s}\) and re-derive the reported
values, or decide that the stated value describes the controller as it now
stands rather than the runs, and say which in Section 4.3.

## Decide `signed` in Section 3.2.5

`THESIS_WRITING_GUIDE.md` bans `signed` as a modifier in prose, headings,
captions, axes and tables, because the equation and displayed values establish
the algebraic direction. One supplied use remains in Section 3.2.5:
`chapters/03_software_implementation.tex` says `signed distance` in the sentence
after Equation 3.18, supplied on 2026-09-04 and applied verbatim.
`the distance of the desired tool point from this plane along the
surface-normal direction` would satisfy the rule, since Equation 3.16 gives the
negative initial value and Equation 3.18 fixes the direction. The author must
settle this supplied wording.

## Reconcile the Chapter 3 state subscripts with the settled `CE` convention

`THESIS_WRITING_GUIDE.md` settles the visible Contact Establishment quantities
as \(s_{\mathrm{CE}}\), \(t_{\mathrm{CE,start}}\), \(t_{\mathrm{CE,end}}\),
\(R_{\mathrm{EE,clearance}}\) and \(p_{\mathrm{Tool,clearance}}\), and the
approach quantities as \(s_{\mathrm{app}}\) and \(v_{\mathrm{app}}\).
Section 3.2 carries none of them: it writes \(s_c\), \(v_c\), \(s_{c,\max}\),
\(s_a\), \(v_a\), \(s_{a,\max}\), \(t_{\mathrm{start}}\) and
\(t_{\mathrm{end}}\), and \(t_{\mathrm{start}}\) denotes two different instants,
the start of Surface Approach in Section 3.2.3 and the start of Contact
Establishment in Section 3.2.5.

The text supplied on 2026-09-04 uses \(s_c\) and \(t_{\mathrm{start}}\)
throughout and was applied verbatim, so the chapter now carries the older
notation in three more sentences. Table 4.3, Appendix C and the symbol list use
\(s_{c,\max}\), \(v_c\) and \(v_a\) with it. Either convert all of them in one
pass, or withdraw the `CE` convention from the guide; do not leave the two
standing together.

## Retire the superseded null-space script in `MyController`

`MyController/experiments/analysis/make_nullspace_figure.py` is the version
that produced the withdrawn Figure 5.6: two panels, no net-displacement bars,
and the \(\Delta\sigma_{\min,\mathrm{dist}}\) labels. It sits beside the run
archive, so it is the copy a session on the lab machine reaches for first, and
running it silently reverts the figure. Either overwrite it from
`code/python/figures/make_nullspace_figure.py` in this repository, which is now
the authoritative generator, or delete it and leave a pointer here. Not done
because it changes a second repository.

## Publish the records the withdrawn figure generators read

The records behind the two figures the thesis includes are now in
`code/python/experiments/results/`, and both scripts redraw from a checkout
with no arguments. What remains is the other four generators.
`make_coc_figures.py` and `compare_angle_metrics.py` read
`Thesis_Final_Control/experiments/derived/metrics.csv`, 141 kB, and
`plot_setup_diagnostics.py`, `plot_angle_descent.py` and the two-panel mode of
`compare_angle_metrics.py` read raw run directories from the same archive. They
draw `MAIN_B_KR`, `MAIN_C_KP`, `MAIN_H_direction`, `MAIN_D_sign`,
`MAIN_D_diagnostics`, `MAIN_DQ_metric_comparison`, `MAIN_DQ_metric_summary` and
`MAIN_DQ_descent`, none of which any chapter now includes.

Nothing is broken while they stay withdrawn. Copying `metrics.csv` alone would
restore most of them for the cost of a small file, and is worth doing if any of
those figures is brought back. Preserve `MyController`'s calibration exclusion
in anything further that is copied.

## Decide whether the null-space figure should print its minus sign

`make_figures.py` sets no `axes.unicode_minus`, unlike `figure_style.py`, which
sets it `False` and explains why: the serif faces carry no U+2212, and a
Type-42 subset then embeds a glyph the viewer cannot draw, so the sign
disappears. `make_nullspace_figure.py` imports the former and its
`_net_value_label()` writes U+2212 deliberately. The committed
`MAIN_NS_nullspace_automatic.pdf` therefore prints the last bar of panel (c) as
`0.006`, with the sign present in the text layer and absent from the drawing.
Section 5.5 is written against that rendering: `the measured net displacement
was negative, so its absolute value was 0.006`. The figure and the sentence
agree as they stand, so nothing is wrong in the submitted document.

Two ways to close it, and neither is free. Set `axes.unicode_minus = False` in
`make_figures.py` and regenerate, which prints `-0.006` and lets the sentence
report the signed value directly; or leave both and keep the workaround. The
first changes a Chapter 5 figure and the text beside it, so it is not a
tidying edit. Not done because it is an editorial decision, not a defect.

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

## Decide on `parallel alignment` thesis-wide

The Abstract, Section 1.4 and Section 6.1 describe the result as rotation
`towards the configured surface`. The longer form it replaced, `towards
parallel alignment with the configured surface`, and its variant `the
configured surface-parallel orientation`, remain in eight places: Section 1.1
once, Section 3.2.2 once, Section 4.5.2 twice, and Chapter 5 four times.

Both are defensible, but one quantity now has two names. Decide which survives.
Section 1.1 and Section 1.4 carry the two forms two pages apart.

## Restore the one-recording statement to Section 4.6.2

The supplied Section 4.6.2 of 2026-09-07 dropped the sentence `Both come from
one trial, so no between-trial variability is evaluated`, and the words `in one
trial` from the sentence above it. Nothing else in the thesis says it: the only
other hits for a single trial are Section 4.6.1, which says the wrench
comparison used one trial, and the two are now stated asymmetrically.

`THESIS_WRITING_GUIDE.md` requires it twice -- under *A single trial does not
carry a \(\pm\) sample standard deviation*, which asks a single-trial evaluation
to state that between-trial variability was not evaluated, and under *Settled
compression and evidence hierarchy*, whose `Section 5.1 is one trial per test
and states so` has been amended to record the gap rather than assert a rule the
thesis no longer meets.

The author's instruction that produced the change says the opposite of the text
it supplied: `I would, however, not pretend that they were physically recorded
as two different trials. They came from one recording.` Presenting the two
evaluations separately is what the supplied text does; saying they come from one
recording is what it no longer does. One sentence after the reset-to-zero
sentence would satisfy both -- `Both evaluations come from one recording, so no
between-trial variability is evaluated` -- and it would not disturb the separate
presentation. Applied as supplied under the verbatim rule; the decision is the
author's.

## Decide the centred dot in the Section 4.6.2 predictions

`THESIS_WRITING_GUIDE.md` requires scalar multiplication in a displayed
calculation to carry a centred dot, `\(K\mathbin{\cdot}e\)`. The supplied
predictions of 2026-09-07 write `K_{p,n}\,n_s^\top(e_p-e_{p,0})` and
`K_{R,t_1}\,t_1^\top(e_R-e_{R,0})` with a thin space, where the withdrawn
display used `\mathbin{\cdot}`. Applied as supplied.

The two forms are one edit apart and the choice is the author's. Restoring the
dot would leave the visible sentence and the mathematics unchanged; keeping the
thin space means the rule should say that a product of a gain with a projected
error is an exception, since this is now the only displayed product in Chapter 4
that omits it.

## Bring the determiner openers down

Pattern 9 in `THESIS_VOICE.md` asks for sentences opening with `The`, `This`,
`These`, `It` or `A` to stay under about a third. Measured on 2026-09-02, no
chapter meets it: Chapter 1 sits at 36 %, Chapter 5 at 45 %, Chapter 3 at
50 %, Chapter 4 at 59 %, Chapter 6 at 61 %, and Chapter 2 at 66 %. The rule
previously claimed the figure had been brought to 29--30 %, which was withdrawn
as false in the same pass.

Every revision so far has improved sentence length and left the openers
untouched, because an opener is invisible one sentence at a time and only a
whole-chapter count exposes it. The fix is per chapter and mechanical: start
from the condition, the participle, the quantity, or a subordinate clause,
per the rule's own list. Chapters 2, 6 and 4 are the worst and would gain
most.

## Decide whether \(m_R\) follows the general rotational impedance law

Equations 2.20, 2.21 and 2.23 were generalised on 2026-09-03 to
\(m=K_Re_R+D_R(\omega_d-\omega_{\mathrm{EE}})\), on the author's instruction,
which named those three equations. Equation 2.41 in Section 2.7.2 still defines
the rotational-impedance contribution as
\(m_R=K_Re_R-D_R\omega_{\mathrm{EE}}\), so Chapter 2 now states the law in two
forms nine pages apart, the second silently assuming \(\omega_d=0\).

The same expression sits in two other places and moves with it: the \(m_R\)
row of `frontmatter/symbols.tex`, and the settled force-and-moment names table
in `THESIS_WRITING_GUIDE.md` under *Technical conventions that must remain
explicit*. Either generalise all three, or state beside Equation 2.42 that it
is written at the implemented \(\omega_d=0\). Not done because the instruction
named three equations and this is a fourth.

## Decide `mode` in the Section 3.2 Manual Guidance return

The paragraph supplied on 2026-09-03 reads `input \texttt{p} captures the
reached pose and returns control according to the previously active mode`.
`THESIS_WRITING_GUIDE.md` reserves `state` for each runtime node and rules out
`phase`, `gate`, `mode` or `sequence step` as an alternate label for one, and
the thesis uses `mode` elsewhere only for the four selectable null-space modes.
A reader meeting it here has to rule out that reading first.

Applied as supplied, under the verbatim rule. The smallest change that would
satisfy both is `according to the previously active controller configuration`,
which is the word Section 3.1 already uses for the surface-contact sequence and
Cartesian pose hold as the two configurations of one callback.

## Check two terms in the supplied Section 3.2.5 impedance paragraph

Applied verbatim on 2026-09-03; both crossings are the author's to settle.

`permits contact-induced alignment` names no body. `THESIS_WRITING_GUIDE.md`
requires every rotation claim to name what rotated, because the physical tool
orientation is never measured independently, and the Chapter 4 sentence this
paragraph replaces read `permits contact-induced end-effector rotation`. The
sentence describes what the configuration allows rather than reporting a
measurement, so it may stand; `permits contact-induced end-effector rotation`
is the wording that would satisfy both.

`tangential position retention` reuses the words of `Cartesian position
retention`, which is the settled name of the pose-hold acceptance criterion
\(\max\lVert e_p(t)\rVert_2<2\,\mathrm{mm}\). The two are unrelated
quantities. `retains the tangential tool position` would keep them apart.

## Settle the zero-vector notation for a desired velocity

`THESIS_WRITING_GUIDE.md` keeps \(\mathbf{0}\) as the one bold symbol in the
thesis, so that the zero vector is distinguishable from the scalar zero.
Chapter 2 follows it for \(\dot p_d=\mathbf{0}\). The supplied Chapter 3
sentence writes \(\omega_d=0\), and the contact-establishment passage in
Section 3.2.5 already writes \(\dot p_d=0\), so Chapter 3 uses the plain zero
for the same kind of quantity that Chapter 2 sets bold. Decide which the thesis
uses and apply it to all four places at once.

## Decide three long supplied sentences

All three were supplied by the user and applied as given, under the rule that
supplied wording is not altered for style. Each is over the 28-word limit in the
register baseline, and each is the longest sentence its revision added. Confirm
whether they stand as written or may be split.

- Chapter 1, Motivation, 34 words: `Together, the difference between the
  configured and physical surfaces and the difference between the desired and
  achieved tool orientations determine the angular mismatch between the tool
  face and the physical surface at contact entry.` It lifted the chapter mean
  from 18.7 to 19.5 words. Splitting after `tool orientations` would restore
  the register without changing the claim.
- Section 3.2.6, 30 words: `The low rotational stiffness generates a
  comparatively small restoring commanded moment towards the held desired
  orientation, allowing the contact-induced moment to dominate and produce
  passive alignment with the changed surface.` Supplied on 2026-09-03 with the
  rewrite of the whole subsection, replacing the 38-word sentence previously
  listed here. Splitting after `desired orientation` would bring it under the
  28-word limit without changing the mechanism it states.
- Section 2.7.2, 30 words: `The exact composition depends on the order of the
  two finite rotations, whereas this difference enters only through second- and
  higher-order terms and therefore disappears in the first-order small-angle
  representation.` Supplied on 2026-09-06 and offered as an optional addition
  after Equation 2.53, where it is what licenses the additive form. Splitting
  after `finite rotations` would bring it under the limit and leave both halves
  standing.

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

## The real-time claim now carries no stated bound

The Abstract and Section 6.1 both open with `A real-time Cartesian impedance
controller was implemented`. Until 2026-09-02 that claim was bounded twice: a
limitations paragraph stating that worst-case callback execution time and
scheduling jitter were not measured and that the assembled torque command
carried no application-side saturation or torque-rate limiter, and a future-work
paragraph proposing both. The supplied Sections 6.2 and 6.3 replaced the
sections containing them, so neither survives, and no other chapter states the
bound. Chapter 3 describes the callback structure but makes no claim about
measured timing.

Decide whether to restore a bound. One sentence in Section 6.2.4 would do it,
or a fourth paragraph in Section 6.3. The alternative is to soften the claim
itself in both places, which touches the Abstract and the Kurzfassung together.

## Follow-on physical-angle measurement

The reported logs define the contact-entry angle relative to the configured
surface reference. They do not contain an independently measured physical plane
normal or the tool face's motion relative to the end effector under load. A
follow-on experiment must record both before a run-wise physical tool--surface
angle can be evaluated.

## Confirm two supplied sentences in Section 5.1

The four rule crossings logged on 2026-09-06 were settled by the author the
same day and are done: the plausibility assessment stays and is presented as a
defined perturbation test, the three captions were shortened to the supplied
forms, Appendix B regained the model-estimated wrench group, and Chapter 4
gained Section 4.6 with the methodology for both evaluations.

What remains is two fragments of the supplied text that were not applied
exactly, each a clause or a word. `as in the original time-history evaluation`
would put draft history into the thesis, which the repository rules forbid, so
the sentence before the Case-D mechanism figure names the three compliance-centre
positions instead. `the subscript \(\mathrm{est}\)` became `the
\(\mathrm{est}\) index`, because `subscript` is not used in thesis prose.
Restore either if the supplied wording is meant to stand.

## \(u\) now names two different directions

The Section 2.7.2 construction of 2026-09-06 defines the first-order direction
of a general angular tool offset as
\(u=(\theta_{t_1}t_1+\theta_{t_2}t_2)/\sqrt{\theta_{t_1}^2+\theta_{t_2}^2}\).
The author supplied the symbol and it was applied. \(u\) is already the
base-frame orientation-error axis of \(\Delta R\), in Section 2.2 and in its own
symbol-list row, so the List of Symbols now carries two rows containing \(u\),
and one chapter uses the letter for two different directions five sections
apart.

This is the same collision the withdrawn axis--angle construction had with
\(\phi\), and it has the same smallest fix: an index. \(u_\theta\) is
withdrawn by name in `THESIS_WRITING_GUIDE.md` and would have to be un-withdrawn
to be used, so \(u_t\) for the tangent-plane direction is the free candidate.
The other rotation axes are indexed that way --
\(u_{\mathrm{CE}}\) in Chapter 3, \(u_{\mathrm{offset}}\) in
Section 3.2.2 -- and the bare \(u\) belongs to the generic axis--angle
construction of Section 2.3. Two files change:
`chapters/02_theoretical_background.tex`, in Equations 2.54 to 2.58 and the
sentences around them, and the symbol-list row.
