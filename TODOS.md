# Open items

This file contains only agreed work that remains unfinished. Completed items are
removed in the turn in which they are finished.

## Confirm the material the new summaries dropped is carried elsewhere

The supplied Abstract and Kurzfassung of 2026-09-04 dropped three things the
previous versions carried, and each needs a home in the body or a decision that
it is not needed.

- The angular-evaluation basis: `The angular conditions were defined relative to
  the configured surface geometry, and the contact response was calculated from
  the measured end-effector orientations.` Chapter 4 defines this, so this is
  probably already covered; confirm the wording there is explicit enough to
  carry the claim alone.
- The rotational-stiffness interval that produced the \(64\,\%\) reduction.
  Chapter 5 reports it; confirm the Conclusion still states it, since the
  Abstract no longer does.
- The largest measured Cartesian position error against its \(2\,\mathrm{mm}\)
  limit, now written qualitatively as `Cartesian position retention was
  maintained throughout the tested conditions`. Confirm the measured value and
  the limit both appear in Chapter 5.

## Remove the duplicate TCP expansion in Chapter 2

`chapters/02_theoretical_background.tex:760` spells out `tool centre point
(TCP)`. Since 2026-09-04 Chapter 1 spells it out first, at the \(r_c\)
sentence, so the Chapter 2 parenthesis is a second introduction. The duplicate
predates the change — the old Abstract expanded TCP as well — so this is
tidying rather than a fault. Drop the parenthesis in Chapter 2 and leave the
words.

## Reconcile the sentence after Equation 3.2 with its `\approx`

Equation 3.2 became
\(\theta_{\mathrm{offset}}\approx\theta_{\mathrm{offset},t_1}t_1+
\theta_{\mathrm{offset},t_2}t_2\) on 2026-09-04, under the supplied lead-in
`For small configured angular offsets, the pre-contact orientation offset is
represented to first order in the surface tangent plane by`. The instruction
named the equation and the sentence before it, so the sentence *after* it was
left as it stood: `The scalars \(\theta_{\mathrm{offset},t_1}\) and
\(\theta_{\mathrm{offset},t_2}\) are the components of this rotation vector
along the two surface tangents.`

Those two statements disagree. If the scalars are exactly the components of one
rotation vector, the sum is exact and the equation takes an equals sign; that
is the reason the equation carried `=` until now. Either the following sentence
becomes `are the surface-tangent components used to construct the offset`, or
the equation goes back to `=`. Not resolved here because the instruction named
neither.

## Check the revived \(\theta_{t_1}\) and \(\theta_{t_2}\) against older drafts

Dropping the index \(a\) on 2026-09-04 made \(\theta_{t_1}\) and
\(\theta_{t_2}\) the components of the general offset in Section 2.7.2. Both
spellings were previously **withdrawn** names for the *configured* offset, and
`THESIS_WRITING_GUIDE.md` carried that withdrawal until the same day.

Nothing in the current thesis is ambiguous: the configured quantity keeps its
`offset` index in all 21 of its uses, and the two families never meet in one
section. The risk is external — a supervisor or examiner holding an earlier
draft will have met \(\theta_{t_1}\) as the configured offset. If any circulated
version used the old spelling, say once in Section 2.7.2 which quantity the
symbol names there.

## Decide whether the \(n_s\times\theta\) display is boxed

The Section 2.7.2 rewrite supplied on 2026-09-04 gave the cross-product step as
a plain display, and that is how it was applied. The message that carried it
closed by singling the step out — `the particularly useful addition is
\(\boxed{n_s\times\theta}\), because it immediately explains where your
numerator comes from` — which reads as emphasis on which addition matters
rather than as typesetting instruction, since the rewrite block itself showed
the relation unboxed.

The reason to ask is that Section 3.2.5 does carry a `\boxed` display, added on
the author's instruction two days earlier, so a box here would not be foreign
to the document. The reason not to is that the two do different jobs: the
Chapter 3 box summarises a chain of five position symbols, whereas this is one
step of a derivation whose result is already set as a numbered equation two
displays later. Box it only if the author wants the derivation's turning point
marked.

## Decide whether the three `\approx` relations stay

Instructed on 2026-09-04 and applied. The symbol now appears in three places:
Equation 2.51, \(\theta\approx\theta_{t_1}t_1+\theta_{t_2}t_2\); Equation 3.2,
the same construction for \(\theta_{\mathrm{offset}}\); and the unnumbered
\(n_s\times\theta\approx\theta_{t_1}t_2-\theta_{t_2}t_1\) display added to
Section 2.7.2 later the same day. The ground is that the two scalars read as
rotation angles about \(t_1\) and \(t_2\), and finite rotations about different
axes do not add. `THESIS_WRITING_GUIDE.md` records the blanket ban as narrowed
to these three rather than lifted.

The third is not an independent decision. \(n_s\times\theta\) is exact given
\(\theta\), so its symbol is inherited: if Equation 2.51 goes back to `=`, that
display does too, and if 2.51 keeps `\approx` the display keeps it. Decide 2.51
and 3.2, and the third follows.

The smallest change that would satisfy the old rule is the route the guide
gives first: state that \(\theta_{t_1}\) and \(\theta_{t_2}\) are the
components of the one rotation vector \(\theta\) along the two tangents, which
makes the sum exact and restores the equals sign. That route is now closed on
both sides — Chapter 3 took it until 2026-09-04 and no longer does — so the
thesis is at least self-consistent. What remains is the single question of
which reading it uses.

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

## Decide `signed` in Sections 3.2.5 and 4.5

`THESIS_WRITING_GUIDE.md` bans `signed` as a modifier in prose, headings,
captions, axes and tables, on the ground that the defining equation and the
displayed positive and negative values already establish the algebraic
direction. Three uses stand against it, in two places.

`chapters/04_experimental_setup_and_evaluation.tex` uses `signed component
about \(t_1\)` twice in Section 4.5.1, once before Equation 4.3 and once
after it. Write `component about \(t_1\)`. Not done because the passage is
settled text and the change was not asked for; the new Figure 4.3 beside it now
states the direction convention, which is what those two uses were reaching
for.

`chapters/03_software_implementation.tex` uses `signed distance` once in
Section 3.2.5, in the sentence after Equation 3.18 supplied on 2026-09-04 and
applied verbatim. `the distance of the desired tool point from this plane along
the surface-normal direction` would satisfy both, since Equation 3.16 already
gives the negative initial value and Equation 3.18 fixes the direction. The two
places are one decision: keeping the word in one and dropping it in the other
would leave the ban half applied.

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
