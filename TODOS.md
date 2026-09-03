# Open items

This file contains only agreed work that remains unfinished. Completed items are
removed in the turn in which they are finished.

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

## Correct `signed component` in Section 4.5

`chapters/04_experimental_setup_and_evaluation.tex` uses `signed component
about \(t_1\)` twice in Section 4.5.1, once before Equation 4.3 and once
after it. `THESIS_WRITING_GUIDE.md` bans `signed` as a modifier in prose,
headings, captions, axes and tables, on the ground that the defining equation
and the displayed positive and negative values already establish the algebraic
direction. Write `component about \(t_1\)`. Not done because the passage is
settled text and the change was not asked for; the new Figure 4.3 beside it now
states the direction convention, which is what those two uses were reaching
for.

## Retire the superseded null-space script in `MyController`

`MyController/experiments/analysis/make_nullspace_figure.py` is the version
that produced the withdrawn Figure 5.6: two panels, no net-displacement bars,
and the \(\Delta\sigma_{\min,\mathrm{dist}}\) labels. It sits beside the run
archive, so it is the copy a session on the lab machine reaches for first, and
running it silently reverts the figure. Either overwrite it from
`code/python/figures/make_nullspace_figure.py` in this repository, which is now
the authoritative generator, or delete it and leave a pointer here. Not done
because it changes a second repository.

## Publish enough data to reproduce the figures

The run CSV files and derived contact metrics remain outside the repository.
Choose whether to publish `experiments/derived/metrics.csv` from
`Thesis_Final_Control` and one complete null-space run from `MyController`.
Preserve `MyController`'s calibration exclusion: its measured plane and
tool-axis calibration files are not to be published. If the data are placed in
this repository, `make_nullspace_figure.py` and the other scripts that read run
directories take a `--results` path, so the location is free; without it they
resolve to `code/python/experiments/`.

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

## Decide two long supplied sentences

Both were supplied by the user on 2026-09-02 and applied as given, under the
rule that supplied wording is not altered for style. Each is over the 28-word
limit in the register baseline, and each is the longest sentence its revision
added. Confirm whether they stand as written or may be split.

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
