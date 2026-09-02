# Thesis Writing Guide

This file is the standing editorial guide for this thesis. Update it whenever a
new recurring preference, technical convention, or evidence rule is agreed.
The current thesis contains one combined Results and Discussion chapter.
The earlier contact-alignment campaign was preserved in an appendix while the
calibrated-plane, axis-specific campaign was being measured. That campaign is
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
\(J(q)\) has full rank, the null space is one-dimensional` is normal
technical prose and stays.

**The construction survives in four more places than the table above lists**,
and the 2026-08-27 consistency pass found them by grepping for a sentence- or
clause-initial `What`, `Whether` or `Which` followed by a lower-case word.
What it caught, and what replaced it: `what the phase transition changes is the
generated Cartesian reference` became `the phase transition changes the
generated Cartesian reference`; `Which definition holds a displacement is
examined experimentally in …` became `The two definitions are compared
experimentally in …`; `What varies inside this configuration is the secondary
torque` became `Only the secondary torque varies inside this configuration`;
and `Whether the commanded pose was in fact retained is consequently checked by
\Cref{…} rather than assumed` became `\Cref{…} therefore checks that the
commanded pose was retained rather than assuming it`. Run that grep over the
chapters and the appendices before submitting; the expected count is zero.

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
4. the scope within which the finding applies.

**The Abstract carries the headline percentages and the two acceptance
values.** Agreed 2026-09-01, replacing `Keep measured values out of the
Abstract, without exception`. The permitted set is the Case~A--D headline
percentages with their reference conditions, the rotational-stiffness interval
that produced one of them, and the largest measured Cartesian position error
against its limit. Everything else stays out: no per-condition response means,
no achieved offsets, no compliance-centre coordinates, no measurement counts.

The reason for the change is that the qualitative wording could not state the
main finding. `A displaced centre produced a slightly larger response` is true
and says nothing about the result that matters, which is direction selection:
the displacement selected for the offset direction raised the response by
\(4.0\,\%\) and \(4.3\,\%\), while the opposite displacement reduced it
by \(97.6\,\%\) and \(99.2\,\%\). Those four numbers *are* the finding,
and a reader cannot infer the asymmetry from `slightly larger`.

**This is not a return to the exception withdrawn on 2026-08-25.** That one
admitted a pair of per-condition means — `changed the measured
contact-establishment rotation from \(-1.63^\circ\) to \(+4.43^\circ\)` —
which made one experimental condition look more important than the finding, and
it stays withdrawn. A percentage stated against its reference condition is a
relation rather than a condition-specific measurement, which is the distinction
that separates the two.

**The measurement count is still excluded**, under the rule below, and so are
the local axis symbols \(t_1\) and \(t_2\): the Abstract names `the same
surface-tangent axis` in words instead.

**The measurement count does not go in the Abstract.** A supervisor pass briefly asked
for it, and it was added; the author then removed it as repetitive, which it
was — the same figure was appearing in the Abstract, the Kurzfassung, the
Introduction, twice in the results chapter, and the Conclusion. **State the
total number of measurements once, in the methodology chapter, and nowhere else.**
Elsewhere write `were evaluated experimentally`, `all reported contact experiments`,
or `the largest measured response`. A count that appears six times reads as padding, not as
evidence.

Write the Abstract in four parts, in order: the engineering problem; the
implemented approach; the evaluation method; and the main findings within the
investigated scope. Prefer one claim per sentence — an Abstract in which every
sentence carries a full conclusion reads as machine-polished however accurate
it is.

State the angular evaluation positively: `The angular conditions were defined
relative to the configured surface geometry, and the contact response was
calculated from the measured end-effector orientations.` The Kurzfassung uses
the corresponding statement: `Die Winkelbedingungen wurden relativ zur
konfigurierten Flächengeometrie definiert, und die Kontaktreaktion wurde aus den
gemessenen Endeffektororientierungen bestimmt.` The physical-normal and
instantaneous physical-angle limitations belong in Section 6.2.2 and are not
repeated in either summary.

**The Abstract and Kurzfassung may use the thesis's symbols.** The supplied
Abstract of 2026-09-02 withdrew the earlier rule that they contain no local
axis symbols such as \(t_1\) or \(t_2\). It names \(t_1\) and \(t_2\) for the
rotation and displacement axes, \(r_c\) for the lever arm, \(r_c\times f\) for
the moment it generates, and \(\gamma_{t_1}\) for the response. The reason the
earlier rule gave — that a first-time reader has not met the surface frame —
was outweighed by the cost it imposed, which the rule itself recorded: an
Abstract that names no axis cannot say which stiffness was varied without
implying that both tangent entries were.

What the summaries still avoid is a coordinate convention the reader must
reconstruct. Phrases such as `sign-independent`, `assisting side`, `the side
reversed`, and `matched the sign` do not appear in either, and neither uses the
`positive-offset condition` and `negative-offset condition` names, which belong
to the body chapters that define them against measured values.

**Write `offset direction`, not `offset sign`, in the two summaries.** The
Abstract defines the pair itself — `positive and negative pre-contact angular
offsets were investigated about \(t_1\)` — so `for both offset directions` is
readable where `for both offset signs` asks the reader to hold a coordinate
convention the summaries never state.
This keeps `both signs` out of the Abstract and the Kurzfassung while the body
chapters continue to use the `positive-offset condition` and
`negative-offset condition` names settled below.

**Angular test conditions are described as directions of rotation, and are
named by their offset direction where one has to be identified repeatedly.**
Throughout the thesis, the configured orientation offset
\(\theta_{\mathrm{offset},t_1}\) defines the desired pre-contact tool direction,
the achieved pose-based initial angular offset \(\theta_{0,t_1}\) gives the
condition reached at contact entry, and the contact-establishment response
\(\gamma_{t_1}\) gives the measured outcome. Use `both directions of rotation`
or `both rotational directions` for aggregate comparisons. The plus and minus
symbols remain in scalar equations and numerical values because they encode the
coordinate direction.

**`positive-offset condition` and `negative-offset condition` are the settled
names for the two directional test conditions.** Agreed 2026-09-01. They
replace `the direction of rotation generated by the configured \(+10^\circ\)
offset`, which was accurate and unreadable: eleven words, repeated nine times in
Chapter 5 alone, forcing the reader to re-derive the condition at every
comparison. **This overturns the earlier ban on `positive condition`**, which is
what produced the long form. Define the pair once, at the chapter opening,
against the achieved offsets it names -- at the TCP-centred condition,
\(+9.31^\circ\) and \(-9.41^\circ\) about \(t_1\) -- then use the short
names. The Abstract and the Kurzfassung do not use the two condition names,
because a first-time reader has not met the definition; they write `positive and
negative pre-contact angular offsets` once and `both offset directions`
thereafter.

**The Introduction describes the geometry before it introduces local tangent
symbols.** Write `both directions of rotation about one axis in the surface
plane` until the surface frame and its tangent basis are defined in
Chapter 2. The symbols \(t_1\) and \(t_2\) begin where their geometry is
established.

**Compliance-centre selection is described through displacement and rotational
directions.** Write `the displacement direction selected for the corresponding
initial angular-offset direction` for the aligned case, which names the offset
the displacement is matched to instead of leaving the rotation unqualified.
When the other outer position is meant, write `the outer position in the other
displacement direction`. Phrases such as `the
matching side`, `the opposite side`, `the side matched the initial-deviation
sign`, and `initial-deviation sign` are not used. The technical compounds
`robot-side` and `application-side` retain their established meanings.

**Revise the Abstract last**, after the body text is settled, and derive the
Kurzfassung from the finished English rather than paraphrasing it independently.

The Abstract no longer expands \abbr{DOF} on first use, since it writes
`seven-degree-of-freedom` in words. The acronym is still introduced by
Chapter 1 and by the title, so the abbreviation list is unaffected.

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
  The contribution list lives here and separates implemented controller
  functions from experimentally established findings. Section 6.2 contains
  the corresponding validation boundaries.
- Theoretical Background: explain only the mathematics required to understand
  the controller and experiments.
- Controller Design and Implementation: explain how the verified controller
  realizes the theory, without line-by-line code narration.
- Experimental Methodology: document what was used, varied, held constant,
  measured, and calculated in the completed experiments.
- Results and Discussion: report measured values, quantitative analysis, and
  interpretation in positive form.
- Conclusion: state what was learned without repeating the full controller
  architecture.

**Limitations have one chapter-level home.** Chapters 1--5 state what was done,
calculated and measured in positive form. Section 6.2 contains every evidence
gap, unevaluated case, unresolved measurement limit, and boundary on
generalisability. Do not repeat a limitation in the Abstract, Introduction,
Methodology, metric definition, or Results.

Explain a concept authoritatively once. In particular, avoid repeating
Cartesian impedance, point-shift derivations, gain transformations, damping,
null-space projection, or energy/passivity arguments across chapters.

### Settled compression and evidence hierarchy

The main contact argument contains Cases A--D only: the TCP-centred baseline,
rotational stiffness, cross-axis translational stiffness, and tangential
compliance-centre position. Every reported contact comparison uses commanded
rotation about \(t_1\); \(t_2\) remains only as the perpendicular stiffness or
lever coordinate where required. **The reported surface-contact study is
Cases A--D and nothing else**: 19 settings and 57 trials, with the
12 Cartesian pose-hold trials bringing the complete reported data set to 69
trials. The tool-axis comparison was withdrawn on 2026-09-01; see
*Appendix D* below for why, and do not reinstate its counts.

State the experimental exclusion once in Chapter 4: the contact evaluation
uses the \(t_1\) data set, which provided repeatable comparisons, whereas the
\(t_2\) measurements showed greater variability. Section 6.2.2 gives the full
limitation and may identify tool-mount play about \(y_{\mathrm{EE}}\),
approximately aligned with \(t_2\), as one possible contributor. Future Work
calls for repeating the evaluation with improved tool constraint and an
independent physical-orientation measurement; it does not repeat the full
limitation.

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
the corresponding sample standard deviations for Cases A--D. Cases A--C do not
repeat this information or add a separate maximum-scatter sentence. Individual
standard deviations appear in the main text only where their spread affects the
interpretation; Case D therefore names its higher-spread condition explicitly.

**Section 4.3.3 states the repetitions, the reporting form, and the totals,
in that order.** Its settled wording is `Each parameter setting was evaluated
in three repeated trials. The reported values are arithmetic means with sample
standard deviations. Cases A--D comprised 19 parameter settings and 57
surface-contact trials. The 12 Cartesian pose-hold trials bring the complete
experimental data set reported in this thesis to 69 trials.` The earlier
qualification `and where relevant in the supporting checks` went with the
supporting check itself on 2026-09-01: every reported setting now carries its
sample standard deviation in its Appendix-D table, so the unqualified form is
accurate.

**The repeated mean and spread definition appears once.** Chapter 5 defines the
arithmetic means and directs the reader to the Appendix-D standard deviations
in its opening. Cases A--C proceed directly to their comparisons. Case D
identifies the largest spread because that condition differs visibly from the
rest: the direction generated by the \(+10^\circ\) configured offset at
\(r_{c,t_2}=-20\,\mathrm{mm}\), with a sample
standard deviation of \(0.44^\circ\). The generic sentence explaining that
markers are means and error bars are one sample standard deviation is omitted;
the chapter opening and the figure convention already establish it.

A standard deviation that rounds to \(0.00^\circ\) at the reported two
decimals is written `\(\pm0.00\)`. It is the correctly rounded sample standard
deviation at the precision the rest of the table uses, and switching that one
entry to a third decimal or to an inequality would break the column for no
gain.

The main contact evaluation uses the contact-establishment response
\(\gamma_{t_1}\). Its positive and negative values retain the response
direction. The commanded normal force \(F_n\) and commanded TCP
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

measured value → absolute and percentage comparison → interpretation.

Use it as the default, not as a template for every paragraph. Four consecutive
paragraphs built to that shape is itself a fault; vary what each paragraph does,
per *Vary the architecture, not the vocabulary* in
[THESIS_VOICE.md](THESIS_VOICE.md).

Tie each interpretation to the evidence it rests on. A claim in a results
subsection carries a `\cref` to the table or figure that supports it, in the
sentence that makes the claim.

Match the certainty of the wording to one configuration and three repetitions.
Prefer `indicates`, `supports`, `is consistent with`, and `strongly influences`
to `proves` and `decides`. Name the cases or parameter interval directly so
the sentence is specific by construction. Section 6.2 carries the
generalisability boundary.

**Do not use `signed` as a modifier in thesis prose, headings,
captions, axes, or tables.** The defining equation and the displayed positive
and negative values establish the algebraic direction. Name the quantity
directly as the `contact-establishment response`, `normal-force component`,
`clearance`, or `component along` a defined direction. State the meanings of
positive and negative values once beside the definition when the reader needs
them.

**Each main case ends with one percentage-based headline comparison.** Keep
the detailed results in their physical units. At the end of each Case A--D
discussion, add one percentage for that case's main result and retain the
corresponding absolute values. The Chapter 6 conclusion repeats only these
headline percentages. State the denominator or reference condition clearly.
Skip a percentage when its reference is near zero, crosses sign, or would
obscure the physical quantity.

Carry one main claim per sentence. A clause answering more than about two of
*what / where / how / when / why* is algorithmically compressed however correct
it is; split it so the reasoning is presented step by step.

Where a claim is the main finding of its section, give the measurement before
the conclusion. `The response changed by several degrees when the lever was
displaced by 60 mm. The changes produced by the tested stiffness values were
substantially smaller. Across Cases A--D, the compliance-centre position
therefore had the largest measured influence.` reads as derived from
the data; the same content with the conclusion first reads as announced.

The target style for this thesis is: impersonal academic English, passive voice
for performed actions, direct language for mathematical and physical relations,
one main claim per sentence, explicit links between measurements and
interpretations, and conclusions tied to the named measurements. Literary
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
`the improvement fell as \(K_R\) rose`, `the lever direction determines the
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

**Every visible figure caption and table caption must fit on one rendered
line**, and should normally remain below about 12 words. Each corresponding
entry in the List of Figures or List of Tables must also fit on one line. This
is a hard layout limit rather than a preference. If a caption or list entry
wraps, retain only the descriptive noun phrase that identifies the plotted
quantity, comparison, geometry, or parameter set, and move every explanation
to the surrounding text. **A noun phrase, never a question** — see the
question-framing ban under *Scientific narrative*, which covers captions as
well as headings.

Good examples:

- `Contact-establishment settling at 4, 8, and 12 s.`
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
reading `\([\theta_{\mathrm{offset},t_1},\theta_{\mathrm{offset},t_2}]\) (deg)` was inconsistent twice over, in
its brackets and in spelling out the degree where the rest of the document sets
the symbol. The direction-check table was corrected on 2026-08-25 to
`Configured Orientation-Offset Components, \([\theta_{\mathrm{offset},t_1},\theta_{\mathrm{offset},t_2}]\) \([{}^\circ]\)`
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

**`cross-axis` is not used.** Withdrawn 2026-09-02, replacing the earlier
rule that kept `cross-axis translational stiffness` wherever \(K_{p,t_2}\)
stood beside it. It names an axis only by its relation to another axis, which
the reader must first identify. Where the tangent symbols are available, the
Case-C parameter is `the translational stiffness along \(t_2\)`, and the
subsection heading, the figure axis label, the figure caption and the appendix
caption all carry that name. In the Abstract and the Introduction, where
\(t_1\) and \(t_2\) are not defined until Chapter 2, it is `translational
stiffness along the surface`, in the singular, which states the plane without
implying that both tangent entries were varied. Do not write `along the surface
tangents` there; the plural reads as a sweep of both entries.

**Positive values carry no explicit sign.** Agreed 2026-09-02 for Chapter 5 and
its figures, and applied to the whole thesis. Write \(9.31^\circ\),
\(7.57^\circ\), \(10^\circ\), \(40\,\mathrm{mm}\); keep the minus sign on
negative quantities, so a directional pair reads \(10^\circ\) and
\(-10^\circ\). A leading plus adds nothing where no sign is written on the
positive member of the pair, and it makes a results table look as though two
different conventions were in use. Figure labels follow the prose: the Case-A,
Case-B, Case-C and Case-D legends were changed on the same date, since a figure
that still prints \(+9.31^\circ\) contradicts the sentence beside it.

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

- **state** for each runtime node of the controller flow. Do not give the same
  node an alternate runtime label such as phase, gate, mode or sequence step.
  `Sequence` may
  still name the ordered surface-contact path, and `configuration` may still
  distinguish the selectable null-space alternatives; neither replaces
  `state` for a runtime node. The contact-press state is **Contact
  Establishment**, and its measured quantity is the **contact-establishment
  response**. Visible quantities associated with that state use the
  `\mathrm{CE}` subscript. The older `set` form remains only in literal
  software keys and internal source labels.

  **Contact-Impedance Hold** is the thesis name for input `t`. It is a
  Cartesian pose hold using the Contact Establishment impedance and is separate
  from the four null-space modes of ordinary Cartesian Pose Hold. `Test Mode`
  and `Setup-Impedance Hold` are withdrawn as reader-facing names. **Manual
  Guidance** is the one name for the state entered by input `g`; `Guidance
  Mode` is withdrawn.

- **centre of compliance** for the point the \(6\times6\) stiffness is
  defined about, \(p_c\), with \(r_c=p_c-p_{\mathrm{TCP}}\) as its lever.
  Attributively, `compliance-centre lever`, `compliance-centre coordinate`.

  **\(r_c\) points from the TCP to the centre, and there is no second
  symbol.** An earlier convention defined \(r_c=p_{\mathrm{TCP}}-p_c\) and
  carried a separate \(d_c=p_c-p_{\mathrm{TCP}}=-r_c\) for what the plots
  and tables report, with a standing warning never to rename one into the
  other. **That is withdrawn.** \(d_c\) is removed from the thesis, and
  \(r_c\) now *is* the reported coordinate: `centre position +40 mm`
  and \(r_{c,t_2}=+40\,\mathrm{mm}\) are the same statement. Labelling a
  `centre position` axis \(r_{c,t_2}\) is now correct rather than a sign
  error.

  The displacement direction is checked against the active Case-D result: the
  direction generated by the \(+10^\circ\) configured offset about \(t_1\)
  uses the outer position \(r_{c,t_2}=+40\,\mathrm{mm}\) for its largest
  response.

  **The compliance-centre contribution is \(r_c\times f\), using the complete
  commanded force.** The point-shift blocks carry
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
  \(r_c=0\) and in the complete moment relation \(m=m_R+r_c\times f\). It is
  introduced there without \(p_c\), as the displacement from the TCP to the
  virtual CoC.

  **The thesis and source use opposite names for the same physical lever.** The
  thesis always defines \(r_c=p_c-p_{\mathrm{TCP}}\). The current controller
  instead uses the internal source-side lever
  \(\ell_c=p_{\mathrm{TCP}}-p_c=-r_c\), although its C++ identifier is
  `r_c`. Its adjoint block is therefore `+[ell_c]_x`, which is identical to the
  thesis block `-[r_c]_x`. Appendix A states this mapping before reproducing
  the implementation signs.

  The tool-frame parameter `compliance_center_offset_ee` stores the thesis
  displacement \(r_c\) and is negated when the source forms \(\ell_c\). The
  surface-frame parameter `r_tcp_from_compliance_center_surface` stores
  \(\ell_c\) directly. Do not describe the two parameter keys as carrying the
  the same vector direction.

  **Only the end-effector-frame definition is used in the reported
  experiments.** Every non-zero experimental displacement is configured with
  `compliance_center_offset_ee` and held constant in end-effector coordinates.
  The surface-frame branch may be described as an implemented option, but it is
  not an experimental condition. The former definition-frame comparison and
  its three settings are excluded from the thesis results and measurement totals.

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

  Chapter 3's subsection over the surface frame and the static tool geometry
  is **Surface Frame, Tool Reference, and Tool Geometry**, settled on
  2026-09-01. It replaced `Surface and Tool Reference`, which named neither the
  tool rectangle nor the target orientation the subsection defines, by way of
  an intermediate `Surface Frame, Tool Geometry, and Target Orientation` agreed
  earlier the same day. The earlier
  `Surface-Relative Geometry and Tool Representation` placed the selected-point
  algorithm beside the static rectangle before the phase sequence had given
  that algorithm a purpose.

  **This is not in tension with the shortening of the Section 4.2 heading.**
  That heading listed `Physical Surface`, which Section 4.2 does not produce;
  this one lists three things the subsection does define, and a reader looking
  for the target orientation would not find it under `Reference`.

  **The final two subsections are separate: `Operator-Controlled Hold Before
  Grinding` and `Grinding`.** They were merged on 2026-09-01, because `Grinding`
  then had a single sentence beneath it while the hold above it had four, and
  **that merge was reversed the same day**. Grinding now carries two paragraphs
  of its own -- what the state does, and the statement that it lies outside the
  experimental evaluation -- which is the balance the merge was reaching for.
  Both subsections keep their own `\label{}` keys.

  **The generic uses of `task` were thinned on 2026-08-26 and again on
  2026-08-27, selectively.** What survives is only what names a standard
  quantity of redundancy resolution or is credited to a cited source:
  `the task Jacobian`, `task-producing singular values` and `task mappings`, `task-related
  component` and `first-order task component`, and an `assembly task` or
  `insertion task` attributed to a source. What went, and what replaced it:

  | Was | Now |
  |---|---|
  | selected task directions | selected Cartesian directions; selected compliance directions |
  | the intended surface task | the intended surface-contact sequence |
  | This task-level result | This experimental result |
  | Cartesian task retention, task-retention criterion | Cartesian position retention, position-retention criterion |
  | the investigated task | the investigated contact configuration |
  | without changing the commanded Cartesian task | without changing the commanded Cartesian motion |
  | the Cartesian task stays primary | neither contributes a first-order Cartesian wrench |
  | the primary Cartesian pose-hold task | the primary Cartesian pose-hold objective |
  | For the surface-contact task | For surface contact |

  **`the investigated task` and `the Cartesian task` were permitted by the
  earlier version of this rule and are now withdrawn**, written here as literal
  strings so a rename cannot revive them. `the investigated task` was the bound
  on the direction-independence claim in the Abstract, the Kurzfassung
  (`die untersuchte Aufgabe`), Chapter 1 and Chapter 6, and it named the least
  checkable thing in a sentence whose whole job is to say what the claim is
  limited to: one robot, one tool, one configured surface reference, one press trajectory.
  `the investigated contact configuration` names that, and matches
  `in the investigated configuration` under *Calibrate the certainty to the
  evidence* in [THESIS_VOICE.md](THESIS_VOICE.md). `the Cartesian task` went
  because in both places it stood for something the thesis can state exactly —
  the commanded Cartesian motion in Chapter 1, and the absence of a first-order
  Cartesian wrench in Chapter 5, which is what the null-space projector
  actually guarantees.

  **Do not run this as a bulk substitution.** Every surviving hit above is a
  standard term or a citation, and replacing one of those with `configuration`
  or `motion` would trade a term of art for a vaguer synonym, which
  *What must never be done to sound less generated* rules against. The check is
  per occurrence: if the word names the six singular directions of \(J\), the
  operational-space inertia, or a cited author's application, it stays.

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

  The **Grinding state** keeps its name, as do the **grinding tool** and the
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
  geometric tool reference during contact establishment.

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
  presumes edge contact, and the Contact Establishment state is designed to seat the tool face
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
- **configured orientation offset** for the deliberate pre-contact angular
  setting: a `configured orientation offset about t1`. Its vector is
  \(\theta_{\mathrm{offset}}\), and its surface-tangent components always carry
  the full index \(\theta_{\mathrm{offset},t_1}\) and
  \(\theta_{\mathrm{offset},t_2}\). Use `zero orientation offset`; identify a
  non-zero condition by its configured value or its direction of rotation. Do not use
  `commanded rotation`, `commanded tool orientation offset`, `tilt`, `tool
  tilt`, `signed tilt`, `excitation`, or `mismatch` for this configured
  quantity.

  **The configured offset establishes a pre-contact condition; it does not
  prescribe the rotation measured during contact.** It is applied during Tool
  Orientation before Surface Approach and sets the desired pre-contact tool
  direction. At the start of Contact Establishment, the achieved condition is
  the **pose-based initial angular offset**
  \(\theta_{0,t_1}\). Contact Establishment holds the captured orientation
  reference and produces the **contact-establishment response**
  \(\gamma_{t_1}\). The chain is therefore
  \(\theta_{\mathrm{offset},t_1}\to\theta_{0,t_1}\to\gamma_{t_1}\).

  In Chapter 3 the configured vector and its rotation are
  \(\theta_{\mathrm{offset}}=\theta_{\mathrm{offset},t_1}t_1+
  \theta_{\mathrm{offset},t_2}t_2\),
  \(u_{\mathrm{offset}}=\theta_{\mathrm{offset}}/
  \lVert\theta_{\mathrm{offset}}\rVert\), and
  \(R_{\mathrm{offset}}=R(u_{\mathrm{offset}},
  \lVert\theta_{\mathrm{offset}}\rVert)\). The desired tool-normal direction
  is \(n_d=R_{\mathrm{offset}}(-n_s)\). For zero offset,
  \(R_{\mathrm{offset}}=I\) and \(n_d=-n_s\). The former
  \(\theta_{\mathrm{cmd}}\), \(u_{\mathrm{cmd}}\),
  \(R_{\mathrm{cmd}}\), \(\theta_{t_1}\), and \(\theta_{t_2}\) forms are
  withdrawn.

  A quantitative experimental axis uses `Achieved Initial Angular Offset`
  followed by \(\theta_{0,t_1}\) and its unit. A table condition column uses
  the same name. The configured offset may be stated
  where the pre-contact setting, parameter file, or direction-selection rule
  is the subject. It is never substituted for the achieved entry condition.

  **The angular evaluation uses the configured surface and measured
  end-effector pose.** In Chapters 1--5, state that
  \(\theta_{0,t_1}\) is the achieved pose-based initial angular offset
  calculated relative to the configured surface reference. Do not introduce a symbol or equation
  for a physical entry angle, and do not call \(\theta_{0,t_1}\) a measured
  physical angle. Section 6.2.2 carries the consolidated limitation: the
  physical surface normal and instantaneous tool--surface angle were not
  measured independently in each experiment.

  **State the physical problem before the configured offset.** Tool
  Orientation has access to the configured normal \(n_s\), not an independent
  measurement of the physical normal \(n_{\mathrm{phys}}\). With zero offset
  it makes the desired tool face parallel to the configured plane. If the
  physical plane differs, that nominal alignment leaves a physical
  tool--surface error at contact entry. The contact interaction is intended to
  permit a rotation that reduces this remaining mismatch.

  **The Chapter 1 motivation separates two contact-entry angular differences.**
  The first lies between the configured and physical surfaces through placement
  and calibration tolerances. The second lies between the desired tool
  orientation and the orientation achieved before surface approach within the
  configured orientation tolerance. Figure 1.1 draws the configured surface as
  a solid red line, the physical surface as a solid blue line, and a schematic
  tool face at the orientation reached before approach as a solid dark-green
  line. The one dashed element is the black construction datum carrying the
  desired tool direction. Tool-mount play remains part of the measurement limitation in Section
  6.2.

  **The configured offset is not a surrogate for the surface-reference
  difference.** It is only the desired pre-contact orientation offset relative
  to \(n_s\). Do not equate it with, or describe it as an approximation of, the
  unknown physical difference. A zero offset specifies parallelism with the
  configured plane; a non-zero offset specifies a deliberate angular offset about
  the selected surface tangents.

  Keep the three chapter roles separate. Chapter 2 derives the directional
  compliance-centre rule from the generic tangent-plane angular offset
  \(\theta_a\) that contact should reduce. Chapter 3 defines the configured
  pre-contact offset and constructs \(n_d=R_{\mathrm{offset}}(-n_s)\).
  Chapter 4 explains how varying that setting supplied reproducible
  reference-relative entry conditions, then distinguishes it from the achieved
  \(\theta_{0,t_1}\). It states in words that the physical surface may differ
  from the configured reference by an unknown angular amount. No equation is
  introduced for that unmeasured relation.

**There is no fixture in this work, and the word must not appear.** No fixture,
jig, clamp, or workholding device was used: the surface is simply positioned,
and the tool is held in the gripper. Earlier drafts used `fixture` loosely for
three different things, and each needs its own correct name:

- where the *surface* is meant — `the surface`, or `the surface placement`
  where the tolerance of that placement is the point;
- where the *gripper's hold on the tool* is meant — `the tool mount`. This is
  the one that carries the \(\pm2^\circ\) of unloaded play and the associated
  measurement limitation;
- where the *whole rig* is meant — `the setup`.

Getting this wrong is not only a wording fault. Earlier drafts attributed a
contact observation to "the fixture" while another section explained it
through the tool mount, so the thesis named two different causes for one
observation.

**The word `automatic` is not used in thesis prose, in any form.** Not
`automatic`, `automatically`, or `automatic-`. It contrasts what the controller
does with an unstated manual alternative that this thesis never ran, and in
every place it appeared the specific name was already available and carried more
information:

| Was | Now |
|---|---|
| the automatic sequence | the controller state sequence |
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

**Use `experiment`, `measurement`, or `trial`; `run` is not thesis prose.** Use
`experiment` for the complete test procedure or one executed contact condition,
`trial` for one repetition of a parameter setting, and `measurement` when
counting observations in an experimental data set. Thus write
`experiments`, `contact experiment`, `pose-hold trial`, `before each
experiment`, and `experiment-specific configuration`. State repeated settings
as `Each parameter setting was evaluated in three repeated trials` or `Three
repeated measurements were performed for each parameter setting`. Use `number
of experiments` or `number of trials`, and write `no experiment was discarded`.
`Run` remains only where it is part of literal code, a software identifier, a
command, a filename, or an exact logged field name. In running prose about
software execution, use `execute`.

**Reserve `reported` for a data-selection distinction.** It is useful when a
sentence distinguishes the selected data set from archived or excluded
experiments. It adds nothing to ordinary references to experiments,
measurements, responses, quantities, values, data sets, endpoints or trials;
name those objects directly.

**Experimental results are measured, not recorded.** Use `measured` for
quantities, values, responses and observations. Reserve `recorded` for the
literal data-acquisition or storage process, and for a document or table that
contains information. Do not write `newly measured`, `already measured`,
`previously measured` or `re-measured` when the chronology is irrelevant;
these forms describe how the campaign was assembled rather than what it found.
State the measurement directly, or omit the acquisition history:

| Was | Now |
|---|---|
| the three scheduled repetitions for each newly measured setting | the three scheduled repetitions of each setting |
| the \(5\,\mathrm{N\,m/rad}\) condition … is not a separate measurement | the \(5\,\mathrm{N\,m/rad}\) condition is the corresponding zero-lever reference of Case~A |

The same applies to the measurement-count bookkeeping. Where one case reuses a
condition from an earlier case, state the relation between the cases — `a
condition that a case shares with an earlier one is counted with that earlier
case` — and not the acquisition history that produced it. Never write `not
counted again`, `not measured twice`, or `an additional measurement`.

Do not build a name out of the state a quantity happens to be in. The term
`frozen` is not used in thesis prose. State when a quantity is selected and
that it is held constant, then use its ordinary technical name. For example,
the centre of compliance is selected at the clearance transition and held
constant during contact establishment; subsequent references call it the centre of compliance.

Symbols follow the same rule. One point, one subscript: \(p_c\), \(r_c\),
\(K_c\), \(D_c\).

## Mathematical notation

**The global symbol list contains important recurring quantities, not every
temporary variable in a derivation.** A local axis--angle pair, an intermediate
matrix, a one-equation time bound, or a figure-only wrench projection is defined
beside its use and omitted from the list. Removing such an entry never removes
the symbol from the mathematics. The list retains the surface geometry,
input--condition--response chain, compliance-centre quantities, controller
matrices, and null-space quantities used across chapters.

At the first equation in which a new symbol appears, introduce it in the
surrounding running text by giving the quantity name, the symbol, and its short
role in that equation. The definition may appear immediately before or after
the equation, but the reader must not have to infer the symbol from the
expression alone. Do not repeat a definition that has already been established
unless the symbol is assigned a different local meaning.

**Do not introduce a second symbol for a quantity already defined.** Before a
new symbol is accepted, compare its physical quantity, reference point, frame,
sign, and evaluation instant with the existing notation. Reuse the established
symbol only when all five agree; matching units alone are insufficient. In
particular, two angular quantities are not interchangeable when one is a
surface-relative entry condition and the other is a controller tracking error
relative to its desired orientation. If the definitions differ, retain two
symbols and state the distinction once where they first meet.

Whenever running text names a defined mathematical quantity, place its symbol
immediately after that name. For example, write `the configured orientation
offset \(\theta_{\mathrm{offset}}\)` and `the commanded joint torque
\(\tau_{\mathrm{cmd}}\)`. This rule applies to repeated uses as well as to the
first definition. It does not apply to generic physical nouns that do not denote
a specific defined variable, or to an unambiguous pronoun or shortened reference
such as `this matrix` or `the value`.

**Reserve \(\tau_{\mathrm{cmd}}\) for the complete implemented command.** Use
\(\tau_{\mathrm{model}}\) for the general model-compensated balance that
includes an explicit gravity term, and \(\tau_{\mathrm{cmd,cart}}\) for the
implemented Cartesian-only command before the null-space contribution is
added. One symbol must not denote both the general balance and the complete
implemented command.

**A direction that exists in two frames carries the non-default frame in its
subscript.** The tool-face normal is \(n_{\mathrm{Tool,EE}}\) in
end-effector coordinates and \(n_{\mathrm{Tool}}\) in the base frame, with
\(n_{\mathrm{Tool}}=R_{\mathrm{EE}}n_{\mathrm{Tool,EE}}\). They are one
physical direction in two frames, and the suffix is what says which; its
absence says the base frame, under *No frame suffix means the base frame*
below.

This replaces \(n_{\mathrm{EE}}\) and \(n_T\), which were read as two different
quantities: \(n_{\mathrm{EE}}\) looked like a property of the end effector
rather than of the tool, and \(n_T\) named no frame at all. The longer form is
deliberate — it is harder to misread, and the pair \(n_{\mathrm{T,EE}}\) /
\(n_{\mathrm{T},0}\) was rejected for the same reason. `Tool` stays capitalised
and roman in both.

**The Tool Orientation transition quantities are
\(\theta_{\mathrm{app,err}}\) and \(\varepsilon_{\mathrm{app}}\).**
Agreed 2026-08-31. The tool-axis error and its configured tolerance take the
`app` subscript already carried by \(s_{\mathrm{app}}\),
\(v_{\mathrm{app}}\) and \(s_{\mathrm{app,max}}\), because all of them are
set by the one approach parameter group that Tool Orientation and Surface
Approach share. Section 3.3 defines both beside their use and Figure 3.3 states
the condition; as Chapter 3 transition quantities neither enters the global
symbol list.

**\(\theta_{\mathrm{align}}\) must not be used for them.** That symbol names
the withdrawn pose-based alignment consistency metric further down this file,
and reusing it for a live quantity would leave the withdrawal unenforceable and
put two different angles under one name.

**One typeface: plain italic.** Every symbol — scalars, vectors, and matrices
alike — is set plain: \(F\), \(f\), \(m\), \(e_p\), \(e_R\), \(p\), \(q\),
\(K\), \(D\), \(J\), \(R\), \(T\), \(N\). Do not use `\mathbf`.

**Show scalar multiplication with a centred dot in displayed calculations.**
Write \(K\mathbin{\cdot}e\) and
\(350\mathbin{\cdot}(-0.22923)\), rather than leaving the factors adjacent.
The cross product remains \(\times\), and established matrix products may
remain juxtaposed where a centred dot could be read as a vector inner product.

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

**Gains carry the surface frame they are diagonal in, as \(S\); the
base-frame forms carry nothing.** The
directional gains are defined along \([t_1,t_2,n_s]\) and are written
\(K_{p,S}=\operatorname{diag}(K_{p,t_1},K_{p,t_2},K_{p,n})\),
\(K_{R,S}\), \(D_{p,S}\) and \(D_{R,S}\); their base-frame representations take
no index at all, so \(K_p=R_{\mathrm{surface}}K_{p,S}
R_{\mathrm{surface}}^\top\). The chain the reader follows is *gains in surface
coordinates → \(R_{\mathrm{surface}}\) → gains in base coordinates*, and it is
stated once, in the sentence that introduces the two congruence transforms.

**\(a_s\) is withdrawn, with \(\tilde t_1\).** Both are written here as
literal strings so a rename cannot revive them. The first-tangent hint is
\(e_{x_0}\) in every reported experiment and Appendix C records it as
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
are specific to rotation about \(t_1\): every tested non-zero centre position
increased the response in one rotational direction and reduced it in the other
relative to the TCP-centred condition. That sentence is what bounds them. It is
a scientific commitment, not filler, and it is not dropped when the section is
shortened.

**The tool clearance is defined from physical corner positions.** For each
tool-face corner, Chapter 3 defines
\(p_i(t)=p_{\mathrm{TCP}}(t)+R_{\mathrm{EE}}(t)r_{i,\mathrm{EE}}\) and its
clearance \(h_i(t)=n_s^\top(p_i(t)-p_s)\). The minimum
\(h_{\mathrm{Tool}}(t)=\min_i h_i(t)\) is the clearance between the
rectangular tool face and the configured surface reference. Smaller values place a
corner closer to the surface. Do not interpose a separate projection or
extent notation between the corner position and this physical clearance.

The controller source compares the rotated corner offsets along the descent
direction. Chapter 3 states that this is equivalent to comparing \(h_i\),
because \(p_{\mathrm{TCP}}\) and \(p_s\) are common to all four corners. The
implementation bridge stays in prose; the discarded projection construction
is not shown as a second set of equations.

**The minimum clearance and the selected-point average have different jobs.**
The transition condition is
\(h_{\mathrm{Tool}}(t)\leq h_{\mathrm{clearance}}\), so
\(h_{\mathrm{Tool}}\) determines when approach ends. The selected index set
\(\mathcal I_{\mathrm{sel}}\) contains the corners satisfying
\(h_i-h_{\mathrm{Tool}}\leq\varepsilon_{\mathrm{sel}}\), where
\(\varepsilon_{\mathrm{sel}}\) is the **tool-point selection tolerance** and
\(N=\lvert\mathcal I_{\mathrm{sel}}\rvert\). Its mean
\(r_{\mathrm{Tool,EE}}=N^{-1}\sum_{i\in\mathcal I_{\mathrm{sel}}}
r_{i,\mathrm{EE}}\) determines which geometric tool point the contact-establishment reference
uses. Never use the normal coordinate of that averaged point as the minimum
tool clearance.

The List of Symbols carries separate rows for \(h_i\),
\(h_{\mathrm{Tool}}\), \(h_{\mathrm{clearance}}\) and
\(\varepsilon_{\mathrm{sel}}\). The calibrated-geometry table in Chapter 4
records the selection-tolerance value, and the phase-parameter table records
the tool-clearance value. Chapter 3 may repeat the reported
\(h_{\mathrm{clearance}}=0.020\,\mathrm{m}\) beside its physical
interpretation, with the table cross-reference: the closest part of the tool
face, rather than the TCP, is \(20\,\mathrm{mm}\) above the plane at the
transition.

**The one-, two- and four-corner outcomes are principal geometric cases, not an
exhaustive list for the implemented selector.** The finite selection tolerance
can place three corners in \(\mathcal I_{\mathrm{sel}}\) while excluding the
fourth. Chapter 3 therefore does not claim that a three-corner set is impossible
and does not derive an auxiliary three-scalar rectangular construction. It
presents the leading corner, leading-edge midpoint and tool-face centre as the
principal outcomes shown in the figure.

**The clearance index is spelled out, and `clr` is withdrawn** — written here
as a literal string so a rename cannot revive it. The compact form was tried
first and replaced on the author's instruction, for the reason that already
spelled out \(p_{\mathrm{Tool}}\) over \(p_T\): an abbreviated index costs
the reader a lookup on every equation it appears in, and these symbols appear
in six. At \(t_{\mathrm{CE,start}}\), the controller retains
\(R_{\mathrm{EE,clearance}}=R_{\mathrm{EE}}(t_{\mathrm{CE,start}})\),
\(p_{\mathrm{TCP,clearance}}=p_{\mathrm{TCP}}(t_{\mathrm{CE,start}})\), and
\(r_{\mathrm{Tool,EE}}\). The selected tool point at that instant is
\(p_{\mathrm{Tool,clearance}}=p_{\mathrm{TCP,clearance}}
+R_{\mathrm{EE,clearance}}r_{\mathrm{Tool,EE}}\).
Its projection onto the configured surface reference is \(p_{\mathrm{Tool},0}\), from
which the contact-establishment reference is generated. During contact establishment the orientation
reference is \(R_d(t)=R_{\mathrm{EE,clearance}}\).

**\(p_{\mathrm{Tool},0}\) is the surface reference point, not a starting
reference.** `starting reference` is withdrawn, written here as a literal
string so a rename cannot revive it: the first commanded contact-establishment position is
\(p_{\mathrm{Tool,clearance}}\), which the initial value of
\(s_{\mathrm{CE}}\) is chosen to reproduce, so calling the projected point
the starting reference contradicts the equation two lines below it. The settled
sentence is that the orthogonal projection *defines the surface reference
point* \(p_{\mathrm{Tool},0}\), followed by the statement that it is the
point on the configured reference plane directly below the selected tool point at the
clearance transition. The symbol-list row says the same in fewer words: its
projection onto the configured surface reference.

**The clearance criterion is explained once, after
\(h_{\mathrm{Tool}}(t)\leq h_{\mathrm{clearance}}\), in four sentences.**
The approach trajectory is generated for the TCP whereas the transition is
determined from the physical tool geometry; because
\(h_{\mathrm{Tool}}\) is the minimum clearance of the four corners,
\(h_{\mathrm{clearance}}\) refers to the part of the face closest to the
plane rather than to the TCP; at the reported
\(0.020\,\mathrm{m}\) that part of the face is \(20\,\mathrm{mm}\)
above the plane at the transition; and the criterion therefore gives the same
specified clearance for different tool orientations and is purely geometric.
The passage before the corner equations no longer repeats the TCP contrast —
it states only that a corner can lie well below the TCP when the face is not
parallel to the surface, which is why the four corners are evaluated. The orientation symbol
carries the frame as well as the instant, matching
\(p_{\mathrm{TCP,clearance}}\) beside it. Subsequent prose says that the
offset is retained or held constant; it does not build a name from the state of
the quantity.

**The base-frame unit axes carry the base-frame index:** \(e_{x_0}\),
\(e_{y_0}\), and \(e_{z_0}\).
Section 2.1 names the base axes \(x_0\), \(y_0\), \(z_0\), so their unit
vectors carry the same index. Chapter 4 and the parameter appendix used bare
`e_x` and `e_z` for the same vectors until 2026-08-26; both were harmonised,
along with the \(n_s=R_{\mathrm{EE}}e_{z_0}\) box in Figure 4.2, and the
symbol list retains only \(e_{x_0}\) and \(e_{z_0}\), which recur in the
document. The unused \(e_{y_0}\) entry is omitted.

**Section 2.6 is settled, and its shape is deliberate.** Agreed 2026-08-26:
the section opens by saying *why* the frames differ — the impedance law is
evaluated in the base frame while the gain values are specified relative to the
configured surface reference, because the directions that matter for contact are
\(t_1\), \(t_2\) and \(n_s\). Then, in order: the four surface-frame
matrices, the axis order in one sentence, the two congruence transforms into
the base frame, the block-diagonal \(K\) and \(D\), and a forward
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

**Do not attach `task` to inertia, stiffness, or damping in thesis-facing prose
or notation.** The surface-resolved operational-space inertia is
\(\Lambda_S(q)\), and \(\lambda_i(q)\) is its directional entry. Each
controller state or configuration supplies the active stiffness entry
\(k_i\); the common damping rule then gives \(d_i(q)\). `Task-inertia`,
\(\Lambda_{\mathrm{task}}\), and corresponding stiffness or damping names are
withdrawn. Literal source identifiers remain unchanged inside listings.

### The frame index appears only where frames are compared or transformed

**When a frame index is shown it is a lower index, and there are three of
them:**

\[
(\cdot)_0=\text{base coordinates},\qquad
(\cdot)_S=\text{surface coordinates},\qquad
(\cdot)_{\mathrm{EE}}=\text{end-effector coordinates}.
\]

**No frame suffix means the base frame.** Agreed 2026-09-01, replacing the
earlier rule that wrote \(0\) wherever two frames were being compared. Every
Cartesian vector, orientation, velocity, wrench, Jacobian, and stiffness or
damping matrix is expressed in \(\{0\}\) unless it says otherwise, and the
base-frame index is never written. Only \(S\) and \(\mathrm{EE}\) appear:

\[
r_c=R_{\mathrm{surface}}r_{c,S}
\qquad\text{and}\qquad
r_c=R_{\mathrm{EE}}r_{c,\mathrm{EE}}.
\]

**\(R_{\mathrm{surface}}\) is expanded once.** Agreed 2026-09-02. The
definition \(R_{\mathrm{surface}}=[\,t_1\ t_2\ n_s\,]\) belongs at the equation
in Section 2.5 that introduces the surface frame. Later sections write
\(R_{\mathrm{surface}}\) and cross-reference that equation; they do not restate
the column expansion unless the individual components are carried through the
local derivation, as they are where \(r_c\) is resolved into
\(r_{c,t_1}t_1+r_{c,t_2}t_2+r_{c,n}n_s\). Two restatements were removed on that
date: an unnumbered display two lines below the defining equation, which gave
the coordinate order by repeating the matrix rather than by naming it, and an
opening clause in Section 2.7.2 that reopened the definition before the
compliance-centre transformation. A matrix restated a third time reads as
though it were being defined again.

The earlier rule was self-defeating. It kept \(0\) on the quantities that
happened to appear beside a surface-frame twin — \(r_{c,0}\),
\(K_{p,0}\), \(\Lambda_0\), \(\Delta R_0\), \(\gamma_0\) — while
\(e_p\), \(e_R\), \(f\), \(m\), \(n_s\), \(t_1\) and \(t_2\)
carried no index at all, although all of them are base-frame quantities too.
A reader met two conventions in one equation. **These forms are withdrawn**,
written here as literal strings so a rename cannot revive them: `\Delta R_0`,
`K_{p,0}`, `D_{p,0}`, `K_{R,0}`, `D_{R,0}`, `K_0`, `D_0`, `\Lambda_0`,
`r_{c,0}`, `n_{\mathrm{Tool},0}`, `\gamma_0`.

**A suffix that names a point or a body is not a frame suffix.** In
\(p_{\mathrm{EE}}\) the index says whose position is given, and that
position is in the base frame; in \(r_{c,\mathrm{EE}}\) the index after the
comma says which coordinate frame the components are in. Chapter 2 states this
distinction in its opening, because it is the one place the convention can be
misread.

**Do not run this as a substitution.** Three families of index look like a
base-frame index and are not: the base *axis* names \(e_{x_0}\),
\(e_{y_0}\), \(e_{z_0}\), \(x_0\), \(y_0\), \(z_0\); the *initial*
or *reference* values \(\theta_{0,t_1}\), \(\phi_0\), \(u_0\),
\(t_{\mathrm{app},0}\), \(\Delta q_{\mathrm{null},0}\); and
\(p_{\mathrm{Tool},0}\), whose \(0\) is the zero of the
contact-establishment coordinate \(s_{\mathrm{CE}}\), not a frame. The last
of these sits one line from \(n_{\mathrm{Tool},0}\), which *was* a frame
index and was removed. Convert occurrence by occurrence and check the counts,
per *Never normalise notation with a bulk regex* below.

**\(\Lambda_S\) and the four surface-frame gain matrices keep their
suffix**, because they are genuinely the non-default representation:
\(K_{p,S}\), \(D_{p,S}\), \(K_{R,S}\), \(D_{R,S}\), \(r_{c,S}\),
\(r_{c,\mathrm{EE}}\), \(n_{\mathrm{Tool,EE}}\) and
\(r_{\mathrm{Tool,EE}}\) are all unchanged.

**The superscript form \(r_c^{S}\) is withdrawn**, written here as a literal
string so a rename cannot revive it. It mixed two things in one expression —
the coordinates of the displacement in the surface frame, and the
transformation of those coordinates into the base frame — and it put the frame
index above the line where the rest of the thesis puts it below. The surface
coordinates are \(r_{c,S}=[\,r_{c,t_1},\;r_{c,t_2},\;r_{c,n}\,]^\top\), with
the inverse \(r_{c,S}=R_{\mathrm{surface}}^\top r_c\) available where a
base-frame vector has to be resolved.

**The tangential vector stays \(r_{c,t}\).** `r_{c,t,0}` is written here as a
literal string so a rename cannot revive it: a triple index is hard to read,
and \(\lVert r_{c,t}\rVert\) is frame independent and would carry no index
anyway, so indexing the vector alone would split a pair that belongs together.
The scalar components \(r_{c,t_1}\), \(r_{c,t_2}\) and \(r_{c,n}\) are
unchanged for the same reason — they are positive or negative surface-frame coordinates and
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
bibliography was brought into line with it on 2026-08-25 in `Thesis.tex`:

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
bulk, compile `Thesis.tex` immediately afterwards, and diff the set of
`\macro` tokens against the previous commit — any token that is new is a merge.

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

The block rotation
\(T_R=\operatorname{diag}(R_{\mathrm{surface}},R_{\mathrm{surface}})\)
remains local to the inertia-scaled-damping derivation and has no global
symbol-list entry. The global list names only the response component
\(\gamma_{t_1}\) evaluated in the reported contact study. Other components
remain local to generic surface-frame relations where they are mathematically
required.

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
  contact establishment`, not the parameter name that sets it;
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
orientation`, `the controller forms`, `during contact establishment`, `while the press
continues`.

Use `elapsed time` for the seconds since an experiment started. Preserve a
different label only when it is the exact name of a logged field or literal
software identifier.

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
- **Which duration.** A \(4.0\,\mathrm{s}\) contact-establishment timeout was stated in three
  places in the methodology chapter. Every completed experiment used
  \(5.0\,\mathrm{s}\); the \(4.0\,\mathrm{s}\) figure matched no parameter file.
- **Which plane.** The implementation chapter gave the active baseline surface
  point and tilt angles as \(p_s=(0.526,0.017,0.002)\,\mathrm{m}\),
  \(a=-0.474^\circ\), \(b=2.270^\circ\), which appear in no parameter file,
  no calibration overlay, and no experiment record. The configured reference plane is
  \(p_s=(0.5153,-0.1072,0.0031)\,\mathrm{m}\), \(a=-1.585^\circ\),
  \(b=+0.988^\circ\), used throughout the campaign.
- **Which procedure.** The physical plane comes from **one seated pose of the
  complete tool face**, as `tools/measure_plane.cpp` performs it. The plane
  normal is the *configured* end-effector axis carried into the base frame, and
  for the stored plane that axis was the **nominal \(+Z_{\mathrm{EE}}\)**:
  the plane was calibrated before the tool normal and was never measured again
  afterwards, so \(n_s=R_{\mathrm{EE}}[0,0,1]^\top\) and **not**
  \(n_s=R_{\mathrm{EE}}n_{\mathrm{EE}}\), which this guide asserted until
  2026-08-24. The two differ by the \(1.56^\circ\) between the calibrated tool
  normal and \(+Z_{\mathrm{EE}}\), and Section 4.2.1 states that difference as a
  calibration offset common to every reported experiment. The plane point is the
  tool-face centre of that same pose,
  \(p_s=p_{\mathrm{EE}}+R_{\mathrm{EE}}r_{\mathrm{face,EE}}\). The repository
  contains no plane-fitting routine of any kind. The **tool-normal seatings**
  are a separate
  calibration and measure the tool, not the surface. The controller holds only
  the configured plane, set from the tilt angles \(a\) and \(b\), and contains
  no calibration routine at all — the calibration tools are separate
  executables — so any sentence implying the controller measured the surface is
  wrong by construction.

  **Section 4.2 states what each calibration supplied.** The seated-pose
  calibration defined \(p_s\), \(n_s\) and
  \(R_{\mathrm{surface}}\) for the controller. The yaw-capture calibration
  defined \(n_{\mathrm{Tool,EE}}\) for the pose-based angular evaluation. The
  controller retained the surface reference from the seated-pose calibration,
  and the \(1.56^\circ\) value states the common difference between the two
  orientation references. Section 6.2.2 carries the consequence for physical
  tool--surface-angle interpretation.

**Rule.** A number or configuration fact has one home — the methodology chapter
or the parameter appendix — and every other mention cross-references it rather
than restating it from memory. Before submitting, grep each key value across all
chapters and confirm a single answer.

## What belongs in the thesis at all

**State the levels actually tested, never an illustrative sweep.** Section 4.4.4
carried a generic five-level scaling \(\alpha\in\{0.5,0.75,1,1.25,1.5\}\) and
then spent a paragraph explaining that this was *not* what was executed. A
hypothetical set up only to be dismissed wastes the reader and invites the
question of which numbers are real. Give the tested values: \(5\), \(15\) and
\(50\,\mathrm{N\,m/rad}\); \(300\), \(800\) and \(2000\,\mathrm{N/m}\).

**Separate theory from configuration.** Chapter 2 carries the law and its
assumptions; Chapter 3 carries what was built and which options were selected.
An enumeration of selectable software modes is a control-design decision, not
theory — the four null-space modes moved out of Chapter 2 for that reason, and
the theory chapter now gives one complete null-space torque instead. The same
split applies to limitations: mathematical properties of a method stay with the
method, while evidence gaps and implementation shortcomings are consolidated
in Section 6.2.

**Tooling built only for your own analysis is not thesis content.** A second
diagnostic log existed to support offline inspection and appeared in three
chapters and two appendices before being removed. If a facility did not
contribute to a reported result, it does not need documenting. The same applies
to exception handling, persistence ordering, and any other detail that matters
only when debugging an experiment.

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
subsequent output chain — none of which is a mathematical relation — while
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
\section{Surface-Contact Sequence}
  \subsection{Surface Frame, Tool Reference, and Tool Geometry}
  \subsection{Tool Orientation}
  \subsection{Surface Approach, Clearance and Tool-Point Selection}
  \subsection{Operator-Controlled Hold Before Contact Establishment}
  \subsection{Contact Establishment}
  \subsection{Operator-Controlled Hold Before Grinding}
  \subsection{Grinding}
\section{Cartesian Pose Hold}
\section{Robot-Side Safety and Command Handling}
\section{Real-Time Data Recording}
```

**One register at a time.** Agreed 2026-09-01, after a read found the
chapter hard to follow because its prose alternated between five things: what
the controller is intended to do, how the software implements it, which
keyboard input the operator uses, which configuration the experiments used, and
material already derived in Chapter 2. The opening of Section 3.2 carried all
five in one paragraph. It is now four: the state path, the transitions, the
Manual Guidance interaction, and the Contact-Impedance Hold tuning loop.

**Capability first, then the configuration the experiments used.** Where the
controller supports alternatives, state both, then say which was used, in that
order and in separate sentences. The tool-fixed and surface-fixed compliance-
centre definitions are the standing example: both are described, and the
sentence after them says that all non-zero displacements used in the
experiments were tool-fixed.

**Name the actor and the instant.** `Figure 3.2 presents one callback as a
closed Cartesian feedback loop` became `shows the computations performed during
one real-time control cycle`; `The desired orientation \(R_d\) remains the
reference of the impedance law` became `During Contact Establishment, the
controller keeps \(R_d\) fixed at the orientation captured at the clearance
transition`. An abstract grammatical subject leaves the reader to work out who
acts and when.

**`branch` and `mask` are not used.** Withdrawn 2026-09-02, replacing the
earlier rule that required the names `TCP-centred branch` and
`\abbr{CoC}-shifted branch`. Both words describe the source rather than the
control law: a `branch` is a path through code, and a `mask` is the array that
implements the selection. Say where the impedance is defined —
`the impedance is defined either directly at the TCP or about a displaced
virtual \abbr{CoC}` — and, for the rotational selection, say what reaches the
spring term: `\(e_R\) is resolved in the surface frame so that only the
selected rotational components contribute to the rotational spring term`. Four
uses were rewritten on that date, in Sections 3.1, 3.2.5 and 3.2.7 and in
Appendix A.

**Keep forward references to a minimum.** Agreed 2026-09-02. Cite a later
chapter only where the current section cannot be understood without it, not to
advertise that a value or a procedure appears later. Chapter 3 states how the
controller is implemented; the settings compared in an experiment, their
numerical values, the virtual disturbance and the evaluated quantities belong
in Chapter 4, and a Chapter 3 paragraph that lists them is removed rather than
cross-referenced. The Section 3.3 paragraph naming the four pose-hold settings
was deleted on that date for this reason.

**Delete a sentence that restates its predecessor.** Two were removed on
2026-09-01: `This validation enforces exclusive selection between the two
definitions`, after the sentence stating that the loader requires exactly one
definition; and `Cartesian pose hold captures these references directly at
state entry`, after the sentence giving the capture.

**A state name is a proper noun.** Tool Orientation, Surface Approach,
Pre-Contact Hold, Contact Establishment, Pre-Grinding Hold, Grinding, Cartesian
Pose Hold, Contact-Impedance Hold and Manual Guidance are capitalised wherever
they name the runtime state, including in captions. Lower case is reserved for
the generic physical process, as in `the approach direction` or `different tool
orientations`.

**The chapter follows one controller into its two configurations.** Section 3.1
ends by naming the surface-contact sequence and Cartesian pose hold as two
configurations of the same callback. Section 3.2 then completes the entire
surface-contact account in execution order before Section 3.3 introduces pose
hold. Common safety and recording follow both. Do not introduce both
configurations and then leave them while geometry or state machinery is
explained elsewhere.

**State-dependent impedance is not an independent section ahead of the
sequence.** The contact reference is generated first in `Contact Establishment`.
Directional stiffness, inertia-scaled damping and the virtual-centre point shift
then state which impedance acts on it. The pose-hold gain facts belong only in
`Cartesian Pose Hold`.

**The two controller flow charts come before the implementation equations.**
The operating-state chart begins with Robot Recovery and Controller Selection,
then branches to the surface-contact sequence, Cartesian Pose Hold,
Contact-Impedance Hold and Manual Guidance. A shared red path states every condition that ends an
active controller state. The detailed surface-contact chart then shows Tool
Orientation, Surface Approach, the optional Operator-Controlled Hold Before
Contact Establishment, Contact Establishment,
Operator-Controlled Hold Before Grinding and Grinding in execution order. It
shows one blue `Move to Stored \(q_{\mathrm{init}}\)` box leading into Tool
Orientation on an arrow reading `\(q_{\mathrm{init}}\) reached`. The former
`Initial Configuration` box is withdrawn. That the robot may instead start from
the current \(q\) after input `g` enters Manual Guidance is stated in the body
text and is not drawn. Input `q` there
stores the current configuration as \(q_{\mathrm{init}}\) for a later session.
During active control, input `g` enters Manual Guidance. Input `p` recaptures
the reached pose and restarts the originating controller configuration. The
surface-contact sequence restarts at Tool Orientation; ordinary Cartesian Pose
Hold and Contact-Impedance Hold recapture the reached pose as their held
reference. Input `p` is not a start command.

Contact-Impedance Hold is drawn as a state, in the same capsule as the
sequence states, and is connected to the contact sequence. Input `t` enters it from the sequence, and input `s` restarts the
sequence at Tool Orientation after \(K_p\), \(K_R\), or \(r_c\) is set.

**A controller flow chart is a state machine with only the required experiment
orchestration shown around it.** Every black rounded capsule is an operating or
controller state. Blue rectangular boxes distinguish controller initialisation
and selectable configurations from those states. Box text stays short and never becomes a sentence or
paragraph. Every arrow states a compact `if` condition and
uses the thesis symbols where they are defined. Place that condition beside a
clear segment, never over an arrow or a box border. The Tool Orientation arrow
uses the compact display condition \(\theta_{\mathrm{app,err}}\leq
\varepsilon_{\mathrm{app}}\lor 8.0\,\mathrm{s}\) `timeout`, while the
body text retains the complete minimum-time and orientation logic. A
disjunction in a chart condition is written \(\lor\) and never as the word
`or`, matching the shared stop condition. The earlier
worded form `angular error within tolerance` is withdrawn: the arrow states the
thesis symbols, and Section 3.3 defines the tool-axis error
\(\theta_{\mathrm{app,err}}\) and its configured tolerance
\(\varepsilon_{\mathrm{app}}\) beside their use. Both are Chapter 3
transition quantities and stay out of the global symbol list, under
*Mathematical notation*. Surface Approach advances at
\(h_{\mathrm{Tool}}\leq h_{\mathrm{clearance}}\) and stops if
\(s_{\mathrm{app}}\geq s_{\mathrm{app,max}}\) first. The Contact Establishment
arrow uses `5.0 s timeout`, while the body text retains the
complete minimum-time, moment-change and timeout logic. Every reported
experiment ended through the timeout. These state-specific phrases prevent one
time symbol from denoting two independent timeout values.
The optional holds remain on the single main path so that the state sequence is
immediately readable. Do not draw or label separate `hold enabled` and `hold
disabled` branches. A disabled hold advances without waiting, while operator
confirmation releases an enabled hold to the following state. Grinding is shown because it is
implemented, not because it was entered experimentally, and the chart does not
mark where the campaign stopped: that is a result, and the body text carries
it.

Use the suffix `end`, never `out`, for any visible time variable that marks the
end of a state or measured interval. Keep `start` for the beginning of an
interval and `max` for a genuine upper bound. Literal software identifiers that
contain `timeout` remain unchanged.

After \(h_{\mathrm{Tool}}\leq h_{\mathrm{clearance}}\), the displayed main path
enters Pre-Contact Hold and continues to Contact Establishment after operator
confirmation. After Contact Establishment ends, the displayed path enters
Pre-Grinding Hold and continues to Grinding after confirmation. The body text,
not extra bypass arrows, explains that a disabled hold advances without a wait.

Do not call a stiffness-and-damping configuration a `state group`. State the
configuration directly and say when it is activated. For the reported
surface-contact experiments, name Surface Approach and Contact Establishment
as the states that used inertia-scaled damping.

**Termination is shared rather than repeated as prose beside every state.**
Operator stop, the configured experiment-duration limit, a robot-side error or reflex,
and communication or control exceptions lead from every active state to the
red Stop state. Recovery failure also leads to Stop before a controller is
selected.

The shared chart label contains only `stop requested` and `robot error/reflex`.
The configured experiment-duration limit and communication or control exceptions stay
in the body text rather than lengthening the diagram. The program-level stop
rail descends through the centre into Stop. Its short condition sits beside
that vertical path and never interrupts it. A robot error or reflex is any
robot-side stop condition reported by libfranka and is not restricted to a
joint-limit violation.

**Static definitions precede one chronological runtime account.** `Surface and
Tool Reference` defines the surface frame, the commanded tool orientation and
the four rectangular tool-face corners, and stops there. Use `corner` and
`corners`, never `vertex` or `vertices`, for that rectangle in visible prose and
figures. The corner positions, clearances, minimum tool clearance,
selected index set and selected tool point belong together in `Surface Approach, Clearance and
Tool-Point Selection`. `Contact Establishment` then carries the clearance capture,
surface projection, initial contact-establishment coordinate,
contact-establishment trajectory,
retained orientation, TCP reconstruction and active impedance, in that order.

**The sign convention of \(s_{\mathrm{CE}}\) is stated before the ramp.**
The coordinate specifies the desired tool-point position along \(-n_s\)
relative to the configured reference plane: negative above the plane, zero on
it, positive below it. Its initial value is negative, which is why calling it a
`commanded displacement towards the surface` misled -- a displacement towards
something does not start negative. State the convention, then the initial
value, then the ramp. Say also that the configured endpoint below the plane is
a **virtual spring reference**, not an expected physical penetration depth.

**Say why the TCP reference is reconstructed.** The controller defines the
selected tool point's trajectory first and calculates the corresponding TCP
reference from it; contact then prevents the tool from following the commanded
reference below the surface, and the resulting position error generates the
commanded pressing force. The mechanism, not just the algebra, belongs beside
the equations.

**Approach and contact establishment are written in the same shape.** Each state carries a
scalar coordinate: \(s_{\mathrm{app}}(t)\) advances the TCP from the captured
\(p_{\mathrm{TCP,start}}\), and \(s_{\mathrm{CE}}(t)\) advances the
selected tool point from \(p_{\mathrm{Tool},0}\). Each is followed by the
position reference it produces —
\(p_d(t)=p_{\mathrm{TCP,start}}-s_{\mathrm{app}}(t)n_s\), and
\(p_{\mathrm{Tool},d}(t)\) with its reconstructed \(p_d(t)\). The parallel
is deliberate: the approach motion was previously described in words while
contact establishment carried a trajectory, which left the tool-point selection reading as
geometry that appeared from nowhere.

Visible quantities associated with Contact Establishment use the subscript
\(\mathrm{CE}\), including \(s_{\mathrm{CE}}\), \(t_{\mathrm{CE}}\),
\(R_{\mathrm{CE}}\), \(u_{\mathrm{CE}}\), and \(\phi_{\mathrm{CE}}\).
The older set form remains only in literal software keys and internal source
labels where renaming it would obscure traceability.

**An evaluation instant is named by its symbol, not described in words.**
Agreed 2026-09-02. Once \(t_{\mathrm{CE,start}}\) and
\(t_{\mathrm{CE,end}}\) are defined in a subsection, every later reference
uses them: write \(\gamma=\phi_{\mathrm{CE}}u_{\mathrm{CE}}=e_R(t_{\mathrm{CE,end}})\),
not \(e_R\big|_{\text{end of Contact Establishment}}\). A worded subscript
is longer, sets prose inside mathematics, and leaves the reader to check that
it means the instant already defined a few lines above.

**Say which quantities in a comparison are fixed.** Agreed 2026-09-02 for the
achieved initial angular offset. \(n_s\) is the configured surface normal and
does not change during a trial, so the subsection states that it is fixed and
is *not* a surface normal evaluated at \(t_{\mathrm{CE,start}}\), and that
the time dependence enters through the measured tool orientation. Without that
sentence, \(n_{\mathrm{Tool}}(t_{\mathrm{CE,start}})\) beside \(-n_s\)
reads as though both were sampled at the same instant, which would make the
offset a measurement of the physical plate rather than of the commanded
reference. The same subsection also gives the achieved tool-normal direction
its own equation, \(n_{\mathrm{Tool}}(t_{\mathrm{CE,start}})=R_{\mathrm{EE}}(t_{\mathrm{CE,start}})n_{\mathrm{Tool,EE}}\),
rather than asserting it in a clause, so the measured input to the comparison
is visible.

**The approach coordinate uses the same piecewise presentation as the contact-establishment
coordinate.** It advances at \(v_{\mathrm{app}}\) from
\(t_{\mathrm{app},0}\) until \(t_{\mathrm{app,max}}\), the instant at which
the configured distance \(s_{\mathrm{app,max}}\) is reached, and then remains
at that distance. The distance is the configured limit; the instant is the
derived endpoint of its ramp. The desired velocity
\(\dot p_d=-v_{\mathrm{app}}n_s\) applies only during the linear approach.
Reaching \(s_{\mathrm{app,max}}\) before the clearance criterion terminates the
approach as unsuccessful; do not describe the descent velocity as active for
the whole state.

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
| A standalone \(\tau_{\mathrm{cart}}=J^\top F\) | Equation 2.69 within the complete torque command |
| \(G_0=R_{\mathrm{surface}}G_{\mathrm{surface}}R_{\mathrm{surface}}^\top\) | Section 2.6 |
| Why a displaced centre produces an aligning moment | Section 2.7, and Chapter 5 for the measurement |
| The null-space projector, damping and conditioning derivations | Section 2.8 |
| \(M(q)Y(q)=J^\top(q)\), \(Y=M^{-1}J^\top\), \(\Lambda=(JY+\varepsilon I)^{-1}\) | reduced to one sentence; the damping implementation is not a contribution of this thesis |

**The nominal controller equation is defined once in Chapter 2.** Chapter 3
references Equation 2.69 rather than repeating
\(\tau_{\mathrm{cmd}}=J^\top(q)F+\tau_{\mathrm{null}}+\tau_c(q,\dot q)\).
The disturbance is an experimental input rather than part of the controller,
so its definition belongs to Section 4.6 alone, where
\(\tau_{\mathrm{dist}}(t)=J_p(q(t))^\top f_d(t)\) already stands. Chapter 3
carries one sentence saying an experiment-specific disturbance torque is added
only for the null-space pose-hold experiment. It does not appear in the
Cartesian pose-hold account either.

**What Chapter 3 must keep**, because these are what was designed rather than
what was derived: the architecture figure; the configured surface-relative
offset \(\theta_{\mathrm{offset}}=\theta_{\mathrm{offset},t_1}t_1+
\theta_{\mathrm{offset},t_2}t_2\) and the
inward normal it rotates; the tool geometry and the selection of
\(p_{\mathrm{Tool}}\); the tool-fixed against surface-fixed compliance-centre
definition; the contact-establishment reference generation, with
\(p_{\mathrm{Tool},d}(t)\) and the reconstructed \(p_d(t)\); the statement that
the orientation captured at the clearance transition is held throughout
Contact Establishment; the \abbr{SVD} details that differ from the theory; and the
real-time-safe recording.

**The point-shift equations are not repeated in Chapter 3.** The implementation
account references Equations 2.39 and 2.40, then states how tool-fixed and
surface-fixed displacements affect their callback update. One sentence says
that the point-shifted impedance lets the commanded normal press contribute to
the rotational response and sends the measurement to Chapter 5. Do not
re-argue the cross terms there.

**A derived controller relation has one canonical equation.** The complete
commanded-moment decomposition, projected null-space velocity, null-space
damping law, surface-frame construction and compliance-lever direction rule
are written as equations in the theory chapter. Later chapters and appendices
cite those equations and state only the term or consequence needed locally.
Figures do not repeat the full relations.

**The Grinding state gets two sentences and no more.** No reported experiment entered
it, so the chapter states that it maintains the normal contact-establishment
reference while superimposing tangential motion with the decoupled impedance.
The preceding hold subsection states that every reported experiment ended there.

**Section 3.2.5 is subdivided by unnumbered `\paragraph` headings.** Agreed
2026-09-01. The subsection had run reference generation, active impedance, gain
transformation, inertia-scaled damping, the two compliance-centre definitions
and the termination condition together as one uninterrupted explanation. The
five headings are `Reference capture and press trajectory`, `Active impedance`,
`Inertia-scaled damping`, `Centre-of-compliance implementation`, and
`Termination`. They are unnumbered, so the section and equation numbering are
unchanged. A `\label{}` that another chapter cross-references must sit on the
subsection, not inside one of these paragraphs: `sec:self_alignment_virtual_center`
is referenced from Chapter 2 and would otherwise print the wrong reference
type.

**The Contact Establishment subsection stays detailed.** It is the one place that explains
something Chapter 2 does not: how the reference is generated during contact.
The sentence that the rotational reference is held while finite rotational
compliance permits contact-induced end-effector rotation is the load-bearing
one, because it establishes that the measured rotation was not commanded by an
orientation trajectory.

**Scope the start of Contact Establishment to the optional pre-contact hold.** In the reported
surface-contact experiments that hold was disabled, so
\(t_{\mathrm{CE,start}}\) is the clearance-transition instant and Contact Establishment begins
there directly. State that scope before the clearance-capture equations. The
generic optional-hold behaviour remains one later sentence: with the hold
enabled, the pose is held until operator confirmation and the contact-establishment references
are captured from the current measured state.

**There is no standalone null-space implementation section.** Cartesian pose
hold states its fixed pose reference and hold impedance, names the four
selectable secondary-torque modes, and says which settings the experiment
compared. It then keeps only the bridge the theory does not fix: the relative
tolerance scaled by the largest current singular value, numerical
symmetrisation of the projector, reuse of that matrix for the logged
\(\dot q_{\mathrm{null}}\), and the sign selection from
\(q\pm\alpha_{\mathrm{probe}}v_7\) with its deadband. Do not restore the
null-space torque equation. Keep the four-mode diagram inside `Cartesian Pose
Hold`. Its common path starts from one `Move to Stored
\(q_{\mathrm{init}}\)` box, the `Initial Configuration` box having been
withdrawn. That operator input `h` in Manual Guidance starts pose hold from the
current \(q\) is stated in the body text and is not drawn. Runtime `g` leaves
Cartesian Pose Hold for Manual Guidance, and `p` returns through capture of the
reached pose. The path then captures the
current end-effector pose and enters the hold. Operator inputs 0, 1, 2, and 3 select no null-space
torque, projected damping, singular-value conditioning, and both terms
together, respectively. A new number switches directly from any active mode
to another. Show \(d_{\mathrm{null}}\) as adjustable in modes 1 and 3, and
\(k_\sigma\) as adjustable in modes 2 and 3. These are selectable software
modes rather than a temporal sequence or the four settings compared in the
pose-hold experiment. The surface-contact sequence held one combined setting,
so the secondary controller was not a variable there.

**Safety and data recording are two sections, not one miscellany.** The former
`Real-Time Operation, Safety, and Data Recording` covered connection setup,
error recovery, collision configuration, validation, the gripper, buffer
allocation, operator input, the start posture, exception handling, saturation
and logging, which is why it read as a list rather than a section.

`Robot-Side Safety and Command Handling` now carries only what bears on
commanding torque to a physical robot: the command is returned directly, no
application-side saturation or torque-rate limiter follows the assembly, the
robot-side collision and reflex monitoring is therefore the independent
protection layer, its thresholds live in Chapter 4, and a libfranka exception
ends the session. Everything the robot needs before torque control is one
sentence, and the keyboard thread is not described again — Section 3.1 has the
architecture.

`Real-Time Data Recording` carries the implementation claim the results depend
on: a preallocated in-memory ring buffer, no file access inside the callback,
bounded memory when the capacity wraps, and the chronological write after
control stops. The column-level description stays in the data-format appendix.

**Chapter 3 carries no tables and no `robot.control` listing, and must not
regain them.** Four went, each for a stated reason: Table 3.1 documented
functional subsystems the architecture figure already carries; Table 3.3 listed
the four null-space modes, which one sentence states; Table 3.4 listed logged
signals, which belong in the data-format appendix; and Table 3.2 said only that
surface-related states express gains relative to the configured surface
reference, that pose hold uses the base frame, and that the contact
establishment translational frame is configurable, all of which the prose now
says. The `robot.control` listing showed nothing the prose does not.

The chapter came out shorter and stronger, which is the test any future
addition to it has to meet.

### Chapter 4 structure

The division of labour is: **Chapter 3 is mechanism and implementation,
Chapter 4 is the physical setup, the settings actually used, the test matrix
and the evaluation method, and the appendices hold the exhaustive
configuration.** That rule is live and governs anything added to either
chapter.

**The compression it called for has been carried out**, so the section-by-section
list below is a record of what was done and why, not a pending worklist. Read
it as the reasoning behind the chapter's present shape; an instruction to
delete something already deleted will otherwise send the next reader hunting
for a table that is not there. Chapter 4 no longer re-explains the controller,
no longer repeats settings in both prose and tables, and no longer restates
values Appendix C carries.

Section by section, as executed:

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
  state sequence; state that the experiments followed the sequence of Chapter 3, give
  the settings in the existing state-parameter table, and add that the
  orientation reached at clearance was retained through Contact Establishment,
  the optional pre-contact hold was disabled and the pre-grinding hold enabled. **A table replaces
  repetition; it is not followed by paragraphs restating its rows.** Give the
  common gains as one table of directional entries with the damping rule, and
  leave the fallback damping matrices to Appendix C. Fold the null-space
  configuration into that table as three rows plus one sentence saying it was
  held fixed so it did not become a variable.
- **Data recording.** Do not list the signals a third time. One sentence
  pointing at Chapter 3 and the data-format appendix. What stays is the data
  quality: three trials per retained setting, 57 reported surface-contact
  trials over 19 settings, and all three trials retained within each
  reported setting.
- **Case matrix.** The cases had been explained three times — a grouping
  table, a prose walk-through, and the master table. The grouping table was
  deleted, leaving one paragraph naming the effects being separated, then the
  master table, then prose only for the cases that need interpretation. Do not
  reintroduce a second case table.
- **Experimental condition and response quantity.** Keep one
  input--condition--response chain: the configured pre-contact input
  \(\theta_{\mathrm{offset},t_1}\) produces the achieved pose-based condition
  \(\theta_{0,t_1}\), and Contact Establishment produces the measured response
  \(\gamma_{t_1}\). Appendix D retains the Case A--D numerical values.
  Define wrench projections locally beside the Case-D mechanism figure rather
  than as a separate methodology subsection. **Remove the mean and sample
  standard-deviation equations** and say instead that repeated settings are
  reported by their arithmetic mean and sample standard deviation.

### Chapter 4, settled after the compression pass

The chapter's purpose is: what hardware and geometry were used, how they were
calibrated, what was held constant, what was varied, and how the results were
calculated. Four rules keep it there.

**State what a quantity means experimentally before defining it
mathematically.** Agreed 2026-09-01, after a read found the difficulty in
Chapter 4 concentrated in Sections 4.2, 4.5 and 4.6, all for the same reason:
the definition arrived before the reason for it. Each of the three was
reordered rather than reworded. Section 4.2.1 now says that the procedure
constructs the configured reference from the nominal end-effector direction
before giving the construction. Section 4.6.2 says what the force direction is
chosen to excite before Equation 4.7 defines it. Section 4.6.3 says what each
motion quantity answers -- was the pose held, how much total redundant motion
occurred, how much net motion remained -- before the integrals. The equations,
tables and chapter order did not change.

**The minus sign of Equation 4.2 is explained where it appears.** The rotation
vector \(\phi_0u_0\) points from the achieved entry direction towards the
inward configured surface normal, and \(\theta_{0,t_1}\) is reported in the
opposite direction so that it follows the same rotational direction as the
configured offset. Section 4.5.1 states that before the equation. Section 4.5.2
carries the matching statement for \(\gamma_{t_1}\): it is formed from the
measured end orientation back to the held entry orientation, so its direction
is opposite to the start-to-end rotation of the end effector. Both belong in
Chapter 4, so that Chapter 5 can report results without re-deriving either
convention.

**A configuration table that only restates the prose around it goes.** The
system table repeated the robot, the tool dimensions, the mounting play, the
operating system, the kernel and the library versions, all of which the section
had just said in sentences. Unlike the gain, phase and case tables, it did no
analytical work. The prose stays and the table is gone; the exhaustive
configuration lives in the parameter appendix.

**The two procedures are not both calibrations, and the headings say so.**
Section 4.2 is `Surface-Reference and Tool-Normal Calibration`, and
Section 4.2.1 is `Surface-Reference Construction`, matching the row headings of
Figure 4.2. The heading was shortened from `Configured Surface Reference,
Physical Surface, and Tool Calibration` on 2026-09-01: a heading that lists
three things is doing the opening paragraph's work, and the configured-against-
physical distinction is stated there instead. Section 4.5 is `Initial Angular
Condition and Contact Response`, replacing `Experimental Condition and Response
Quantity`, which named neither the condition nor the response. The
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

**Section 4.2 says what each procedure produces, and stops there.** The section
had grown to mix procedure, frame definitions, validation and the later
combination of the two results before the reader knew what either procedure
delivered. Its settled opening is two short paragraphs: the first assigns
\(p_s\), \(n_s\) and \(R_{\mathrm{surface}}\) to the surface-reference
construction and \(n_{\mathrm{Tool,EE}}\) to the tool-normal calibration; the
second states that the tool-normal calibration did not revise the configured
surface reference and that the physical surface-reference difference was not
measured independently. The two subsections then state the procedures and send
the exact values and fitting relation to Appendix C.

**The calibration flowchart is withdrawn.** It repeated the two procedures
immediately before Sections 4.2.1 and 4.2.2 stated them again. It is removed
rather than redesigned. Do not restore a calibration flowchart unless it adds
a distinction that neither subsection can state directly.

\(R_dn_{\mathrm{Tool,EE}}=-n_s\) still describes what the
controller does with the calibration, not how the calibration was made, and is
stated in a clause rather than as a numbered equation. The same applies to
\(p_{\mathrm{Tool}}=p_{\mathrm{TCP}}+R_{\mathrm{EE}}r_{\mathrm{Tool,EE}}\): Chapter 4
records the calibrated offsets and the selection tolerance and points at
Chapter 3 for the algorithm that consumes them.

**`virtual disturbance` is the short name for the pose-hold excitation.**
Agreed 2026-09-01. Chapter 4 introduces it once, as `a repeatable internally
commanded disturbance, referred to below as the virtual disturbance`, and every
later use in Chapters 4 to 6 is the short form. The long
`internally commanded point-force-equivalent disturbance` is withdrawn from
running prose: it is five words of definition repeated at every mention. The
logged-field description in the data-format appendix keeps its own wording,
because the identifier is the subject there.

**Write `singular-value conditioning`, never `sigma conditioning`.** The short
form disagreed with the section heading and with every other mention in the
thesis. The same applies to its parameters: `singular-value deadband`, not
`sigma deadband`.

**An acceptance criterion is written as a criterion, not as a definition.**
Equation 4.10 sets a threshold a trial either meets or does not, so the lead-in
is `A trial satisfied the Cartesian position-retention criterion when`, not
`Cartesian position retention is defined by`. The distinction matters because
the quantity being thresholded, the peak position error, is defined elsewhere.

**Table 4.4's second column is `Comparison parameter`.** `Varied quantity` did
not fit the Case-A row, which is a baseline condition rather than a varied
parameter.

**The measurement count has one home.** The repetitions, the total and the analysed total
are stated once, in the data-recording subsection. The
evaluation section says how repeated settings are reported and where the
standard deviations appear, and does not restate the counts.

Every reported setting carries its three repetitions. The \(t_2\) exclusion is
stated separately from the data-set counts, which cover only the reported
\(t_1\) measurements. Do not add the excluded measurements to those counts or
describe the acquisition history used to arrive at them. State the measured
conditions directly, following the rule under *Naming a technical quantity*.

**Isotropic matrices are a table, not a display.** Four \(3\times3\)
matrices whose diagonal entries are all equal spent most of a page saying four
numbers. They are one small table with a sentence saying every entry was
isotropic.

**Tables 4.2 and 4.3 are not restated row by row.** After Table 4.2, retain
only the experimental role of the rotational stiffness and the reference to
the inertia-scaled damping formulation. After Table 4.3, give the chronological
procedure once, followed by one sentence stating the fixed null-space
configuration. The table remains the home of the individual transition and
trajectory values.

**Table 4.3 has only `Quantity` and `Value`; Table 4.4 has no `Evaluated
effect` column.** The removed columns repeated explanations already carried by
Chapter 3 or by each case name. Retain the achieved \(\theta_{0,t_1}\) values
in Table 4.4 because they are measured experimental conditions.

**Chapter 4 documents the reported experiments, so grinding leaves its tables.** No
experiment entered the Grinding state, and the chapter said so four times: a
`Contact establishment and grinding` gain row, a sentence that the configured Grinding state
carried the contact-establishment entries unchanged, a `Configured grinding sweep` row giving
an amplitude and a frequency nothing used, and a closing sentence repeating
that no experiment entered it. All four were reduced on 2026-08-27 to the gain row
`Contact establishment`, a `Pre-grinding hold` row saying that it holds the reached pose at the
end of Contact Establishment, and one closing sentence: every experiment ended
at the \(5\,\mathrm{s}\) timeout, the enabled pre-grinding hold then retained the
reached pose, and the measured data cover orientation, approach and contact establishment
only. **Section 3.2.5 keeps its two sentences**, because Chapter 3 documents
the implemented sequence rather than the reported campaign, and Chapter 6 keeps
the sentence placing sustained grinding outside the evaluation.

**\(\gamma_{t_1}\) is what Chapter 4 says was measured.** The contact establishment
procedure once ended `so the measured alignment rotation is a response to
contact`, which names a physical tool alignment the thesis does not measure.
The settled wording is `the measured contact-establishment response results from the contact
interaction rather than from tracking a time-varying orientation command`.

## The appendices: document and support

**The test for appendix material.** Agreed 2026-09-01. Keep what supports a
reported result, resolves an implementation convention the equations do not
settle, or is needed to reproduce the experiment. Remove repeated figures,
generic source-code boilerplate, and logged fields that no reported result
uses. Applied across all four appendices, this removed about two pages without
losing a value, a convention, or a measurement.

**The main chapters explain and interpret; the appendices document and
support.** An appendix carries the exact code, the logged quantities, the exact
parameters, and the supporting numerical results. It does not re-teach the
compliance-centre mechanism, the null-space law, the contact-establishment trajectory, or the
experimental narrative: each of those has one home in Chapters 2 to 5, and an
appendix that needs one cross-references it. Applied on 2026-08-27, this
removed roughly two pages of restated theory without losing a value, a key, or
a measurement.

**Appendix A is the listings, with one sentence per block.** The chapter opens
by saying what the four listings show — the compliance-centre transformation,
the Cartesian impedance wrench, the null-space torque, the experimental
disturbance, and the final joint-torque command — and names the Eigen aliases a
reader needs to follow them. The count in that opening has to match the listings beneath it: it
claimed two while four sat below it until 2026-09-01, and it says three now
that three remain.

**Appendix A keeps only what is specific to this thesis.** The
state-acquisition listing was deleted on 2026-09-01, because obtaining
\(q\), \(\dot q\), \(J\) and the end-effector pose is standard libfranka
usage that Chapter 3 already describes, and the torque-assembly listing was cut
to the four lines that combine the wrench, the null-space torque, the
disturbance and the Coriolis term. What survives is the compliance-centre
point-shift, the branch selection, and that final assembly. Section A.2 is
`Final Torque Assembly`. **The sign-convention paragraph is the one thing that
must never be cut**, because an examiner comparing the equations with the
source would otherwise read the implementation as carrying the wrong sign.

**Set the code identifier in monospace and the thesis vector in maths.** The
appendix has to say that \(r_c\) and the source variable `r_c` point in
opposite directions, and a reader who meets both in the same typeface sees the
sentence assert \(r_c=-r_c\). Write the thesis quantity as \(r_c\), the
source identifier as `\texttt{r\_c}`, and the internal lever as
\(\ell_c\); then state that `\texttt{r\_c}` in the listings represents
\(\ell_c\), and that the upper-right block
\([\ell_c]_\times=-[r_c]_\times\) is the block of the adjoint the theory
chapter defines. Each block then carries at most one sentence, for something the code does
not say by itself: the direction of \(r_c\), that both configured definitions
store \(r_c\) and differ only in the frame it is expressed in, and that the
disturbance term is non-zero only in the pose-hold study. Do not re-explain the
point shift, the tool-fixed against surface-fixed distinction, or the torque
assembly in prose beside the code that performs them.

**Appendix B is the state mapping and the signal table, and nothing else.**
The sections are `Control States` and `Recorded Signals`, and the table is
`Recorded \abbr{CSV} signal groups`.

**The control-state mapping is not in the thesis.** It was reordered into a
table on 2026-09-01 and removed later the same day: an integer-to-state mapping
is file-format documentation, and Figures 3.1, 3.3 and 3.7 already give the
state sequence a reader needs. It belongs with the recorded data, not in the
appendix. The remaining section is `Evaluation Signals`.

**Appendix B lists the signals the reported results are calculated from, not
the file schema.** The external-wrench group, its stored reference values and
its corrected forms were removed on 2026-09-01, together with the
clearance-capture positions, the press coordinate, and the final commanded
torque: the model-estimated wrench fed only the optional termination condition,
and every experiment ended through the timeout instead, so none of them enters
a reported figure or value. Say once that the complete schemas are documented
with the recorded data.

**A wrench row names the frame it acts on, the frame it is expressed in, and
its moment reference point.** All three are needed, and the third was missing:
libfranka's `O_F_ext_hat_K` acts on the stiffness frame \(\{K\}\), is
expressed in the base frame \(\{0\}\), and its moment is referenced to the
base origin. State all three, then that
\({}^{\mathrm{EE}}T_K=I\) in the experimental configuration, so
\(\{K\}=\{\mathrm{EE}\}\). It lists the groups needed to interpret and
reproduce the reported evaluations. Derived angular-deviation aliases and the
unused `t_align` field are omitted rather than documented only because the
logger wrote them. A
table cell is a definition, not a paragraph: name the quantity, its frame and
its unit, and send anything longer to the section that owns it. The former
`Evaluation Quantities` section was deleted on 2026-08-27 and **must not be
restored**. The reported quantities already have their proper homes:
\(\gamma_{t_1}\) in Section 4.5.2, and \(E_N\),
\(\Delta\eta\) and the position-retention criterion in
Section 4.6. The contact-establishment report markers
`t_align_fraction`, `deviation_min` and `align_status` went with it: none feeds
a state exit, a command, or a reported result, which is the rule under *What
belongs in the thesis at all*.

**Appendix C holds the parameters needed to reproduce the reported experiments.**
It is the reproducibility record, so a parameter, its configuration key and its
value belong there and an explanation of what the parameter does does not — and
a parameter that was configured but never acted on does not belong either. The
pre-contact hold was disabled in every reported experiment and no experiment entered Grinding,
so their gain rows, the grinding-sweep row, the grinding damping factor and the
paragraph explaining that the gate gains were inactive were all removed on
2026-08-27. What remains of both is the `Pre-grinding hold` row, because it is
where every reported experiment ended. The state list for inertia-scaled damping is
scoped the same way: `Reported contact states using inertia-scaled damping —
Surface Approach and Contact Establishment`.

**Appendix C distinguishes fallback damping from active fixed damping.** Its
table is `State-specific stiffness and fallback damping parameters`, and a
sentence before it says that the contact experiments used inertia-scaled
damping during Surface Approach and Contact Establishment, so the damping
vectors listed for those two states are the configured fallback values. Without
that sentence a reader takes the fallback numbers for the active contact
damping coefficients. In
the state-and-configuration table, the matrices listed for Surface Approach
and Contact Establishment are labelled as fallbacks because inertia-scaled
damping is active in those states. The pose-hold values are labelled as fixed
damping because those matrices remain active there.

**The tool clearance carries its thesis name in Appendix C too.**
`Surface clearance` is withdrawn as a row label, written here as a literal
string so a rename cannot revive it; the row reads
`Tool clearance, \(h_{\mathrm{clearance}}\)` against the unchanged key
`descend_surface_clearance`, matching Chapter 3, the symbol list and the
Chapter 4 phase-parameter table. The selection-tolerance value is written the
way its home in the Chapter 4 calibrated-geometry table writes it,
\(0.1\,\mathrm{mm}\), rather than as \(10^{-4}\,\mathrm{m}\). The damping and compliance-centre section was one page
of prose re-deriving the operational-space inertia, the \abbr{LDLT} solve, the
fallback rule and the active end-effector-frame definition; it is now one table plus two
sentences pointing at `Contact Establishment` for the damping calculation and the
point shift, and at the case table and Appendix D for the tested displacement
components. \(\Lambda(q)\) and its regularisation are named in a table row
rather than set as an equation, since neither carries a symbol-list entry and
neither is referred to from anywhere else.

**The Appendix C row for the selection tolerance names the thesis quantity and
the source key side by side:** `Tool-point selection tolerance,
\(\varepsilon_{\mathrm{sel}}\)` against
`tool_contact_feature_tie_tolerance`. The thesis-facing terminology follows the
`tie` withdrawal under *Mathematical notation*; the literal key keeps its
spelling, per the rule that source identifiers are reproduced rather than
renamed to match the prose.

**Appendix D is the four main-case tables and one sentence introducing
them.** Its chapter title is `Numerical Results for Main Surface-Contact
Cases`, and it carries no section heading, because the tables are its only
content. The intermediate-direction section is withdrawn with every
experiment about \(t_2\). What was
cut on 2026-08-27, and must not come back: repeated definitions of tool-fixed
and surface-fixed, of the leading-feature rule, and of the general
compliance-centre direction rule; second paragraphs generalising a result the
sentence above already stated; and the mounting-play qualification, which
Chapter 6 carries. What stays because the appendix is the only place it exists:
the \(\sin\phi_0\) projection that explains why a
\(40\,\mathrm{mm}\) tool-axis displacement gives under \(7\,\mathrm{mm}\) of
tangential lever.

**The shifted centre may be glossed as a virtual lever arm.** Agreed
2026-09-02. Beside the formal decomposition \(m=m_R+r_c\times f\), write that
the shifted \abbr{CoC} makes the commanded press act *as if* it had a virtual
lever arm \(r_c\) relative to the TCP, which generates the additional moment
\(r_c\times f\). The gloss states the mechanism the equation encodes and is not
a second claim, so it carries no measurement and needs no citation. Keep the
`as if`: no physical lever exists, and the displacement is a control-law
quantity rather than a tool geometry.

**The projection is an effective lever arm, not a moment.** `The tangential
projection \(\lVert r_{c,t}\rVert=\lVert r_c\rVert\sin\phi_0\) supplies
the normal-press moment` was withdrawn on 2026-09-01: the projection determines
the lever arm, and the cross product produces the moment. Write that only the
tangential projection contributes to the moment generated by the commanded
normal press, and that at \(\phi_0=9.30^\circ\) and
\(\lVert r_c\rVert=40\,\mathrm{mm}\) the **effective tangential lever
arm** is \(6.47\,\mathrm{mm}\), substantially smaller than the
\(40\,\mathrm{mm}\) tangential displacement of Case~D. The initial-angular-offset table and plot, the direction plots, the TCP-height classification,
and the pose-based alignment consistency check are withdrawn because they
duplicate the main response relation or introduce secondary outcomes outside
the main \(\gamma_{t_1}\) comparison.

Appendix D is settled. Its structure is the exact numerical values behind
Cases A--D.

**The tool-axis displacement check is withdrawn from the thesis.** Removed on
2026-09-01, with Section D.2, Table D.5, Figure D.1, and the Chapter 5 sentence
that had briefly cited it. Two reasons, and the second is the decisive one.
It read as an additional experiment rather than as evidence, because no main
chapter depended on it. More importantly, **it could not establish what it
appeared to establish**: the displacement ran along the tool axis, which is
inclined to \(n_s\), so every setting carried a large normal component *and*
a small tangential one, and the result therefore cannot separate them
experimentally.

The two statements the thesis needs are already carried elsewhere.
Section 2.7.2 derives \(r_c\times f_n=r_{c,t}\times f_n\), because
\(r_{c,n}n_s\times F_nn_s=0\); and Case~D shows experimentally that
reversing the tangential displacement reverses which offset direction is
reinforced. **Do not reinstate the check**, and do not replace it with the
broader claim that a normal \abbr{CoC} displacement is irrelevant to
alignment: the complete coupling is
\(r_c\times f=r_c\times f_n+r_c\times f_t\), so a normal component can
still couple with a tangential commanded force. The precise statement, and the
only one to make, is that **the surface-normal component of the compliance-centre
displacement does not contribute to the moment generated by the commanded
normal force**.

**An appendix table caption is a short noun phrase, like every other caption.**
The Appendix D captions had grown to four and five lines carrying
`Varied: …  Held fixed: …  Reference: …`, which is the procedure the rule
under *Figures and tables* keeps out of captions. Where the table itself
already shows that information — a `Reference` column naming the Case-A row, a
bold `TCP` column heading, a spanning header naming the coordinate — the
caption says nothing about it. Where it does not, one sentence of body text
before the table carries it. The optional short caption was dropped from these
tables at the same time: once the caption is a noun phrase, a second shorter
form for the list of tables has nothing left to shorten.

## Evidence and claims

Never invent measurements, repetitions, fitted values, confidence intervals,
p-values, contact locations, timing bounds, or safety conclusions.

**A single trial does not carry a \(\pm\) sample standard deviation as
experimental variability.** Variation among time samples within one stationary
window describes temporal fluctuation in that trial. It does not establish
between-trial repeatability, and the samples may be time-correlated. A
single-trial table therefore reports the stationary-window means and states
that between-trial variability was not evaluated. Where repeated trials are
available, calculate the sample standard deviation across the trial-level
means.

Distinguish:

1. measured observation;
2. model-based interpretation;
3. hypothesis requiring another experiment.

Trace every geometric metric through its measurement chain. The primary angular
result is the contact-establishment response and does not require the calibrated
tool normal. The appendix reconstructs a separate pose-based tool axis from the
end-effector pose and a calibrated tool-to-end-effector transform. Because the
mounted tool can rotate approximately ±2° about \(y_{EE}\), that secondary
quantity is not a directly measured physical tool-face axis. Do not rename
\(y_{EE}\) as \(t_2\) without transforming it into the configured surface
frame.

**The word `inferred` is not used for it, and neither is `EE-inferred`.** Both
were removed. Name the chain instead: `alignment angle calculated from the
end-effector pose`, `end-effector-based alignment angle`, or `pose-based
alignment angle`.

### Separate the desired offset, achieved initial offset, and response

The orientation chain has three symbol families. \(\theta_{\mathrm{offset},t_i}\)
is a component of the configured orientation offset about surface tangent
\(t_i\). It defines the desired pre-contact tool direction during Tool
Orientation and does not prescribe the rotation during Contact Establishment.
The achieved pose-based initial angular offset \(\theta_{0,t_1}\) is the
contact-entry condition relative to the configured surface reference. The
contact-establishment response \(\gamma_{t_1}\) is the measured response about
that tangent.

The experiment tables and comparison figures identify their angular condition
with \(\theta_{0,t_1}\), not with \(\theta_{\mathrm{offset},t_1}\). The
configured offset remains in the methodology as the controller input that
generated this condition. A physical
initial tool--surface error is not substituted for either quantity unless an
independent physical surface normal and the tool orientation under load have
both been measured.

**\(\gamma_{t_1}\) is not the start-to-end end-effector rotation.** It
represents the end-of-contact-establishment orientation change from the
measured end orientation back to the held entry reference. The corresponding
start-to-end end-effector rotation points in the opposite rotational direction.
For the \(+10^\circ\) configured offset at the TCP,
\(\gamma_{t_1}=+7.56^\circ\), while the start-to-end end-effector rotation
points along \(-t_1\) with a magnitude of \(7.56^\circ\).

**`configured flat direction` is withdrawn; write `parallel alignment with the
configured surface`.** Agreed 2026-09-01, on the ground that `flat direction`
names no defined quantity and reads as informal beside the surface frame it
depends on. The attributive form is `parallel to the configured surface`.

**The withdrawn phrase covered two different things, and they take different
replacements.** Where it named the *direction* \(-n_s\) -- in the
\(\phi_0\) construction of Section 4.5, in its symbol-list row, and in the
definition of \(\theta_{0,t_1}\) -- write `the inward configured surface
normal`, which is what \(-n_s\) is and is already fixed by
\(n_d=-n_s\). Where it named the *alignment state* the end effector rotates
towards, write `parallel alignment with the configured surface`. Substituting
the alignment wording for the direction vector produces a rotation measured to
a state rather than to a direction, which is not what the equation does. For a
start-to-end end-effector rotation towards parallel alignment with the
configured surface,
\(\gamma_{t_1}\) points in the same surface-tangent direction as the achieved
initial angular offset \(\theta_{0,t_1}\), and
\(\lvert\gamma_{t_1}\rvert\) gives its size. The plus and minus symbols remain
on equations and data values. Running prose uses `both directions of rotation`
for an aggregate comparison and the named conditions above for a single one;
`both signs` and `reversed condition` are still not used. State the physical
motion explicitly; do not compress it into the label
`correction-directed response`.

The construction is \(\gamma=\phi_{\mathrm{CE}}u_{\mathrm{CE}}\) from
\(R_{\mathrm{CE}}=R_{\mathrm{EE,clearance}}
R_{\mathrm{EE}}^\top(t_{\mathrm{CE,end}})\), with the reported component
\(\gamma_{t_1}=t_1^\top\gamma\).
\(R_{\mathrm{EE,clearance}}\) is the **orientation reference held through
contact establishment** and equals
\(R_{\mathrm{EE}}(t_{\mathrm{CE,start}})\), which is why the logged
\(e_R\) is exactly zero there. The achieved initial angular offset is
calculated from the current end-effector pose, calibrated tool normal and
configured surface reference, giving \(\theta_{0,t_1}\). `extract_metrics.py`
reads the response \(\gamma_{t_1}\) from the final \(e_R\).

**State the direction relation at the opening of Chapter 5, before any number
depends on it.** The opening gives the relation between \(\theta_{0,t_1}\),
\(\gamma_{t_1}\), and the corresponding start-to-end end-effector rotation,
including the reason: \(\gamma_{t_1}\) is calculated from the measured end
orientation back to the held entry reference, so its direction is opposite to
the start-to-end rotation. A reader who meets \(+7.57^\circ\) without that
sentence takes it for a physical rotation of \(+7.57^\circ\), and deferring
the explanation to the Case-D mechanism figure leaves three case sections
misread before it arrives. Beside that figure, state that \(M_{t_1}\) points
along
\(-t_1\), \(\gamma_{t_1}\) points along \(+t_1\), and the start-to-end
end-effector rotation points along \(-t_1\). This bridge prevents the response
coordinate from being mistaken for the physical direction of motion.

**Say what the quantity is; do not give the direction relation a convention
name.** State that \(R_{\mathrm{CE}}\) rotates from the measured end orientation
back to the held start orientation, or that \(e_R\) has that relation. Naming
it `the current-to-reference convention` reads as *the convention currently in
use* and invites a reader to look for a superseded one.

**Do not coin an informal name for a defined quantity to carry a direction
argument.** Section 4.5.2 said the metric was independent of `the plane-zero
alignment`, which names nothing the thesis defines, and justified that
independence by saying the tool axis `is known only to within a degree or two
and shifts as the tool settles in the gripper`. Both were removed on
2026-08-25. The second states a mechanical clearance as though it were a
calibrated knowledge bound, which the \(\pm2^\circ\) rule below forbids, and
asserts a motion during contact that was not tracked. The defensible statement
names the chain instead: the calculation uses only the measured end-effector
orientations and therefore does not require the instantaneous tool--gripper
rotation. Do not call the response independent of relative tool--gripper
motion, because that motion can still affect the contact dynamics and measured
end-effector response. The surface frame enters only as the directions the
rotation is resolved along.

**The pose-based alignment consistency metric is withdrawn.** Its unsigned
angle depended on the assumed fixed tool-to-end-effector relation and was not
an independent physical tool-orientation measurement. Do not restore
\(\theta_{\mathrm{align}}\), its before--after reduction, their scatter plot,
or their logger-only aliases as reported thesis quantities.

**Each main surface-contact comparison changes one controller parameter and
reports one response.** The achieved pose-based initial angular offset is
\(\theta_{0,t_1}\), and the response is the measured contact-establishment
rotation \(\gamma_{t_1}\). Chapter 5 table headings name the changed parameter
directly and call the output `Measured contact-establishment rotation`; generic columns such as
`Varied entry` and `Value` are not used. Subsection titles, captions, axes and
the surrounding prose use the same input--response vocabulary. The commanded
wrench time history in Case D is the mechanism figure and remains the one
exception to a response-only comparison plot.

**The TCP-height flatness classification is withdrawn from the reported
results.** It is derived from existing measurements, is not used in the Chapter
5 comparison, and can be mistaken for a second response criterion. Do not
restore its table, count, or classification language. The physical face angle
was not measured under load.

**Do not write that a lever was insufficient to align the tool**, or that it
`did not remove the full initial angular offset`. Both read as claims about the
physical tool face, whose orientation under load was not tracked. Report the
measured contact-establishment response about \(t_1\) and do not add an
inferred final physical alignment.

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
relative to the tool** for the whole of contact establishment. Say so where it is introduced.

**Chapter 2 also says how the point is chosen and what it is for.** Naming the
three outcomes without the rule that produces them left a reader unable to see
where the point comes from, and unable to tell whether it serves the command or
only the evaluation. Both belong in the compliance-centre section, in two
clauses: the leading corner along the descent direction, with selected corners
averaged, and the fact that the contact-establishment reference is generated on the point
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
the contact-establishment trajectory moves it as \(p_{\mathrm{Tool},d}(t)=p_{\mathrm{Tool},0}+s_{\mathrm{CE}}(t)(-n_s)\),
and the TCP target is reconstructed from it as
\(p_d(t)=p_{\mathrm{Tool},d}(t)-R_{\mathrm{EE,clearance}}r_{\mathrm{Tool,EE}}\), which produces the
press. The centre of compliance is a separate mechanism acting through
\(r_c\) on the force–moment coupling. Do not merge the two chains.

**Never write that the compliance centre moves the force application point.**
The physical surface force still acts at the actual contact point. What changes
is the point about which the compliance is defined, and therefore the
translation–rotation coupling: the same normal press produces a different
  rotational response as \(p_c\) moves. Give that explanation before introducing
  \(r_c=p_c-p_{\mathrm{TCP}}\) and \(r_c\times f\), not
after. If \(p_c\) lies on the relevant line of action the moment contribution
becomes small or zero. Reversing a tangential displacement reverses the moment
direction. Whether that moment supports correction depends on the direction of
the achieved initial angular offset.

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
been removed. **The net displacement is
\(\Delta\eta=v_{\mathrm{ref}}^\top\Delta q_{\mathrm{null}}\)**, the
scalar projection of the net projected joint motion onto one common direction.
Both are angles in radians and both are reported in degrees, so the two panels
that carry them can be read against one another. They are reported together,
because for the sigma-only settings they differ by orders of magnitude, and
that difference is the result.

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
`Both sigma-only settings ended the disturbance interval with a net
displacement close to zero` states it directly, and the two-orders-of-magnitude
relation against the uncontrolled \(7.517^\circ\) carries the size.

Two things survive that compression and are not dropped with the deviations:
the `\cref` to the figure panel the claim rests on, which every results
subsection must carry, and the relation `a factor of about six` between the two
cumulative-motion values. Stripping uncertainty is not licence to strip the
evidence pointer or the ratio.

**\(v_{\mathrm{ref}}\) is recovered from the data, not read from the log**,
and the earlier wording here —
`\(\Delta\eta_{\mathrm{dist}}=v_7(q_5)^\top[q(9\,\mathrm{s})-q(5\,\mathrm{s})]\)`
— was **wrong on both halves** and is withdrawn. Checked against
`make_nullspace_figure.py` on 2026-08-26: \(v_7\) is absent from the experiments
without null-space torque, because the controller records it only while the
conditioning term is selecting a sign. The axis is therefore the normalised
**arithmetic mean of the three net projected displacement vectors of the
baseline condition** \(\Delta q_{\mathrm{null},0}\), and what is projected is
the trapezoidal integral of the projected joint velocity over
\(t\in[5,9]\,\mathrm{s}\), not the raw joint difference between the two
instants. Section 4.6 says `the arithmetic mean of the three net projected
displacement vectors measured in the condition without null-space torque`, and
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
the law. **Nor does \(E_N\) quantify the switching.** What was measured is
cumulative projected motion, not a count of direction changes, so the larger
value is written as `consistent with greater back-and-forth redundant motion`,
never as having `quantified the greater switching activity`. Describe the
switching as the mechanism the controller implements, and the cumulative motion
as the measurement consistent with it. The defensible finding is a parameter selection:
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
  full rank.
- Use `rank` and `full rank` for the Jacobian throughout the thesis. Do not use
  `row rank` or `full row rank`. For the \(6\times7\) Jacobian, full rank means
  \(\operatorname{rank}(J)=6\).
- A retained singular value is inverted as \(1/\sigma_i\).
- Distinguish the virtual-centre lever \(r_c=p_c-p_{\mathrm{TCP}}\) from the
  tool-geometry lever \(r_{\mathrm{Tool}}=p_{\mathrm{Tool}}-p_{\mathrm{TCP}}\). \(r_{\mathrm{Tool}}\) locates the contact
  reference relative to the TCP; \(r_c\) locates the virtual centre of
  compliance relative to the TCP. They never appear in the same expression.
  \(r_c\) shapes the **commanded** wrench through \(\mathrm{Ad}(r_c)\);
  \(r_{\mathrm{Tool}}\) belongs to the physical contact geometry.
- **The direction-selected lever rule uses the following cross-product
  orientation.** For the generic tangent-plane angular offset
  \(\theta_a=\theta_{a,t_1}t_1+\theta_{a,t_2}t_2\), it is
  \(r_{c,t}=\lVert r_{c,t}\rVert(\theta_{a,t_1}t_2-
  \theta_{a,t_2}t_1)/\sqrt{\theta_{a,t_1}^2+
  \theta_{a,t_2}^2}\). It reduces to
  \(r_{c,t}=+\lVert r_{c,t}\rVert t_2\) when \(\theta_{a,t_1}>0\) and
  \(r_{c,t}=-\lVert r_{c,t}\rVert t_1\) when \(\theta_{a,t_2}>0\).
  The exact normal-press contribution is
  \(r_{c,t}\times f_n=\lVert r_{c,t}\rVert F_n
  (\theta_{a,t_1}t_1+\theta_{a,t_2}t_2)/
  \sqrt{\theta_{a,t_1}^2+\theta_{a,t_2}^2}\). With \(F_n<0\), it acts
  opposite to \(\theta_a\). In Case D, the direction generated by the
  \(+10^\circ\) configured offset uses \(r_{c,t_2}>0\) for the outer position
  that produced the larger response.

  **The reversed numerator
  \(\theta_{\mathrm{offset},t_2}t_1-
  \theta_{\mathrm{offset},t_1}t_2\) is wrong and was
  removed** from Chapter 2 and Chapter 5 on 2026-08-25. It survived the \(r_c\)
  redefinition because it sits two equations away from the moment it feeds, and
  in both chapters it contradicted the moment printed immediately below it.
  Any future change to the lever convention is checked against both
  anchors above, not against the formula alone.
- **The desired tool-normal direction is \(n_d=R_{\mathrm{offset}}(-n_s)\), and
  for zero configured offset \(n_d=-n_s\), never \(+n_s\).** A tool face
  parallel to the surface requires the tool normal to point into the plane, so
  the configured offset is applied to the inward normal \(-n_s\). Writing
  \(n_d=R_{\mathrm{offset}}n_s\) makes the zero-offset
  target point out of the surface instead of into it.

  **\(n_{\mathrm{flat}}\) and \(s_a\) are withdrawn**, written here as
  literal strings so a rename cannot revive them. The earlier two-step form
  \(n_{\mathrm{flat}}=s_an_s\) with \(s_a=-1\) named an intermediate
  direction that is neither measured nor calibrated, and it put a third symbol
  beside a notation that already separates the two things that matter: the
  calibrated tool geometry, \(n_{\mathrm{Tool,EE}}\) with its base-frame
  representation \(n_{\mathrm{Tool},0}=R_{\mathrm{EE}}n_{\mathrm{Tool,EE}}\),
  and the controller reference \(n_d\). Naming the intermediate direction
  \(n_{\mathrm{Tool},\dots}\) instead was considered and rejected for the same
  reason. The sign is fixed at \(-1\) for every reported experiment, so it needs no
  symbol in the chapters; the parameter appendix records it as
  `tool_axis_target_sign` \(=-n_s\), which is where a reader checks the
  configured value.
- **There is no \(f_C\).** A symbol for an abstract environment-on-tool contact
  force was introduced and then removed. Build every moment statement on the
  commanded wrench \(F=[f^\top,m^\top]^\top\). The model-estimated external
  wrench is an implementation signal used only by the optional contact establishment
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

  1. **Name the component the relation is exact for.** Decompose the complete
     commanded force as \(f=f_n+f_t\). The normal-force contribution is then
     the exact quantity \(r_{c,t}\times f_n\), while
     \(r_c\times f=r_c\times f_n+r_c\times f_t\) retains the tangential-force
     contribution.
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
- **\(m=m_R+r_c\times f\) is an identity, and is written with an equals
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
  sum — those terms are inside \(r_c\times f\).
- **\(r_c=0\) is not a zero-moment condition.** Setting
  \(r_c=0\) makes \(\mathrm{Ad}(r_c)\) the identity, so it removes the complete
  additional coupling introduced by the virtual point shift and every
  \(r_c\)-dependent term of the shifted \(K_{\mathrm{TCP}}\) and
  \(D_{\mathrm{TCP}}\) — both the off-diagonal blocks and the added rotational
  entries \([r_c]_\times^\top K_p[r_c]_\times\) and
  \([r_c]_\times^\top D_p[r_c]_\times\).

  The ordinary rotational impedance \(m_R\), finite rotational compliance,
  tool geometry and physical contact interaction remain, so contact-induced
  robot rotation can still occur.

  The general form to use is: *setting \(r_c=0\) removes the additional
  translation--rotation coupling introduced by the virtual point shift; the
  ordinary rotational impedance and the physical tool and contact geometry
  remain.* **Never write that a zero lever gives a zero moment.**
- **A contact-point term obtained by subtraction is not evidence for a
  physical contact moment.** If an assumed geometric point is used to write
  \(M_{t_1,\mathrm{est}}=M_{t_1,\mathrm{lever,geom}}+
  M_{t_1,\mathrm{contact}}\), then
  \(M_{t_1,\mathrm{contact}}\) is defined from the other two terms. It neither
  predicts \(M_{t_1,\mathrm{est}}\) nor identifies a separately observed
  pressure centre or contact couple. Omit this residual construction from a
  results explanation unless an independent contact-moment quantity is
  available. In particular, never attribute a preceding rotation to the sign
  of one baseline-referenced endpoint estimate.
- **The physical contact moment is distinct from the virtual
  compliance-centre contribution.** Setting \(r_c=0\) gives
  \(r_c\times f=0\), but a surface force acting away from the
  TCP can still produce
  \(m_{\mathrm{contact},\mathrm{TCP}}=(p_{\mathrm{contact}}-
  p_{\mathrm{TCP}})\times f_{\mathrm{contact}}\). Use
  \(f_{\mathrm{contact}}\) directly; do not expand it into paired
  action-direction aliases in the nearby definition.
  In a standalone supporting report, this relation may state the physical
  flattening mechanism. If the pressure centre was not observed, do not assign
  it a measured position or evaluate the cross product from the selected tool
  point.

  A quasi-static endpoint balance may define the surface-on-robot contact
  moment as the negative of the controller moment after inertia and other
  external moments have explicitly been neglected. Label that value as a
  quasi-static balance inference. Do not equate it with a clearance-referenced
  model-estimated moment change, and do not use the latter to identify the
  moment that initiated a preceding rotation.
- **A wrench comparison uses one reference on both sides.** Compare an
  absolute command with an absolute TCP-referenced estimate, or subtract the
  same physical-state baseline from both. Never place an absolute command
  beside a clearance-referenced estimator change and call their difference a
  consistency error. For a rotation applied while a normal load remains, use
  the stationary loaded state immediately before the rotation as the moment
  baseline for both command and estimate. The reported absolute comparison
  reads the estimator force and moment variables directly and shifts their
  wrench reference to the TCP with the equations below.
- **Never cross a physical or controller lever with a force from the other
  side.** The virtual lever \(r_c\) is crossed with the commanded force \(f\), and an
  assumed physical contact lever is not crossed with the model-estimated force
  to manufacture a contact-moment explanation.

  The required spatial-wrench reference shift is a separate operation.
  Libfranka's \({}^{O}F_{K,\mathrm{ext}}\) is the wrench on stiffness frame
  \(K\) expressed in the base frame. Its base-frame moment contains the
  base-to-\(K\) force lever:
  \[
    {}^{O}m_{O,\mathrm{est}}
    ={}^{O}m_{K,\mathrm{est}}
     +p_K\times{}^{O}f_{\mathrm{est}}.
  \]
  Therefore,
  \[
    {}^{O}m_{K,\mathrm{est}}
    ={}^{O}m_{O,\mathrm{est}}
     -p_K\times{}^{O}f_{\mathrm{est}}.
  \]
  Use \(p_K=p_{\mathrm{TCP}}\) only after
  \({}^{EE}T_K=I\) has been verified. This coordinate transformation does not
  identify a physical contact lever or pressure centre. For a
  baseline-referenced result, shift the current and baseline wrenches at their
  own reference positions before subtraction.
- The complete translational command contributes \(r_c\times f\). Directional
  analysis may isolate \(r_c\times f_n\), where \(f_n\) is the normal component
  of that same complete commanded force.
- **The compliance-centre hierarchy is stated once, in Section 2.7.3, and
  applied everywhere else.** The order is
  \(r_c\to(r_{c,t_1},r_{c,t_2},r_{c,n})\to r_{c,t}\), then
  \(\theta_{\mathrm{offset}}\to\) the selected direction, then
  \(m=m_R+r_c\times f\). \(r_{c,t_1}\) and \(r_{c,t_2}\) are scalar
  coordinates that may be positive or negative, and \(r_{c,t}\) is the tangential vector they form. Chapters 4
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

  **The tool-axis supporting check reuses the initial angular-offset magnitude \(\phi_0\)
  before using the sine.** This is the shortest-rotation magnitude from the
  calibrated tool normal to the inward surface-normal direction \(-n_s\),
  already defined with the pose-based entry condition. Do not introduce a
  second angle for the same offset magnitude. State that a tool-axis displacement
  contains normal and tangential components, and use
  \(\lVert r_{c,t}\rVert=\lVert r_c\rVert\sin\phi_0\). At the
  outer setting, \(40\,\mathrm{mm}\) is the configured total tool-axis
  displacement \(\lVert r_c\rVert\), whereas \(6.47\,\mathrm{mm}\) is its
  tangential projection at the achieved pose-based \(9.30^\circ\) initial
  angular-offset magnitude,
  stated to two decimal places. Never present the projection as a second
  configured CoC magnitude.

  **The reference direction is \(-n_s\), not \(n_s\)**, and the earlier wording
  `the angle between the tool axis and \(n_s\)` was corrected on 2026-08-25.
  A flat tool axis points into the surface, so measured from \(n_s\) the
  nominal angle is \(170^\circ\) rather than \(10^\circ\). The arithmetic
  would survive that direction error because
  \(\sin(180^\circ-\alpha)=\sin\alpha\). The same sine therefore follows from
  either reading. State the geometry the zero-offset target already fixes —
  \(n_d=-n_s\), further up this list — rather than one that
  happens to give the same number. Say which controller input generated the
  condition, but evaluate the projection with the achieved pose-based initial
  angular-offset magnitude rather than the configured value.

  **\(r_c\times f_n=r_{c,t}\times f_n\) is the load-bearing result.** The
  normal component of the displacement drops out of the normal-press moment,
  so only the tangential part acts. State it in the theory and cite it in
  the tool-axis supporting check rather than re-arguing the cross product there.
- **The frame distinction is an implementation option, not an experimental
  variable.** The theory may distinguish the surface-fixed and tool-fixed
  transformations because both branches exist in the controller. Every
  reported non-zero displacement uses the tool-fixed definition in
  end-effector coordinates. Surface-frame components in tables and plots are
  derived projections used to describe direction; they are not a second
  configured definition. Do not restore the former definition-frame
  experiment.
- **Plots and tables carry the actual surface-frame component
  \(r_{c,t_2}\) for the reported \(t_1\) experiments, never a sign-flipped
  stand-in.** For the direction generated by the \(+10^\circ\) configured
  offset, the corresponding outer position is \(+40\,\mathrm{mm}\). Never
  adjust a reported value to make a coordinate look tidy.
- **Every reported non-zero displacement was configured tool-fixed, in
  end-effector coordinates.** The mapping for the active Case-D comparison is
  \(r_{c,t_2}=-\) `offset_ee_y`, checked against the experiment overlays on
  2026-08-25. The plotted coordinate is its surface-frame projection in the
  flat target orientation rather than a surface-fixed configured vector.

  **Chapter 4 says this where Case D is introduced, not only in the
  appendix.** The theory distinguishes a surface-fixed displacement from a
  tool-fixed one whose base-frame vector rotates with the end effector, and
  Appendix C records which the campaign used; Section 4.4 said only that the
  tangential position was varied along the tangent perpendicular to the
  configured offset direction. A reader therefore had every reason to take
  \(r_{c,t_1}\) and \(r_{c,t_2}\) for surface-frame coordinates held constant
  throughout the experiment, which is not what the implementation does. Three sentences
  were added on 2026-08-25 and later simplified: all non-zero displacements
  were configured tool-fixed in end-effector coordinates, and the tangential
  coordinates reported for Case~D are their surface-frame projections in the
  flat target orientation. This is a statement of what was configured, not a
  second derivation.
- **The model-estimated external wrench is not theory, and Chapter 2 does not
  carry it.** The former Section 2.4.4 and the commanded-versus-model-estimated
  half of Section 2.7 are deleted, and Figure 2.2 is a commanded-wrench figure
  only. Neither was needed to derive the impedance law or the compliance-centre
  mechanism, and both interrupted the one narrative the chapter has to carry:
  \(r_c\to\mathrm{Ad}(r_c)\to K_{\mathrm{TCP}},D_{\mathrm{TCP}}\to
  m=m_R+r_c\times f\to\) the tangential direction rule.

  **It survives as an implementation signal only.** The `Contact Establishment`
  subsection says in one short passage that libfranka
  supplies it, that it is stored at the clearance transition, and that the
  estimated external moment change can trigger the optional termination
  condition. Describe that optional path in words rather than promoting its
  values to flow-chart or thesis-wide symbols. Every reported experiment terminated
  through the timeout instead. The data-format appendix retains the literal
logged field names and bias columns. That is the whole of it.

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
  thesis-wide mathematical symbols and is referred to in words only in the
  `Contact Establishment` subsection of Chapter 3.
  `F_{n,\mathrm{cmd}}`, `M_{t_i,\mathrm{cmd}}`,
  `F_{K,n}` and `f_{K,n}` are withdrawn. \(\tau_{\mathrm{cmd}}\) keeps its
  index because it is a joint torque rather than a Cartesian wrench component.

  \(F_n\) is the commanded normal-force component, and \(f_n=F_nn_s\) is
  the corresponding vector. Say so once where both first appear rather than
  leaving the reader to infer it.

  **Estimated quantities use the lower index \(\mathrm{est}\), never a hat.**
  Where a standalone supporting report needs local symbols for the
  model-estimated external wrench, use forms such as
  \(f_{\mathrm{est}}\), \({}^{O}\!m_{O,\mathrm{est}}\), and
  \(M_{t_1,\mathrm{est}}\). This local report notation does not create
  thesis-wide symbols; the main chapters continue to refer to the signal in
  words. When a standalone report references every estimated quantity to one
  stored clearance value, state that convention once and omit a repeated
  \(\Delta\) from the local symbols.

  **Treat a wrench frame change as a spatial transformation.** Libfranka's
  `O_F_ext_hat_K` is the external wrench acting on stiffness frame \(K\),
  expressed relative to base frame \(O\). Expressing the wrench relative to
  \(O\) includes the base-origin moment; the subscript \(K\) identifies the
  frame on which the wrench acts, not the origin of the expressed moment. The
  base-relative moment is shifted to \(K\) through
  \({}^{O}\!m_K={}^{O}\!m_O-p_K\times{}^{O}\!f\). When
  \({}^{EE}T_K=I\) has been verified, \(p_K=p_{\mathrm{TCP}}\) and this is
  \({}^{O}\!m_{\mathrm{TCP}}={}^{O}\!m_O-
  p_{\mathrm{TCP}}\times{}^{O}\!f\). For a bias-subtracted change, transform
  both endpoint wrenches before subtraction when the reference position
  changes. The shorter form \(\Delta m_{\mathrm{TCP}}=\Delta m_O-
  p_{\mathrm{TCP}}\times\Delta f\) assumes a fixed reference position and
  \(K=\mathrm{TCP}\).

  **Keep libfranka's wrench sign and the orientation-error sign separate.**
  `O_F_ext_hat_K` is positive for a wrench applied by the robot to the
  environment. Do not negate it as though the signal were a contact sensor
  reporting the environment-on-robot reaction. A clearance-referenced value
  is a change from the stored estimate, not an absolute endpoint contact
  wrench, so its action--reaction counterpart does not explain a preceding
  motion. The controller's rotational error maps the current orientation to
  the desired orientation. When the desired orientation is the held entry
  pose, the entry-to-end rotation has the opposite sign to the endpoint error.

  **Name the action--reaction quantity by the bodies, not by the operator.**
  In an equilibrium explanation, call the opposite-sign physical quantity the
  `external moment exerted on the robot`. Do not call it a `hand moment`; the
  term is specific to one way of applying the load and does not describe
  surface contact or another external interaction. A local symbol may use the
  directional index \(M_{t_1,\mathrm{ext\to robot}}\).

  **The orientation-offset family carries `offset`, not `cmd`.**
  `\theta_{\mathrm{tilt}}` and `R_{\mathrm{tilt}}` are withdrawn, written here
  as literal strings so a rename cannot revive them. `tilt` was the last place
  in the notation where the word survived, and it named three different things
  at once — the physical tool tilt, the configured offset, and the measured
  response — while the prose ban on `tilt` under *Naming a technical quantity*
  had already removed it everywhere else. The settled chain is
  \(\theta_{\mathrm{offset}}=\theta_{\mathrm{offset},t_1}t_1+
  \theta_{\mathrm{offset},t_2}t_2\), its magnitude
  \(\lVert\theta_{\mathrm{offset}}\rVert\) as the configured offset angle, the
  unit axis \(u_{\mathrm{offset}}=\theta_{\mathrm{offset}}/
  \lVert\theta_{\mathrm{offset}}\rVert\), and
  \(R_{\mathrm{offset}}=R(u_{\mathrm{offset}},
  \lVert\theta_{\mathrm{offset}}\rVert)\)
  through the Rodrigues relation of Section 2.3.

  The index is what separates the configured input from the response
  \(\gamma_{t_1}\)
  and from the physical tool orientation, neither of which the thesis measures
  in the same frame, so it distinguishes rather than decorates. That is the
  difference from the withdrawn wrench indices: nothing was ever going to be
  confused with `F_{n,\mathrm{cmd}}`, because no estimated normal force is
  reported at all. The scalar components retain both `offset` and their tangent
  index: \(\theta_{\mathrm{offset},t_1}\) and
  \(\theta_{\mathrm{offset},t_2}\).
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
  | \(r_c\times f\) | commanded | compliance-centre contribution |
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

  **Say which quantity is commanded.** \(m\) is what the controller computes
  and what the experiments report, through
  \(M_{t_i,\mathrm{cmd}}=t_i^\top m\); the implementation forms
  \(K_{\mathrm{TCP}}\) and \(D_{\mathrm{TCP}}\) and returns the complete
  wrench. The analytical contribution \(r_c\times f\) explains the mechanism
  and supplies the lever-direction relation; it is not a separately commanded
  signal.

  This is a rule about **symbols only**. Ordinary prose such as `the press`,
  `the normal press` or `press-induced moment` describes the physical action
  and stays.
- At an effective physical contact point, the instantaneous moment relation is
  \({}^{O}\!m_{\mathrm{TCP},\mathrm{est}}=
  (p_{\mathrm{contact}}-p_{\mathrm{TCP}})\times
  {}^{O}\!f_{\mathrm{est}}+{}^{O}\!m_{\mathrm{contact},\mathrm{est}}\).
  The selected geometric point \(p_{\mathrm{Tool}}\) is not automatically the
  physical contact point. For a bias-subtracted change, retain both endpoint
  lever--force products unless the effective contact lever is explicitly
  treated as constant. Force is independent of the reference point; moments
  carry one because they are not.
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
- configured orientation offset and achieved pose-based initial angular offset;
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
a completed case identifier to an unfinished, exploratory, or diagnostic trial.
The case counts must reconcile with the stated total number of analysed measurements.
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

**The disturbance-interval quantities carry no `dist` suffix.** Agreed
2026-09-02. They are \(\Delta\sigma_{\min}\) and \(\Delta\eta\), defined once in
Section 4.6.3 and used unchanged in Chapters 5 and 6 and in the symbol list.
The subscript restated the evaluation interval that the defining equation
already fixes, and it made two short symbols long enough to break across lines.
The maximum Cartesian position error is \(\lVert e_p\rVert_{\max}\), used in
the figure paragraph and in Section 5.2.2 rather than the worded `peak
Cartesian position error`. The waveform quantities \(f_{\mathrm{dist}}\),
\(\tau_{\mathrm{dist}}\), \(F_{\mathrm{dist}}\) and \(s_{\mathrm{dist}}\) keep
their suffix: there the word distinguishes the commanded disturbance from the
measured signals beside it.

**\(\Delta\eta\) is reported in degrees, like \(E_N\).** Agreed
2026-09-02. Both are angles whose unit is the radian, and panel~(c) of the
pose-hold figure is read against panel~(a), so one unit is used for both: the
axis is `Net Displacement, \(\Delta\eta\) [°]`, the bar values are printed
to three decimals as the \(E_N\) values in Section 5.2 are, and Chapters 5
and 6 carry the degree value alone. Section 4.6.3 states the unit once, in the
sentence \(E_N\) already carried — `The unit of \(\Delta\eta\) is radians,
and the values are expressed in degrees` — and the symbol-list row keeps
`[rad]` with the conversion named in its description, again as \(E_N\) does.

**The radian value is not kept in brackets beside it.** Chapters 5 and 6 had
read `\(0.131\,\mathrm{rad}\) (\(7.51^\circ\))`, which states one
measurement twice and makes the reader choose. Worse, the bracketed degrees had
been converted from the *rounded* radian value rather than from the data, so
two of the four were wrong in the last digit: the inactive mode is
\(7.517^\circ\) and not \(7.51^\circ\), and \(k_\sigma=1.5\,\mathrm{N\,m}\)
is \(0.015^\circ\) and not \(0.017^\circ\). **Convert from the measurement,
never from the printed value**, and check any surviving pair of units in the
thesis against the derived summary before trusting it.

**`fixed` is not used of the compliance centre.** Agreed 2026-09-02, first for
`fixed displaced centre` and `fixed displacement` and then for `a fixed CoC`.
Write `a displaced centre`, `a displaced CoC`, `the CoC displacement`, and,
where several positions were compared, `different CoC positions`. The centre is a configured parameter that does not change during
a trial, so `fixed` adds nothing to `displaced` and invites the reader to look
for a moving centre that the study never tested. Worse, `fixed` already carries
a precise and unrelated sense in `tool-fixed` and `surface-fixed`, so a reader
meeting `a fixed CoC` in Section 1.3 has to rule out the frame reading first.
Four uses were rewritten, in Sections 1.3, 1.4 and 6.1.

Two neighbouring terms are **not** covered by this and must survive it.
`tool-fixed displacement` and `surface-fixed displacement` name the frame the
displacement is fixed in, which is the distinction Sections 2.7 and 3.2.7 turn
on. And `a fixed centre position` in the limitations means the position was
held constant through contact, stated against `a centre position changed during
contact`, which the study did not cover. Check which sense is meant before
removing the word.

**State which setting won on which quantity.** Corrected 2026-09-02. The
pose-hold conditioning comparison had read `\(1.5\,\mathrm{N\,m}\) achieved
comparable suppression of net displacement with substantially less redundant
motion`, in Section 5.2.2 and again in the conclusion. It is the wrong way
round on the first quantity: \(2.0\,\mathrm{N\,m}\) left the smaller final
displacement, \(0.006^\circ\) against \(0.015^\circ\), and reduced it by
\(99.9\,\%\)
against \(99.8\,\%\). What the higher magnitude cost was cumulative motion,
\(E_N\) rising from \(0.283^\circ\) to \(1.619^\circ\). Both chapters now
state the trade-off in that order. Where two settings differ on two quantities,
name the quantity each one wins on rather than declaring one setting better.

**A time-course observation is stated plainly, and may carry the times read
off the traces.** Amended 2026-09-02, twice. The rule first required a sentence
marking the comparison qualitative, and that caveat was withdrawn from
Section 5.1.3 the same day it was written. It then said the observation carried
no rate metric at all, and that half is now withdrawn too: Section 5.1.3 states
that the response at \(r_{c,t_2}=40\,\mathrm{mm}\) reaches its approximately
steady value at about \(2.3\,\mathrm{s}\) and the TCP response at about
\(3.6\,\mathrm{s}\), roughly \(1.3\,\mathrm{s}\) later. Section 6.1 keeps
the qualitative form.

Three conditions make such a reading admissible, and all three have to hold.
The time is read from a plotted trace the section already cross-references, so
the reader can check it against the figure. It is hedged to the digit the trace
supports — `about`, and one decimal — because a settling time read off a curve
is not a fitted quantity. And the paragraph has already said whether the traces
are single repetitions or means. Do not promote such a reading to a defined
metric, a table column, or a symbol; it stays a statement about what the figure
shows. The scope of the campaign is set out in Section 6.2 rather than repeated
beside each observation.

**The two null-space terms were evaluated separately, and the text says so.**
Corrected 2026-09-02. The third contribution bullet had read `a projected
null-space controller combining joint damping and singular-value conditioning
was implemented and evaluated separately`, which reads as one combined
controller that was evaluated apart from the contact study. Section 4.6 lists
four settings -- no null-space torque, projected damping alone, and
conditioning at \(k_\sigma=1.5\) and \(2.0\,\mathrm{N\,m}\) -- so the two terms
were never active together in the pose-hold trials. Write `Projected null-space
damping and singular-value conditioning were implemented and evaluated
separately in Cartesian pose hold`. Mode 3, where both act together, belongs to
the surface-contact cases only.

**A quantity is discussed where its figure shows it.** Agreed 2026-09-02.
\(\Delta\sigma_{\min}\) appears in panel~(b) of the pose-hold figure, which
carries only the two singular-value-conditioning settings, so it is discussed
in Section 5.2.2 and not in the projected-damping subsection. Section 5.2.1
reports what panel~(a) and panel~(c) show: the cumulative motion \(E_N\) and
the net displacement \(\Delta\eta\). The withdrawn paragraph had explained
that damping did not drive the robot towards a larger \(\sigma_{\min}\),
which is a property of the conditioning term stated where that term is
compared. Its \(-1.26\times10^{-3}\) damping-mode value left the thesis with
it; the \(-2.13\times10^{-3}\) inactive-mode value remains in Section 5.2.2
as the comparison baseline. \(\Delta\sigma_{\min}\) itself stays defined in
Section 4.6.3, named in the figure paragraph, and listed in the symbol list.

**Say `net displacement`, not `net redundant displacement`.** Agreed
2026-09-02. \(\Delta\eta\) is already a projection onto the null-space
reference direction, so `redundant` restates the projector.

**A results paragraph does not narrate its own error bars.** Agreed 2026-09-02
for the pose-hold figure paragraph. Say what each panel shows and what the
shaded bands indicate in one clause -- `the spread across the repeated trials`
-- rather than repeating `\(\pm\) one standard deviation` once per panel. The
sample standard deviations are tabulated in Appendix D, and the repetition
count is stated once at the head of the chapter.

## Results and conclusion priorities

The reported contact campaign is restricted to configured orientation offsets
about \(t_1\). The principal experimental conclusions are:

1. Within the tested range, tangential compliance-centre position produced the
   largest response variation. Every tested non-zero tangential position
   increased the response in one rotational direction and reduced it in the
   other relative to the TCP-centred condition.
2. Raising \(K_{R,t_1}\) reduced the measured response over the tested range.
3. Varying the perpendicular translational stiffness \(K_{p,t_2}\) produced
   only a \(0.03^\circ\) response span and was smaller than the rotational-
   stiffness effect.
4. At the TCP, the measured end-effector rotation was towards parallel
   alignment with the configured surface in both tested directions of rotation
   about \(t_1\). The TCP-centred condition added no CoC-induced moment and
   therefore favoured neither rotation direction, while a displaced centre
   produced a larger alignment response when selected for a known rotational
   direction.

No result comparison, conclusion, caption, table, or active plot reports an
experiment with a configured orientation offset about \(t_2\). The symbol
\(t_2\) remains
where it denotes the second surface-frame axis or the perpendicular coordinate
of a \(t_1\) experiment, including \(K_{p,t_2}\) and \(r_{c,t_2}\).

### What the contact study is investigating, and in which order

The contact chapters are built on one open question, stated in running text and
never as a heading (the question-framing ban above still binds): **in the
intended application, the direction and tangent-plane axis of the initial
tool--surface angular offset can be unknown before contact, so the appropriate
location of the centre of compliance can also be unknown.** The experiments
deliberately command both directions of rotation about \(t_1\). The campaign
establishes whether a neutral fixed centre can be selected in advance, or
whether a displaced centre has to be chosen for the known rotational direction.

The narrative is therefore **not** "a displaced centre improves alignment, so
find the best displaced lever". Chapter 1 introduces the question without
answering it. Chapter 4 separates the main A--D matrix from the supporting
checks. Chapter 5 reports the main cases, Appendix D reports the supporting
checks, and Chapter 6 states the result.

The purposes of the main cases are settled and are stated in this order:

| Case | What it establishes |
|---|---|
| A | The contact-induced response with \(p_c=p_{\mathrm{TCP}}\), \(r_c=0\): the zero-coupling reference, not yet an answer. |
| B | Whether rotational stiffness changes the response about \(t_1\). It reduces the response magnitude over the tested range. |
| C | Whether cross-axis translational stiffness changes the response about \(t_1\). Its influence is smaller over the tested range. |
| D | Whether one fixed non-zero tangential centre can increase the response in both directions of rotation about \(t_1\). It cannot: every tested non-zero position increased one direction and reduced the other relative to the TCP. This is the central experiment. |

Appendix D carries no supporting check; the tool-axis comparison was
withdrawn on 2026-09-01.

The measurement hierarchy is fixed. The main A--D study contains 19 settings
and 57 surface-contact trials. The null-space pose-hold study adds four
settings and 12 trials, giving 69 trials in the complete reported data set.
Shared reference conditions are counted with the main case in which they first
appear.

The synthesis is that \(p_c=p_{\mathrm{TCP}}\) provides the neutral fixed centre
for the reported \(t_1\) study because it selects no tangential lever direction.
A displaced centre produces a larger alignment response when its position is
selected for the corresponding initial angular-offset direction.

The design sequence that follows from this — start at the TCP, evaluate the
required alignment, introduce a direction-selected shift where more authority
is needed, and return to the TCP afterwards — is **controller-design
interpretation and future work**. Only the first two steps of it were
implemented and measured; do not present the scheduling and the return as
completed adaptive functionality.

### The shifted centre is an alignment mechanism, not a steady-contact centre

**Do not summarise the compliance-centre result as "find the best non-zero
  lever and use it."** That reading does not survive the model. The contribution
  \(r_c\times f\) does not vanish when the tool reaches a flat
orientation: as long as a normal press is present and \(r_c\neq0\), a fixed
tangential lever keeps commanding rotation in one direction, whether or not
alignment has already been achieved. A lever selected for one direction of the
initial angular offset therefore carries its preferred rotational direction
into the steady contact afterwards.

The defensible summary separates two regimes:

- **Transient alignment.** A tangential displacement supplies a moment whose
  direction depends on the displacement direction from the TCP. The \(t_1\)
  measurements show that every tested non-zero position increased the response
  in one rotational direction and reduced it in the other.
- **Sustained contact.** \(r_c=0\) gives \(r_c\times f=0\), so the TCP is the
  neutral centre: no preferred tangential direction, and the tool responds to
  the actual contact geometry.

The implemented state structure already embodies this, and the thesis says so:
the point-shifted impedance is used during Contact Establishment, while the Grinding state
returns to the decoupled branch. That is **architecture consistency, not
experimental evidence**: the reported quantitative experiments ended at the
pre-grinding hold.

**This argument is the second reason for the TCP, not the first.** The first is
the neutral fixed reference needed when the initial direction of rotation about
\(t_1\) is unknown. The sustained-contact reading follows it and is written as the consequence it is:
once the press continues after alignment, a retained tangential lever also
retains its preferred coupling-moment direction, so \(r_c=0\) is the
appropriate neutral virtual reference for the state that follows.

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

**The settled term for the reported campaign is `neutral fixed centre`, and
it is qualified wherever it appears.** It denotes the TCP-centred condition
\(r_c=0\), which selects no tangential lever direction.

**Neutral means neutral with respect to \(r_c\times f\), never equal
response magnitudes.** Agreed 2026-09-01. The TCP-centred responses were
\(+7.57^\circ\) and \(-10.83^\circ\), so a bare `neutral fixed centre`
invites a reader to infer a symmetry the measurements do not show. State the
sense with the term: the condition is neutral because \(r_c=0\) gives
\(r_c\times f=0\), so it adds no \abbr{CoC}-induced moment and favours
neither rotation direction, and it is not neutral in measured response
magnitude. Chapter 6 carries both halves in adjacent sentences. Do not use `sign-independent fixed centre`; the two angular
conditions are described as directions of rotation. The claim is specific to
one robot, one tool, one configured surface reference, one press trajectory,
and the tested centre positions.

Where the claim is stated, scope it to rotation about \(t_1\). At the TCP, the
measured end-effector rotation was towards parallel alignment with the
configured surface in both tested rotational directions. Every tested non-zero position increased the response
in one direction and reduced it in the other relative to the TCP-centred
condition. The neutral default therefore avoids selecting one rotational
direction in advance. Do not claim that it was the only tested position with a
response towards parallel alignment with the configured surface in both
directions; the small outer-position responses also represented rotation
towards that alignment.

**`universally optimal centre` remains banned, as does `best` and `optimal` for
any centre.** So does any statement extending the result to every robot, tool,
contact geometry, surface, grinding process, or impedance controller. The
surface-contact campaign did not test a displacement held through sustained grinding, and did
not vary the surface orientation during contact; say that where the claim is
made.

**Neutrality and a direction-specific alignment response are separate
properties, and the thesis states the separation at least once in Chapter 5 and
once in Chapter 6.** Write that the TCP provides the neutral fixed reference
for the reported \(t_1\) study, and that a displaced centre produces a larger
alignment response when its position is selected for a known direction of
rotation.

**`rotational authority` is withdrawn.** Agreed 2026-09-01: it names no measured
quantity, and the thesis has two exact statements for what it reached at --
`a larger alignment response` for the measured outcome, and `an additional
commanded moment` for the mechanism. Use whichever the sentence is about.
`neutral fixed reference with no direction-selected lever` goes with it: write
that the TCP-centred condition adds no CoC-induced moment and therefore favours
neither rotation direction. `neutral fixed centre` survives as the settled term
for the condition itself.

**No informal manual test, demonstration, or video is reported anywhere in the
thesis.** This overturns an earlier ruling that admitted the pre-grinding hold
observation as labelled qualitative evidence. That paragraph has been removed
from Chapter 5. The reason for the change is that a hand-applied check carries
no controlled condition and no measured quantity, so a reader cannot separate
it from the measured cases however carefully it is labelled. The
  sustained-contact argument does not need it: it rests on the mechanism, that
  \(r_c\times f\) persists while the press is present, and on the
Case-D measurements.

### Scope of the reported tangent-axis result

The reported contact results cover rotation about \(t_1\) only. The end
effector rotated towards parallel alignment with the configured surface at the
TCP for both tested directions of rotation, while the selected tangential lever changed the
response only slightly for the direction generated by the \(+10^\circ\)
configured offset. This is consistent with contact geometry and
tool-mount compliance contributing to the response, but those contributions
were not isolated. The conclusion must not claim that either mechanism was
sufficient on its own, and it must not generalise the result to rotation about
another tangent.

**Every rotation claim names the body that rotated.** Because the physical tool
orientation is never measured independently, a sentence may say the **end
effector** rotated, never that "contact rotated the tool":

When the direction of \(\gamma_{t_1}\) is contrasted with the motion it
represents, write `the measured end-effector rotation from the start to the end
of Contact Establishment`. Do not call that motion a physical rotation without
naming the end effector.

| Was | Now |
|---|---|
| contact still rotated the tool | contact still produced end-effector rotation |
| the physical tool may have rotated further than the end effector did | the physical tool may have undergone additional rotation relative to the end effector |

`further` is wrong even as a hedge, because it implies the direction of the relative
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
rotation was **not tracked separately during the contact experiments**. The blanket
phrasing claims the measurement was never made, which is wrong and gives away a
result the thesis actually has.

The general point is that **an alignment-directed end-effector rotation is not
an independent measurement of physical tool alignment**.

Two claims must not be made from this:

- **Not that the TCP is the best centre, or the optimal one.** The defensible
  claim is that the TCP is the neutral fixed reference about \(t_1\), since it
  adds no virtual coupling moment and selects no tangential direction. A
  displaced centre may produce a larger alignment response for a known
  direction of rotation.
- **Not that the lever magnitude scales an alignment time.** Narrowed
  2026-09-02, replacing a blanket ban on any timing claim. The contact
  establishment interval was fixed at \(5\,\mathrm{s}\), and no
  alignment-time metric was defined, tabulated, or compared across the tested
  lever magnitudes, so no dependence of a settling time on
  \(\lVert r_{c,t}\rVert\) may be asserted. What may be said about magnitude
  is the model statement: for the same elastic press and a perpendicular lever,
  the predicted contribution is proportional to \(\lVert r_{c,t}\rVert\).

  What the ban had also been catching, and should not have been, is the reading
  of a settling time off a plotted trace. Section 5.1.3 gives the two times of
  the Case-D wrench figure under the conditions in *A time-course observation is
  stated plainly* above. Those are two positions of one comparison, hedged and
  traceable to the panel, not a metric fitted across the magnitude range.

Basic settling, formulation-equivalence, and repeatability checks support the
measurements but should not dominate the conclusion.

**The conclusion summarises the results chapter; it does not reproduce it.** A
separate entry of equal length for every case repeats Chapter 5 and obscures the
main ordering. Keep continuous prose, with one compact headline percentage for
each main Case A--D result.

**The opening sentence of Chapter 6 names the measured quantity, not an
alignment.** `implemented for contact-induced alignment of a rectangular tool
with a configured surface reference` was withdrawn on 2026-09-01: it claims a
physical tool--surface alignment, which Section 6.2.2 states was never measured
independently, so the chapter's first sentence contradicted its own
limitations. The settled form is `implemented to generate compliant
contact-induced end-effector rotation towards the configured surface-parallel
orientation`. **`configured surface-parallel orientation` is the noun form**
of the alignment wording settled above; `parallel alignment with the
configured surface` remains the form used when the state is meant.

**The Case-D finding is stated as direction selection, before its
percentages.** Within the tested range, a fixed displaced centre acted
principally as a direction selector rather than as a means of increasing the
response: it raised the response slightly in the favourable direction and
reduced it almost entirely in the opposite one. A conclusion that opens on
\(4.0\,\%\) and \(97.6\,\%\) leaves the reader to infer that finding
from the arithmetic.

**The conditioning result is qualified by when the term was active.** Write
that the complete singular-value-conditioning modes were active before and
during the disturbance and produced net displacements close to zero.
`conditioning kept the net displacement close to zero` reads as isolated
disturbance rejection, which the timeline rules out.

The conclusion instead states the main findings as continuous prose: the
controller was implemented and active in every reported experiment;
compliance-centre position had the largest measured influence; every tested
non-zero position increased the response in one rotational direction and
reduced it in the other about \(t_1\); and the stiffness effects were smaller. The isolated
null-space result remains bounded to free-space hold under the commanded
force-equivalent.

The conclusion supplied on 2026-09-02 replaced the earlier rule that it carry
the Case A--D headline percentages with their reference conditions. It names no
case at all, and rounds the direction-dependent figures to `approximately
\(4\,\%\)` and `approximately \(98\,\%\) to \(99\,\%\)`, keeping the exact
\(4.0\), \(4.3\), \(97.6\) and \(99.2\,\%\) values in Chapter 5 where the
comparison is made. The percentages that stay exact in the conclusion are the
ones stated against a named reference condition: \(81.3\), \(115.1\),
\(63.9\) and \(0.4\,\%\). Standard deviations and the absolute values stay in
Chapter 5. A further value appears only where it carries a physically
meaningful bound, such as the largest measured position error against its
acceptance limit.

**The conclusion explains the mechanism before the numbers.** As supplied on
2026-09-02, it opens on what shifting the centre does to the stiffness and
damping matrices -- the off-diagonal coupling, and the virtual lever arm that
generates \(r_c\times f\) -- and only then reports what changed in the
measurements. It also states what each result means for using the controller:
the TCP-centred centre suits the final configuration after alignment because it
removes the directional preference, and an adaptive strategy can displace the
centre for the offset direction and return it to the TCP once alignment is
established. Those two sentences are conclusions drawn from the measurements,
not future work, and they stay in Section 6.1.

**Each case section explains its own case, and does not compare across cases.**
Agreed 2026-09-02. Two cross-case paragraphs were removed from the end of
Case~D: the one ranking the response variation of the tangential centre against
the two stiffness effects, and the one giving the direction-dependent
percentages relative to the TCP-centred magnitudes. Both compared Cases~B,
C and D rather than explaining Case~D, and the conclusion already carries the
ranking with its percentages. Nothing was lost by the removal: the
\(4.84^\circ\) and \(0.03^\circ\) spans are stated in Cases~B and C where they
are measured, and the \(7.69^\circ\) and \(11.21^\circ\) Case-D spans are the
difference between endpoint values the case still reports. A case section ends
on what its own measurement shows.

**Target length.** Chapter 6 should sit at roughly half the length of the
results chapter it summarises. The reduction comes from cutting duplication,
not from dropping findings.

The central findings the conclusion must carry are: the stiffness parameters
had a relatively small effect; compliance-centre placement had the largest
measured effect; its required displacement direction depended on the known
direction of rotation about \(t_1\); and null-space conditioning was isolated in free-space
Cartesian pose hold, while the combined mode and a physical disturbance remain
untested.

Settling, formulation-equivalence, and repeatability checks belong in Chapter 5.
Do not restate them in the conclusion.

Do not give every case section the same length. Case D is the principal finding
and carries the longest treatment; Case C's effect was limited and its
treatment is short. In Chapter 6, the four headline percentages remain within
continuous prose and do not recreate the complete case structure.

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
| Direction-dependent centre-position response | Case D, where each displaced centre increased one rotational direction and reduced the other |
| Measurement interpretation | Case A and the response definition |
| Implications for parameter selection | Main-results synthesis after Case D |
| Scope of interpretation | deleted; Chapter 6 *Limitations* already carried it |

The editorial unit is **question, then figure or table, then observation, then
interpretation, then conclusion** — and then the next question. A case section
states what it tests before its table, and its interpretation follows its own
figure rather than waiting several pages.

A plot that is an evaluation consistency check rather than a finding does not
interrupt the argument; it goes to the supporting-plots appendix and is
referred to from the chapter.

**Every supporting plot must carry something its table does not.** The appendix
is not a place to keep every available plot: a figure that reaches the same
conclusion as its table is removed, however correct it is, because an appendix
of near-duplicates reads as accumulation rather than judgement.

**Appendix D now carries no figure at all.** The tool-axis against tangential
displacement plot was the one supporting figure this rule admitted, and it was
withdrawn on 2026-09-01: the main Case-D comparison already plots the
tangential curve, and the two response spans it added are two numbers that its
own table states exactly. Do not restore it. The rule stands for any future
supporting plot.

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
`Scope of the Surface-Contact Results`; `Calibration and Measurement Scope`;
`Tool-Mount Compliance`; `Scope of Null-Space and Real-Time Validation`. The
first, second and fourth were renamed on 2026-09-01 to say that each subsection
bounds a scope rather than cataloguing faults, and each opens by stating what
the measurement does cover before naming what lies outside it. The `\label{}`
keys were left unchanged, since they reach no reader. A reader can
then find the limitation that bears on the result they are checking, instead of
reading a catalogue.

**Prioritise Future Work; do not mirror the limitations one for one.** Deriving
exactly one proposed experiment from each limitation produces a complete,
evenly weighted list that reads as generated. State the three extensions
considered most important, each with the question it would settle, then cover
the remainder briefly in a single paragraph.

**Do not number the priorities in the prose.** `The first priority is`, `The
second priority is`, `The third priority is` was withdrawn on 2026-09-01: three
paragraphs opening on the same frame is the templating that *The templated
section* rules against, and the ordinal asserts a ranking the thesis does not
defend. Name the three areas in one lead-in sentence, then give each its own
paragraph opening on its subject.

**Every limitation with a practical next step gets one.** Section 6.2.4 records
that worst-case execution time and scheduling jitter were not measured, and
that the assembled command carried no application-side saturation or
torque-rate limiter. Future Work carries the corresponding paragraph: measure
callback execution time and jitter at \(1\,\mathrm{kHz}\), and implement
and evaluate a final saturation and rate-limiting stage alongside the
robot-side monitoring. This is not a reversal of the rule above, which forbids
a mechanical one-to-one mirror, not the inclusion of a real next step. For this thesis the three are a
repeated \(t_2\) and additional tangent-plane evaluation with improved tool
constraint, independent measurement of the tool-face angle, and a combined-mode
null-space study with a physical disturbance.

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

When measurements are taken for a calibrated pilot after the main campaign:

- label it as a separate pilot and do not silently add it to the earlier experiment
  count;
- state which earlier experiments are decoupled controls and which experiments activate the
  point-shifted law;
- report the controller lever using
  \(r_c=p_c-p_{\mathrm{TCP}}\), its surface-frame displacement direction, and
  its value rather than calling it simply “left” or “right”;
- keep the measured end-effector response separate from any operator-observed
  contact state when tool-to-gripper motion is unmeasured;
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
\needspace{3\baselineskip}%
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
- search for `task`; `task frame` and `R_{\mathrm{task}}` must return zero in
  running text, headings and the symbol list, and every surviving hit must be a
  standard redundancy-resolution term, a literal
  source identifier, a `\label{}` key, or an application credited to a cited
  source. `the investigated task` and `the Cartesian task` must also return
  zero;
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
- grep the Abstract and the Kurzfassung for digits, and check each hit against
  the permitted set under *Abstract and Kurzfassung*: the Case~A--D headline
  percentages with their reference conditions, the rotational-stiffness
  interval, the largest Cartesian position error against its limit, and numbers
  that name a thing rather than measure one, such as the robot's degrees of
  freedom. A per-condition response mean, an achieved offset, a
  compliance-centre coordinate, or a measurement count is a fault;
- check that the two summaries carry the same values, and that a number added
  to one was added to the other;
- check Abstract, Kurzfassung, Results, and Conclusion for identical certainty;
- remove duplicated theory and unsupported causal claims;
- compile `Thesis.tex`;
- resolve undefined references and overfull boxes;
- visually inspect changed pages.

The final test for every sentence is whether it belongs in a robotics/control
thesis whose reader knows nothing about the author’s repository, coding
history, or earlier drafts.
