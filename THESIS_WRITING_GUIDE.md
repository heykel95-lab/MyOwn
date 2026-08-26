# Thesis Writing Guide

This file is the standing editorial guide for this thesis. Update it whenever a
new recurring preference, technical convention, or evidence rule is agreed.
The current thesis contains one combined Results and Discussion chapter.
The earlier contact-alignment campaign was preserved in an appendix while the
calibrated-plane, axis-specific campaign was being recorded. That campaign is
now complete and reported in full, so the appendix has been removed and must
not be reinstated. Do not replace the main results with planned or empty
sections; update the main chapter only after new measurements have been
checked.

## Scientific narrative

Write the thesis as one completed engineering investigation:

problem → necessary theory → controller design → experimental method →
measurements → interpretation → limitations → conclusions.

Do not narrate the history of the code, repository, experiments, drafts, or
interpretation. The controller source is evidence used to verify the technical
description; it is not the subject of the thesis.

Use declarative scientific prose. Do not create headings or passages framed as
“Research Question”, “Experimental Question”, “RQ1”, “central question”, or
similar.

**The ban covers every name the reader sees, not only section headings.**
Chapter titles, section and subsection headings, figure and table captions,
short caption entries, and appendix titles are all declarative noun phrases. A
caption reading `Which lever pairs with which force to give which moment.`
was replaced by `Moment relations on the commanded and observed sides.` — the
question form had slipped in because the caption was written to describe what
the figure explains rather than to name what it shows.

The test is mechanical: **no title or caption may begin with `Which`, `What`,
`How`, `Why`, `Does`, `Do`, `Is`, `Are`, `Can`, `When` or `Where`, and none
may end with a question mark.** Grep for those openers across `\caption{`,
`\caption[`, `\chapter{`, `\section{` and `\subsection{` before submitting.

**The ban now extends to the running text as well.** The earlier version of this
rule allowed `One experiment asks whether displacing the centre of compliance
in any direction produces alignment` as a useful section opener. A supervisor pass
overturned that: the thesis does not need to keep telling the reader it is
answering questions, and the construction was the largest remaining source of
an AI-written impression after the repetition. State what a case *evaluates* or
*separates*, not what it *asks*:

| Was | Now |
|---|---|
| The supporting check asks whether displacing the centre in any direction produces alignment | The tool-axis supporting check separates the contribution of the tangential displacement component from that of a displacement along the tool axis |
| Case E asks whether the lever effect persists when the commanded misalignment changes | Case E evaluates the dependence of the lever effect on the commanded misalignment magnitude |
| Two matters were investigated experimentally: whether … and whether … | The experimental investigation addressed contact-induced rotational alignment and the selection of a fixed centre of compliance |
| This thesis investigates whether … It also asks whether … | This thesis investigates contact-induced alignment … and evaluates whether a fixed centre can be selected independently of … |
| The cases are reported in the order in which they narrow one question | The cases are reported in the order in which they progressively constrain … |
| Steps three and four carry the question stated above | Steps three and four establish whether … |
| The design question that remains is when … | The remaining design issue is when … |

`evaluates`, `separates`, `establishes`, `addressed`, `constrain` and
`determines` are the verbs to reach for. A single embedded `whether` clause is
fine — `evaluates whether a fixed centre can be selected` — because it names
what was evaluated rather than posing a question to the reader.

**No sentence begins with a `Wh-` word used as a fronted nominal.** The
pseudo-cleft `What X does is Y` is the commonest form and reads as an answer to
a question the reader was never asked. State the subject and let the verb
carry the sentence:

| Was | Now |
|---|---|
| What changes is the point about which the impedance is defined | The point about which the impedance is defined changes |
| What changes at the phase transition is the generated reference | The phase transition changes the generated reference |
| What the four settings compare is the closed-loop behaviour | The four settings compare the closed-loop behaviour |
| What the measurement supports is a statement about the end effector | The measurement supports a statement about the end effector |
| What the measurements establish is that every lever tested is direction dependent | The measurements establish that every lever tested is direction dependent |
| What translational compliance alone does not supply is a commanded rotational contribution | Translational compliance alone supplies no commanded rotational contribution |
| What it does provide is the property a fixed centre requires | It supplies the property a fixed centre requires |
| Whether the tool ended flat is not read from any of these | None of these determines whether the tool ended flat |

`When …` and `Where …` as ordinary subordinate clauses are unaffected: `When
\(J(q)\) has full row rank, the null space is one-dimensional` is normal
technical prose and stays.

State the investigated dependencies directly. For example:

> The experimental study evaluates the influence of the paired surface-tangent
> rotational stiffness \(K_{R,t_1}=K_{R,t_2}\) and virtual
> centre-of-compliance placement on contact-induced tool alignment.

Use “aim”, “objective”, and “investigation” sparingly. Avoid proposal wording
for completed work (`will investigate`, `is planned`, `will be evaluated`).
Future work is the only place for proposed experiments.

## Abstract and Kurzfassung

The Abstract carries the general shape of the work and nothing more:

1. the problem, stated generally;
2. the idea used to attack it;
3. what was found, in general terms;
4. what limits the generality.

**Keep measured values out of the Abstract, without exception.** No degrees, no
stiffness values, no distances. State the direction, the ordering, and the sign
of an effect instead: `reduced the measured alignment response`, `no tested
setting improved on the most compliant baseline`, `differed between the two
surface tangent directions`.

**The exception for the strongest measured effect is withdrawn.** This rule
once admitted one magnitude — `approximately 6 degrees of improvement` — so the
reader had the scale of the headline result. The Abstract carried it as
`a selected 40 mm displacement changed the measured set-up rotation from
\(-1.63^\circ\) to \(+4.43^\circ\)`, and that sentence was removed on
2026-08-25 along with its Kurzfassung counterpart. The reason is that a pair of
per-condition means makes one experimental condition look more important than
the finding the Abstract exists to state, and those values belong in Chapter 5
where the condition that produced them is on the page. The qualitative finding
is what the Abstract needs: the compliance-centre position produced the largest
response variation, an assisting tangential displacement lies perpendicular to
the required rotation direction, and reversing the sign of the initial angular
deviation requires the displacement on the opposite side of the TCP.

**The run count does not go in the Abstract.** A supervisor pass briefly asked
for it, and it was added; the author then removed it as repetitive, which it
was — the same figure was appearing in the Abstract, the Kurzfassung, the
Introduction, twice in the results chapter, and the Conclusion. **State the
total number of runs once, in the methodology chapter, and nowhere else.**
Elsewhere write `were evaluated experimentally`, `all reported contact runs`,
`the worst run`. A count that appears six times reads as padding, not as
evidence.

Write the Abstract in four parts, in order: the engineering problem; the
implemented approach; the experiment and its main findings; the principal
limitation. Prefer one claim per sentence — an Abstract in which every sentence
carries a full conclusion reads as machine-polished however accurate it is.

**Revise the Abstract last**, after the body text is settled, and derive the
Kurzfassung from the finished English rather than paraphrasing it independently.

Symbol names that identify a thing rather than measure it — the tangents
\(t_1\) and \(t_2\), the robot's degrees of freedom — are not values and may
stay where dropping them would make a finding vague.

This rule costs the Abstract its specificity, which is the trait that
otherwise marks prose as the author's own (see [THESIS_VOICE.md](THESIS_VOICE.md)).
Accept that for the Abstract and the Kurzfassung only; every other chapter
keeps its numbers.

**The single-page limit is suspended.** The Abstract and the Kurzfassung
previously had to fit one page each, and neither was allowed to spill onto a
second. That constraint was blocking ordinary revision of the Abstract, so it
does not apply for now: do not cut material from either text, or decline a
requested edit, on length grounds alone. Do not reinstate it without being
asked.

The reasoning is kept here so the rule can be restored later. It existed
because an Abstract a reader cannot take in on one page stops working as a
summary, and because the Abstract and the Kurzfassung were laid out to occupy
one page each. When it is restored, the trade it forces is that new material
displaces old rather than being added to it.

The two are translations of one another and must stay matched in content,
certainty, and structure. **This rule is not suspended.** A cut on one side is
a cut on the other, and an Abstract that grows is followed by a Kurzfassung
that grows with it.

German needs roughly a fifth more space than English for the same statements,
so the Kurzfassung will run longer than the Abstract it mirrors. That is
accepted rather than weakening the German. Do not close such a gap by
compounding German nouns to shorten the word count: long compounds break lines
badly and fit *fewer* words on the page, not more.

Judge length in the compiled PDF rather than by word count. At the current
settings roughly 520 words fills a page, which is worth knowing when deciding
how a text will sit even while no limit is enforced.

## Roles of the chapters

- Introduction: define the contact-alignment problem, relevant literature gap,
  scope, and substantial contributions. Keep the problem statement at the
  problem level — frame consistency, collision thresholds, and the absence of a
  torque-rate saturation stage are implementation details and belong to the
  controller or safety sections. Group the related work by topic (Cartesian
  impedance control; real-time implementations on torque-controlled robots;
  compliance-centre placement and contact alignment), say for each source what
  it established and which part is adopted here, then state the gap. A single
  compressed paragraph of citations reads as synthesised rather than reviewed.
  The contribution list lives here, split into implemented, experimentally
  established, and implemented-but-not-validated; Chapter 6 refers back to it
  rather than repeating it.
- Theoretical Background: explain only the mathematics required to understand
  the controller and experiments.
- Controller Design and Implementation: explain how the verified controller
  realizes the theory, without line-by-line code narration.
- Experimental Methodology: document what was used, varied, held constant,
  recorded, and calculated in the completed experiments.
- Results and Discussion: report observations, quantitative analysis,
  interpretation, and evidence limitations.
- Conclusion: state what was learned without repeating the full controller
  architecture.

Explain a concept authoritatively once. In particular, avoid repeating
Cartesian impedance, point-shift derivations, gain transformations, damping,
null-space projection, or energy/passivity arguments across chapters.

### Settled compression and evidence hierarchy

The main contact argument contains Cases A--D only: the TCP-centred baseline,
rotational stiffness, cross-axis translational stiffness, and tangential
compliance-centre position. The orientation-offset-magnitude comparison is a
supporting appendix check together with the definition-frame, tool-axis, and
intermediate-direction checks. The main study therefore contains 37 settings
and 111 runs; the four supporting checks contain 18 settings and 54 runs. The
complete surface-contact total remains 55 settings and 165 runs.

Chapter 5 carries one comparison figure for each main case and retains the
Case-D commanded-wrench mechanism figure. It does not repeat those plots as
numeric tables. The complete numeric values belong in Appendix D. Uncertainty
for Case D is shown directly on the main comparison figure, so the separate
appendix spread plot is removed.

**Every setting of the main Cases A--D carries its sample standard deviation,
in its Appendix-D table.** The earlier arrangement gave means alone for Cases A
to C and mean \(\pm\) SD for Case D only, while Section 4.3.3 said results were
reported as the arithmetic mean and sample standard deviation. The Case A, B
and C tables were completed on 2026-08-25 from
`Thesis_Final_Control/experiments/derived/metrics.csv`, using the same
`contact_rotation_t{1,2}_deg` column and the same sample standard deviation
over three repetitions that `make_coc_figures.py` computes, and every mean
already in those tables was reproduced before any spread was added.

The division of labour is then: **the tables carry the spread, the figures
carry the means.** Only the Case-D comparison also draws error bars, because
the higher-spread conditions are part of what that figure shows. Do not add
error bars to the other comparison figures to make them
match; a figure whose spread is invisible at plotted scale gains nothing from
the marks. Chapter 5 states once in its opening that the comparative response
values are arithmetic means over three repetitions and that Appendix D carries
the corresponding sample standard deviations for Cases A--D. Each main case
then gives one compact summary of its repetition scatter. Individual standard
deviations appear in the main text only where their spread affects the
interpretation; Case D therefore names its higher-spread conditions explicitly.

**The supporting checks report means, and the methodology sentence says so.**
The offset-magnitude, tool-axis and intermediate-direction tables give the
response alone; the definition-frame table gives mean \(\pm\) SD because the
comparison it makes is between two close values. Section 4.3.3 was therefore
reworded on 2026-08-25 to `Results are reported as arithmetic means, with
sample standard deviations given for the main comparisons and where relevant in
the supporting checks`, which is what the appendix actually does. **Do not
restore the unqualified wording**, and do not recompute the supporting tables
to justify it: the main argument rests on Cases A--D, the supporting checks are
read as separations rather than as measurements to be compared within their own
scatter, and the author declined the work as disproportionate.

**Cases A to C state their scatter in one form; Case D does not.** A, B and C
each carry one sentence of the shape `Repetition scatter remained at or below
\(X^\circ\) across all Case-N settings in Table N`, harmonised on
2026-08-26 from three different phrasings. **Case D is deliberately excluded
from that form.** A single maximum is misleading there, because four conditions
carry a much larger spread than the rest, and quoting only the largest would
either hide them or make every setting look uncertain. Case D therefore says
that scatter was small at most settings, points at the Appendix-D table for
every value, and names the four high-spread conditions where its error bars
appear. Do not force Case D into the A--C sentence.

A standard deviation that rounds to \(0.00^\circ\) at the reported two
decimals is written `\(\pm0.00\)`. It is the correctly rounded sample standard
deviation at the precision the rest of the table uses, and switching that one
entry to a third decimal or to an inequality would break the column for no
gain.

The main contact evaluation uses the signed set-up rotation
\(\gamma_{t_i}\). The commanded normal force \(F_n\) and commanded TCP
moment \(M_{t_i}\) appear only in the Case-D mechanism plot. Selected-tool-point
and TCP displacement metrics and the fully blocked spring-force scale are not
reported quantities and are not defined. A quantity used in one local appendix
equation remains local and does not receive a List-of-Symbols entry.

Chapter 3 explains the controller signal path. It contains no subsystem,
gain-frame, null-space-mode, or logged-signal table and no `robot.control`
syntax listing. The code appendix retains only the compliance-centre point
shift and core torque assembly. Chapter 4 states the calibration principle and
the values needed to interpret the experiments; the exact calibration record
and fitting relations belong in Appendix C.

## Style

Sentence-level voice is in [THESIS_VOICE.md](THESIS_VOICE.md): the machine-prose
patterns to avoid, the weak-verb replacement table, the paragraph rewrite
procedure, and the originality rules. Read it before writing or rewriting any
prose. The rules below cover tone and framing.

Use clear technical English rather than rhetorical or promotional language.
Avoid expressions such as:

- “the answer is visible before any fitting”;
- “a sweep is worth nothing until…”;
- “costs alignment and buys nothing”;
- “this is the substantive question”;
- “surprisingly”, “remarkably”, “clearly”, or “as can easily be seen”;
- repeated “This demonstrates that…” constructions;
- compressed one-line openers written to be quotable — “The floor came first”,
  “Nothing tested came close to the lever”, “The limitation bites”. The
  *Register* section of [THESIS_VOICE.md](THESIS_VOICE.md) governs these and
  carries the replacement table.

Prefer the sequence:

measured value → comparison → interpretation → limitation.

Use it as the default, not as a template for every paragraph. Four consecutive
paragraphs built to that shape is itself a fault; vary what each paragraph does,
per *Vary the architecture, not the vocabulary* in
[THESIS_VOICE.md](THESIS_VOICE.md).

Tie each interpretation to the evidence it rests on. A claim in a results
subsection carries a `\cref` to the table or figure that supports it, in the
sentence that makes the claim.

Match the certainty of the wording to one configuration and three repetitions.
Prefer `indicates`, `supports`, `is consistent with`, and `strongly influences`
to `proves` and `decides`; bound a general-sounding claim with `within the
tested range` or `in the investigated configuration`. Having a limitations
section does not license certainty elsewhere.

Carry one main claim per sentence. A clause answering more than about two of
*what / where / how / when / why* is algorithmically compressed however correct
it is; split it so the reasoning is presented step by step.

Where a claim is the main finding of its section, give the measurement before
the conclusion. `The response changed by several degrees when the lever was
displaced by 60 mm. The changes produced by the tested stiffness values were
substantially smaller. Within the investigated range, the compliance-centre
position therefore had the largest measured influence.` reads as derived from
the data; the same content with the conclusion first reads as announced.

The target style for this thesis is: impersonal academic English, passive voice
for performed actions, direct language for mathematical and physical relations,
one main claim per sentence, explicit links between measurements and
interpretations, and conclusions limited to the tested configuration. Literary
expressions, slogan-like conclusions, and overly compressed sentences are
avoided. The list of things never to do in pursuit of this — deliberate errors,
casual filler, vague synonyms, invented observations — is in
[THESIS_VOICE.md](THESIS_VOICE.md).

Do not over-academize simple statements. Prefer “The measured alignment
increased as rotational stiffness decreased” over inflated wording.

Use British spelling consistently, including `centre`, `behaviour`, and
`optimisation`, except in literal software identifiers.

Write impersonally. Never use `I`, `we`, `our`, `us`, `my`, or `the author`, and
put anything the author did to the apparatus, the campaign, or the data into the
passive: `the rotational stiffness was raised`, `the plane was determined from
one seated pose`, `the controller was implemented`. Naming a case or the thesis as
the agent — `Case D held every gain at baseline`, `this thesis built` — is the
same sentence with the pronoun hidden, and is rewritten the same way. The active
voice stays where the subject is a physical quantity, an effect, or an artefact:
`the improvement fell as \(K_R\) rose`, `the sign of the lever determines the
direction of the induced moment`, `\cref{tab:results_case_d} shows`. The rule and its examples are in the
*Impersonal voice* subsection of [THESIS_VOICE.md](THESIS_VOICE.md).

Do not passivise everything. A uniformly passive chapter is heavier and reads as
more artificial, not less; mathematical and factual statements stay active
(`the Jacobian maps joint velocity to Cartesian velocity`). And a passive
sentence must still carry content — `Four selectable laws are implemented.` is
too generic, where `Four null-space control configurations were implemented.
These comprised an inactive mode, projected joint damping, a singular-value-based
torque, and a combination of the latter two terms.` states what they were.

## Figures and tables

How a figure is drawn or generated is in
[FIGURE_STYLE.md](FIGURE_STYLE.md): TikZ conventions, routing and clearance
rules, plot settings, and how to check a figure in the compiled document. The
rules below cover captions and what the text around a figure must carry.

Keep figure and table captions short, preferably one line and normally below
about 12 words. Use a descriptive noun phrase that identifies the plotted
quantity, comparison, geometry, or parameter set. **A noun phrase, never a
question** — see the question-framing ban under *Scientific narrative*, which
covers captions as well as headings.

Good examples:

- `Set-up settling at 4, 8, and 12 s.`
- `Paired tangent-axis stiffness results (n=5 per setting).`
- `Alignment response by compliance-centre coordinate.`
- `Phase-specific inertia-scaled damping policy.`

Do not place the interpretation, complete procedure, limitations, or a second
discussion paragraph inside the caption. Put that information in the body text
immediately before or after the figure or table. A caption may retain essential
sample-size or uncertainty notation such as `n=5` or `mean ± SD`.

Use an optional short LaTeX caption only when a longer self-contained caption
is scientifically necessary:

```tex
\caption[Short list entry]{Longer caption required to interpret the item.}
```

The List of Figures and List of Tables must always contain concise entries.

**A table column heading takes the same form as a plot axis: descriptive name,
symbol, then the unit in square brackets.** The thesis uses square brackets for
a unit everywhere else — every axis, every symbol-list row — so a heading
reading `\([\theta_{t_1},\theta_{t_2}]\) (deg)` was inconsistent twice over, in
its brackets and in spelling out the degree where the rest of the document sets
the symbol. The direction-check table was corrected on 2026-08-25 to
`Commanded Rotation Components, \([\theta_{t_1},\theta_{t_2}]\) \([{}^\circ]\)`
and `CoC Components, \([r_{c,t_1},r_{c,t_2},r_{c,n}]\) \([\mathrm{mm}]\)`.
A bare symbol vector as a heading also leaves the reader to work out what the
components are of; naming them costs two words. Grep for a unit in round
brackets before submitting.

Never use “tangential stiffness” for a parameter sweep without naming the
axis. State \(t_1\), \(t_2\), or explicitly state that both entries were
changed together. The calibrated-plane campaign varies the rotational
stiffness of one tangent at a time, holding the orthogonal entry at 5 Nm/rad,
so its results are axis-specific and are described as such. The earlier
campaign in the appendix assigned the common values 5, 15, and 50 Nm/rad to
both entries together; those data establish the effect of the paired setting
only and must not be described as an isolated \(t_1\)- or \(t_2\)-axis
effect.

Plots must use the same typeface as the thesis. This document loads
`lmodern`, so generated plots use LaTeX-rendered Latin Modern Roman and Latin
Modern mathematics; do not substitute Times New Roman or a sans-serif default.
Export plots as vector PDF with embedded fonts.

Design each plot at approximately its final printed width instead of creating
an oversized canvas that LaTeX later shrinks. Normally use labels of at least
9--10 pt and tick labels of at least 8.5--9 pt at final size. Prefer short axis
labels, a restrained colour-blind-safe palette, light horizontal grids, and
open markers that remain legible in print. Remove internal plot titles that
repeat the caption, unused panels, and diagnostics that are not discussed in
the text. Visually inspect every plot inside the compiled thesis, not only as a
standalone file.

## Naming a technical quantity

Give each quantity one name and use it everywhere. Where several names are in
circulation, the settled choices are:

- **centre of compliance** for the point the \(6\times6\) stiffness is
  defined about, \(p_c\), with \(r_c=p_c-p_{\mathrm{TCP}}\) as its lever.
  Attributively, `compliance-centre lever`, `compliance-centre coordinate`.

  **\(r_c\) points from the TCP to the centre, and there is no second
  symbol.** An earlier convention defined \(r_c=p_{\mathrm{TCP}}-p_c\) and
  carried a separate \(d_c=p_c-p_{\mathrm{TCP}}=-r_c\) for what the plots
  and tables report, with a standing warning never to rename one into the
  other. **That is withdrawn.** \(d_c\) is removed from the thesis, and
  \(r_c\) now *is* the reported signed coordinate: `centre position +40 mm`
  and \(r_{c,t_2}=+40\,\mathrm{mm}\) are the same statement. Labelling a
  `centre position` axis \(r_{c,t_2}\) is now correct rather than a sign
  error.

  The change removes a real contradiction. Under the old convention the
  supporting intermediate-direction table gave
  \(r_c=[0,-40,0]\,\mathrm{mm}\) for the selected
  \(+10^\circ\) condition about \(t_1\) while the Case-D results showed the
  assisting centre for that same condition at \(+40\,\mathrm{mm}\) along
  \(t_2\). Both now read \(+40\,\mathrm{mm}\).

  **The coupling moment is positive: \(m_{\mathrm{cpl},K}=r_c\times f_K\).** Every
  moment built on the lever follows the same sign —
  \(m_{\mathrm{cpl},D}=r_c\times f_D\) and
  \(m_{\mathrm{cpl}}=r_c\times f\) — and the point-shift blocks carry
  \(-[r_c]_\times\) where they once carried \(+[r_c]_\times\). Terms
  quadratic in the lever, \([r_c]_\times^\top K_p[r_c]_\times\) and its
  damping counterpart, are unchanged, because the sign cancels.

  **The Introduction does not carry \(p_c\).** Chapter 1 names the point in
  words throughout — `centre of compliance`, `virtual CoC`, `compliance
  centre` — and leaves the symbol to Chapter 2, where it is defined. This is a
  deliberate exception to the rule under *Mathematical notation* that a defined
  quantity carries its symbol wherever it is named; do not "restore" the symbol
  there.

  The lever \(r_c\) does stay in Chapter 1, because the chapter uses it at
  \(r_c=0\) and in \(m_{\mathrm{cpl},K}=r_c\times f_K\). It is introduced there
  without \(p_c\), as the displacement from the TCP to the virtual CoC.

  **The implementation stores \(r_c\) itself, in both definitions.** The
  tool-frame `compliance_center_offset_ee` and the surface-frame
  `compliance_lever_surface` both define \(p_c-p_{\mathrm{TCP}}\). Neither
  branch negates: the source forms `r_c = R_EE * offset` and
  `r_c = R_base_surface * lever`, so the variable named `r_c` in the listings
  is \(r_c\) in the thesis convention, and the two branches differ only in the
  frame the stored vector is expressed in.

  **The opposite-vector convention is withdrawn.** The surface-frame parameter
  was once named `r_tcp_from_compliance_center_surface` and stored \(-r_c\),
  and the rule was that the listings were not edited to match while the code
  appendix stated the sign relation instead. Both halves are gone: the key was
  renamed and its negation dropped at all four read sites on 2026-08-25, and
  the code appendix now reproduces the source as it stands, with no sign
  correction in the prose around it.
- **surface frame** for the directional frame \(\{S\}\) the contact
  experiments are resolved in, with
  \(R_{\mathrm{surface}}=[\,t_1\;\;t_2\;\;n_s\,]\). **Never `surface task
  frame`.** The longer name implies a separate surface frame and a separate
  task frame standing beside it, and this thesis has only the one. The
  headings are `Surface Frame`, and the symbol list describes \(\{S\}\) and
  \(R_{\mathrm{surface}}\) as the surface frame.

  **`task` is reserved for generic prose and for source identifiers.** `the
  Cartesian task`, `the primary task`, `the task Jacobian`, `task-retention`
  and `the intended surface task` all stay, because each names the controlled
  objective rather than a frame. So do literal identifiers inside a listing —
  `tau_task`, `Lambda_task`, `diagonal_in_task_frame` — which reproduce the
  source and are not renamed to match the prose. Existing `\label{}` keys keep
  their spelling for the same reason the `automatic` ban exempts them: they
  reach no reader.

  Chapter 3's section over the surface frame, the tool orientation and the
  tool geometry is **Surface-Relative Geometry**, not `Surface-Relative Task
  Representation`, which named those three constructions more abstractly than
  they are.

  **The generic uses of `task` were thinned on 2026-08-26, selectively.** What
  survives is what genuinely names the controlled objective or a standard
  quantity: `the Cartesian task`, `the primary task`, `the task Jacobian`,
  `task-producing singular values`, `task-related component`, `the investigated
  task`, and an `assembly task` or `insertion task` credited to a cited source.
  What went, and what replaced it:

  | Was | Now |
  |---|---|
  | selected task directions | selected Cartesian directions; selected compliance directions |
  | the intended surface task | the intended surface-contact sequence |
  | This task-level result | This experimental result |
  | Cartesian task retention, task-retention criterion | Cartesian position retention, position-retention criterion |

  **`Cartesian position retention` is the accurate name, not `pose
  retention`.** The criterion is
  \(\max\lVert e_p(t)\rVert_2<2\,\mathrm{mm}\) over the disturbance
  interval — a position-error norm alone. Calling it pose retention would imply
  the orientation is checked too, which it is not, and the guide requires a name
  that says what the quantity is. The experiment keeps its own name, `Cartesian
  pose hold`, because that is what the controller regulates.
- **surface** for the flat object the tool is pressed against, and **surface
  plane** where the plane itself is meant. Not `workpiece`: the only property
  that matters is the plane the tool contacts, and `surface` already carries
  the frame, normal, and tangents. `workpiece` also reads as if it might be the
  tool. It is not — the robot holds the tool; the surface is stationary. Since
  both are flat, the two must never be allowed to blur: **`surface` always
  means the contacted plane.** The tool's own flat side is the **tool face**,
  never a bare `surface`, and its measurements are `tool-face dimensions`.

  **`grinding face` is retired; write `tool face`.** The attributive compounds
  go with it, because `grinding-face direction` and `grinding-face geometry`
  cost four syllables to say what `tool normal` and `tool geometry` say
  exactly:

  | Was | Now |
  |---|---|
  | grinding face | tool face |
  | grinding-face direction, grinding-face normal | tool normal |
  | grinding-face geometry | tool geometry |
  | grinding-face orientation | tool orientation |
  | grinding-face axis | tool axis |
  | grinding-face point | tool point |
  | Grinding-Face Direction Calibration *(heading)* | Tool Normal Calibration |

  The **grinding phase** keeps its name, as do the **grinding tool** and the
  **grinding sweep**: those name the process and the object, not the face.

  One exception to the pattern. The centre of the face is the **tool-face
  centre**, not the `tool centre`, which a reader two lines from
  \(p_{\mathrm{TCP}}\) will read as the tool centre point.

  **Keep the surface generic.** Describe it as `a plane surface`, `a given
  surface`, or simply `the surface`. Do not name its material: the results are
  reported as a response of the impedance law to a plane, and naming a material
  invites a reader to attribute the response to that material's stiffness or
  friction, none of which was measured or varied. The same applies to the tool
  and to the gripper fingers.

  **This is a robotics thesis, not a materials one.** Do not carry material
  properties at all — no grades, no surface finish, no hardness, no tribology.
  They are not variables of the study, they were not measured, and listing them
  even as *unrecorded* invites a materials reading of a control result. Limits
  on replication are stated in robotics terms: payload parameters, robot
  transforms, the real-time computer. Statements about what the *controller*
  does or does not model stay — `no environment friction model or friction
  coefficient is used in the control command` is a control-design fact, not a
  materials claim.
- **selected tool point** for the point or edge of the grinding face used as
  the geometric contact reference, \(p_{\mathrm{Tool}}\), with the **tool
  contact-reference offset**
  \(r_{\mathrm{Tool}}=p_{\mathrm{Tool}}-p_{\mathrm{TCP}}\) as its lever. It is
  a different point from the centre of compliance and the two are never used
  for one another.

  **Bind the symbol to the point positively at its first appearance**, by
  naming what \(p_{\mathrm{Tool}}\) is and what it does: the point of the tool
  face that contacts the surface, or is predicted to contact it, used as the
  contact reference during set-up.

  An earlier version of this rule required the sentence *the subscript \(T\)
  is the tool point and not the \(T\) of a homogeneous transformation
  matrix*. **That is withdrawn**, on two counts. It is the `X, not Y`
  correction that *The negation-correction reflex* and *The `X, not Y`
  disclaimer* in [THESIS_VOICE.md](THESIS_VOICE.md) both rule against, and it
  reaches for typographic vocabulary where the thesis should be describing
  geometry.

  **`subscript` is not used in thesis prose**, in any chapter or in the symbol
  list. Where a symbol's index carries a frame, a phase or a point, say what
  the symbol *is* — `\(n_{\mathrm{Tool,EE}}\) is the tool-face normal in
  end-effector coordinates`, `a frame or phase index is added when needed` —
  rather than describing its notation to the reader.

  The symbol has been \(p_{\mathrm{contact}}\), then \(p_g\), then
  \(p_T\). **The index is spelled out as `Tool`**, because a single \(T\)
  reads as the contact, as a transpose, or as a homogeneous transformation
  before it reads as the tool. One name now: \(p_{\mathrm{Tool}}\) in every
  chapter, the symbol list, and every figure, with
  \(r_{\mathrm{Tool,EE}}\) for its end-effector-frame offset. The two levers
  were at one point \(r_c\) and \(r_C\),
  distinguished only by the case of one letter, which no reader can hold across
  a page and which a printed index does not reliably show;
  \(r_{\mathrm{Tool}}\) against \(r_c\) is the replacement and must not
  drift back. The earlier displacement metrics
  \(\Delta p_{\mathrm{Tool}}\), \(s_{\mathrm{Tool}}\),
  \(\Delta p_{\mathrm{TCP}}\), and \(s_{\mathrm{TCP}}\) are withdrawn because
  they are not reported in the results.

  The wording is settled with the symbol: it is the **selected tool point** in
  every chapter, never a `tool feature` and never a bare `edge`. `edge`
  presumes edge contact, and the set-up phase is designed to seat the tool face
  flat.

  **Do not write `selected tool point or edge`.** \(p_{\mathrm{Tool}}\) is one position
  vector; where an edge leads, the controller uses its midpoint. Say what it is
  once, at the definition — depending on the tool orientation it is a leading
  corner, the midpoint of a leading edge, or the tool centre — and then call it
  the selected tool point everywhere else.

  \(r_{\mathrm{Tool,EE}}\) is what is **fixed relative to the tool** once the
  contact reference has been selected. Its base-frame representation
  \(r_{\mathrm{Tool}}=R_{\mathrm{EE}}r_{\mathrm{Tool,EE}}
  =p_{\mathrm{Tool}}-p_{\mathrm{TCP}}\) rotates with the tool, so do not write
  that \(r_{\mathrm{Tool}}\) is fixed by the geometry: name the frame the
  statement is true in.
- **pole** is implementation vocabulary from the parameter names. Keep it in
  equation labels and parameter keys, not in the running text.
- **commanded tool orientation offset** for the deliberate angular command: a
  `commanded tool orientation offset about t1`. Its components are the
  **commanded rotation axis**, **commanded rotation direction**, and **offset
  angle**. Use `zero orientation offset` and `reversed orientation offset` for
  the corresponding conditions. Do not use `tilt`, `tool tilt`, or `signed
  tilt` where this commanded quantity is meant. Not
  `excitation`, which is borrowed from system identification and describes an
  input signal rather than a commanded orientation, and not `mismatch`, which
  implies an unwanted discrepancy where the angle is deliberate.

  **In the Chapter 5 comparison tables the condition column is `Initial
  commanded orientation`.** It identifies the input condition without adding
  a second measured entry angle. A quantitative plot axis uses `Commanded
  orientation offset` followed by \(\theta_{t_i}\) and its unit. The shorter
  `Commanded offset` remains available in compact methodology tables where the
  condition has already been introduced. These are presentation forms of the
  same commanded tool orientation offset, not separate quantities.

  The supporting intermediate-direction table heading is **not** an instance
  of it. That column holds
  `Commanded rotation direction` — the tangent-plane direction of the command,
  with rows `about t1`, `-45 deg from t1` and so on, at a common offset
  magnitude. It names a different component and keeps its own heading.

**There is no fixture in this work, and the word must not appear.** No fixture,
jig, clamp, or workholding device was used: the surface is simply positioned,
and the tool is held in the gripper. Earlier drafts used `fixture` loosely for
three different things, and each needs its own correct name:

- where the *surface* is meant — `the surface`, or `the surface placement`
  where the tolerance of that placement is the point;
- where the *gripper's hold on the tool* is meant — `the tool mount`. This is
  the one that carries the \(\pm2^\circ\) of play and the \(t_2\) limitation;
- where the *whole rig* is meant — `the setup`.

Getting this wrong is not only a wording fault. The anomalous \(10^\circ\)
\(t_2\) repetition was attributed to "the fixture" in two places while
Section 5.10 explained it through the tool mount, so the thesis named two
different causes for one observation.

**The word `automatic` is not used in thesis prose, in any form.** Not
`automatic`, `automatically`, or `automatic-`. It contrasts what the controller
does with an unstated manual alternative that this thesis never ran, and in
every place it appeared the specific name was already available and carried more
information:

| Was | Now |
|---|---|
| the automatic sequence | the run sequence |
| the automatic disturbance experiment | the internally commanded disturbance experiment |
| automatic error recovery | error recovery |
| automatic leading-feature selection | leading-feature selection |
| the automatic gripper action / a failed automatic action | the gripper action / a failed gripper action |
| these automatically damped phases | the phases using inertia-scaled damping |
| executed automatically immediately before torque control | executed immediately before torque control |

The ban covers running text, captions, and headings. It does **not** cover
literal source: `robot.automaticErrorRecovery()` is the libfranka call and the
`AutomaticDisturbance` type is the implementation's own name, so both stay
verbatim inside listings. Existing `\label{}` keys and generated figure
filenames also keep their spelling, since neither reaches the reader.

**`bias`, `biased` and `unbiased` are not used in thesis prose.** The word
carries a statistical meaning the thesis never intends, and in the
compliance-centre discussion it hid the actual mechanism: a tangential
\(r_c\) does not bias anything, it selects a tangential direction and
therefore a rotational sense for the coupling moment. Name that instead:

| Was | Now |
|---|---|
| the lever biases the steady contact | the lever keeps a preferred rotational direction while the press continues |
| a biased response | a direction-dependent response; a directional asymmetry |
| the additional biased moment | the additional one-sided moment |
| an unbiased centre | a centre that selects no tangential direction |
| \(\tau_\sigma\) biases the robot toward the sampled direction | \(\tau_\sigma\) drives the robot toward the sampled direction; applies an active torque toward |
| alignment-angle bias | common calibration offset; systematic calibration-related offset |

The ban covers running text, captions and headings alike. Literal source
identifiers keep their spelling.

**`sweep` is not used for a set of tested parameter values.** It is too vague:
it names neither the quantity that was varied nor the values it took, and it
carries an impression of a continuous traverse where the campaign tested a
handful of discrete settings. Name the quantity and the positions instead:

| Was | Now |
|---|---|
| Case~D is the main compliance-centre sweep | Case~D is the main compliance-centre variation |
| would appear as one column of the sweep | would appear as one column of the table |
| The preceding sweep establishes the final dependence | The preceding lever positions establish the final dependence |
| comparable with the tangential sweep of Case~D | comparable with the tangential displacement of Case~D |
| The tool-axis sweep is flat across its whole range | The tool-axis response is flat across the whole tested range |
| the per-setting spread of this sweep | the per-setting spread of these lever positions |

**The grinding sweep keeps the word**, because there it names a physical
oscillating motion of a definite amplitude and frequency rather than a set of
parameter values, and it is the name the controller parameter carries. Literal
identifiers such as `grind_sweep_enabled` keep their spelling in listings and
in the parameter appendix.

**A run is recorded or it is not; it is never `newly recorded`.** The thesis
does not sort its measurements by when they were captured, so `newly recorded`,
`already recorded`, `previously recorded` and `re-recorded` all invite a reader
to look for an ordering the thesis never reports, and they read as an account of
how the campaign was assembled rather than of what it measured. Say `recorded`,
or say nothing about recording at all:

| Was | Now |
|---|---|
| the five newly recorded intermediate-direction settings | the five supporting intermediate-direction settings |
| the three scheduled repetitions for each newly recorded setting | the three scheduled repetitions of each setting |
| the \(5\,\mathrm{N\,m/rad}\) condition … is not a separate measurement | the \(5\,\mathrm{N\,m/rad}\) condition is the corresponding zero-lever reference of Case~A |

The same applies to the run-count bookkeeping. Where one case reuses a
condition from an earlier case, state the relation between the cases — `a
condition that a case shares with an earlier one is counted with that earlier
case` — and not the recording history that produced it. Never write `not
counted again`, `not recorded twice`, or `an additional run`.

Do not build a name out of the state a quantity happens to be in. The term
`frozen` is not used in thesis prose. State when a quantity is selected and
that it is held constant, then use its ordinary technical name. For example,
the centre of compliance is selected at the clearance transition and held
constant during set-up; subsequent references call it the centre of compliance.

Symbols follow the same rule. One point, one subscript: \(p_c\), \(r_c\),
\(K_c\), \(D_c\).

## Mathematical notation

At the first equation in which a new symbol appears, introduce it in the
surrounding running text by giving the quantity name, the symbol, and its short
role in that equation. The definition may appear immediately before or after
the equation, but the reader must not have to infer the symbol from the
expression alone. Do not repeat a definition that has already been established
unless the symbol is assigned a different local meaning.

Whenever running text names a defined mathematical quantity, place its symbol
immediately after that name. For example, write `the alignment angle
\(\theta_{\mathrm{align}}\)` and `the commanded joint torque
\(\tau_{\mathrm{cmd}}\)`. This rule applies to repeated uses as well as to the
first definition. It does not apply to generic physical nouns that do not denote
a specific defined variable, or to an unambiguous pronoun or shortened reference
such as `this matrix` or `the value`.

**A direction that exists in two frames carries the frame in its subscript.**
The tool-face normal is \(n_{\mathrm{Tool,EE}}\) in end-effector coordinates
and \(n_{\mathrm{Tool},0}\) in the base frame, with
\(n_{\mathrm{Tool},0}=R_{\mathrm{EE}}n_{\mathrm{Tool,EE}}\). They are one
physical direction in two frames, and the subscript is what says which.

This replaces \(n_{\mathrm{EE}}\) and \(n_T\), which were read as two different
quantities: \(n_{\mathrm{EE}}\) looked like a property of the end effector
rather than of the tool, and \(n_T\) named no frame at all. The longer form is
deliberate — it is harder to misread, and the pair \(n_{\mathrm{T,EE}}\) /
\(n_{\mathrm{T},0}\) was rejected for the same reason. `Tool` stays capitalised
and roman in both.

**One typeface: plain italic.** Every symbol — scalars, vectors, and matrices
alike — is set plain: \(F\), \(f\), \(m\), \(e_p\), \(e_R\), \(p\), \(q\),
\(K\), \(D\), \(J\), \(R\), \(T\), \(N\). Do not use `\mathbf`.

The thesis previously mixed the two, with \(e_p\) bold in Chapter 2 and plain in
Chapter 3, and with the appendices bolding matrices the chapters set plain. The
majority form was already plain, and plain is what the symbol list now shows.

The **one exception** is the zero vector \(\mathbf{0}\), where the bold
distinguishes it from the scalar zero. Keep that.

**Do not mark design values with a star.** Reuse the symbol already defined for
the physical quantity and state in prose that the value is used for sizing. If
a genuinely different quantity is needed, use a descriptive subscript and
define it once. Do not create a second family of starred force, displacement,
moment, damping, or fit symbols.

**The wrench is \(F\), everywhere.** It is never \(W\). \(W\) previously
appeared in Appendix C for the local-to-base rotation of a stiffness frame,
which is a rotation and therefore takes \(R\) — there written
\(R_{\mathrm{local}}\), matching \(R_{\mathrm{surface}}\) in the main text.
Rotation matrices are \(R\) without exception.

**Gains carry the frame they are diagonal in, as \(S\) or \(0\).** The
directional gains are defined along \([t_1,t_2,n_s]\) and are written
\(K_{p,S}=\operatorname{diag}(K_{p,t_1},K_{p,t_2},K_{p,n})\),
\(K_{R,S}\), \(D_{p,S}\) and \(D_{R,S}\); their base-frame representations keep
the \(0\) already in use, so \(K_{p,0}=R_{\mathrm{surface}}K_{p,S}
R_{\mathrm{surface}}^\top\). The chain the reader follows is *gains in surface
coordinates → \(R_{\mathrm{surface}}\) → gains in base coordinates*, and it is
stated once.

**\(a_s\) is withdrawn, with \(\tilde t_1\).** Both are written here as
literal strings so a rename cannot revive them. The first-tangent hint is
\(e_{x_0}\) in every reported run and Appendix C records it as
`surface_tangent1_hint_base = [1,0,0]`, so a separate theory symbol for it
added a layer of abstraction over a constant. Section 2.5 now projects
\(e_{x_0}\) directly. **Chapter 3 keeps the concept, in words**: the hint is
a configuration parameter there, not a fixed axis, which is why the
implementation carries a fallback when it lies close to \(n_s\). That is the
Chapter 2 / Chapter 3 split under *Separate theory from configuration*, not an
inconsistency.

**Section 2.5 says why the projection is needed, and does not walk through the
dot product.** The settled form is: the first tangent follows the base-frame
\(x_0\)-direction as closely as possible while remaining in the surface
plane, and *because the surface is not exactly parallel to the base
\(x_0y_0\)-plane*, \(e_{x_0}\) is projected and normalised. That clause is
a checkable particular — the calibrated tilts are \(-1.585^\circ\) and
\(+0.988^\circ\) — and it replaced three sentences explaining that
\(n_s^\top e_{x_0}\) is a scalar component and \(n_s(n_s^\top e_{x_0})\)
the vector it scales. Explaining a projection to the reader is the
*Textbook restatement* pattern; stating why one is required is not.

**Section 2.5 is settled, and \(\tilde t_1\) is withdrawn.** Agreed
2026-08-26. The section states what the frame is for, then constructs it in
three steps: the first tangent as one normalised expression, the second by the
cross product, and \(R_{\mathrm{surface}}\). The
intermediate unnormalised tangent `\tilde{t}_1` is written here as a literal
string so a rename cannot revive it — \(t_1\) is now defined directly, in one
fraction, and a symbol that exists only to be normalised away a line later
earns nothing. The Gram--Schmidt naming and its citation went with it: the
projection is explained in words instead, which *Textbook restatement* in
[THESIS_VOICE.md](THESIS_VOICE.md) prefers over naming the standard procedure.

**The reference-direction caveat stays.** \(t_1\) is fixed by a configured
choice rather than by the surface, so *an axis-specific result holds with
respect to the configured reference direction*. Chapter 5's central findings
are axis specific — the \(t_1\)-against-\(t_2\) asymmetry, the opposite
assisting lever directions — and that sentence is what bounds them. It is a
scientific commitment, not filler, and it is not dropped when the section is
shortened.

**The base-frame unit axes are \(e_{x_0}\), \(e_{y_0}\), \(e_{z_0}\).**
Section 2.1 names the base axes \(x_0\), \(y_0\), \(z_0\), so their unit
vectors carry the same index. Chapter 4 and the parameter appendix used bare
`e_x` and `e_z` for the same vectors until 2026-08-26; both were harmonised,
along with the \(n_s=R_{\mathrm{EE}}e_{z_0}\) box in Figure 4.2, and the
symbol list carries one row for the family.

**Section 2.6 is settled, and its shape is deliberate.** Agreed 2026-08-26:
the section opens by saying *why* the frames differ — the impedance law is
evaluated in the base frame while the gain values are specified relative to the
calibrated surface, because the directions that matter for contact are
\(t_1\), \(t_2\) and \(n_s\). Then, in order: the four surface-frame
matrices, the axis order in one sentence, the two congruence transforms into
the base frame, the block-diagonal \(K_0\) and \(D_0\), and a forward
pointer saying that translation and rotation are still decoupled at that stage
and that the compliance-centre transformation of Section 2.7 can couple them.

**The four gain matrices are written out as explicit \(3\times3\) arrays,
not as `\operatorname{diag}`.** The point of the section is which entry sits on
which axis, and the explicit form shows the \([t_1,t_2,n_s]\) ordering where
`diag` asks the reader to reconstruct it. This does **not** conflict with
*Isotropic matrices are a table, not a display* under Chapter 4: that rule
governs four numeric matrices whose diagonal entries are all equal, which say
four numbers and belong in a table. These are symbolic definitions and each
entry is a distinct named gain.

**Section 2.5 does not pre-empt it.** The column-order paragraph ends at the
column order and points forward; naming \(K_{p,t_1}\), \(K_{p,t_2}\) and
\(K_{p,n}\) there as well made the same statement twice, one page apart.

**\(R_{\mathrm{task}}\) is withdrawn, with \(K_{p,\mathrm{task}}\),
\(D_{p,\mathrm{task}}\), \(K_{R,\mathrm{task}}\), \(D_{R,\mathrm{task}}\),
\(K_{\mathrm{task}}\) and \(D_{\mathrm{task}}\)** — written here as literal
strings so a bulk rename cannot revive them. A generic task frame introduced
ahead of the surface frame and then set equal to it,
\(R_{\mathrm{task}}=R_{\mathrm{surface}}\), is an alias the reader has to carry
for no gain: this thesis has one directional frame, and the gains are defined
along its axes. State them along \([t_1,t_2,n_s]\) directly.

\(\Lambda_{\mathrm{task}}(q)\) is **not** an instance of this. It is the
operational-space inertia of the Cartesian task, it names no frame, and it
keeps its index.

### The frame index appears only where frames are compared or transformed

**When a frame index is shown it is a lower index, and there are three of
them:**

\[
(\cdot)_0=\text{base coordinates},\qquad
(\cdot)_S=\text{surface coordinates},\qquad
(\cdot)_{\mathrm{EE}}=\text{end-effector coordinates}.
\]

**The index is written only where two frames are actually being compared or one
is being transformed into another**, and nowhere else. Its whole job is to say
which of two representations is meant; on a quantity that appears in one frame
only, it is dead weight the reader has to carry through every equation. The two
places it earns its keep are

\[
r_{c,0}=R_{\mathrm{surface}}r_{c,S}
\qquad\text{and}\qquad
r_{c,0}=R_{\mathrm{EE}}r_{c,\mathrm{EE}},
\]

which is exactly the surface-fixed against tool-fixed contrast that the
definition-frame supporting check examines. Section 2.7.2 states both, one line
apart. \(K_{p,0}\) against \(K_{p,S}\) and \(\gamma_0\) against \(\gamma_S\)
are the other instances.

**Bare \(r_c\) is the default form and stays.** It is used throughout Chapters 1
to 6, the figures and the appendices — in \(r_c=p_c-p_{\mathrm{TCP}}\),
\(\mathrm{Ad}(r_c)\), \([r_c]_\times\), \(m=m_R+r_c\times f\), the
direction-selected lever rule and every reported coordinate. **Do not replace it
globally with \(r_{c,0}\).** Where no frame index is shown, the base-frame
representation is implied, and the symbol list says so.

**The superscript form \(r_c^{S}\) is withdrawn**, written here as a literal
string so a rename cannot revive it. It mixed two things in one expression —
the coordinates of the displacement in the surface frame, and the
transformation of those coordinates into the base frame — and it put the frame
index above the line where the rest of the thesis puts it below. The surface
coordinates are \(r_{c,S}=[\,r_{c,t_1},\;r_{c,t_2},\;r_{c,n}\,]^\top\), with
the inverse \(r_{c,S}=R_{\mathrm{surface}}^\top r_{c,0}\) available where a
base-frame vector has to be resolved.

**The tangential vector stays \(r_{c,t}\).** `r_{c,t,0}` is written here as a
literal string so a rename cannot revive it: a triple index is hard to read,
and \(\lVert r_{c,t}\rVert\) is frame independent and would carry no index
anyway, so indexing the vector alone would split a pair that belongs together.
The scalar components \(r_{c,t_1}\), \(r_{c,t_2}\) and \(r_{c,n}\) are
unchanged for the same reason — they are signed surface-frame coordinates and
carry no second index — and \(\lVert r_c\rVert\) takes none either.

Macros defined in `config/commands.tex` (`\vF`, `\mK`, `\R{3}`, …) predate this
convention. `\R{n}` for \(\mathbb{R}^n\) is in active use and stays; the
bold-producing ones are not used in the chapters and should not be reintroduced.

**cleveref cannot type a label set inside a `longtable`.** Both obvious fixes
are wrong and the second is worse, because it looks right in the source:
`\label{}` alone gives the correct number with the wrong type, so `\Cref`
printed `Section 4.4` for a table; `\label[table]{}` fixes the type but builds
the number from the enclosing section prefix, so the same reference printed
`Table 4.3.2` for Table 4.3. Reference a `longtable` as literal
`Table~
ef{...}`, which takes its number from `\@currentlabel` and is right
in both respects. Check the rendered words in the PDF, not the source — neither
failure raises a warning.

**An unnumbered chapter's contents entry goes before the chapter, never after
it.** `\addcontentsline` records `\thepage` where it stands, so the line

```tex
\bibliography{config/literature}
\addcontentsline{toc}{chapter}{Bibliography}
```

wrote the page current *after* the reference list had been typeset: the
contents named the bibliography's last page, four pages past where it starts.
Nothing warns, and the number is plausible enough to survive several reads. The
correct order is the one the two front-matter lists already use, and the
bibliography was brought into line with it on 2026-08-25 in `Thesis.tex`,
`Professor_Draft.tex` and `Review_Draft.tex`:

```tex
\cleardoublepage
\phantomsection
\addcontentsline{toc}{chapter}{Bibliography}
\bibliography{config/literature}
```

`\phantomsection` gives hyperref an anchor on the right page, and the
`\cleardoublepage` before it is what keeps the entry from landing on the
previous chapter's last page. Verify by reading the page number off the
compiled bibliography and comparing it with the contents; a `.toc` file cannot
be checked against itself.

**Never normalise notation with a bulk regex.** A backslash-stripping
substitution across the `.tex` files silently produced 190 undefined macros and
four merged control sequences (`\times\e_R` collapsing into `\timese_R`), none
of which is visible without a compile. If a notation change has to be made in
bulk, compile both `Thesis.tex` and `Professor_Draft.tex` immediately
afterwards, and diff the set of `\macro` tokens against the previous commit —
any token that is new is a merge.

## Units in the list of symbols

Every symbol carries its unit. Do not write `mixed`, which tells the reader
nothing about a quantity they came to the list to look up.

A matrix whose blocks carry different units lists those units. A full
\(6\times6\) Cartesian stiffness is `[N/m], [N m/rad]`, its damping is
`[N s/m], [N m s/rad]`, and its coupling sub-blocks are `[N/rad], [N m/m]`. The
operational-space inertia is `[kg], [kg m], [kg m^2]`. Where one row lists a
stiffness and a damping together, label which units belong to which.

Write a product of units as a product: `N m` and not `Nm`, `N s/m` and not
`Ns/m`, `kg m^2` and not `kgm^2`. Use a thin space, `\,`, so the factors stay
separable in print.

Dimensionless entries are `[-]`. A quantity whose rows carry different units,
such as a Jacobian, lists them in the order the rows appear: `[m/rad], [-]`.

**That form belongs to the matrix, not to a scalar computed from it.** A
singular value of the geometric Jacobian is one number, so `[m/rad], [-]` says
it carries two units at once, which it does not. The rows the \abbr{SVD}
combines have different units, and the consequence is that the scalar's value
depends on the Jacobian representation and the length unit rather than that it
has two units. \(\sigma_i\), \(\sigma_{\min}\) and
\(\Delta\sigma_{\min,\mathrm{dist}}\) therefore take `[-]`, and the
representation dependence is stated in the description column, where the rule
above already sends every qualification. Corrected on 2026-08-25. The same
applies to any other scalar formed from a mixed-unit matrix: give the units
column one entry, and explain the dependence in words beside it.

The units column holds units and nothing else. Words such as `linear`,
`angular`, `scale dependent` or `mixed` are not units, and a reader scanning
the column for a unit has to stop and parse them. Where a unit needs
qualifying, the description column carries the qualification: the Jacobian's
description says which rows come first, and the singular values say that their
value follows the length unit of the linear rows.

## Abbreviations

Every abbreviation is spelled out once, at its first appearance in the running
text, with the short form in brackets. After that the short form alone is used:

```tex
seven-degree-of-freedom (\abbr{DOF}) Franka Emika Panda
the singular value decomposition (\abbr{SVD})
```

Declare it in `config/acronyms.tex` so it reaches the abbreviation list:

```tex
\DeclareThesisAcronym{SVD}{SVD}{Singular Value Decomposition}
```

`\abbr` does not expand anything by itself. It prints the short form and marks
the entry as used so the list can include it, which means a first use that is
not spelled out by hand stays unexplained everywhere.

A symbol list entry does not count as introducing an abbreviation. `SVD`
appeared in a symbol description and a group heading while the running text
never once expanded it.

Axis-label strings such as `base XYZ` are not abbreviations and are not
declared; they name the axes rather than standing in for words.

Check with a scan for two-to-six-letter capital tokens in the chapters, not by
memory — the ones that slip through are the ones that feel too familiar to
notice.

## Software identifiers in the text

Do not print long configuration or field names in the running text. A name
carrying two or more underscores is a file-format detail rather than a
scientific quantity, and it reads as source code instead of prose. State what
the setting does:

- `the centre of compliance is selected at clearance and held constant during
  set-up`, not the parameter name that sets it;
- `the model-estimated external wrench`, not the field it is read from;
- `the end-effector pose reported by the robot`, not the state member;
- `the gate-hold translational damping`, not the parameter key.

A short parameter name with at most one underscore may be printed where the
exact key matters, for example where a reader would otherwise be unable to
locate the setting. Literal identifier lists, such as the set of phase labels a
log can contain, remain acceptable because the identifiers themselves are the
subject.

Complete parameter names belong in the parameter appendix and the data-format
appendix, where the identifier is the point.

**`run time` and `runtime` are not used for the moment of execution.** Written
that way the words name a part of the implementation rather than anything the
reader can check, and they read as source vocabulary in prose that is otherwise
about geometry and measurement. Say what happens and to what: `that direction
\(n_T\) follows from \(n_{\mathrm{EE}}\) and the measured end-effector
orientation`, `the controller forms`, `during set-up`, `while the press
continues`.

**The elapsed-time sense keeps the words.** The logged `Run time` column and
its row in the Chapter 3 table name the seconds since the run started, which is
a physical quantity. Do not sweep those away with the ban.

## Repository and software language

Do not mention Git repositories, branches, tags, commits, checkouts,
uncommitted changes, earlier implementations, or draft-merging history in the
thesis. Reproducibility should be expressed using scientifically relevant
information such as:

- robot and tool;
- operating system, real-time kernel, compiler, Eigen, and libfranka versions;
- control and logging rates;
- tool geometry and robot transforms;
- active controller parameters;
- experimental procedure and repetitions.

Different configurations may be distinguished only when the difference
materially affects the scientific interpretation.

## Cross-chapter factual consistency

Every configuration fact — which terms were active, which gain values, which
durations, which calibration procedure — must read identically in every chapter
that states it. A supervisor pass found four contradictions of this kind, none
visible from inside any single chapter:

- **What was active.** Chapter 3 said the combined null-space mode was used,
  Chapter 4 said the singular-value bias was *not* active, Chapter 6 said both
  terms ran together. Resolve against
  `backmatter/appendix_controller_parameters.tex`, which transcribes the
  parameter files, then state it once and cross-reference that table.
- **Which gain.** The baseline translational stiffness appears as
  \(\operatorname{diag}(2000,2000,800)\) in the surface frame and
  \(\operatorname{diag}(2000,2000,350)\) in base coordinates. Two diagonal
  matrices in frames \(10^\circ\) apart cannot both be the same gain: a
  congruence transform of a diagonal matrix is not diagonal. Naming the frame
  is not enough — the numbers must reconcile.
- **Which duration.** A \(4.0\,\mathrm{s}\) set-up timeout was stated in three
  places in the methodology chapter. Every recorded run of every campaign used
  \(5.0\,\mathrm{s}\); the \(4.0\,\mathrm{s}\) figure matched no parameter file.
- **Which plane.** The implementation chapter gave the active baseline surface
  point and tilt angles as \(p_s=(0.526,0.017,0.002)\,\mathrm{m}\),
  \(a=-0.474^\circ\), \(b=2.270^\circ\), which appear in no parameter file,
  no calibration overlay, and no run record. The calibrated plane is
  \(p_s=(0.5153,-0.1072,0.0031)\,\mathrm{m}\), \(a=-1.585^\circ\),
  \(b=+0.988^\circ\), used by all 193 recorded runs.
- **Which procedure.** The physical plane comes from **one seated pose of the
  complete tool face**, as `tools/measure_plane.cpp` performs it. The plane
  normal is the *configured* end-effector axis carried into the base frame, and
  for the stored plane that axis was the **nominal \(+Z_{\mathrm{EE}}\)**:
  the plane was calibrated before the tool normal and was never measured again
  afterwards, so \(n_s=R_{\mathrm{EE}}[0,0,1]^\top\) and **not**
  \(n_s=R_{\mathrm{EE}}n_{\mathrm{EE}}\), which this guide asserted until
  2026-08-24. The two differ by the \(1.56^\circ\) between the calibrated tool
  normal and \(+Z_{\mathrm{EE}}\), and Section 4.2.1 states that difference as a
  calibration offset common to every reported run. The plane point is the
  tool-face centre of that same pose,
  \(p_s=p_{\mathrm{EE}}+R_{\mathrm{EE}}r_{\mathrm{face,EE}}\). The repository
  contains no plane-fitting routine of any kind. The **tool-normal seatings**
  are a separate
  calibration and measure the tool, not the surface. The controller holds only
  the configured plane, set from the tilt angles \(a\) and \(b\), and contains
  no calibration routine at all — the calibration tools are separate
  executables — so any sentence implying the controller measured the surface is
  wrong by construction.

  **Section 4.2 states the consequence of that, not only the fact.** Saying the
  two calibrations were kept independent, and quoting the \(1.56^\circ\)
  between the calibrated tool normal and nominal \(+Z_{\mathrm{EE}}\), leaves
  the obvious examiner question unanswered: if the tool is seated flat, why is
  the physical tool normal not used to define the surface normal? Four
  sentences added on 2026-08-25 answer it. The surface frame the controller
  holds is a configured geometric reference rather than an independent
  measurement of the physical plane normal; it was taken from the nominal
  end-effector axis at one seated pose; the \(1.56^\circ\) is the difference
  between those two orientation references and applies equally to every
  reported run; and because it limits an absolute interpretation of the
  physical tool--surface angle, the main comparisons report the signed
  end-effector set-up rotation instead. That last clause is the point of the
  passage — the calibration limitation is the reason the primary metric is what
  it is, so stating it strengthens the metric choice rather than conceding a
  weakness.

**Rule.** A number or configuration fact has one home — the methodology chapter
or the parameter appendix — and every other mention cross-references it rather
than restating it from memory. Before submitting, grep each key value across all
chapters and confirm a single answer.

## What belongs in the thesis at all

**State the levels actually tested, never an illustrative sweep.** Section 4.4.4
carried a generic five-level scaling \(\alpha\in\{0.5,0.75,1,1.25,1.5\}\) and
then spent a paragraph explaining that this was *not* what was run. A
hypothetical set up only to be dismissed wastes the reader and invites the
question of which numbers are real. Give the tested values: \(5\), \(15\) and
\(50\,\mathrm{N\,m/rad}\); \(300\), \(800\) and \(2000\,\mathrm{N/m}\).

**Separate theory from configuration.** Chapter 2 carries the law and its
assumptions; Chapter 3 carries what was built and which options were selected.
An enumeration of selectable software modes is a control-design decision, not
theory — the four null-space modes moved out of Chapter 2 for that reason, and
the theory chapter now gives one complete null-space torque instead. The same
split applies to limitations: mathematical properties of a method stay with the
method, implementation shortcomings go to Chapter 3 or the limitations.

**Tooling built only for your own analysis is not thesis content.** A second
diagnostic log existed to support offline inspection and appeared in three
chapters and two appendices before being removed. If a facility did not
contribute to a reported result, it does not need documenting. The same applies
to exception handling, persistence ordering, and any other detail that matters
only when debugging a run.

**Do not trim a derivation the reader needs.** An earlier pass reduced the
orientation-error and forward-kinematics sections to a few lines each, on the
grounds that the material is standard. Both were restored from
`a8f8337^`, because a thesis that states a convention without deriving it leaves
the examiner unable to check the sign work that the whole controller depends on.
Length targets for Chapter 2 are suspended: cut repetition and dimension
restatements, not derivations.

## What may be set as a numbered equation

Sort the material before typesetting it:

- **a trajectory or a physical relation** → a numbered equation;
- **if/else logic, a transition criterion, a configuration rule** → prose, or
  an algorithm if it is long enough to need one;
- **a software sequence** → a diagram or a sentence;
- **an experimental value** → the methodology chapter or a table.

Chapter 3 previously broke this in both directions at once. It numbered a
configuration condition (`tool-frame definition ⊕ surface-frame definition =
true`), a start-up order (`FCI connection → error recovery → collision
configuration → robot model`), a return statement, a ring-buffer row, and a
post-run output chain — none of which is a mathematical relation — while
leaving genuine implementation relations in prose. All five have been rewritten
as sentences. Do not reintroduce that form.

### Chapter 3: the settled structure

Chapter 3 was partly repeating Chapter 2 and partly anticipating Chapters 4
and 5, which is what made it read as a second theory chapter. The rule that
fixes it is one sentence: **Chapter 3 says how the equations of Chapter 2 were
built into the controller that ran the experiments, and derives nothing.** The
earlier seven-point plan in this guide is superseded by the structure below.

```tex
\section{Controller Architecture and Real-Time Control Cycle}
\section{Surface-Relative Geometry and Tool Representation}
  \subsection{Surface Frame and Tool Orientation}
  \subsection{Tool Geometry and Selected Contact Point}
\section{Phase-Dependent Cartesian Impedance}
  \subsection{Directional Stiffness and Damping}
  \subsection{Virtual Centre of Compliance}
\section{Contact Sequence and Reference Generation}
  \subsection{Orientation and Surface Approach}
  \subsection{Contact Set-Up}
  \subsection{Auxiliary and Post-Set-Up Modes}
\section{SVD-Based Null-Space Implementation}
\section{Real-Time Operation, Safety, and Data Recording}
```

The chapter introduction is short and says why the equations are not repeated:
the relations of Chapter 2 are referenced rather than restated, and the
numerical settings are in Chapter 4 and Appendix C.

**What Chapter 3 does not contain.** Each of these is in Chapter 2 and is
cross-referenced from Chapter 3 in a clause:

| Removed from Chapter 3 | Lives in |
|---|---|
| The construction of \(R_{\mathrm{surface}}\) from \(a_s\) and \(n_s\) | Section 2.5 |
| \(e_p=p_d-p_{\mathrm{EE}}\), \(\Delta R=R_{\mathrm{EE}}^\top R_d\), \(e_R\) | Section 2.2 |
| The impedance wrench \(F=K\Delta x+D\Delta v\) | Section 2.4 |
| A standalone \(\tau_{\mathrm{cart}}=J^\top F\) | inside the one final torque equation |
| \(G_0=R_{\mathrm{surface}}G_{\mathrm{surface}}R_{\mathrm{surface}}^\top\) | Section 2.6 |
| Why a displaced centre produces an aligning moment | Section 2.7, and Chapter 5 for the measurement |
| The null-space projector, damping and conditioning derivations | Section 2.8 |
| \(M(q)Y(q)=J^\top(q)\), \(Y=M^{-1}J^\top\), \(\Lambda_0=(JY+\varepsilon I)^{-1}\) | reduced to one sentence; the damping implementation is not a contribution of this thesis |

**The nominal controller equation is
\(\tau_{\mathrm{cmd}}=J^\top(q)F+\tau_{\mathrm{null}}+\tau_c(q,\dot q)\), and
\(\tau_{\mathrm{dist}}\) is not in it.** The disturbance is an experimental
input rather than part of the controller, so its definition belongs to
Section 4.6 alone, where \(\tau_{\mathrm{dist}}(t)=J_p(q(t))^\top f_d(t)\)
already stands. Chapter 3 carries one sentence saying an experiment-specific
disturbance torque is added only for the null-space pose-hold experiment and is
therefore not part of the nominal formulation. It does not appear in the
null-space section either.

**What Chapter 3 must keep**, because these are what was designed rather than
what was derived: the architecture figure; the commanded surface-relative
offset \(\theta_{\mathrm{tilt}}=\theta_{t_1}t_1+\theta_{t_2}t_2\) and the
flat-axis target it rotates; the tool geometry and the selection of
\(p_{\mathrm{Tool}}\); the tool-fixed against surface-fixed compliance-centre
definition; the set-up reference generation, with
\(p_{\mathrm{Tool},d}(t)\) and the reconstructed \(p_d(t)\); the statement that
the orientation captured at the clearance transition is held for the whole of
set-up; the \abbr{SVD} details that differ from the theory; and the
real-time-safe recording.

**Two implementation equations are restated deliberately.**
\(K_{\mathrm{TCP}}=\operatorname{Ad}^\top(r_{c,0})K_c\operatorname{Ad}(r_{c,0})\)
and its damping counterpart appear in Chapter 3 not as a derivation but as a
concise statement of what the code evaluates. One sentence then says that the
point-shifted impedance lets the commanded normal press contribute to the
rotational response, and sends the measurement to Chapter 5. Do not re-argue
the cross terms there.

**The grinding phase gets a short paragraph and no more.** No reported run
entered it, so the chapter states that it maintains the normal set-up reference
while superimposing a tangential motion, that it returns to the decoupled
impedance, and that it was not entered in the reported experiments.

**The set-up subsection stays detailed.** It is the one place that explains
something Chapter 2 does not: how the reference is generated during contact.
The sentence that the rotational reference is held while finite rotational
compliance permits contact-induced end-effector rotation is the load-bearing
one, because it establishes that the measured rotation was not commanded by an
orientation trajectory.

**The real-time section is short.** What it must carry is the
\(1\,\mathrm{kHz}\) callback, the absence of blocking file input or output
inside it, the preallocated logging buffer, the write after control stops, and
the active robot-side monitoring. Connection order, error recovery, collision
setup, model loading, the keyboard thread and the individual exception types
are compressed into one paragraph.

**Delete Table 3.1** (functional subsystems — software documentation the
architecture figure already carries), **Table 3.3** (four null-space modes, one
sentence suffices) and **Table 3.4** (logged signals, which belongs in the
data-format appendix). **Simplify Table 3.2** or drop it: the point is only that
surface-related phases express gains relative to the calibrated surface, pose
hold uses the base frame, and the set-up translational frame is configurable.
**Remove the `robot.control` listing**, which shows nothing the prose does not.

The chapter should come out shorter and stronger, not longer.

### Chapter 4 restructure, agreed and not yet carried out

The division of labour is: **Chapter 3 is mechanism and implementation,
Chapter 4 is the physical setup, the settings actually used, the test matrix
and the evaluation method, and the appendices hold the exhaustive
configuration.** Chapter 4 currently breaks this by re-explaining the
controller, repeating settings in both prose and tables, and restating values
that Appendix C already carries. It should lose roughly a fifth to a third of
its length without losing any scientific content.

Section by section:

- **Experimental system.** Apparatus only. \(T_s=1\,\mathrm{ms}\) is not a
  numbered equation; write that the controller ran through the Franka Control
  Interface at the nominal \(1\,\mathrm{kHz}\) rate.
- **Calibration.** Keep how the surface plane and the grinding-face direction
  were obtained, the validation measurement, and the resulting values. Move the
  runtime relations \(n_T=R_{\mathrm{EE}}n_{\mathrm{EE}}\) and
  \(R_dn_{\mathrm{EE}}=-n_s\) to Chapter 3: they describe how the controller
  uses the calibration, not how it was calibrated.
- **Calibrated geometry.** Replace the vector equations for the face centre,
  half-width and half-length with one calibrated-geometry table, and
  cross-reference the contact-point construction in Chapter 3 rather than
  repeating \(p_{\mathrm{Tool}}=p_{\mathrm{TCP}}+R_{\mathrm{EE}}r_{\mathrm{Tool,EE}}\).
- **Common configuration.** This is the largest duplication. Do not retell the
  phase sequence; state that the runs followed the sequence of Chapter 3, give
  the settings in the existing phase-parameter table, and add that the
  orientation reached at clearance was retained through set-up, the pre-set-up
  gate was disabled and the pre-grinding gate enabled. **A table replaces
  repetition; it is not followed by paragraphs restating its rows.** Give the
  common gains as one table of directional entries with the damping rule, and
  leave the fallback damping matrices to Appendix C. Fold the null-space
  configuration into that table as three rows plus one sentence saying it was
  held fixed so it did not become a variable.
- **Data recording.** Do not list the signals a third time. One sentence
  pointing at Chapter 3 and the data-format appendix. What stays is the data
  quality: three repetitions, 165 runs over 55 settings, none discarded, all
  165 analysed.
- **Case matrix.** The cases are currently explained three times — a grouping
  table, a prose walk-through, and the master table. **Delete the grouping
  table.** Keep one paragraph naming the three effects being separated, then the
  master table, then prose only for the cases that need interpretation: why an
  axial displacement is nominally weak, and why the lever direction changes with
  the commanded orientation.
- **Evaluation quantities.** Equations belong here, unlike in Chapter 3: the
  signed set-up rotation and its surface-resolved component, the alignment-angle
  definition with its tool-mount assumption, and the wrench projections all
  define how results are calculated. **Remove the mean and sample
  standard-deviation equations** and say instead that repeated settings are
  reported by their arithmetic mean and sample standard deviation.

### Chapter 4, settled after the compression pass

The chapter's purpose is: what hardware and geometry were used, how they were
calibrated, what was held constant, what was varied, and how the results were
calculated. Four rules keep it there.

**A configuration table that only restates the prose around it goes.** The
system table repeated the robot, the tool dimensions, the mounting play, the
operating system, the kernel and the library versions, all of which the section
had just said in sentences. Unlike the gain, phase and case tables, it did no
analytical work. The prose stays and the table is gone; the exhaustive
configuration lives in the parameter appendix.

**The two procedures are not both calibrations, and the headings say so.**
Section 4.2 is `Surface Reference and Tool Calibration`, and Section 4.2.1 is
`Surface-Reference Construction`, matching the row headings of Figure 4.2. The
upper procedure records one seated pose and takes \(n_s\) from the nominal
\(+Z_{\mathrm{EE}}\) axis, so it constructs a configured geometric reference
rather than measuring the physical plane normal — which is what the section's
own prose says. Calling it a `surface-plane calibration` contradicted that in
the heading while the paragraph below it conceded the point. Section 4.2.2
keeps `Tool Normal Calibration`, because that procedure does estimate a
physical direction. The `\label{}` keys were left unchanged, since they reach
no reader.

**\(T_4\) is removed from the thesis entirely.** The tool-normal calibration
is reported as three seated yaw orientations, \(T_1\)--\(T_3\), and the
fourth capture appears nowhere: not in Section 4.2.2, not in the parameter
appendix, and not in Figure 4.2. Softening it to `an additional capture held
out of the fit` was an intermediate step on 2026-08-26 and is superseded the
same day.

The reason is the rule under *What belongs in the thesis at all*: a facility
that did not contribute to a reported result does not need documenting. No
residual, angle or agreement value for the fourth pose exists in the thesis or
the repository, it enters no equation, and it supports no claim, so every
mention of it asked the reader to hold a quantity that goes nowhere.

**Write what the estimate used, not how many seatings were performed.** `The
complete tool face was seated at three yaw orientations` and `Three seated yaw
captures entered the fit` are the settled forms. **If the residual is ever
computed, the fourth pose may come back with it** — as a reported number, not
as a bare mention.

**Section 4.2 says what each calibration produces, and stops there.** The
section had grown to mix procedure, frame definitions, validation and the later
combination of the two results before the reader knew what either calibration
delivered. The settled shape is: state the two quantities needed, name what
each procedure supplies —
\(p_s\), \(n_s\) and \(R_{\mathrm{surface}}\) from the surface calibration,
\(n_{\mathrm{Tool,EE}}\) from the tool calibration — and leave the combination
to the chapters that use it. The transformation into the base frame belongs to
Chapter 3 and the pose-based alignment estimate to its appendix consistency
check; Section 4.2 cross-references both rather than deriving either.

**The figure carries the same division.** Each band runs input, method, result,
and the checks hang below the result box feeding nothing. Giving `Re-seated
check` and `Held-out check` the same place in the arrow chain as
\(R_{\mathrm{surface}}\) and \(n_{\mathrm{Tool,EE}}\) is what made readers take
a validation step for a third calibration output.

\(R_dn_{\mathrm{Tool,EE}}=-n_s\) still describes what the
controller does with the calibration, not how the calibration was made, and is
stated in a clause rather than as a numbered equation. The same applies to
\(p_{\mathrm{Tool}}=p_{\mathrm{TCP}}+R_{\mathrm{EE}}r_{\mathrm{Tool,EE}}\): Chapter 4
records the calibrated offsets and the selection tolerance and points at
Chapter 3 for the algorithm that consumes them.

**A run count has one home.** The repetitions, the total and the analysed total
are stated once, in the data-recording subsection. The
evaluation section says how repeated settings are reported and where the
standard deviations appear, and does not restate the counts.

Every setting now carries its three repetitions and nothing was discarded, so
the subsection states that and stops. Do not reintroduce an excluded-run
sentence, and do not describe how the complete set was arrived at: `recorded`
is the only permitted verb, per the rule against `re-recorded` under *Naming a
technical quantity*.

**Isotropic matrices are a table, not a display.** Four \(3\times3\)
matrices whose diagonal entries are all equal spent most of a page saying four
numbers. They are one small table with a sentence saying every entry was
isotropic.

## Evidence and claims

Never invent measurements, repetitions, fitted values, confidence intervals,
p-values, contact locations, timing bounds, or safety conclusions.

Distinguish:

1. measured observation;
2. model-based interpretation;
3. hypothesis requiring another experiment.

Trace every geometric metric through its measurement chain. The primary angular
result is the signed end-effector rotation and does not require the calibrated
tool normal. The appendix reconstructs a separate pose-based tool axis from the
end-effector pose and a calibrated tool-to-end-effector transform. Because the
mounted tool can rotate approximately ±2° about \(y_{EE}\), that secondary
quantity is not a directly measured physical tool-face axis. Do not rename
\(y_{EE}\) as \(t_2\) without transforming it into the calibrated surface
frame.

**The word `inferred` is not used for it, and neither is `EE-inferred`.** Both
were removed. Name the chain instead: `alignment angle calculated from the
end-effector pose`, `end-effector-based alignment angle`, or `pose-based
alignment angle`.

### Use one measured angle in the main results

The command/response chain has two symbol families. \(\theta_{t_i}\) is the
commanded orientation offset about surface tangent \(t_i\), and
\(\gamma_{t_i}\) is the **signed set-up response** about that tangent.

**\(\gamma_{t_i}\) is not the end-effector rotation, and must not be called
it.** The settled definition, agreed 2026-08-26, is:

> The signed set-up response \(\gamma_{t_i}\) represents the end-of-set-up
> orientation change relative to the held set-up reference. Its sign is chosen
> such that a response that reduces a commanded offset has the same sign as
> that offset.

Earlier wording — `the signed measured end-effector rotation about surface
tangent \(t_i\) from the beginning to the end of set-up` — was wrong by a
sign, because \(\gamma_0\) is \(e_R\) at the end of set-up and \(e_R\)
runs from the measured orientation *back* to the held reference. Verified
against the logs on 2026-08-26: for the \(+10^\circ\) command about
\(t_1\) at the TCP, \(\gamma_{t_1}=+7.56^\circ\) while the end effector
physically rotated \(-7.56^\circ\). Every reported value is correct; only
the name was.

**The sign rule is `same sign as the commanded offset`, never `positive means
aligned`.** Correction occurs when \(\gamma_{t_i}\) and \(\theta_{t_i}\)
share a sign, and \(\lvert\gamma_{t_i}\rvert\) is then the size of the
correction. The half-rule `a positive \(\gamma_{t_i}\) denotes
alignment-directed rotation` holds only for a positive offset and inverts on
the reversed-offset conditions, which Cases A and D both report: at
\(\theta_{t_1}=-10^\circ\) the baseline gives \(\gamma_{t_1}=-10.76^\circ\),
which is the **largest** correction of that group, not a motion the wrong way.
Chapter 5 carried the half-rule until 2026-08-26 and now carries the full one.

The construction is \(\gamma_0=\phi_{\mathrm{set}}u_{\mathrm{set}}\) from
\(R_{\mathrm{set}}=R_{\mathrm{set,start}}R_{\mathrm{set,end}}^\top\), with
\(\gamma_S=R_{\mathrm{surface}}^\top\gamma_0=
[\gamma_{t_1},\gamma_{t_2},\gamma_n]^\top\) in surface coordinates.
\(R_{\mathrm{set,start}}\) is the **orientation reference held through
set-up**, captured at the clearance transition; the measured orientation
coincides with it at the start of the phase, which is why the logged
\(e_R\) is exactly zero there. Do not describe it as a second measured pose:
the log carries no end-effector orientation column at all, and
`extract_metrics.py` reads the final \(e_R\) directly. Do not introduce a
second signed deviation vector for the set-up-entry orientation.

**The sign relation is restated wherever it is used to read a number, not only
where it is defined.** Section 4.5.1 derives it and says what follows. A reader
meeting the first results figure is by then a chapter away from the
derivation, so two restatements were added on 2026-08-25 and both stay:

- the opening of Chapter 5, immediately before the main results, giving the
  reading rule alone — \(\gamma_{t_i}\) carries the same sign as the
  commanded offset when the response reduces it, and its magnitude is the size
  of the correction;
- the Case-D mechanism figure, where the commanded moment and the reported
  rotation carry opposite signs on the same time axis. Without a bridge
  sentence the figure looks as though a negative commanded moment produced a
  positive rotation. Say what \(\gamma_{t_1}\) is, cross-reference
  Section 4.5.1, and say that the alignment-directed response therefore appears
  as a positive \(\gamma_{t_1}\) against a negative \(M_{t_1}\).

Restating this is not the internal repetition the guide bans elsewhere: what is
repeated is a reading rule of three lines, not an explanation or a derivation,
and it is placed where a misreading would otherwise happen.

**Say what the quantity is; do not give the sign rule a convention name.**
State that \(R_{\mathrm{set}}\) rotates from the measured end orientation back
to the held start orientation, or that \(e_R\) has that relation, and let the
sign follow. Naming it `the current-to-reference convention` reads as *the
convention currently in use* and invites a reader to look for a superseded one.
The general rule is that a sign convention is stated, not christened.
`the surface-frame rotation convention`, `the selected lever convention` and
`the Denavit--Hartenberg convention` are unaffected because each names the
frame, object or source that fixes it.

**Do not coin an informal name for a defined quantity to carry a sign
argument.** Section 4.5.1 said the metric was independent of `the plane-zero
alignment`, which names nothing the thesis defines, and justified that
independence by saying the tool axis `is known only to within a degree or two
and shifts as the tool settles in the gripper`. Both were removed on
2026-08-25. The second states a mechanical clearance as though it were a
calibrated knowledge bound, which the \(\pm2^\circ\) rule below forbids, and
asserts a motion during contact that was not tracked. The defensible statement
names the chain instead: the quantity comes from the measured end-effector
orientation, the calibrated tool normal does not enter it, it is therefore
independent of the relative tool--gripper rotation of Section 4.1.1, and the
surface frame enters only as the directions the rotation is resolved along.

The pose-based alignment error is appendix-only. It is unsigned and depends on
the assumed fixed tool-to-end-effector relation, so neither it nor its
before--after reduction appears in Chapter 5 tables, figures, or comparisons.
The appendix may define \(\theta_{\mathrm{align}}\) locally for the consistency
check, but \(\Delta\theta_{\mathrm{align}}\), \(\theta_{\mathrm{dev}}\),
\(\Delta\theta_{\mathrm{set}}\), and their resolved variants are not
thesis-wide reported symbols.

**Each main surface-contact comparison changes one input and reports one
response.** The response is the measured set-up rotation
\(\gamma_{t_i}\). Chapter 5 table headings name the changed input directly
and call the output `Measured set-up rotation`; generic columns such as
`Varied entry` and `Value` are not used. Subsection titles, captions, axes and
the surrounding prose use the same input--response vocabulary. The commanded
wrench time history in Case D is the mechanism figure and remains the one
exception to a response-only comparison plot.

The TCP-height flatness classification is appendix-only supporting evidence.
It does not appear as a column in the Chapter 5 comparison tables or as a
second outcome in their narratives. Appendix D retains the classified
conditions, the geometric interpretation and the tool-mount qualification.

The **TCP-height flatness criterion** answers *is the final measured TCP
  position geometrically consistent with the calibrated rectangular face lying
  flat on the surface?* This is the right quantity for calling a condition
  flat, as long as the wording stays explicit that it is geometry-based rather
  than an independent physical orientation measurement. Where it is
  satisfied, write `classified as flat by the TCP-height criterion` or `the
  final geometry was consistent with a flatly seated tool face`. Never
  claim the physical face angle was measured as zero: the tool orientation was
  not tracked under load.

**Do not write that a lever was insufficient to align the tool**, or that it
`did not remove the full initial deviation`. Both read as claims about the
physical tool face, whose orientation under load was not tracked. A residual
pose-based alignment angle is not by itself evidence of residual physical tilt,
because the instantaneous relative tool--gripper rotation was not tracked
during the contact runs. Report what was measured — the signed set-up rotation changed from \(-1.63\) to
\(+4.43^\circ\) about \(t_2\) with the selected \(40\,\mathrm{mm}\) lever, and
the final configuration satisfied the TCP-height flatness criterion.

### Three distinct points: selected tool point, TCP, compliance centre

\(p_{\mathrm{Tool}}\), \(p_{\mathrm{TCP}}\) and \(p_c\) are different points and the prose
must keep them apart.

- \(p_{\mathrm{Tool}}\) is the selected tool point: the point or edge of the grinding face
  that contacts, or is predicted to contact, the surface. The controller
  determines it from the rectangular face geometry and the current tool
  orientation.
- \(p_{\mathrm{TCP}}\) is the Cartesian reference point of the controller.
- \(p_c\) is the virtual centre of compliance: a software-defined point about
  which the Cartesian stiffness and damping are formulated before being
  transformed to the TCP. It is **not** the physical contact point.

\(p_{\mathrm{Tool}}\) is **selected at the clearance transition and then held constant
relative to the tool** for the whole of set-up. Say so where it is introduced.

**Chapter 2 also says how the point is chosen and what it is for.** Naming the
three outcomes without the rule that produces them left a reader unable to see
where the point comes from, and unable to tell whether it serves the command or
only the evaluation. Both belong in the compliance-centre section, in two
clauses: the leading corner along the descent direction, with tied corners
averaged, and the fact that the set-up reference is generated on the point
while the TCP target is reconstructed from it. The algorithm itself stays in
Chapter 3, which the theory chapter cross-references rather than repeats.
Once the tool starts to rotate under contact it is a geometric contact
reference, not the exact point at which the surface force acts at every
instant, and a sentence that treats it as the latter overstates what the
geometry gives.

The two levers are named separately and never stand in for one another:

- \(r_{\mathrm{Tool}}=p_{\mathrm{Tool}}-p_{\mathrm{TCP}}\) is **tool geometry** — the offset from the TCP
  to the selected contact reference, fixed by the face geometry and the current
  orientation. In end-effector coordinates it is \(r_{\mathrm{Tool,EE}}\), so
  that \(p_{\mathrm{Tool}}=p_{\mathrm{TCP}}+R_{\mathrm{EE}}r_{\mathrm{Tool,EE}}\); the
  implementation has \(p_{\mathrm{TCP}}=p_{\mathrm{EE}}\), which is worth
  stating once rather than silently writing \(p_{\mathrm{EE}}\) in its place.
- \(r_c=p_c-p_{\mathrm{TCP}}\) is **virtual controller geometry** — the
  software-defined displacement used by the point-shift transformation of the
  Cartesian impedance. It carries no tool geometry at all.

They combine as \(p_{\mathrm{Tool}}-p_c=(p_{\mathrm{Tool}}-p_{\mathrm{TCP}})-(p_c-p_{\mathrm{TCP}})=r_{\mathrm{Tool}}-r_c\),
which is worth stating because it separates the physical contact geometry from
the virtual shift.

The contact sequence therefore originates at the selected tool point, not at
the TCP and not at the centre of compliance: the face geometry gives \(p_{\mathrm{Tool}}\),
the set-up trajectory moves it as \(p_{\mathrm{Tool},d}(t)=p_{\mathrm{Tool},0}+s_{\mathrm{set}}(t)(-n_s)\),
and the TCP target is reconstructed from it as
\(p_d(t)=p_{\mathrm{Tool},d}(t)-R_{\mathrm{clr}}r_{\mathrm{Tool,EE}}\), which produces the
press. The centre of compliance is a separate mechanism acting through
\(r_c\) on the force–moment coupling. Do not merge the two chains.

**Never write that the compliance centre moves the force application point.**
The physical surface force still acts at the actual contact point. What changes
is the point about which the compliance is defined, and therefore the
translation–rotation coupling: the same normal press produces a different
rotational response as \(p_c\) moves. Give that explanation before introducing
\(r_c=p_c-p_{\mathrm{TCP}}\) and \(m_{\mathrm{cpl},K}=r_c\times f_K\), not
after. If \(p_c\) lies on the relevant line of action the moment contribution
becomes small or zero; displacing it to one side produces a moment that assists
the required alignment, and to the other side one that opposes or reverses it.

Use `model-estimated external wrench` for
`O_F_ext_hat_K`. Do not call it a directly measured wrench. A location derived
from that signal is an `equivalent contact location`, not necessarily a
physical point contact.

Use `repeatability-based interpretation threshold` for the approximately
two-standard-deviation threshold from five repetitions. Do not present it as a
universal noise floor or formal equivalence test.

The fitted compliance-centre model is an **additive** or **separable quadratic
response model** unless a \(t_1t_2\) interaction term is estimated. The
cross-shaped sampling does not identify that interaction. The location near
\(t_1=62\,\mathrm{mm}\), \(t_2=30\,\mathrm{mm}\) is a
**model-predicted local optimum**, not an experimentally confirmed optimum.
A single unused point is a **held-out consistency check**, not broad external
validation.

Avoid absolute normal-coordinate claims. The earlier statement that the normal
coordinate carried little explanatory power rested on a single setting at
\(+20\,\mathrm{mm}\), which the coupling model itself predicts to be too small
to resolve. It is superseded and must not be reinstated.

The normal coordinate was afterwards sampled at \(-60\), \(0\), \(+40\),
\(+60\) and \(+120\,\mathrm{mm}\). The alignment response rose across the whole
of that range, from \(3.73\) to \(6.80^\circ\), and the residual angle fell from
\(4.81\) to \(1.91^\circ\). It is not symmetric about zero, and it does not turn
over. Report both, bounded to the sampled range, and do not name a best
position:

> The alignment response increased with the normal compliance-centre
> coordinate, and continued to increase up to the largest tested magnitude.

Note the second clause. Writing that the maximum is not bracketed, or that no
best magnitude can be reported, describes the sampling rather than the
measurement and belongs to neither the results nor the discussion.

A purely normal press cannot produce that dependence at all. A normal lever
drops out of \(f\times r_c\) and enters only as \(K_{p,t}r_n^2\) of added
rotational stiffness, which is even in the sign of \(r_n\) and resists the
correction rather than adding to it. The measurement therefore indicates a
tangential component in the press. That inference is a model-based
interpretation and is written as one.

**There is no residual floor.** An earlier reading treated a residual near
\(3^\circ\) as a limit of the arrangement, and attributed it to motion within
the tool mount. The \(120\,\mathrm{mm}\) setting reached \(1.91^\circ\), so the
value was a property of the settings then tested. Do not describe any residual
as a floor unless a setting has been shown not to pass it.

If damping was not varied, report only that no sustained oscillation was
observed with the selected damping. Do not claim a measured damping effect.

Matched free-space null-space trials compare the four selectable null-space
modes under an internally commanded point-force equivalent. Claims from those
trials remain limited to that hold condition and must not be extended to
physical disturbances or contact response.

### The two null-space motion quantities, and what the sigma result says

**\(E_N\) is the cumulative projected null-space motion, not a
displacement.** It integrates \(\lVert N_q\dot q\rVert_2\) over the
disturbance interval, so it is a path length: a configuration that moves
repeatedly in alternating directions accumulates \(E_N\) while ending where it
started. The words `excursion` and `displacement` are wrong for it and have
been removed. **The net redundant displacement is
\(\Delta\eta_{\mathrm{dist}}=v_{\mathrm{ref}}^\top\Delta q_{\mathrm{null}}\)**,
a signed projection of the net projected joint motion onto one common
direction. The two are reported together, because for the sigma-only settings
they differ by orders of magnitude, and that difference is the result.

**The null-space subsections report means and the interpretation, not
\(\pm\) SD.** Sections 5.2.1 and 5.2.2 carried a standard deviation on
almost every value — nine of them across two subsections — which buried the
result under its own scatter. They were removed on 2026-08-26 and the figure
keeps them: the shaded bands and error bars of
`fig:results_nullspace_automatic` already show the spread, and the appendix
carries the numbers. The prose now states the mean and what follows from it.

**Say `close to zero`, not `smaller than the scatter`.** The sigma-only net
displacements were once described as having a magnitude `smaller than the
scatter across the three repetitions`, which forces the reader back into a
standard-deviation discussion to understand a result that is simply near zero.
`Both sigma-only settings ended the disturbance interval with a net redundant
displacement close to zero` states it directly, and the two-orders-of-magnitude
relation against the uncontrolled \(0.131\,\mathrm{rad}\) carries the size.

Two things survive that compression and are not dropped with the deviations:
the `\cref` to the figure panel the claim rests on, which every results
subsection must carry, and the relation `a factor of about six` between the two
cumulative-motion values. Stripping uncertainty is not licence to strip the
evidence pointer or the ratio.

**\(v_{\mathrm{ref}}\) is recovered from the data, not read from the log**,
and the earlier wording here —
`\(\Delta\eta_{\mathrm{dist}}=v_7(q_5)^\top[q(9\,\mathrm{s})-q(5\,\mathrm{s})]\)`
— was **wrong on both halves** and is withdrawn. Checked against
`make_nullspace_figure.py` on 2026-08-26: \(v_7\) is absent from the runs
without null-space torque, because the controller records it only while the
conditioning term is selecting a sign. The axis is therefore the normalised
**arithmetic mean of the three net projected displacement vectors of the
baseline condition** \(\Delta q_{\mathrm{null},0}\), and what is projected is
the trapezoidal integral of the projected joint velocity over
\(t\in[5,9]\,\mathrm{s}\), not the raw joint difference between the two
instants. Section 4.6 says `the arithmetic mean of the three net projected
displacement vectors recorded in the condition without null-space torque`, and
that wording is the one to keep.

**Do not write that the conditioning term returned, recovered or restored
\(\sigma_{\min}\) or the configuration.** The selected null-space law was
active from the start of every pose-hold trial, so the first
\(5\,\mathrm{s}\) were a pre-disturbance settling interval and the
conditioning torque was never switched on after a displacement had occurred.
What the measurements show is that the redundant configuration was
**prevented** from being displaced: the net displacement stayed near zero and
\(\sigma_{\min}\) changed by about \(2\times10^{-5}\) across the
disturbance interval, against \(-2\times10^{-3}\) without null-space torque.
Chapter 4 states the timeline explicitly so the reading cannot drift back.

**The three modes behave differently in kind, and the prose says which kind.**
Without null-space torque the disturbance displaces the redundant
configuration. Projected damping reduces the displacement while the motion
lasts, and \(\tau_d=-d_{\mathrm{null}}N_\tau\dot q\) vanishes with that
motion, so it requests no return. Singular-value conditioning is an active
configuration objective that drives the redundant configuration towards a
locally larger \(\sigma_{\min}\).

**\(\tau_\sigma\) is not a brake and is not dissipative.** It behaved as
disturbance rejection here only because the tested disturbance acted away from
the configuration the objective favours; a disturbance acting towards larger
\(\sigma_{\min}\) would move with it. Say that where the rejection is
claimed. There is also **no stored preferred configuration**: the
implementation holds no \(q_{\mathrm{ref}}\) spring and compares
\(q\pm\alpha_{\mathrm{probe}}v_7\) at every cycle, so write `drives the
redundant configuration towards a local region with larger
\(\sigma_{\min}\)`, never `returns to its preferred configuration`.

**\(k_\sigma\) is a commanded torque magnitude, not a proportional gain.**
The command is \(\tau_\sigma=k_\sigma N_\tau(s_\sigma v_7)\) with
\(s_\sigma\in\{-1,0,+1\}\), and the deadband alone decides when the
selector is zero. The larger tested magnitude therefore produces repeated
direction changes near the locally preferred region. Call that **switching
activity** or **oscillatory null-space motion**; `dithering` is not used, and
the larger \(E_N\) is **not** evidence of poorer rejection or of a fault in
the law. The defensible finding is a parameter selection:
\(k_\sigma=1.5\,\mathrm{N\,m}\) gave the same suppression of net
displacement with substantially less redundant motion, and a smoother
conditioning law is future work rather than a retrofit to these experiments.

**The comparison is between complete modes, not isolated torques.** Because the
conditioning torque was active before the disturbance, the sigma-only trials
entered it from a redundant configuration displaced by approximately
\(0.013\,\mathrm{rad}\) from the one at which the other trials began. State
this where the comparison is made; do not claim the difference isolates an
instantaneous opposing torque at identical joint configurations.

## Technical conventions that must remain explicit

- Wrench ordering is force followed by moment.
- Position error is desired minus current.
- State the orientation-error convention and frame in which its components are
  expressed.
- The Jacobian-transpose mapping and null-space projector convention must match
  the implementation.
- Six singular values belong to the \(6\times7\) Jacobian;
  \(\sigma_{\min}=\sigma_6\), while \(v_7\) is the structural null direction at
  full row rank.
- A retained singular value is inverted as \(1/\sigma_i\).
- Distinguish the virtual-centre lever \(r_c=p_c-p_{\mathrm{TCP}}\) from the
  tool-geometry lever \(r_{\mathrm{Tool}}=p_{\mathrm{Tool}}-p_{\mathrm{TCP}}\). \(r_{\mathrm{Tool}}\) locates the contact
  reference relative to the TCP; \(r_c\) locates the virtual centre of
  compliance relative to the TCP. They never appear in the same expression.
  \(r_c\) shapes the **commanded** wrench through \(\mathrm{Ad}(r_c)\);
  \(r_{\mathrm{Tool}}\) belongs to the physical contact geometry.
- **The direction-selected lever rule has one sign, and it is
  \(r_{c,t}=\rho_c(\theta_{t_1}t_2-\theta_{t_2}t_1)/\sqrt{\theta_{t_1}^2+\theta_{t_2}^2}\).**
  It reduces to \(r_{c,t}=+\rho_c t_2\) for a positive \(t_1\) offset and
  \(r_{c,t}=-\rho_c t_1\) for a positive \(t_2\) offset. Three independent
  things fix it and must agree: the supporting intermediate-direction table,
  whose four selected rows read
  \([0,+40,0]\), \([+28.3,+28.3,0]\), \([-28.3,+28.3,0]\) and \([-40,0,0]\,\mathrm{mm}\);
  the Case-D measurements, where the \(+10^\circ\) command about \(t_1\) is
  assisted at positive \(r_{c,t_2}\); and the moment that follows it,
  \(m_{\mathrm{cpl},K}\approx-F_{K,n}\rho_c(\theta_{t_1}t_1+\theta_{t_2}t_2)/
  \sqrt{\theta_{t_1}^2+\theta_{t_2}^2}\), which is opposite to the commanded
  offset.

  **The reversed numerator \(\theta_{t_2}t_1-\theta_{t_1}t_2\) is wrong and was
  removed** from Chapter 2 and Chapter 5 on 2026-08-25. It survived the \(r_c\)
  redefinition because it sits two equations away from the moment it feeds, and
  in both chapters it contradicted the moment printed immediately below it.
  Any future change to the lever convention is checked against all three
  anchors above, not against the formula alone.
- **The flat tool-axis target is the inward surface normal,
  \(n_{\mathrm{flat}}=s_an_s\) with \(s_a=-1\), and the commanded rotation is
  applied to it: \(n_d=R_{\mathrm{tilt}}n_{\mathrm{flat}}\).** For zero
  commanded offset \(n_d=-n_s\), never \(+n_s\). The two-step form matches the
  implementation, which builds the signed flat axis first and rotates it
  afterwards, and it matches the parameter appendix, where the tool-axis target
  sign is negative. Writing \(n_d=R_{\mathrm{tilt}}n_s\) drops \(s_a\) and
  makes the zero-offset target point out of the surface instead of into it.
- **There is no \(f_C\).** A symbol for an abstract environment-on-tool contact
  force was introduced and then removed. Build every moment statement on the
  commanded wrench \(F=[f^\top,m^\top]^\top\). The model-estimated external
  wrench is an implementation signal used only by the optional set-up
  termination condition and is assigned no thesis-wide mathematical symbol.
  Figure 2.2 draws the commanded side only.
- **\(m_{r_{\mathrm{Tool}}}=r_{\mathrm{Tool}}\times\Delta\hat f_{\mathrm{ext}}\)
  does not appear anywhere in the thesis.** The symbol is deleted from the
  symbol list, from Section 2.7, and from Figure 2.2. The earlier rules that
  paired each lever with a viewpoint, that called the quantity a reconstruction
  rather than a measurement, and that forbade adding it to the commanded terms,
  are all withdrawn along with it — they existed to manage a quantity that is
  no longer there.

  The reason is that it put an assumed contact lever on the observed side of a
  figure whose only job is to separate command from observation. The
  model-estimated wrench already carries its own force and moment estimates, so
  nothing has to be reconstructed from \(r_{\mathrm{Tool}}\). Drawing the tool lever
  beside the virtual one also invited the reading that \(r_{\mathrm{Tool}}\)
  and \(r_c\) are two versions of the same thing.
- **\(r_{\mathrm{Tool}}\) belongs to the tool geometry and to reference
  generation, and to nothing else.** It is introduced where the physical tool
  face is introduced, because the face geometry is what determines it, and it
  is used to convert the selected tool-point reference into \(p_d\). It does
  not enter the compliance-centre point shift, it does not appear in
  Section 2.7, and it is never crossed with a commanded force.
- **The commanded and model-estimated quantities are never equated.** Changing
  \(r_c\) changes the commanded impedance and therefore the closed-loop
  interaction, which can in turn change the model-estimated external wrench.
  The estimated external moment is the result of that interaction, not an
  algebraic sum of commanded terms.
- **`\approx` does not appear in the thesis, in any chapter, appendix, or
  figure.** Every displayed and inline relation is written with an equals sign.
  This is not a licence to assert equalities that are false: a relation that
  was approximate is made exact before the symbol changes, by naming the
  quantity the relation actually holds for. The four routes used, in order of
  preference:

  1. **Name the component the relation is exact for.** The press-direction
     rule was \(m_{c,K}\approx-F_{K,n}\rho_ct_1\) because \(f_K\) carries
     tangential components. Defining the normal component
     \(f_{K,n}=-F_{K,n}n_s\) and the moment it alone produces,
     \(m_{\mathrm{cpl},K,n}=r_{c,t}\times f_{K,n}\), makes it an identity, and
     one sentence then says that tangential components add further terms to
     \(m_{\mathrm{cpl},K}\).
  2. **State the rounding in the prose.** The calibrated \(n_s\), \(t_1\),
     \(t_2\) and \(R_{\mathrm{surface}}\) are quoted to six decimals; the
     lead-in says `to six decimal places` and the equation takes `=`.
  3. **Write the ideal condition as an equality and put the residual in the
     next sentence.** The tool-normal invariance is an equality under perfect
     seating, and the sentence after it says seating scatter leaves no
     direction that satisfies it exactly.
  4. **Replace the relation with a bound or a statement in words.** A
     quasi-static force balance is `both are negative and track one another in
     magnitude`, not `\(F_n\approx-F_{n,\mathrm{cmd}}\)`;
     \(40\sin10^\circ\) is `under \(7\,\mathrm{mm}\)`, not `\(\approx
     6.9\,\mathrm{mm}\)`.

  The hedging words stay: `approximately`, `about`, and `of the order of` are
  required by *Hedge to the evidence* in
  [THESIS_VOICE.md](THESIS_VOICE.md) and are unaffected by this rule, which
  governs the symbol alone. Grep for `\approx` across `chapters/`,
  `frontmatter/`, `backmatter/` and `figures/` before submitting; the expected
  count is zero.
- **\(m=m_R+m_{\mathrm{cpl}}\) is an identity, and is written with an equals
  sign.** It holds exactly for the shifted \(6\times6\) law, provided \(f\) is
  the translational part of the same commanded wrench \(F=[f^\top,m^\top]^\top\)
  rather than the \(r_c=0\) expression. Writing \(m=[r_c]_\times f+K_Re_R-D_R
  \omega_{\mathrm{EE}}\) out of \(\mathrm{Ad}(r_c)^\top K_c\mathrm{Ad}(r_c)\)
  leaves no remainder: the lower-right block's
  \([r_c]_\times^\top K_p[r_c]_\times e_R\) is what the lever produces from the
  \(-K_p[r_c]_\times e_R\) part of the force the same shift creates, and the
  damping block follows identically. Verified numerically against the
  implemented `shiftGainToTcp` on 2026-08-25.

  **The earlier "mechanism explanation, not an identity" ruling is withdrawn.**
  It required "approximately" on the grounds that the lower-right block carries
  further \(r_c\)-dependent terms, which is true of the block and false of the
  sum — those terms are inside \(r_c\times f\). What the approximation actually
  concealed is narrower and is now stated where it belongs: the expressions
  \(f_K=K_pe_p\) and \(f_D=D_p(\dot p_d-\dot p_{\mathrm{EE}})\) of
  `eq:commanded_force_split` are the \(r_c=0\) forms, and under the shift the
  elastic and damping split applies to the shifted force instead. The sign
  analysis continues to use \(m_{\mathrm{cpl},K}=r_c\times f_K\) at \(e_R=0\), where the
  two coincide.
- **\(r_c=0\) is not a zero-moment condition, and it does not remove
  \(m_{\mathrm{cpl},K}\) alone.** The earlier wording of this rule said "it removes
  \(m_{\mathrm{cpl},K}\) alone", which is too narrow and has been replaced. Setting
  \(r_c=0\) makes \(\mathrm{Ad}(r_c)\) the identity, so it removes the
  **complete** additional coupling the virtual point shift introduces:
  \(m_{\mathrm{cpl},K}\), \(m_{\mathrm{cpl},D}\), \(m_{\mathrm{cpl}}\), and every remaining
  \(r_c\)-dependent term of the shifted \(K_{\mathrm{TCP}}\) and
  \(D_{\mathrm{TCP}}\) — both the off-diagonal blocks and the added rotational
  entries \([r_c]_\times^\top K_p[r_c]_\times\) and
  \([r_c]_\times^\top D_p[r_c]_\times\).

  What it does **not** remove: the ordinary decoupled rotational impedance
  \(m_R\), the finite rotational compliance, the tool geometry \(r_{\mathrm{Tool}}\), the
  physical contact interaction, the external contact moment, and therefore
  contact-induced robot rotation. \(r_{\mathrm{Tool}}\neq0\) means contact can still
  contribute \(m_{r_{\mathrm{Tool}}}\). This is what makes the strong zero-lever \(t_1\)
  rotation unsurprising, and the thesis states it where the reader will
  otherwise assume the opposite.

  The general form to use is: *setting \(r_c=0\) removes the additional
  translation--rotation coupling introduced by the virtual point shift; the
  ordinary rotational impedance and the physical tool and contact geometry
  remain.* **Never write that a zero lever gives a zero moment.**
- **Never cross a lever from one side with a force from the other.** With
  \(m_{r_{\mathrm{Tool}}}\) gone the commonest form of this error is gone with
  it, but the principle stands: \(r_c\) is crossed with the commanded force
  \(f\), and nothing is crossed with the model-estimated external force.
- The complete translational command carries a moment, not only its elastic
  part: \(m_{\mathrm{cpl}}=r_c\times f\). The sign analysis then retains
  \(f_K\) alone, giving \(m_{\mathrm{cpl},K}=r_c\times f_K\),
  and says that it is doing so — otherwise \(f_K\) appears to
  enter arbitrarily. The damping coupling follows from the shifted damping
  matrix in the same way.
- **The compliance-centre hierarchy is stated once, in Section 2.7.3, and
  applied everywhere else.** The order is
  \(r_c\to(r_{c,t_1},r_{c,t_2},r_{c,n})\to r_{c,t}\), then
  \(\theta_{\mathrm{tilt}}\to\) the selected direction, then
  \(m=m_R+r_c\times f\). \(r_{c,t_1}\) and \(r_{c,t_2}\) are signed
  scalars and \(r_{c,t}\) is the tangential vector they form. Chapters 4
  and 5 must not re-derive any of it.

  **The complete list of compliance-centre symbols is \(r_c\),
  \(r_{c,t_1}\), \(r_{c,t_2}\), \(r_{c,n}\), \(r_{c,t}\) and
  \(\lVert r_{c,t}\rVert\).** `\rho_c` is withdrawn: a vector already has a
  norm, and a second magnitude symbol only had to be kept in step with it. A
  superscript `sel` for the selected displacement was tried and withdrawn too;
  the selection rule prescribes the magnitude and fixes the direction, so one
  \(r_{c,t}\) carries both. The distinction that matters in the tool-axis
  supporting check is between
  \(\lVert r_c\rVert\) and \(\lVert r_{c,t}\rVert\).

  **The tool-axis supporting check introduces the projection geometry before
  using the sine.** Define \(\alpha_{\mathrm{axis}}\) as the **acute
  inclination of the tool axis relative to the inward surface-normal direction
  \(-n_s\)**, and say that this is the direction the tool axis takes when the
  face lies flat. Then state that a tool-axis displacement contains normal and
  tangential components, and use
  \(\lVert r_{c,t}\rVert=\lVert r_c\rVert\sin\alpha_{\mathrm{axis}}\). At the
  outer setting, \(40\,\mathrm{mm}\) is the configured total tool-axis
  displacement \(\lVert r_c\rVert\), whereas \(6.95\,\mathrm{mm}\) is its
  tangential projection at the nominal \(10^\circ\), stated to two decimal
  places. Never present the projection as a second configured CoC magnitude.

  **The reference direction is \(-n_s\), not \(n_s\)**, and the earlier wording
  `the angle between the tool axis and \(n_s\)` was corrected on 2026-08-25.
  A flat tool axis points into the surface, so measured from \(n_s\) the
  nominal inclination is \(170^\circ\) rather than \(10^\circ\). The arithmetic
  survives the error, since \(\sin170^\circ=\sin10^\circ\), which is exactly
  why it went unnoticed: the reported \(6.95\,\mathrm{mm}\) is right under
  either reading. State the geometry the flat-axis convention already fixes —
  \(n_{\mathrm{flat}}=-n_s\), further up this list — rather than one that
  happens to give the same number. Say which commanded offset set the
  inclination, and call it *nominal*, because the orientation phase reached
  approximately \(9.3^\circ\) about \(t_1\) rather than the commanded
  \(10^\circ\).

  **\(r_c\times f_n=r_{c,t}\times f_n\) is the load-bearing result.** The
  normal component of the displacement drops out of the normal-press moment,
  so only the tangential part acts. State it in the theory and cite it in
  the tool-axis supporting check rather than re-arguing the cross product there.
- **The definition frame belongs with the components, not at the end of the
  section.** A surface-fixed displacement holds
  \(r_{c,S}=[r_{c,t_1},r_{c,t_2},r_{c,n}]^\top\) constant with
  \(r_{c,0}=R_{\mathrm{surface}}r_{c,S}\); a tool-fixed one holds
  \(r_{c,\mathrm{EE}}\) constant, and its base-frame vector
  \(r_{c,0}=R_{\mathrm{EE}}r_{c,\mathrm{EE}}\) rotates with the end effector.
  Supporting check 1 examines exactly this property, so it has to exist in the
  theory before the check appears. This transformation pair is one of the two
  places a frame index is written at all; the rule is under *The frame index
  appears only where frames are compared or transformed*.
- **Plots and tables carry the actual surface-frame components
  \(r_{c,t_1}\) and \(r_{c,t_2}\), never a sign-flipped stand-in.**
  Case D reports \(r_{c,t_2}\) for commands about \(t_1\) and
  \(r_{c,t_1}\) for commands about \(t_2\), so the selected displacement
  appears at \(+40\,\mathrm{mm}\) in the first comparison and at
  \(-40\,\mathrm{mm}\) in the second.

  **`-r_{c,t_1}` is withdrawn**, written here as a literal string so a rename
  cannot revive it. It was introduced so that the selected side would read
  positive in both panels, which made the reader learn an artificial
  convention and hid the result it was meant to present. The sign difference
  between \(+\theta_{t_1}\Rightarrow r_{c,t_2}>0\) and
  \(+\theta_{t_2}\Rightarrow r_{c,t_1}<0\) is exactly what the
  lever-selection rule predicts, so the figures show it rather than conceal
  it.

  **Changing that axis means mirroring the series, not relabelling it.** The
  \(t_2\) data were plotted against the negated coordinate, so moving to
  \(r_{c,t_1}\) negates every \(x\) value while the measured responses stay
  where they are. Done on 2026-08-25 for Figure 5.4(b), the Case-D table and
  the offset-magnitude legends. The run configuration remains the anchor:
  `P2_t2_pos_p040` sets `compliance_center_offset_ee_x = -0.040`, which is
  \(r_{c,t_1}=-40\,\mathrm{mm}\). Never adjust a reported value to make a
  coordinate look tidy.
- **Every reported non-zero displacement except the surface-fixed conditions
  of supporting check 1 was configured tool-fixed, in end-effector
  coordinates**, and the surface-frame vectors in the supporting
  intermediate-direction table are what those settings realise in the flat target
  orientation. The mapping is \(r_{c,t_1}=\) `offset_ee_x` and
  \(r_{c,t_2}=-\) `offset_ee_y`, checked against the run overlays on
  2026-08-25. Say which frame a tabulated vector is in; a table headed
  \([r_{c,t_1},r_{c,t_2},r_{c,n}]\) whose values were configured in another
  frame needs that sentence or it reads as a contradiction of supporting
  check 1.

  **Chapter 4 says this where Case D is introduced, not only in the
  appendix.** The theory distinguishes a surface-fixed displacement from a
  tool-fixed one whose base-frame vector rotates with the end effector, and
  Appendix C records which the campaign used; Section 4.4 said only that the
  tangential position was varied along the tangent perpendicular to the
  commanded rotation. A reader therefore had every reason to take
  \(r_{c,t_1}\) and \(r_{c,t_2}\) for surface-frame coordinates held constant
  through the run, which is not what the implementation does. Three sentences
  were added on 2026-08-25: unless stated otherwise the non-zero displacements
  of the main study were configured tool-fixed in end-effector coordinates; the
  tangential coordinates reported for Case~D are the surface-frame directions
  those settings realise in the flat target orientation; and the definition
  frame itself is examined in the supporting check. This is a cross-reference
  and a statement of what was configured, not a second derivation.
- **The model-estimated external wrench is not theory, and Chapter 2 does not
  carry it.** The former Section 2.4.4 and the commanded-versus-model-estimated
  half of Section 2.7 are deleted, and Figure 2.2 is a commanded-wrench figure
  only. Neither was needed to derive the impedance law or the compliance-centre
  mechanism, and both interrupted the one narrative the chapter has to carry:
  \(r_c\to\mathrm{Ad}(r_c)\to K_{\mathrm{TCP}},D_{\mathrm{TCP}}\to
  m=m_R+r_c\times f\to\) the tangential direction rule.

  **It survives as an implementation signal only.** Section 3.5.3 says in one
  short passage that libfranka supplies it, that it is stored at the clearance
  transition, and that the estimated external moment change can trigger the
  optional termination condition. This explanation is written in words and
  introduces no mathematical symbol. Every reported run terminated through the
  timeout instead. The data-format appendix retains the literal recorded field
  names and bias columns. That is the whole of it.

  **`F_{n,\mathrm{ext}}` is withdrawn**, with the symbol-list rows for
  \(\hat f_{\mathrm{ext}}\), \(\hat f_{\mathrm{ref}}\) and
  \(\Delta\hat F_{\mathrm{ext}}\). One steady-state sentence was all that
  used it, and that sentence now rests on the alignment angle alone. Do not
  reintroduce a second normal-force quantity to support a claim that does not
  need one.
- **No index means commanded.** This thesis-wide rule replaces carrying `cmd`
  through every equation, figure and axis label. The commanded quantities are
  \(f\), \(f_n\), \(f_t\), \(F_n=n_s^\top f\), \(m\) and
  \(M_{t_i}=t_i^\top m\). The model-estimated external wrench has no
  thesis-wide mathematical symbols and is referred to in words only in
  Section 3.5.3. `F_{n,\mathrm{cmd}}`, `M_{t_i,\mathrm{cmd}}`,
  `F_{K,n}` and `f_{K,n}` are withdrawn. \(\tau_{\mathrm{cmd}}\) keeps its
  index because it is a joint torque rather than a Cartesian wrench component.

  \(F_n\) is the signed scalar commanded normal force, and \(f_n=F_nn_s\) is
  the corresponding vector. Say so once where both first appear rather than
  leaving the reader to infer it.
- **The settled force and moment names.** `press` as a symbol name was
  withdrawn, because \(f_{\mathrm{press}}\) read as the complete force pressing
  against the surface when it was only the spring term. The subscript now says
  which term it is:

  | Symbol | Is | Name |
  |---|---|---|
  | \(f\) | commanded | complete commanded force |
  | \(m\) | commanded | complete commanded TCP moment |
  | \(f_n=F_nn_s\) | commanded | normal component of \(f\) |
  | \(f_t=(I_3-n_sn_s^\top)f\) | commanded | tangential component of \(f\) |
  | \(m_R=K_Re_R-D_R\omega_{\mathrm{EE}}\) | commanded | rotational-impedance contribution |
  | \(m_{\mathrm{CoC}}=r_c\times f\) | commanded | compliance-centre contribution |
  | \(M_{t_i}=t_i^\top m\) | commanded | the moment the plots carry |

  **The whole thesis turns on \(m=m_R+r_c\times f\)**, and the same language
  is used in the theory, the figures, the methodology and the results. The
  controller evaluates the complete shifted wrench; it never forms an isolated
  coupling moment. Where the directional effect of a displaced centre has to be
  explained, decompose the **complete** force as \(f=f_n+f_t\) and use
  \(r_c\times f_n\); do not switch to an elastic force for the occasion.

  **`f_K`, `f_D`, `m_{c,K}`, `m_{c,D}`, `m_{r_c}`, `m_{r_c,0}`,
  `m_{\mathrm{cpl},K}`, `m_{\mathrm{cpl},D}`, `m_{\mathrm{cpl}}` and
  `m_{\mathrm{cpl},K,n}` are all withdrawn**, and are written here as literal
  strings so a bulk rename cannot revive them. They split the commanded force
  into an elastic and a damping part in order to name a coupling moment the
  controller does not command, and the results chapter then re-derived the sign
  in that split notation while its own figure plotted
  \(F_{n,\mathrm{cmd}}\) and \(M_{t_i,\mathrm{cmd}}\) from the complete
  wrench. That mismatch is the confusion this convention exists to remove.

  **Four spellings are banned outright**, and are written here as literal
  strings so that a bulk rename cannot quietly revive them: `m_{r_c,0}`,
  `m_{r_c}`, `m_{c,K}` and `m_{c,D}`. The earlier ruling that produced them —
  `trans` retired, the commanded pair named for the lever — is withdrawn.

  The fatal objection is to the first. It names a quantity by a condition the
  quantity does not require: the rotational impedance is present at every lever
  setting, and an index reading "at \(r_c=0\)" tells the reader it exists only
  there. \(m_R\) says what it is. The first two were also
  near-indistinguishable in print while naming different contributions, and the
  elastic and damping parts shared their index with \(p_c\), \(r_c\), \(K_c\)
  and \(D_c\), which name the centre rather than the coupling.

  **\(m_{r_{\mathrm{Tool}}}\) is unchanged.** It is the observed side and
  keeps its lever name.

  **Say which quantity is commanded.** \(m\) is what the controller computes
  and what the experiments report, through
  \(M_{t_i,\mathrm{cmd}}=t_i^\top m\); the implementation forms
  \(K_{\mathrm{TCP}}\) and \(D_{\mathrm{TCP}}\) and returns the complete
  wrench. \(m_{\mathrm{cpl}}\) and \(m_{\mathrm{cpl},K}\) are analytical
  components, used to explain the mechanism and to derive the lever direction.
  Chapter 2 states this once, where the decomposition is introduced. Do not
  write that the controller commands, adds, or sends \(m_{\mathrm{cpl},K}\).

  This is a rule about **symbols only**. Ordinary prose such as `the press`,
  `the normal press` or `press-induced moment` describes the physical action
  and stays.
- The measured moment transfer is
  \(M_{\mathrm{contact}}=M_{\mathrm{TCP}}+r_{\mathrm{Tool}}\times\Delta\hat
  f_{\mathrm{ext}}\), with \(M_{\mathrm{TCP}}\) the model-estimated external
  moment about the TCP. Force is independent of the reference point and
  therefore carries no point subscript; the moments carry one because they do
  not. Both moments are referred to the value stored at the clearance
  transition, which is stated once and not repeated as a \(\Delta\) on every
  symbol.
- Keep frame labels, signs, units, control frequency, and actual parameter
  values.
- Distinguish the controller’s lack of an additional application-level
  saturation stage from command handling performed by libfranka.

The complete centre-of-compliance derivation belongs once in the theoretical
chapter. The implementation chapter gives the active construction; the
methodology and results chapters use it without re-deriving it.

## Experimental-method rules

Chapter 4 describes completed experiments, not an ideal or future protocol.
It should state:

- robot, tool, surface, and relevant software stack;
- configured and physical plane definitions;
- initial angular mismatch;
- fixed gains and swept variables;
- phase durations;
- repetitions;
- response metrics and steady-state calculation;
- repeatability assessment.

Introduce the complete experimental campaign before the detailed procedure.
Use stable, concise case identifiers such as `Case A`, `Case B`, and `Case C`
when several validation checks and parameter studies are reported. Group the
cases briefly in prose or bullets and provide one compact table containing:

- case identifier and short name;
- varied quantity or comparison;
- tested settings and repetitions;
- purpose or principal outcome.

Use the same identifiers in the Results and Discussion headings. Do not assign
a completed case identifier to an unfinished, exploratory, or diagnostic run.
The case counts must reconcile with the stated total number of analysed runs.
When different cases use different outcomes, include a second compact mapping
from each case to the metrics actually used in its Results section. Do not
present a logged diagnostic as a universal primary metric.

Keep the configured normal \(n_{\mathrm{cfg}}\) distinct from the physical
normal \(n_{\mathrm{phys}}\). Describe only the physical-plane method actually
used for the reported data, which is the single seated pose of
\Cref{subsec:plane_calibration_protocol}. A proposed multi-point fit belongs in
Future Work, not in the completed methodology or results.

Hardware constraints belong in setup and operating constraints, not in the
scientific purpose statement.

## Results and conclusion priorities

The principal experimental conclusions of the calibrated-plane campaign are:

1. Within the tested range, compliance-centre placement produced the largest
   variation in the alignment response. For each commanded rotation axis one lever
   direction improves alignment and the opposite direction does not, and the
   improving direction is opposite for the two surface tangents. With the lever
   in the other direction, almost no alignment improvement was measured.

   The magnitude that improves alignment also differs between the tangents, and
   this is separate from the direction. About \(t_2\) a \(60\,\mathrm{mm}\)
   lever turned the tool through zero to the opposite side, \(30\,\mathrm{mm}\)
   left it near zero, and \(10\,\mathrm{mm}\) produced no improvement; about
   \(t_1\) the same \(60\,\mathrm{mm}\) improved alignment. Report the two
   tangents separately and do not quote one lever for both.

   The consequence of the wrong direction is also axis dependent. About \(t_2\)
   the opposing lever moved the alignment component from \(-5.2\) to
   \(-21.1^\circ\) where the contact alone reached \(-6.9^\circ\); about
   \(t_1\) it removed the correction without reversing it. The contact face is
   \(20\,\mathrm{mm}\) half-width across \(t_2\) against \(60\,\mathrm{mm}\)
   across \(t_1\).

   **Do not compress this into `the favourable sign is opposite`.** That phrase
   asks the reader to hold three things at once — that a lever has a sign, that
   one sign is favourable, and that which one is favourable depends on the
   commanded rotation axis — none of which the phrase itself states. Say what improves
   alignment, then say that it reverses. `favourable` is usable as shorthand
   only after it has been defined at its first appearance, which is Case D in
   Chapter 5; the Abstract, Introduction, and Conclusion cannot rely on that
   definition and must spell the relation out.
2. Raising the rotational stiffness about the commanded rotation axis reduces alignment over
   the tested range. Because the tangent entries were varied separately, report
   this per axis and not as a common paired setting.
3. Reducing the translational stiffness perpendicular to the commanded rotation axis
   improves alignment about \(t_2\) only. The condition that varied the
   translational and rotational entries together was removed from the reported
   campaign on 2026-08-24: varying one entry at a time is the controlled
   comparison, and the paired setting added no separable finding. **Do not
   reinstate it**, and do not restore the claim that a high rotational
   stiffness removes the benefit, which rested on it.
4. The alignment response increased with the normal compliance-centre
   coordinate across the whole sampled range, and continued to increase up to
   the largest tested magnitude. The coupling model predicts no first-order
   dependence at all, so the measurement indicates a tangential component in
   the press. This was the largest single effect measured, which the earlier
   campaign had reported as no effect.
5. Alignment is larger for a mismatch about \(t_2\) than about \(t_1\), and
   commanding the same mismatch about the tool-face axes places the response
   near the linear combination of the tangent components, which attributes the
   asymmetry to the surface frame rather than to the face geometry.

### What the contact study is investigating, and in which order

The contact chapters are built on one open question, stated in running text and
never as a heading (the question-framing ban above still binds): **the initial
angular tool--surface misalignment is unknown before contact, so the
appropriate location of the centre of compliance is also unknown before
contact.** What the campaign establishes is whether one fixed centre can be
selected in advance of that knowledge, or whether the centre has to be chosen
per misalignment.

The narrative is therefore **not** "a displaced centre improves alignment, so
find the best displaced lever". Chapter 1 introduces the question without
answering it. Chapter 4 separates the main A--D matrix from the supporting
checks. Chapter 5 reports the main cases, Appendix D reports the supporting
checks, and Chapter 6 states the result.

The purposes of the main cases are settled and are stated in this order:

| Case | What it establishes |
|---|---|
| A | The contact-induced response with \(p_c=p_{\mathrm{TCP}}\), \(r_c=0\): the zero-coupling reference, not yet an answer. |
| B | Whether rotational stiffness can control the direction-dependent response. It changes the magnitude, chiefly about \(t_1\), and does not produce the missing alignment-directed \(t_2\) response at zero lever. |
| C | Whether cross-axis translational stiffness resolves the direction dependence. Its influence is smaller over the tested range. |
| D | Whether one fixed non-zero tangential centre can assist different misalignment signs and both principal directions. It cannot: the assisting side reverses with the sign, and the required lever differs between \(t_1\) and \(t_2\). This is the central experiment. |

Appendix D carries three supporting checks without case letters:

| Supporting check | What it establishes |
|---|---|
| Orientation-offset magnitude | The displaced-centre response is not a simple proportional scaling of the commanded angular magnitude. |
| Definition frame | A displacement is not defined by magnitude and nominal coordinates alone; the frame holding it changes the response. |
| Tool-axis displacement | The tangential component produces the press-induced moment; the tool-axis response spans \(0.34^\circ\) against \(7.73^\circ\) for the tangential displacement. |
| Intermediate tangent directions | One fixed non-zero tangential displacement does not reproduce the direction-selected rule across the four tested directions; the \(t_2\) comparison, \(+4.43\) against \(-1.61^\circ\), is the decisive separation. |

The run hierarchy is fixed. The main A--D study contains 37 settings and 111
runs. The four supporting checks contain 18 independently counted settings
and 54 runs. Together they retain the complete 55-setting, 165-run
surface-contact data set; that total already excludes the discarded combined
stiffness condition and must not be reduced again. The null-space pose-hold
study adds four settings and 12 runs, giving 177 recorded experimental runs in
the complete data set. Shared reference conditions are counted with the main
case in which they first appear.

The synthesis is that no tested non-zero tangential centre is
direction-independent, so \(p_c=p_{\mathrm{TCP}}\) is the fixed default
centre for the investigated task, and a displaced centre is a
condition-dependent means of adding rotational alignment authority. The
The diagonal similarity in the intermediate-direction check is **not** evidence
that a fixed lever is universal:
the fixed \(t_1\) lever retains a substantial projection along the selected
direction there, and the thesis says so where the numbers appear.

The design sequence that follows from this — start at the TCP, evaluate the
required alignment, introduce a direction-selected shift where more authority
is needed, and return to the TCP afterwards — is **controller-design
interpretation and future work**. Only the first two steps of it were
implemented and measured; do not present the scheduling and the return as
completed adaptive functionality.

### The shifted centre is an alignment mechanism, not a steady-contact centre

**Do not summarise the compliance-centre result as "find the best non-zero
lever and use it."** That reading does not survive the model. The coupling
moment \(m_{\mathrm{cpl},K}=r_c\times f_K\) does not vanish when the tool reaches a flat
orientation: as long as a normal press is present and \(r_c\neq0\), a fixed
tangential lever keeps commanding rotation in one direction, whether or not
alignment has already been achieved. A lever that assists one initial
misalignment therefore carries its preferred rotational direction into the
steady contact afterwards.

The defensible summary separates two regimes:

- **Transient alignment.** A tangential displacement supplies a corrective
  moment while the natural contact response is weak or opposed. The \(t_2\)
  measurements demonstrate this.
- **Sustained contact.** \(r_c=0\) gives \(m_{\mathrm{cpl},K}=0\), so the TCP is the
  neutral centre: no preferred tangential direction, and the tool responds to
  the actual contact geometry.

The implemented phase structure already embodies this, and the thesis says so:
the point-shifted impedance is used during set-up, while the grinding phase
returns to the decoupled branch. That is **architecture consistency, not
experimental evidence**: the reported quantitative runs ended at the
pre-grinding gate.

**This argument is the second reason for the TCP, not the first.** The first is
direction independence under an unknown initial misalignment. The
sustained-contact reading follows it and is written as the consequence it is:
once the press continues after alignment, a retained tangential lever also
retains its preferred coupling-moment direction, so \(r_c=0\) is the
appropriate neutral virtual reference for the phase that follows.

**Say it as a displacement of the reference point, never of the force.** The
physical surface force keeps acting where the tool touches. What moves is the
impedance reference point, from the TCP to \(p_c\), and that is what makes the
translational press generate an additional commanded moment. `The pressing
force is displaced to \(p_c\)` is wrong and must not appear.

**`universal fixed centre of compliance` is now banned outright.** The earlier
version of this rule permitted it in one defined sense; a supervisor pass
overturned that, and the term has been removed from the thesis. The reason is
that `universal` claims more than the campaign can support: the experiments
show that the *tested* non-zero tangential displacements are direction
dependent, not that no centre position anywhere in three dimensions, under any
frame definition or geometry, could be direction independent.

**The settled term is `direction-independent fixed centre of compliance`**,
defined in Chapter 1 close to: *a direction-independent fixed centre of
compliance denotes one centre position that can be selected independently of
the sign and tangent-plane direction of the initial angular tool--surface
misalignment.* The definition is task specific — one robot, one tool, one
surface, one press trajectory, the tested range of misalignment directions —
and **it is applied only to the centre positions actually tested**.

Where the claim is stated, scope it to the tested set: `the
direction-independent fixed centre among the tested centre positions`, or
`the TCP-centred configuration as a direction-neutral fixed reference`. Say
once that whether some untested centre position could also be direction
independent was not determined. `universal`, `universally optimal`, `best` and
`optimal` remain banned for any centre.

The claim the thesis may make is that **within the investigated task and
parameter range, the TCP-centred condition is the direction-independent fixed
centre of compliance, because it requires no prior knowledge of the sign or
tangent-plane direction of the initial misalignment.** `fixed centre` and
`default centre` are the usable synonyms.

**`universally optimal centre` remains banned, as does `best` and `optimal` for
any centre.** So does any statement extending the result to every robot, tool,
contact geometry, surface, grinding process, or impedance controller. The
surface-contact campaign did not test a displacement held through sustained grinding, and did
not vary the surface orientation during contact; say that where the claim is
made.

**Universality and alignment authority are separate properties, and the thesis
states the separation at least once in Chapter 5 and once in Chapter 6.** The
centre that is independent of the initial misalignment direction is not
necessarily the centre that produces the largest alignment-directed
end-effector rotation for every condition: about \(t_2\) the selected
\(40\,\mathrm{mm}\) lever changed the response from \(-1.63\) to
\(+4.43^\circ\). Write that the TCP provides the fixed direction-independent
condition, and that a displaced centre can provide greater condition-specific
alignment authority.

**No informal manual test, demonstration, or video is reported anywhere in the
thesis.** This overturns an earlier ruling that admitted the pre-grinding gate
observation as labelled qualitative evidence. That paragraph has been removed
from Chapter 5. The reason for the change is that a hand-applied check carries
no controlled condition and no recorded quantity, so a reader cannot separate
it from the measured cases however carefully it is labelled. The
sustained-contact argument does not need it: it rests on the mechanism, that
\(m_{\mathrm{cpl},K}=r_c\times f_K\) persists while the press is present, and on the
Case-D measurements and supporting definition-frame check.

### Why the two tangents behaved differently, and what may be concluded from it

The conclusion carries this synthesis, because it is what makes the \(t_1\)
and \(t_2\) results one finding rather than two unrelated ones.

About \(t_1\) the end effector already rotated in the assisting direction with
the centre of compliance at the TCP, and the selected lever added little. This
is **consistent with** the contact moment \(m_{r_{\mathrm{Tool}}}=r_{\mathrm{Tool}}\times
f_C\) and the tool-mount compliance already producing that rotation. It does
not show that \(r_{\mathrm{Tool}}\) was sufficient on its own: the contributions of contact
geometry and mounting compliance were never isolated, and the conclusion must
not claim they were.

About \(t_2\) the zero-lever condition satisfied the TCP-height criterion while
the end effector rotated slightly the wrong way. **Do not write that the robot
became correctly aligned.** The defensible reading is that the tool seated
against the surface through the mounting compliance while the end-effector
orientation moved further the other way. The mounting play supports that
reading rather than proving it, because it was measured unloaded.

**Every rotation claim names the body that rotated.** Because the physical tool
orientation is never measured independently, a sentence may say the **end
effector** rotated, never that "contact rotated the tool":

| Was | Now |
|---|---|
| contact still rotated the tool | contact still produced end-effector rotation |
| the physical tool may have rotated further than the end effector did | the physical tool may have undergone additional rotation relative to the end effector |

`further` is wrong even as a hedge, because it implies the sign of the relative
motion is known. It is not: the instantaneous relative tool--gripper rotation
was not tracked. Write `additional rotation relative to the end effector`.

**The \(\pm2^\circ\) is mechanical play, not measurement uncertainty.** Name its
physical origin where it is introduced — clearance in the custom pads clamping
the tool to the gripper fingers, about \(y_{\mathrm{EE}}\), which corresponds
approximately to \(t_2\) in the flat configuration — and say that the robot
does not measure that relative rotation. Never write `the angle measurement has
an uncertainty of \(\pm2^\circ\)`, which claims a calibrated statistical bound
the value does not carry.

**Do not write that relative tool--gripper motion "was not measured".** It was:
the mounting exhibits approximately \(\pm2^\circ\) of rotational play about
\(y_{\mathrm{EE}}\), and the thesis reports that value. The precise
limitation is narrower and must be stated as such — the play was characterised
**in the unloaded condition**, and the **instantaneous** relative tool--gripper
rotation was **not tracked separately during the contact runs**. The blanket
phrasing claims the measurement was never made, which is wrong and gives away a
result the thesis actually has.

The general point is that **satisfying the flatness criterion and producing an
alignment-directed end-effector rotation are not the same thing**, which is
precisely where the two tangents differ.

Two claims must not be made from this:

- **Not that the TCP is the best centre, or the optimal one.** About
  \(t_2\) the TCP-centred impedance rotated the end effector the wrong way.
  What is defensible is the direction-independence claim defined above: the TCP
  is the fixed default centre, since it adds no virtual coupling moment and
  selects no tangential direction, so it can be set before the misalignment is
  known. Where the natural response already assists, no lever is needed, and
  where it is weak or opposed, the direction-selected lever supplies the
  missing authority.
- **Not that the lever magnitude changes an alignment time.** The set-up
  interval was fixed at \(5\,\mathrm{s}\) and no alignment-time metric was
  defined or compared. What may be said is the model statement: for the same
  elastic press and a perpendicular lever, the predicted coupling moment is
  proportional to \(\rho_c\). A timing claim is future work.

Report the \(t_2\) results as lower bounds. Unmeasured tool motion within the
gripper can conceal correction that occurred but cannot create it.

Basic settling, formulation-equivalence, and repeatability checks support the
measurements but should not dominate the conclusion.

**The conclusion summarises the results chapter; it does not reproduce it.** An
earlier version of this guide required one entry per experimental case, in the
results-chapter order. A supervisor pass overturned that: the case-by-case list
repeated Chapter 5 in full and was the single largest source of duplication in
the thesis. **Do not restore it.**

The conclusion instead states the main findings as continuous prose — the
controller was implemented and ran in every reported run; compliance-centre
position had the largest measured influence; the direction that improves
alignment reversed between the tangents, and so did the magnitude that suits
them; stiffness effects were smaller and axis dependent; and the response
increased with the normal coordinate up to the largest tested magnitude. A null
or bounding result is
still reported as such: the zero-orientation-offset baseline stays, and the isolated
null-space result remains bounded to free-space hold under the commanded
force-equivalent.

A value appears in the conclusion only where the finding is unintelligible
without it — the baseline response, a bound on the generality of a claim.
Standard deviations stay in Chapter 5 entirely. Where a value is cut, the
relation may stay: `about eleven times`, `roughly a quarter`, `by a factor of
about seven` carry the size of an effect without repeating the numbers behind
it.

**Target length.** Chapter 6 should sit at roughly half the length of the
results chapter it summarises. The reduction comes from cutting duplication,
not from dropping findings.

The central findings the conclusion must carry are: the stiffness parameters had
a relatively small effect; compliance-centre placement had the largest measured
effect; its favourable direction depended on the commanded rotation axis; the tool mount
introduced measurement uncertainty that bounds the \(t_2\) results; and
null-space conditioning was isolated in free-space Cartesian pose hold, while the
combined mode and a physical disturbance remain untested.

Settling, formulation-equivalence, and repeatability checks belong in Chapter 5.
Do not restate them in the conclusion.

Do not give every case entry the same length. Case D is the principal finding
and carries the longest treatment; Case C's effect was limited and its
treatment is short. Uniform length across five entries is as recognisable as
uniform structure. This applies to the case sections in Chapter 5; Chapter 6 no
longer enumerates the cases at all.

**Interpretation goes directly under the evidence that supports it, and
Chapter 5 has no separate discussion section.** The chapter previously ran all
the cases and then re-discussed them in a Cross-Case Discussion several pages
later: relative parameter influence, the compliance-centre mechanism, axis
dependence, parameter selection, and measurement interpretation. Every one of
those repeated numbers the reader had already met. That section has been
removed and its content distributed to the point where the evidence first
appears:

| Was in the cross-case discussion | Now sits under |
|---|---|
| Relative influence of the parameters | Case C, closing the stiffness pair |
| Physical role of the compliance-centre lever | Case D, under the lever sweep |
| Weak tool-axis sensitivity | Supporting tool-axis check in Appendix D |
| Axis-dependent response | Case A, where the asymmetry first shows |
| Measurement interpretation | Case A, and the flatness summary |
| Implications for parameter selection | Main-results synthesis after Case E, supported by the intermediate-direction check in Appendix D |
| Scope of interpretation | deleted; Chapter 6 *Limitations* already carried it |

The editorial unit is **question, then figure or table, then observation, then
interpretation, then conclusion** — and then the next question. A case section
states what it tests before its table, and its interpretation follows its own
figure rather than waiting several pages.

A plot that is an evaluation consistency check rather than a finding does not
interrupt the argument; it goes to the supporting-plots appendix and is
referred to from the chapter.

**Every supporting plot must carry something the chapter does not, and its
section must say what that is in its first two sentences.** The appendix is not
a place to keep every available plot: a figure that reaches the same conclusion
as a chapter figure is removed, however correct it is, because an appendix of
near-duplicates reads as accumulation rather than judgement. The three that
earn their place, and the reason each does:

| Supporting item | What it carries that the chapter does not |
|---|---|
| Conditions classified as tilted by TCP height | The seven settings behind the flatness count, which the chapter states only as a total |
| Per-setting spread of the Case-D lever positions | The standard deviation of each setting; the chapter figure plots the means alone |
| Comparison with the pose-based alignment estimate | An appendix consistency check between the direct measured set-up rotation \(\gamma_{t_i}\) and the secondary estimate reconstructed from the calibrated tool normal |

A surface-frame component plot of the two outer Case-D positions was removed on
this test. Its own text conceded that it reached the same conclusion as the
chapter's wrench figure, in all three components rather than one, and the two
extra components support no claim the thesis makes. **Do not restore it.** A
figure whose introduction has to say `this is the same conclusion that
\Cref{...} carries in the chapter` has failed the test in its own words.

**Assign each chapter one role and hold it.** Chapter 5 carries observation and
interpretation together, case by case; Chapter 6 carries final conclusions
only, and summarises the limitations without restating the mechanisms.

**Group the limitations under named subsections** rather than listing them as
consecutive paragraphs of identical shape (state limitation, explain mechanism,
state consequence, delimit interpretation). The settled grouping is:
experimental generalisability; calibration and measurement uncertainty;
tool-mount compliance; null-space validation and real-time timing. A reader can
then find the limitation that bears on the result they are checking, instead of
reading a catalogue.

**Prioritise Future Work; do not mirror the limitations one for one.** Deriving
exactly one proposed experiment from each limitation produces a complete,
evenly weighted list that reads as generated. State the three extensions
considered most important, each with the question it would settle, then cover
the remainder briefly in a single paragraph. For this thesis the three are
negative orientation offsets, independent measurement of the tool-face angle, and a
combined-mode null-space study with a physical disturbance.

Items in a bulleted or numbered list begin with a capital letter and are
written as complete statements. Do not continue a lead-in sentence across the
list items in lower case.

Report a comparison as a relation as well as an absolute value, so the reader
sees the size of an effect without dividing the numbers. Prefer `about eleven
times`, `roughly a quarter lower`, or `by a factor of about seven` alongside
the measured values. Round the relation to the precision the repeatability
supports; do not state a ratio to two decimals when the underlying values carry
a tenth of a degree of uncertainty.

### Follow-on pilots

When a calibrated pilot is recorded after the main campaign:

- label it as a separate pilot and do not silently add it to the earlier run
  count;
- state which earlier runs are decoupled controls and which runs activate the
  point-shifted law;
- report the controller lever using
  \(r_c=p_c-p_{\mathrm{TCP}}\), rather than calling its sign simply “left” or
  “right”;
- retain the pose-based alignment metric and the operator-observed contact
  state as separate outcomes when tool-to-gripper motion is unmeasured;
- report mean and sample standard deviation only for repeated conditions; and
- call a selected lever provisional until the orthogonal axis and an
  independent physical-angle measurement have been checked.

## Energy, passivity, and stability

Do not include an energy-based experimental objective, energy metric, or
energy-monitoring proposal unless it is directly relevant to a performed study.
Do not restore a standalone stability or passivity chapter. Algebraic symmetry
and positive-(semi)definiteness may be stated where needed, but they do not
prove closed-loop stability or passivity of the sampled
robot–controller–environment system.

## Headings must not be stranded

A heading carries no information on its own. If it falls at the foot of a page
while what it introduces starts on the next, the reader meets a label with
nothing under it and has to turn the page to learn what it labels.

The document class already holds ordinary chapter and section headings with the
text beneath them. Hand-built headings do not inherit that. A heading placed
before a `longtable`, a `tabular`, a figure or a listing needs the space
reserved explicitly, because `\nobreak` does not hold across an environment
that begins its own breakable structure:

```tex
\needspace{5\baselineskip}%
\par\noindent\textbf{Group heading}\par\nobreak
\begin{longtable}{...}
```

Reserve enough for the heading and the first few rows, not for the heading
alone. Check the compiled document rather than the source: whether a heading
strands depends on where the page happens to break.

## Final editorial checklist

Before accepting a revision:

- run the quick scan in [THESIS_VOICE.md](THESIS_VOICE.md) over changed prose;
- read every paragraph's first sentence alone and rewrite any that reads as a
  slogan rather than a technical statement;
- check that each results subsection cross-references the table or figure its
  claim rests on;
- check that definitive wording is bounded to the tested range;
- check that the conclusion states findings rather than repeating Chapter 5's
  values and standard deviations;
- search for question-driven headings and literal research questions;
- search the running text for names carrying two or more underscores;
- search for `frozen`, and for any name built from a quantity's state;
- search for `automatic` and `automatically`; only literal source identifiers,
  `\label{}` keys, and figure filenames may keep them;
- search for `tilt`, `excitation`, and `mismatch` where a commanded tool
  orientation offset is meant;
- search for `task frame` and for `R_{\mathrm{task}}`; the expected count in
  running text, headings and the symbol list is zero, and the surviving `task`
  hits must all be the generic ones or `\Lambda_{\mathrm{task}}`;
- check that one quantity carries one name and one symbol throughout;
- check that every new equation symbol is introduced by quantity name, symbol,
  and short role at its first use;
- check that every running-text use of a defined quantity name is followed
  immediately by its symbol;
- search the symbol list for `mixed` and for units written without a space;
- search the tables for a unit in round brackets, and for `(deg)` in place of
  the degree symbol;
- check that the contents lists the figures, tables and symbols;
- check the contents page number of every unnumbered chapter against the page
  that chapter actually starts on in the compiled PDF;
- check that every setting of Cases A--D carries its sample standard deviation
  in its Appendix-D table, and that Section 4.3.3 still describes what the
  tables do rather than what they might;
- check that any time-history figure says in the text whether its traces are
  single repetitions or averages;
- check that no heading sits at the foot of a page without what it introduces;
- inspect every changed figure in the compiled document, per FIGURE_STYLE.md;
- check that list items begin with a capital letter;
- check that the conclusion covers every experimental case;
- check that each reported comparison also states its relation;
- search for Git, repository, development-history, and draft-comparison terms;
- search for proposal language outside Future Work;
- check configured versus physical plane terminology;
- check `estimated` versus `measured` force/wrench terminology;
- check experiment counts, repetitions, units, and parameter values;
- check predicted versus experimentally confirmed results;
- grep the Abstract and the Kurzfassung for digits; a measured value in either
  is a fault, and the only permitted numbers name a thing rather than measure
  one, such as the robot's degrees of freedom;
- check Abstract, Kurzfassung, Results, and Conclusion for identical certainty;
- remove duplicated theory and unsupported causal claims;
- compile both `Thesis.tex` and `Professor_Draft.tex`;
- resolve undefined references and overfull boxes;
- visually inspect changed pages.

The final test for every sentence is whether it belongs in a robotics/control
thesis whose reader knows nothing about the author’s repository, coding
history, or earlier drafts.
