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
similar. State the investigated dependencies directly. For example:

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

**Keep measured values out of the Abstract, with one exception.** No degrees, no
stiffness values, no distances. State the direction, the ordering, and the sign
of an effect instead: `reduced the measured alignment response`, `no tested
setting improved on the most compliant baseline`, `differed between the two
surface tangent directions`.

The one exception is the **magnitude of the strongest measured effect**:
`approximately 6 degrees of improvement` gives the reader the scale of the
headline result. Everything else — stiffness values, per-condition means,
standard deviations — stays out.

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
passive: `the rotational stiffness was raised`, `the plane was fitted from three
probed points`, `the controller was implemented`. Naming a case or the thesis as
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
quantity, comparison, geometry, or parameter set.

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
  defined about, \(p_c\), with \(r_c=p_{\mathrm{TCP}}-p_c\) as its lever.
  Attributively, `compliance-centre lever`, `compliance-centre coordinate`.
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
  the geometric contact reference, \(p_T\), with the **tool
  contact-reference offset** \(r_T=p_T-p_{\mathrm{TCP}}\) as its lever. It is
  a different point from the centre of compliance and the two are never used
  for one another.

  **State at its first appearance that the subscript \(T\) is the tool point
  and not the \(T\) of a homogeneous transformation matrix.** Without that
  sentence the symbol is genuinely ambiguous, and the whole notation depends on
  the reader not making that substitution.

  The symbol was previously \(p_g\), and before that \(p_{\mathrm{contact}}\)
  in this guide while the chapters used \(p_g\). One name now: \(p_T\) in
  every chapter, the symbol list, and every figure, with \(r_{T,\mathrm{EE}}\)
  for its end-effector-frame offset and \(\Delta p_T\), \(s_T\) for its
  displacement. The two levers were at one point \(r_c\) and \(r_C\),
  distinguished only by the case of one letter, which no reader can hold across
  a page and which a printed subscript does not reliably show; \(r_T\) against
  \(r_c\) is the replacement and must not drift back.

  The wording is settled with the symbol: it is the **selected tool point** in
  every chapter, never a `tool feature` and never a bare `edge`. `edge`
  presumes edge contact, and the set-up phase is designed to seat the tool face
  flat.

  **Do not write `selected tool point or edge`.** \(p_T\) is one position
  vector; where an edge leads, the controller uses its midpoint. Say what it is
  once, at the definition — depending on the tool orientation it is a leading
  corner, the midpoint of a leading edge, or the tool centre — and then call it
  the selected tool point everywhere else.

  \(r_{T,\mathrm{EE}}\) is what is **fixed relative to the tool** once the
  contact reference has been selected. Its base-frame representation
  \(r_T=R_{\mathrm{EE}}r_{T,\mathrm{EE}}=p_T-p_{\mathrm{TCP}}\) rotates with
  the tool, so do not write that \(r_T\) is fixed by the geometry: name the
  frame the statement is true in.
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
\(R_{\mathrm{local}}\), matching \(R_{\mathrm{task}}\) in the main text. Rotation
matrices are \(R\) without exception.

Macros defined in `config/commands.tex` (`\vF`, `\mK`, `\R{3}`, …) predate this
convention. `\R{n}` for \(\mathbb{R}^n\) is in active use and stays; the
bold-producing ones are not used in the chapters and should not be reintroduced.

**cleveref cannot type a label set inside a `longtable`.** Both obvious fixes
are wrong and the second is worse, because it looks right in the source:
`\label{}` alone gives the correct number with the wrong type, so `\Cref`
printed `Section 4.4` for a table; `\label[table]{}` fixes the type but builds
the number from the enclosing section prefix, so the same reference printed
`Table 4.3.2` for Table 4.3. Reference a `longtable` as literal
`Table~ef{...}`, which takes its number from `\@currentlabel` and is right
in both respects. Check the rendered words in the PDF, not the source — neither
failure raises a warning.

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
- **Which procedure.** The physical plane was described both as fitted from
  three probed points and as estimated by seating the tool face. Resolved: the
  physical plane comes from **four probed points**, three fitted and one held
  out at \(0.82\,\mathrm{mm}\), repeated three times; the **seatings** measured
  the grinding-face normal, not the surface. The controller holds only the
  configured plane, set from the tilt angles \(a\) and \(b\), and contains no
  calibration routine at all — so any sentence implying the controller measured
  the surface is wrong by construction.

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

### Chapter 3 restructure, agreed and not yet carried out

The chapter must answer one question: *what does the controller do, from the
surface and tool geometry to the torque sent to the robot?* That chain is
currently fragmented, and the fix is to follow the signal path:

1. **Overall controller concept** — short. The chain in words, one block
   diagram, and what runs at \(1\,\mathrm{kHz}\) against what stays outside the
   real-time loop.
2. **Surface and tool representation** — what is stored, without re-deriving
   Chapter 2: surface frame; grinding-face orientation; face geometry and
   contact-point selection, naming \(p_T\) and saying it is neither the TCP nor
   the centre of compliance.
3. **Phase-dependent reference generation** — collected in one place instead of
   scattered after the impedance law. Approach carries
   \(p_d(t)=p_0+s_{\mathrm{app}}(t)(-n_s)\) with
   \(s_{\mathrm{app}}(t)=\min(v_{\mathrm{app}}t,s_{\max})\). **Set-up is the
   most important section in the chapter** and must carry the relation the
   implementation actually evaluates:
   \(p_{g,d}(t)=p_{g,0}+s_{\mathrm{set}}(t)(-n_s)\) and
   \(p_d(t)=p_{g,d}(t)-R_{\mathrm{clr}}r_{g,\mathrm{EE}}\). The controller does
   not push the TCP down; it prescribes where the selected face point should
   move and reconstructs the TCP target that realises it. This was the largest
   thing missing.
4. **Cartesian impedance and virtual centre of compliance** — error and wrench,
   directional gains and inertia-scaled damping merged into one subsection, then
   the compliance-centre shift, closing on the statement that \(p_T\) fixes
   where the interaction happens geometrically while \(p_c\) fixes the virtual
   reference of the impedance, and that moving \(p_c\) does not move \(p_T\).
5. **Real-time torque calculation** — one callback, in order, ending at
   \(\tau_{\mathrm{cmd}}=J^\top F+\tau_{\mathrm{null}}+\tau_c\), with
   \(\tau_{\mathrm{dist}}\) mentioned only for the pose-hold experiment.
6. **Null-space implementation** — short; the theory is in Chapter 2.
7. **Real-time execution, safety and recording** — 1 to 1.5 pages. Detailed
   tool handling and the full logged-column list move to the appendices.

**Delete Table 3.1** (functional subsystems — software documentation the
architecture figure already carries), **Table 3.3** (four null-space modes, one
sentence suffices) and **Table 3.4** (logged signals, which belongs in the
data-format appendix). **Simplify Table 3.2** or drop it: the point is only that
surface-related phases express gains relative to the calibrated surface, pose
hold uses the base frame, and the set-up translational frame is configurable.
**Remove the `robot.control` listing**, which shows nothing the prose does not.

The chapter should come out shorter and stronger, not longer.

Figures to add, in priority order: grinding-face geometry and leading-feature
selection (four vertices, tie tolerance, the corner/edge/face-centre outcomes);
the three points \(p_T\), \(p_{\mathrm{TCP}}\) and \(p_c\) with the two offsets
and their sum; and set-up reference generation, showing the press coordinate
advancing past the surface so the endpoint reads as a spring reference rather
than a commanded penetration.

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
  repeating \(p_T=p_{\mathrm{TCP}}+R_{\mathrm{EE}}r_{T,\mathrm{EE}}\).
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
  quality: three repetitions planned, 171 runs over 57 settings, one incomplete,
  170 analysed.
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

## Evidence and claims

Never invent measurements, repetitions, fitted values, confidence intervals,
p-values, contact locations, timing bounds, or safety conclusions.

Distinguish:

1. measured observation;
2. model-based interpretation;
3. hypothesis requiring another experiment.

Trace every geometric metric through its measurement chain. The controller
reconstructs the tool axis from the EE pose and a nominal tool-to-EE transform.
Because the mounted tool can rotate approximately ±2° about \(y_{EE}\), this
quantity is not a directly measured physical tool-face axis. Do not rename
\(y_{EE}\) as \(t_2\) without transforming it into the calibrated surface
frame. State that the current angular results describe the combined
robot–gripper–tool response and cannot separate controller compliance from
gripper compliance.

**The word `inferred` is not used for it, and neither is `EE-inferred`.** Both
were removed. Name the chain instead: `alignment angle calculated from the
end-effector pose`, `end-effector-based alignment angle`, or `pose-based
alignment angle`.

### Keep the three alignment quantities separate

They are complementary and are never presented as interchangeable measurements
of one thing:

- **Signed set-up rotation** — answers *how far, and in which direction, did
  the end effector rotate during contact?* This is the primary metric for
  comparing controller settings, and it does not depend on the calibrated
  grinding-face direction.
- **Alignment angle calculated from the end-effector pose** — answers *given
  the measured end-effector orientation and the calibrated rigid tool
  direction, how large is the reconstructed tool–surface angular difference?*
  Useful, but it carries the tool-mount assumption, so it is a supporting
  quantity and never independent proof of the physical grinding-face
  orientation.
- **TCP-height flatness criterion** — answers *is the final measured TCP
  position geometrically consistent with the calibrated rectangular face lying
  flat on the surface?* This is the right quantity for calling a condition
  flat, as long as the wording stays explicit that it is geometry-based rather
  than an independent physical orientation measurement. Where it is
  satisfied, write `classified as flat by the TCP-height criterion` or `the
  final geometry was consistent with a flatly seated grinding face`. Never
  claim the physical face angle was measured as zero: the tool orientation was
  not measured independently under load.

**Do not write that a lever was insufficient to align the tool**, or that it
`did not remove the full initial deviation`. Both read as claims about the
physical grinding face, which was not measured. A residual pose-based
alignment angle is not by itself evidence of residual physical tilt, because
relative motion between the tool and its mount was not measured. Report what
was measured — the signed set-up rotation changed from \(-1.63\) to
\(+4.43^\circ\) about \(t_2\) with the selected \(40\,\mathrm{mm}\) lever, and
the final configuration satisfied the TCP-height flatness criterion.

### Three distinct points: selected tool point, TCP, compliance centre

\(p_T\), \(p_{\mathrm{TCP}}\) and \(p_c\) are different points and the prose
must keep them apart.

- \(p_T\) is the selected tool point: the point or edge of the grinding face
  that contacts, or is predicted to contact, the surface. The controller
  determines it from the rectangular face geometry and the current tool
  orientation.
- \(p_{\mathrm{TCP}}\) is the Cartesian reference point of the controller.
- \(p_c\) is the virtual centre of compliance: a software-defined point about
  which the Cartesian stiffness and damping are formulated before being
  transformed to the TCP. It is **not** the physical contact point.

\(p_T\) is **selected at the clearance transition and then held constant
relative to the tool** for the whole of set-up. Say so where it is introduced.
Once the tool starts to rotate under contact it is a geometric contact
reference, not the exact point at which the surface force acts at every
instant, and a sentence that treats it as the latter overstates what the
geometry gives.

The two levers are named separately and never stand in for one another:

- \(r_T=p_T-p_{\mathrm{TCP}}\) is **tool geometry** — the offset from the TCP
  to the selected contact reference, fixed by the face geometry and the current
  orientation. In end-effector coordinates it is \(r_{T,\mathrm{EE}}\), so
  that \(p_T=p_{\mathrm{TCP}}+R_{\mathrm{EE}}r_{T,\mathrm{EE}}\); the
  implementation has \(p_{\mathrm{TCP}}=p_{\mathrm{EE}}\), which is worth
  stating once rather than silently writing \(p_{\mathrm{EE}}\) in its place.
- \(r_c=p_{\mathrm{TCP}}-p_c\) is **virtual controller geometry** — the
  software-defined displacement used by the point-shift transformation of the
  Cartesian impedance. It carries no tool geometry at all.

They combine as \(p_T-p_c=(p_T-p_{\mathrm{TCP}})+(p_{\mathrm{TCP}}-p_c)=r_T+r_c\),
which is worth stating because it separates the physical contact geometry from
the virtual shift.

The contact sequence therefore originates at the selected tool point, not at
the TCP and not at the centre of compliance: the face geometry gives \(p_T\),
the set-up trajectory moves it as \(p_{T,d}(t)=p_{T,0}+s_{\mathrm{set}}(t)(-n_s)\),
and the TCP target is reconstructed from it as
\(p_d(t)=p_{T,d}(t)-R_{\mathrm{clr}}r_{T,\mathrm{EE}}\), which produces the
press. The centre of compliance is a separate mechanism acting through
\(r_c\) on the force–moment coupling. Do not merge the two chains.

**Never write that the compliance centre moves the force application point.**
The physical surface force still acts at the actual contact point. What changes
is the point about which the compliance is defined, and therefore the
translation–rotation coupling: the same normal press produces a different
rotational response as \(p_c\) moves. Give that explanation before introducing
\(r_c=p_{\mathrm{TCP}}-p_c\) and \(m_c=-r_c\times f_{\mathrm{press}}\), not
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

Matched free-space null-space trials now isolate the projected damping and
singular-value terms under an internally commanded point-force equivalent.
Claims from those trials remain limited to that hold condition and must not be
extended to physical disturbances or contact response.

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
- Distinguish the virtual-centre lever \(r_c=p_{\mathrm{TCP}}-p_c\) from the
  physical-contact lever
  \(r_{\mathrm{contact}}=p_{\mathrm{TCP}}-p_{\mathrm{contact}}\). The two never
  appear in the same expression. \(r_c\) shapes the **commanded** wrench through
  \(\mathrm{Ad}(r_c)\); \(r_{\mathrm{contact}}\) only transfers a **measured**
  moment between two reference points.
- The moment transfer is
  \(M_{\mathrm{contact}}=M_{\mathrm{TCP}}+r_{\mathrm{contact}}\times\Delta\hat
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
used for the reported data. A proposed three-point calibration belongs in
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
   improves alignment about \(t_2\) only, and a high rotational stiffness
   removes that benefit.
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
| Weak tool-axis sensitivity | Case F |
| Axis-dependent response | Case A, where the asymmetry first shows |
| Measurement interpretation | Case A, and the flatness summary |
| Implications for parameter selection | Case H, after the direction rule |
| Scope of interpretation | deleted; Chapter 6 *Limitations* already carried it |

The editorial unit is **question, then figure or table, then observation, then
interpretation, then conclusion** — and then the next question. A case section
states what it tests before its table, and its interpretation follows its own
figure rather than waiting several pages.

A plot that is an evaluation consistency check rather than a finding does not
interrupt the argument; it goes to the supporting-plots appendix and is
referred to from the chapter.

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
  \(r_c=p_{\mathrm{TCP}}-p_c\), rather than calling its sign simply “left” or
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
- check that one quantity carries one name and one symbol throughout;
- check that every new equation symbol is introduced by quantity name, symbol,
  and short role at its first use;
- check that every running-text use of a defined quantity name is followed
  immediately by its symbol;
- search the symbol list for `mixed` and for units written without a space;
- check that the contents lists the figures, tables and symbols;
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
- check Abstract and Kurzfassung each still fit one page in the compiled PDF;
- check Abstract, Kurzfassung, Results, and Conclusion for identical certainty;
- remove duplicated theory and unsupported causal claims;
- compile both `Thesis.tex` and `Professor_Draft.tex`;
- resolve undefined references and overfull boxes;
- visually inspect changed pages.

The final test for every sentence is whether it belongs in a robotics/control
thesis whose reader knows nothing about the author’s repository, coding
history, or earlier drafts.
