# Thesis Voice and Originality

Companion to [THESIS_WRITING_GUIDE.md](THESIS_WRITING_GUIDE.md). That file governs
what a chapter contains and what a claim may assert. This file governs how the
sentences sound, and it exists because a detector pass over Chapters 1 and 2
flagged specific, repeatable prose patterns.

**Read this before writing or rewriting any thesis prose.** Every example below
is real text from this thesis, not invented illustration.

**Start with the next section.** *Register* was added after a supervisor read
the draft and found the opposite failure from the one the rest of this file was
written to fix: not machine flatness but literary compression. Where the two
disagree, Register wins.

## Register: plain technical statement, not slogan

An earlier pass over this thesis chased variety — short sentences, unexpected
openers, a different lead for every section. It overshot. The result was a
results chapter whose paragraphs opened on crafted one-liners:

> Nothing tested came close to the lever.
> The floor came first.
> One setting misbehaves.
> The whole of the null-space evidence.
> The limitation bites.
> Four contributions carry the work.
> Which side the lever sits on decides the outcome.

Each is grammatical and each is short, which is what the rhythm rules asked
for. None of them is how an engineer states a result. They read as slogans
written to be quotable, and a reader who meets six of them stops trusting the
prose around them.

**Rule.** Open a paragraph with the technical statement itself. If a sentence
would work as a pull quote, it is wrong for this thesis.

| Slogan | Technical statement |
|---|---|
| Nothing tested came close to the lever. | The compliance-centre lever produced the largest effect among the parameters investigated. |
| The floor came first. | The zero-tilt condition was used as the experimental baseline. |
| One setting misbehaves. | The \(10^\circ\) \(t_2\) condition showed substantially greater variability than the other settings. |
| The limitation bites. | This limitation affects the interpretation of the measured improvement. |
| Four contributions carry the work. | The main contributions of this thesis are the following. |
| Which side the lever sits on decides the outcome. | The sign of the lever strongly affects the resulting alignment response. |
| That is the whole of the null-space evidence. | No further null-space evidence was recorded. |

### Impersonal voice: no first person, and the author never acts in the sentence

**Never write `I`, `we`, `our`, `us`, `my`, or `the author`.** Not in the
running text, not in a caption, not in an appendix. The thesis currently has
none; keep it that way.

The rule goes further than the pronoun. Anything **the author did to the
apparatus, the campaign, or the data** is written in the passive:

| Author as agent | Passive |
|---|---|
| Case B raised the rotational stiffness and held the orthogonal entry at 5 Nm/rad. | In Case B the rotational stiffness was raised alone, and the orthogonal entry was held at 5 Nm/rad. |
| Case D held every gain at baseline and moved only the lever. | In Case D every gain was held at its baseline value and only the lever was moved. |
| A fourth column placed the compliance centre on the face. | In a fourth column the compliance centre was placed on the face. |
| The compliance-centre study sampled three tangential levels. | In the compliance-centre study three tangential levels were sampled. |
| Three probed points fitted the surface plane. | The surface plane was fitted from three probed points. |
| This thesis built a controller for the Panda. | In this thesis a controller was implemented for the Panda. |
| The probing used the same robot and tool. | The probing was carried out with the same robot and tool. |

Naming a case, a chapter, or "this thesis" as the grammatical subject of an
action is the same first-person sentence with the pronoun swapped out. `Case D
held` is `I held`. Rewrite it as `In Case D … was held`.

**Where active voice stays.** The passive rule applies to author actions, not to
every sentence — an all-passive chapter is unreadable and would break the rhythm
rules below. Keep the active voice where the grammatical subject is a physical
quantity, an effect, or an artefact behaving on its own:

> The improvement fell monotonically as \(K_{R,t_1}\) rose.
> Stiffening the axis being corrected returned less angle on both tangents.
> The sign of the lever determines the direction of the induced moment.
> The controller realises a frame-consistent Cartesian impedance in real time.
> \Cref{tab:results_case_d} shows …

Those are not the author acting; they are the measured system behaving, and the
passive would obscure what moved what. The test: **could the sentence begin with
"I"?** If yes, passivise. If the subject is a stiffness, an angle, a load, a
lever, a table, or the controller, leave it active.

Tense follows §11 below — past for what was done, present for standing
behaviour, equations, and what a table shows.

**Reserve the passive for actions, not for everything.** The verbs that take it
are `was calculated`, `was selected`, `was measured`, `was implemented`, `was
stored`, `was evaluated`, `was constructed`, `was used`. Mathematical and
factual statements stay active, because the passive would only add weight:

> The Jacobian maps joint velocity to Cartesian velocity.
> \Cref{fig:software_data_flow} shows the signal flow.
> The probe distance determines the evaluation points.
> At full row rank, the null space is one-dimensional.

Making every sentence passive is its own tell: a uniformly passive chapter is
heavier to read and sounds *more* machine-made, not less. The target is
impersonal academic prose that mixes passive experimental description with
direct mathematical statement.

**A passive sentence still has to carry content.** The failure mode is a short,
generic passive clause that names an action and stops:

| Too short and generic | Carries the substance |
|---|---|
| Four selectable laws are implemented. | Four null-space control configurations were implemented. These comprised an inactive mode, projected joint damping, a singular-value-based torque, and a combination of the latter two terms. |
| The implementation constructs the torque projector from the full \(6\times7\) geometric Jacobian. | The torque projector was constructed from the full \(6\times7\) geometric Jacobian. At full row rank, the resulting null space is one-dimensional. |

Note the second pair: the action goes passive, and the mathematical consequence
that follows it stays active. That alternation is what keeps the register from
going flat. Where a set of options exists, name them and say which one was used
— `The combined configuration was used in the experiments reported in the
following chapters` is worth more than the count of the options alone.

### One main claim per sentence

The commonest remaining fault is the algorithmically compressed sentence — one
clause carrying six facts. It is grammatical, and it is the clearest signal
left:

> In this thesis a real-time Cartesian impedance controller was implemented for
> the 7-\abbr{DOF} Panda, closing the remaining angle through the impedance
> itself by shifting the \(6\times6\) stiffness and damping to the TCP from a
> chosen centre of compliance during set-up.

That is *what* was implemented, *on which robot*, *what it achieves*, *how*,
*where the matrices go*, and *when* — in one sentence. Unpack it into steps so
the reasoning is presented in order:

> A real-time Cartesian impedance controller was implemented on the
> 7-\abbr{DOF} Panda. During set-up, the \(6\times6\) Cartesian stiffness and
> damping were spatially shifted from a selected centre of compliance to the
> TCP. This coupling allows the normal contact force to generate a corrective
> moment, which reduces the angular misalignment.

Same register, same formality, same passive voice. The difference is that each
sentence advances one step.

**Rule.** If a sentence answers more than about two of *what / where / how /
when / why*, split it.

### Give the observation before the conclusion

A polished headline followed by its evidence reads as announced. The same
content ordered measurement-first reads as derived:

| Announced | Derived |
|---|---|
| Lever placement had the largest measured influence of the parameters examined. Sixty millimetres … multiplied the improvement by about eleven. | The alignment response changed by several degrees when the compliance-centre lever was displaced by 60 mm. The changes produced by the tested stiffness values were substantially smaller. Within the investigated range, the compliance-centre position therefore had the largest measured influence. |

Not every paragraph — a section that has already given its numbers may state the
conclusion first. But where a claim is the section's main finding, put the
measurement in front of it.

### Let the cases differ in length

Cases A–E were given the same shape *and* the same length: bold name, headline,
numeric comparison, interpretation, limitation. Visually clean, and completely
predictable.

Some findings need more explanation than others. **Case D is the main result
and should be the longest entry; Case C's effect was limited and its entry
should be short.** Do not pad a weak case to match a strong one, and do not
compress the main finding to fit the pattern.

### Ordinary technical language, not crafted phrasing

A second list of flagged expressions, from the pass over the conclusion. These
are subtler than the slogans — several are almost conversational, which is what
makes them stand out against the formal text around them.

| Crafted | Ordinary |
|---|---|
| taken the wrong way | applied with the opposite sign |
| landed between the two values | produced values between the two measured responses |
| Both sit close to | Both results are close to |
| works that argument through | provides the corresponding geometric explanation |
| governs how the results should be read | affects the interpretation of the results |
| survives a change | remains valid under changes |
| three things stand between X and Y | the inference is affected by three sources of uncertainty |
| two further caveats sit on that implementation | two additional limitations apply |
| the probe configurations want checking | the probe configurations should be checked |
| set-up duration deserves confirmation | set-up duration should be verified |
| which bounds what the present arrangement can resolve | improvements of approximately this magnitude were therefore not interpreted as effects of the commanded tilt |
| carry the controller / carry the contribution | are used in the controller / present the corresponding results |
| the experiments probe that coupling | the effects of … were investigated in 75 contact runs |
| breaks that assumption | the actual surface pose may differ from the programmed pose |
| that angle has nowhere to go | that angular deviation cannot be absorbed by the commanded motion |
| Direction is what a contact task needs. | A contact task requires this compliance to be direction dependent. |
| Three frames carry the controller | Three right-handed coordinate frames are used in the controller |
| what each case showed | the conclusions and the work that remains |
| whether the trade was struck well | the reported experiments do not evaluate that trade-off |
| a bounded engineering seed | an initial engineering setting rather than an optimised parameter |
| quietly averaged | the record was inspected and the discrepancy resolved before analysis |
| Nothing was discarded. | All 75 runs were retained for analysis. |
| proves nothing about / settles nothing about | does not isolate / is not evaluated for |
| would invert the story | is therefore not plotted as … unless … is first reconstructed |
| deserves particular care | requires particular care |
| Geometric sense in a stiffness matrix does not make it fit for real hardware | A geometrically valid stiffness matrix does not by itself ensure acceptable hardware behaviour |

Note the last row. `bounds what the arrangement can resolve` is abstract; the
replacement says what was actually *done* with the baseline. Prefer the concrete
statement of use over the abstract statement of property.

### Separate an algorithm from its limitations

Chapter 3's null-space section attached a disclaimer to almost every sentence of
the algorithm — the probes are tangent approximations, they are not checked
against joint limits, the magnitude is fixed, the projector is kinematic, the
Jacobian is unscaled. Each is true and each must stay. Interleaved, they make
the algorithm hard to follow and make every sentence read as generated together
with its own caveat.

**Rule.** State the implemented algorithm first, without qualification. Collect
the limits into their own subsection afterwards. Chapter 3 now does this at
*Limits of the Implemented Null-Space Law*; Chapter 4 cross-references that
subsection instead of repeating the list.

The same applies to theory: assumptions belong in Chapter 2, but
implementation-specific shortcomings belong in Chapters 3, 4, or 6.

### Do not explain the same structure three times

Three sections were describing one control loop: the bullet list opening
Chapter 3, the numbered callback order at the end, and an implementation summary
after that. The summary added nothing and has been removed; the opening list was
reduced to prose that points forward to the authoritative one.

**Rule.** One authoritative statement of any sequence. A chapter does not need a
summary section when the next chapter follows immediately from it — a
transition sentence is enough.

### Avoid the repeated contrast pattern

`not X, but Y`; `not only X, but also Y`; `can conceal but not create`;
`identifies X but does not establish Y`. Individually precise, and §5 and §10
below already cover the disclaimer form. What was not covered is the *rate*: as
a habitual construction it produces a recognisable rhythm. Use ordinary
declarative sentences unless the contrast is the point.

### Anchor the interpretation to the table or the figure

The draft announced conclusions and left the reader to find the evidence.
A researcher points at the evidence first, or at least names it in the same
sentence:

> As shown in \cref{tab:results_case_d}, moving the compliance centre had a much
> larger effect than changing either stiffness parameter.

> The large standard deviation in the \(10^\circ\) \(t_2\) condition is caused
> primarily by one repetition.

This makes the interpretation traceable and shows that it came from the data
rather than from the argument. At least one explicit `\cref` to the table or
figure per results subsection, placed where the claim is made.

### Vary the architecture, not the vocabulary

Nearly every paragraph in the draft ran: strong opening claim, two numerical
comparisons, definitive interpretation, limitation or contrast. The repetition
is at paragraph level, so no amount of sentence-level editing reaches it.

Vary what a paragraph *does*. Some state the observation and stop. Some state
the purpose of the comparison before its result. Some carry only the anomaly.
Some are two sentences long. This replaces §12 below, which told you to vary the
*opener* — that produced the slogan table above.

### Calibrate the certainty to the evidence

The draft stated conclusions from one configuration and three repetitions in
language fit for a settled result. Weaken the verb, not the finding:

| Overclaimed | Matched to the evidence |
|---|---|
| proves | indicates, supports, is consistent with |
| decides the outcome | strongly influences the outcome |
| belongs to the surface frame | is more consistent with an effect associated with the surface frame |
| did nothing | produced no detectable change |
| dominates everything else examined | had the largest measured influence within the tested range |
| The three parameters are not of comparable weight. | In the investigated configuration, the compliance centre had a considerably stronger effect than either stiffness. |

`within the tested range`, `in the investigated configuration`, `over this
range` cost four words and are the difference between a defensible claim and
one an examiner can knock down. The existing hedging rules under *Hedge to the
evidence* still apply on top of this.

Including a limitations section does not license certainty elsewhere. These
survived a first pass because each is locally true, and each still reads as
final:

| Final | Tied to the scope |
|---|---|
| the tangent-axis asymmetry stands | the measured asymmetry between the tangent axes remained after this limitation was accounted for |
| the two entries did not act independently | within the tested range, the results indicate that the two entries were not independent |
| the favourable sign is opposite on the two tangents | for the investigated configuration, opposite favourable lever signs were observed for the two tangent directions |

One robot, one tool, one surface, one parameter range. This is not hedging
for its own sake — it connects each claim to the scope that was actually tested.

### Describe what was measured, not a narrative of what happened

`the unfavourable sign removed the correction rather than reducing it` survived
several passes because it is vivid and sounds precise. It describes an event
that did not occur: nothing was removed. A correction that never happened cannot
be taken away. What the log shows is that with the opposite lever sign, the
improvement was \(0.02\pm0.06^\circ\) — that is, **almost no alignment
improvement was measured**.

| Narrative | Measured |
|---|---|
| the unfavourable sign removed the correction rather than reducing it | with the opposite sign, almost no alignment improvement was measured |
| no tested setting improved on the most compliant baseline | the largest improvement was obtained with the lowest tested rotational stiffness |
| displacement along the normal produced no change | moving the centre along the surface normal produced no measurable change above the interpretation threshold |
| the favourable sign is opposite on the two tangents | opposite favourable lever directions were observed for tilts about \(t_1\) and \(t_2\) |

The pattern: a verb implying an action on a quantity (`removed`, `cancelled`,
`destroyed`, `beat`) where the log holds only a number near zero. Replace it
with what the measurement says. `observed` and `measured` are the right verbs
when reporting a campaign, and the negative form is `no measurable change above
the interpretation threshold`, never a bare `no change`.

### What must never be done to sound less generated

Authenticity comes from the work, not from damage to the prose. Never:

- introduce spelling or grammatical errors on purpose;
- insert casual or conversational expressions to sound human;
- replace a precise technical term with a vaguer synonym;
- use the first person where the thesis requires impersonal writing;
- passivise every sentence;
- vary sentence length at random, without improving the explanation;
- add laboratory observations that were not recorded;
- invent a reason for a design decision after the fact;
- paraphrase the same passage repeatedly through a tool.

A detector may still score technical writing highly: equations, fixed
terminology, passive constructions, and predictable structure all push the score
up regardless of authorship. **The score is not the objective.** The objective is
that every statement can be defended from the implementation, the experimental
records, the figures, and the measurements.

### Do not reproduce the results chapter in the conclusion

The conclusion restated almost every value and standard deviation from
Chapter 5. It needs the finding of each case, not its measurements. Keep a
number there only where the conclusion is unintelligible without it — a
resolution floor, a bound. Relations (`about eleven times`, `roughly a
quarter`) survive where the absolute pair does not, which also satisfies the
relation rule in THESIS_WRITING_GUIDE.md.

The per-case entry required by that guide stays. It shrinks; it does not go.

### One thing this section does not license

The supervisor also asked for real experimental reasoning — why a parameter
range was chosen, what was observed during the anomalous repetition, how
tool-mount motion was distinguished from a logging error, whether a finding matched
expectation. Those sentences would be the most valuable additions to the
chapter, and **not one of them may be written without the author supplying the
fact.** Inventing a plausible reason is a worse fault than the missing sentence.
Ask, or leave the gap.

## What the detector is actually reacting to

Two honest statements first.

Detector percentages are not reliable evidence. They score surface statistics —
word predictability and sentence-length uniformity — so competent, plain
technical writing about standard material scores as machine-written whether or
not a machine wrote it. A number from one of these tools is not a verdict on
the work.

That said, the flagged passages in this thesis are genuinely the weaker ones,
and the overlap is not a coincidence. Comparing the flagged text against the
unflagged text in the same chapters gives one dominant pattern:

> **Flagged sentences restate what any robotics reader already knows.
> Unflagged sentences carry a particular of this thesis that a reader could
> check against the hardware, the log, or the equation.**

Every rule below follows from that. Raising the density of thesis-specific,
checkable content is what improves the writing; the detector score falls as a
side effect. Fixing the score by swapping in unusual synonyms does neither.

If a passage was drafted with a tool, the correct fix is the same one applied
below: rewrite it from your own equations, code, and measurements until it says
something only you could say.

## Two limits on this work

**Do not aim for zero.** Past a point, editing for a detector score becomes its
own tell: prose scrubbed of every connective and levelled to a uniform
specificity reads as processed, not as written. Stop at clearly better. A
paragraph that still has an ordinary sentence in it is fine.

**Do not assume.** If a fact about the controller, the campaign, or the
hardware cannot be verified from the code, the logs, or the author, it does not
go in the thesis at all — not as a hedge, not as a plausible-sounding filler,
not as a placeholder to firm up later. Leave the gap and say it is a gap.
Inventing a limitation, an assumption, or a run count to complete a sentence
pattern is a worse fault than the missing sentence.

## The seven flagged patterns

### 1. Textbook restatement

The single largest flagged block. These sentences define terms to an examiner
who has taught them for twenty years.

Flagged, [02_theoretical_background.tex:26](chapters/02_theoretical_background.tex#L26):

> To describe the motion of a robotic manipulator, multiple coordinate frames
> are used simultaneously. A coordinate frame is a right-handed orthogonal
> system of three mutually perpendicular unit vectors anchored at a chosen
> origin.

The definition sentence is deletable with zero loss. Keep only the part that
is a decision of this thesis — that DH is named for indexing, and that poses
come from the robot model:

> Three frames carry the controller: the base frame \(\{0\}\), the joint
> frames \(\{i\}\), and the end-effector frame \(\{\mathrm{EE}\}\), all
> right-handed. The joint indexing follows Denavit--Hartenberg
> \cite{Denavit1955}, though the controller takes its poses and its Jacobian
> from the robot model rather than from a parameterised chain.

**Rule.** Before writing a definition, ask whether the examiner needs it. If a
standard result is genuinely required, cite it and state the one form this
thesis uses — do not reproduce the textbook sentence around it. This is also
the highest-risk zone for similarity matching; see Originality below.

### 2. Connective scaffolding

Openers that announce a logical relation the sentence then fails to earn:
`In this way`, `As a result`, `Therefore`, `This means that`, `In other words`,
`It is important to note that`, `Overall`, `Furthermore`, `Moreover`.

Flagged, [02_theoretical_background.tex:260](chapters/02_theoretical_background.tex#L260):

> Impedance control imposes a desired dynamic behaviour between the
> end-effector motion and the forces acting on it. Instead of commanding only a
> desired position, the robot is made to behave like a virtual spring-damper
> system in Cartesian space. In this way, deviations from the desired pose
> generate restoring forces and moments, while the damping terms reduce
> oscillations. The numerical choice of the stiffness and damping gains is
> therefore part of the controller design, because the same impedance law can
> produce very different contact behaviour depending on the selected values.

Four sentences, about eighty-five words, and after the first clause nothing is
added that the equation below does not state more precisely. Rewritten:

> Impedance control prescribes a dynamic relation between end-effector motion
> and the contact wrench \cite{Hogan1985,Ott2008}. Here that relation is a
> Cartesian spring-damper acting on the pose error \(e\), with stiffness \(K\)
> and damping \(D\) as its only free parameters. Those two matrices carry the
> design freedom this thesis investigates; Chapter~5 reports how far the
> alignment response moves across the tested range of \(K_R\).

**Rule.** Delete the connective and read the sentence again. If it still
follows, leave it deleted. If it no longer follows, the paragraph order is
wrong — fix the order, not the transition.

### 3. Weak verbs where a term of art exists

The one you identified. `puts` is not thesis vocabulary.

Flagged, [02_theoretical_background.tex:185](chapters/02_theoretical_background.tex#L185):

> The multiplication by \(R_{\mathrm{EE}}\) puts \(e_R\), the angular velocity,
> and the commanded rotational gains in the same base frame.

`puts ... in the same frame` also leaves the frame unnamed. Rewritten:

> Left-multiplying by \(R_{\mathrm{EE}}\) expresses \(e_R\) in \(\{0\}\), where
> the angular velocity and the rotational gains are already defined.

| Weak | Use |
|---|---|
| a zero flag / the flag is enabled | setting \(\mu_i=0\); the entry was set to one |
| puts X in frame Y | expresses X in Y, maps X into Y |
| uses | applies, evaluates, forms, drives |
| reads / gets | obtains, retrieves, takes |
| is made to behave like | behaves as, is commanded to track |
| provides a way to | (name the mechanism instead) |
| deals with / handles | (name the operation) |
| plays a role in | (state the role) |
| helps to | (delete) |
| looks at | examines, evaluates |

**Rule.** A vague verb usually hides an unfinished thought. Replacing it forces
the missing specific into the sentence, which is the actual gain.

**Software vocabulary for a mathematical quantity.** `flag`, `enabled`,
`toggled`, `switched on` name a boolean in the source, not the quantity the
equation defines. Where the text has just written \(\mu_i\in\{0,1\}\), the
sentence after it says `setting \(\mu_i=0\)`, not `a zero flag` — otherwise the
same object carries two names one line apart. `contact flags` became `contact
indications` for the same reason.

### 4. Evaluative filler

`useful`, `important`, `another difficulty`, `powerful`, `interesting`,
`straightforward`, `it is worth noting`. These assert value instead of
demonstrating it.

Flagged, [01_introduction.tex:112](chapters/01_introduction.tex#L112):

> The contact-alignment task adds another difficulty. ... A selected local
> linearized centre of compliance provides a useful way to design this
> behaviour by coupling translation and rotation about a chosen point near the
> tool edge or surface contact.

Rewritten so the mechanism replaces the evaluation:

> A tool tilted with respect to the surface cannot be brought flat by
> translational compliance alone: the wrench that closes the gap must also
> carry a moment. Placing the centre of compliance near the tool edge couples
> translation and rotation, so that pressing the tool into the plane also
> rotates it toward the plane. The placement is a task-to-impedance mapping,
> not a claim that the tool pivots about that point physically.

Note what survived — the qualification about the physical pivot is a real
scientific commitment, and it stays. Filler is not the same as care.

### 5. The negation-correction reflex

Stating what something is not, before or instead of what it is:
`It is X, not Y`, `The controller does not subtract transformation matrices`,
`no Euler-angle conversion is used`, `Instead of commanding only a desired
position...`.

One such correction per subsection is precise. Three is a tic, and this thesis
currently clusters them — [02:136](chapters/02_theoretical_background.tex#L136),
[02:160](chapters/02_theoretical_background.tex#L160), and
[01:118](chapters/01_introduction.tex#L118) are within a few pages of each
other.

**Rule.** Keep the negation only where a reader would otherwise assume the
wrong thing — the Euler-angle and matrix-subtraction denials qualify, because
both are what a reader expects. Elsewhere, state the positive and stop.

### 6. Parallel-list padding

Long coordinated lists in one breath, the most recognisable machine cadence.

Flagged, Scope and Contributions:

> It uses a Jacobian-transpose torque mapping, model-based Coriolis
> compensation, phase-specific Cartesian gains, and damping calculated from a
> Cartesian-inertia estimate.

Four items, one sentence, no item developed. Break it and attach the specifics:

> Torques are mapped with \(J^\top\), and Coriolis terms are compensated from
> the model. Each phase carries its own Cartesian gains; damping follows from
> the Cartesian-inertia estimate rather than being set by hand.

**Rule.** Three or more coordinated items in one sentence: either split into
sentences that each carry a detail, or make it a real list where each entry
states a value, a unit, or a consequence.

### 7. Uniform rhythm

Machine prose runs 15–25 words per sentence with little variance. The flagged
blocks above are almost perfectly even; the unflagged block at
[02:36](chapters/02_theoretical_background.tex#L36) swings from four words to
forty.

**Rule.** If five consecutive sentences all sit in the 15–25 word band, rewrite.
A short sentence is allowed after a long one.

**Amended.** This rule previously read "A four-word sentence is allowed and
lands hard", and that is where the slogans came from. Length variety must fall
out of the content — a short sentence because the statement is short, not a
statement compressed to reach a target length. If a four-word sentence is not
a plain technical statement, it is a slogan; see *Register* above.

### 8. The chapter-roadmap paragraph

`\section{Thesis Structure}` at
[01_introduction.tex:162](chapters/01_introduction.tex#L162) was flagged almost
in full, and it is patterns 6 and 7 compounded — five consecutive sentences of
identical shape, `Chapter N <verb>s <list of four or five nouns>`:

> Chapter~\ref{ch:theory} develops the theoretical background for coordinate
> frames, kinematics, Cartesian impedance control, null-space behaviour, and
> stiffness and damping representation. Chapter~\ref{ch:implementation}
> describes the real-time controller implementation on the Panda.
> Chapter~\ref{ch:methodology} presents the experimental methodology, including
> the robot setup, contact geometry, gain-selection workflow, logged data, and
> evaluation metrics. ...

It is also the table of contents rewritten as prose, so it carries almost no
information the reader cannot get by turning back one page. Group the chapters,
vary the sentence length, say which ones carry the contribution, and put one
real number in:

> Chapter~\ref{ch:theory} sets out the impedance law, the frame conventions, and
> the compliance-centre shift; Chapter~\ref{ch:implementation} gives their
> real-time realisation on the Panda. The experimental chapters carry the
> contribution: Chapter~\ref{ch:methodology} documents the calibrated-plane
> campaign of 75 contact runs over 25 settings, and
> Chapter~\ref{ch:results_discussion} reports and interprets the measurements.
> Chapter~\ref{ch:conclusion} states what each case showed.

**Rule.** A structure section does not need one sentence per chapter, and no
chapter needs its contents listed. Two or three sentences is enough.

## Four more patterns, from the Chapters 4 and 5 pass

A later detector pass flagged Chapters 4 and 5 on nearly every page. The seven
patterns above were not the cause — by the counts that matter, Chapter 5 used
fewer connectives and fewer weak verbs than Chapter 2. Four *structural*
patterns were, and they are invisible to a sentence-level read. Measure them
before rewriting; the numbers below are the before/after of the pass that fixed
them.

### 9. The determiner opener

Chapter 5 opened 46 % of its sentences with the bare word `The`, and 59 % with
`The`, `This`, `These`, `It` or `A`. Chapter 1, which the detector left alone,
sits at 22 % and 39 %. A results chapter drifts this way naturally, because
every sentence wants a metric noun phrase as its subject — `The improvement`,
`The response`, `The effect`, `The face-centre condition`.

**Rule.** Keep determiner openers under about a third. Start from the
condition (`With the lever on the favourable side, …`), the participle
(`Stiffening the axis being corrected …`), the quantity (`Sixty millimetres of
lever …`), or the subordinate clause. After the rewrite both chapters sit at
29–30 %.

### 10. The `X, not Y` disclaimer as a paragraph terminator

Chapter 4 carried 26 of these, roughly one per paragraph, always in final
position: `It is an engineering placeholder, not a measured safety boundary`,
`These are Franka reflex thresholds, not commanded-torque saturations`, `not a
gradient magnitude and not an exact finite motion`. Pattern 5 above calls three
a tic; this was the tic industrialised into a template.

The disclaimers are individually correct and several are required by
THESIS_WRITING_GUIDE.md — model-estimated versus measured wrench, virtual
spring scale versus contact force. **Do not delete them.** Vary the syntax and
place them where the misreading would happen:

> The value in the stiffness calculation is an engineering design scale. It
> sets the virtual-spring command scale and is not a measured contact load.

> No tool travels \(180\,\mathrm{mm}\) into the surface, and no such displacement was
> expected of the robot.

The negation rate fell from 12.6 to 6.2 per thousand words without one
scientific commitment being dropped.

### 11. Timeless present in a chapter about completed work

Chapter 4 was written as a specification — `The experiment is performed on`,
`The plane is fitted from three probed points`, `The controller computer uses`
— for work that finished months ago. THESIS_WRITING_GUIDE.md already requires
Chapter 4 to describe completed experiments; the present tense quietly broke
that, and it also removes the author from the page entirely.

**Rule.** Past tense for what was done to the hardware: `Three probed points
fitted the plane`, `The controller computer ran Ubuntu 20.04.3`, `The optional
pre-grind gate stayed disabled for every reported run`. Present tense stays for
the controller's standing behaviour, for equations, and for what a table shows.

**The run procedure is the exception.** §4.5 describes the standing sequence
every run followed, which is closer to an algorithm than to an observation, and
the author's preference is the present indicative there: `The active parameter
set is recorded, and the Panda moves to the configured initial joint pose`. What
must not appear is the **imperative** — `Record the parameter set`, `Move the
Panda`, `Seat the tool` — which reads as an operator manual and leaves a reader
unable to tell a description of what happened from an instruction about what
should happen. Use the present indicative, passive where the actor is the
experimenter and active where the actor is the controller or the robot.
Statements about what was *measured* or *observed* stay in the past regardless.

### 12. The templated section

Chapter 5's five case sections were structurally identical: one-sentence
`Case X varies Y`, table, figure, `For a tilt about t1 …`, `For a tilt about
t2 …`, closing `therefore` generalisation. Once the reader has met Case A, no
token in Cases B–E is a surprise, and next-token predictability is exactly what
these tools score.

**Rule, as originally written and now superseded.** "Vary what each section
leads with. One case can open on the anomaly (`One setting misbehaves.`), one on
the outcome (`Nothing else tested came close to the lever.`)…"

Both of those examples are in the slogan table under *Register*. Chasing a
distinctive opener for each section is what produced them, and it treats a
paragraph-level problem as a first-sentence problem.

**Replacement rule.** The templating is real and still needs fixing, but at the
level of what each section *does*, not how it starts. A section whose result is
a null result is shorter and has no interpretation paragraph. A section
answering a question states the question first. A section with an anomaly gives
the anomaly its own paragraph. A section reusing another case's settings as its
reference says so before the table. Every one of those leads with an ordinary
technical sentence. The case identifiers and the table/figure order stay fixed.

Read *Vary the architecture, not the vocabulary* under *Register* for what
replaced this.

### Vary the frame, keep the term

`commanded tool orientation offset` is the settled name
(THESIS_WRITING_GUIDE.md, *Naming a technical quantity*) and does not change.
Its components are the `commanded rotation axis`, the `commanded rotation
direction`, and the `offset angle`. Repeating the full name in every sentence
is unnecessary once the quantity has been introduced.

One name, many constructions:

| Instead of, every time | Also |
|---|---|
| a commanded tool orientation offset about \(t_1\) | the offset about \(t_1\); the commanded rotation about \(t_1\) |
| for a commanded tool orientation offset about \(t_2\) | with the offset about \(t_2\); about \(t_2\) |
| the sign of the tool tilt | the commanded rotation direction; the offset direction |
| Excited axis *(table header)* | Commanded rotation axis |

`tool tilt`, `excitation`, and `mismatch` are not used for the commanded tool
orientation offset.

## What already reads as your own voice

The unflagged passages share concrete traits. Write toward these.

- **Named particulars a reader could check.** "the upright Panda configuration
  used in this thesis", "according to the manufacturer convention", "the
  libfranka end-effector/tool frame selected through the robot model
  interface".
- **Symbol density.** "the base-frame stiffness and damping matrices
  \(K_{p,0}\), \(D_{p,0}\), \(K_{R,0}\), and \(D_{R,0}\)" — unflagged. Prose
  anchored to the notation is prose only this author can write.
- **Stated commitments.** "This sign convention is implementation-critical."
  "They are not assumed to be diagonal in the base frame."
- **Concrete instances after a general claim.** "if the task frame changes, for
  example because the surface normal changes".
- **Past tense for what was done.** "The Cartesian error vector was defined as"
  — unflagged, where the surrounding present-tense generalities were flagged.
- **Numbers with units.** A sentence carrying `5 Nm/rad` or `1 kHz` is almost
  never flagged.

## Scientific register

The rules in this section were abstracted from a completed engineering thesis
read as a model of the register. What transfers is **convention**: how evidence
is hedged, how prior work is credited, how a limitation is placed. Conventions
are not ownable and cannot be plagiarised. Wording is, so none was taken —
every example below is written in this thesis's own domain.

What separates that text from the flagged prose here is not vocabulary. It is
that an author is visibly present: making judgements, conceding weaknesses,
and declining to claim more than the data carries.

### Credit prior work with the verb that names the contribution

`discuss`, `describe`, `present`, `provide`, and `show the importance of` are
placeholders. They tell the reader a paper exists, not what it changed. A
strong literature section reads as a dated chain of moves, each attributed.

Weak, and still present at
[01_introduction.tex](chapters/01_introduction.tex):

> Ott et al. discuss Cartesian impedance control for flexible joint robots and
> the importance of stable interaction behaviour. Albu-Schäffer et al. describe
> Cartesian impedance control for torque-controlled lightweight robots.

Better — each verb states the move, and the second sentence says why it matters
here:

> Ott et al. extended Cartesian impedance control to flexible-joint robots,
> where joint elasticity limits the stiffness the controller can actually
> realise. Albu-Schäffer et al. built the same law on joint-torque sensing,
> which is the interface this thesis uses.

| Placeholder | Verbs that name a move |
|---|---|
| discusses, describes | extended, generalised, restricted, reformulated |
| presents, provides | derived, measured, identified, established |
| shows the importance of | required, ruled out, reduced X to Y |
| improves on | replaced X with Y, corrected, relaxed the assumption that |

**Rule.** Name the author, date the move where the chronology matters, and use
a verb that could be wrong. A verb that cannot be wrong is not carrying
information.

### Say what the prior work left undone

The gap belongs in one sentence, immediately before the contribution, and it
should name what was skipped rather than gesture at a "need for further study".
Chapter 1 now does this — the RCC literature fixes the compliance centre
mechanically for insertion, and this thesis places it in software and measures
it. Keep that shape when the section moves.

### Hedge to the evidence, and name the hedge

Precision of language should track precision of evidence, visibly:

- `measured` — came off the log.
- `estimated` — inferred through a model, with the model named.
- `suggests` / `is consistent with` — a pattern that another experiment could
  overturn.
- `about`, `approximately`, `of the order of` — the value is real but the
  digits are not all meaningful.

Write `the response is approximately linear in the lever over the tested
range`, not `the response is linear`. Write `an estimated equivalent contact
location`, not `the contact point`. The hedge is not weakness; an unhedged
claim that outruns its evidence is the thing an examiner will find.

### Put the weakness where the number is

When a figure rests on few samples or a fragile inference, say so at the point
of use — a footnote or a trailing clause — not only in a limitations section
pages later. A reader meeting `a factor of about seven` deserves to learn in
the same breath that it came from three repetitions.

> The alignment improved by roughly a factor of seven.\footnote{Three
> repetitions per setting; the factor is quoted to one significant figure
> because the repeatability does not support more.}

This is the single most human move in the register, and the hardest to fake:
volunteering the thing that weakens your own number.

### Report exclusions and carry the denominator

Runs that failed, were aborted, or were discarded are data about the method.
State how many, why, and what the surviving denominator is — then make every
later percentage use it.

> Of the \(N\) attempted runs, \(M\) were discarded after a reflex stop during
> the ramp phase. The remaining \(75\) runs are the basis of every value
> reported below.

Fill in the real counts or drop the sentence; do not invent a number to make
the shape work. If nothing was discarded, say that instead — it is also
information.

### Label an arbitrary choice as arbitrary

Some settings exist to make the experiment run. Saying so costs nothing and
protects the reader from reading a design intent that was never there.

> The \(12\,\mathrm{s}\) phase duration was chosen to let the contact settle
> and is not a limit of the controller.

Prefer this to silence, and to inventing a justification after the fact.

### State assumptions explicitly, each with its consequence

**This thesis currently has no Assumptions and Limitations section.** A short
subsection in Chapter~\ref{ch:theory}, one bullet per assumption, each naming
what it costs, would carry real weight. The pattern is `assumption → what it
limits`:

> - The tool is treated as rigidly held. Motion within the gripper is therefore
>   unmeasured, which makes the \(t_2\) results lower bounds.
> - Contact is treated as quasi-static. Impact transients are outside the range
>   over which the reported stiffness applies.

Confirm which assumptions the implementation actually makes before writing
them; the two above are candidates, not established facts.

### Say what was not analysed, then route it to Future Work

An honest scope boundary is stronger than silence, and it is where a limitation
turns into a contribution to the next study.

> Whether a shorter ramp shortens the whole sequence was not measured here,
> because the phases were not timed independently. It is left to future work.

### Justify what you leave out

If a figure or a case is omitted, give the reason in one clause — `not shown,
as it repeats Figure~5.4 without adding a distinction`. Silent omission reads
as an oversight; a stated one reads as judgement.

### Report null results as results

A parameter that did nothing is a finding, and stating it plainly is more
convincing than passing over it. `Displacing the compliance centre along the
normal produced no change beyond the interpretation threshold` is a result, and
the conclusion should carry it alongside the positive ones.

### Decline the recommendation the data cannot support

Where the answer is conditional, say it is conditional and name the condition,
rather than manufacturing a rule:

> No single stiffness setting was best across both tangents; the favourable
> sign of the lever reverses between them, so the choice follows the axis being
> corrected.

## Rewrite procedure

Applied to any flagged or weak paragraph, in order.

1. **Delete every sentence that a robotics examiner already knows.** Usually
   one to three sentences per flagged block. Do this before rewording anything.
2. **Strike the connective openers.** Re-read; fix paragraph order if the logic
   breaks.
3. **Replace every weak verb** using the table above.
4. **Cut evaluative adjectives.** Keep scientific qualifications.
5. **Add one checkable particular per paragraph** — a symbol, a value with
   units, a frame name, a phase, a cross-reference to a measurement.
6. **Break any sentence carrying three or more coordinated items.**
7. **Read the paragraph aloud.** If every sentence is the same length, shorten
   one to under eight words.
8. **Confirm nothing new was claimed.** Compression must not upgrade a
   model-based interpretation into a measurement; the evidence rules in
   THESIS_WRITING_GUIDE.md still bind.
9. **Check the register.** Does every attribution verb name a move? Does every
   number carry a hedge matched to its evidence? Is the weakest thing about the
   paragraph stated inside it?

Expect a rewritten paragraph to be shorter. If it grew, step 1 was skipped.

## Originality

The passages a detector flags and the passages that trigger similarity matches
are largely the same passages — standard definitions and standard derivations,
where the canonical phrasing is nearly fixed. Handling them well fixes both.

- **Do not patchwrite.** Keeping a source's sentence structure and substituting
  synonyms is the classic detected form, and it is a more serious finding than
  a quotation. Read the source, close it, then write from the equation and from
  your own implementation.
- **Cite the origin of every equation not derived here.** The impedance law,
  the DH convention, the damped least-squares inverse, and the null-space
  projector all carry sources already — keep it that way when text moves.
- **Quote verbatim only when the exact wording is the point**, with quotation
  marks, citation, and page. In control engineering this is rare; prefer to
  state the result in this thesis's own notation.
- **Common knowledge still gets one citation, not a reproduced paragraph.**
  Cite a canonical source once and move to what this controller does.
- **Mark reused own work.** If any text in the thesis appeared in a submitted
  report or paper, say so where it is introduced. Internal repetition across
  chapters is separately banned by THESIS_WRITING_GUIDE.md.
- **Attribute derived figures.** A redrawn figure based on a published one
  needs "adapted from \cite{...}" in the caption; a reproduced figure needs
  permission.
- **Attribute derived code.** Where an appendix listing descends from the
  libfranka examples already cited as `libfrankaCartesianExample`, state that
  in the appendix text rather than presenting it as written from scratch.

### Never cite your own measurements

A citation checker flagged this sentence as requiring a source:

> Moving the lever 60 mm along the tangent perpendicular to the tilted axis
> raised the alignment improvement from 0.56° to 6.05° for a tilt about \(t_1\)
> and from 1.38° to 6.36° for a tilt about \(t_2\), reducing the residual
> misalignment to 0.93° and 2.14°.

It offered a Scribd machine-alignment guide at 11% relevance and a German
structural-engineering blog post on rotational stiffness at 7%.

**Add no citation.** That sentence reports this thesis's own campaign. Citing
either source would attribute the contribution to an unrelated third party and
would be a factual error in the thesis — a worse fault than the one the tool
believes it found. Relevance scores in the single digits are noise, not weak
evidence.

These tools detect *specificity*, and cannot tell a specific claim borrowed from
literature apart from a specific claim that is the author's own result. Every
measurement sentence in Chapter 5 will trip them. Expect that and dismiss it.
Run this kind of check over Chapters 1 and 2, where material genuinely was
paraphrased from sources; treat its output on Chapters 4 and 5 as inapplicable.

The one useful response is to make provenance unmistakable to a human reader,
using the case identifiers the writing guide already requires:

> In Case~C (three repetitions per setting, Table~\ref{tab:...}), moving the
> lever 60 mm along the tangent perpendicular to the tilted axis raised the
> alignment improvement from 0.56° to 6.05° about \(t_1\) ...

The reader now sees which experiment produced the number, and no citation is
implied or needed.

## Quick scan before committing prose

Search the changed `.tex` files for each of these:

- `In this way`, `As a result`, `This means that`, `In other words`,
  `It is important`, `It is worth noting`, `Overall`, `Furthermore`,
  `Moreover`, `Additionally`
- `puts`, `uses`, `provides a`, `helps to`, `plays a role`, `deals with`
- `useful`, `important`, `powerful`, `interesting`, `straightforward`,
  `another difficulty`
- `automatic`, `automatically` — banned in prose by
  THESIS_WRITING_GUIDE.md, *Naming a technical quantity*. Name the thing
  instead: `the run sequence`, `error recovery`, `the gripper action`,
  `the internally commanded disturbance experiment`. Hits inside a listing,
  a `\label{}`, or a figure filename are the permitted exceptions.
- `is a right-handed orthogonal system`, and any other sentence that defines a
  standard term
- `, and ` appearing three or more times in one sentence

Attribution and evidence, per the register section:

- `discuss`, `describes`, `presents`, `provides`, `shows the importance of`
  attached to a cited author
- a factor, ratio, or percentage with no sample size anywhere near it
- `optimum`, `best`, `dominant` without `model-predicted`, `within the tested
  range`, or an equivalent bound
- a parameter value with no reason given, where the reason is "it worked"

Register, per the section at the top of this file:

- Any sentence answering more than two of *what / where / how / when / why* —
  split it.
- `taken the wrong way`, `landed between`, `sit close to`, `works that argument
  through`, `governs how`, `survives a change`, `things stand between`,
  `caveats sit on`, `wants checking`, `wants instrumenting`, `deserves
  confirmation`, `bounds what`
- Are the five case entries all the same length? Case D should be longest,
  Case C shortest.
- Does the main finding of a section announce its conclusion before its
  measurement?

- `\bI\b`, `we`, `our`, `us`, `my`, `the author` — there must be no hits.
  (Search case-sensitively and expect the index variable \(i\) and the identity
  matrix \(I\) as false positives.)
- A case, a chapter, a study, a sweep, a column, or `this thesis` as the subject
  of an action verb: `Case D held`, `Case C varied`, `the study sampled`,
  `this thesis built`. Passivise each one.
- Read every paragraph's first sentence on its own. Would any of them work as a
  pull quote? Rewrite it as a plain technical statement.
- Does each results subsection carry at least one `\cref` to the table or figure
  its claim rests on?
- `decides`, `dominates`, `proves`, `did nothing`, `is the whole of`, `carry the
  work`, `came first`, `came close to`, `bites`
- A conclusion sentence stating a definitive result with no `within the tested
  range`, `in the investigated configuration`, or equivalent bound
- Numbers in the conclusion that already appear in the results chapter and are
  not a bound the conclusion needs

Then check the paragraph as a whole:

- Does every paragraph contain at least one symbol, value, frame, or phase name?
- Are five consecutive sentences all 15–25 words?
- Did anything get longer instead of shorter?
- Does any compressed sentence now claim more certainty than the measurement
  supports?

And count, over the whole chapter — these are the four from the Chapters 4 and
5 pass, and none of them is visible one sentence at a time:

- What fraction of sentences open with `The`, `This`, `These`, `It` or `A`?
  Over about a third, rewrite the openers.
- How many `X, not Y` disclaimers, and do they all sit at the end of a
  paragraph? Vary the syntax; keep the content.
- Is a chapter about completed work written in the present tense?
- Do consecutive paragraphs share one architecture — claim, two numbers,
  interpretation, limitation? That is the pattern to break, and it is invisible
  one sentence at a time.
- Does the conclusion reproduce the results chapter rather than summarise it?

## Register baseline

This file once carried a measured baseline taken from a green revised Chapter 5
— mean sentence length, median, the share of short and long sentences. That
chapter has since been replaced and no revised paragraphs remain anywhere in
the thesis, so the baseline described text that no longer exists and has been
removed rather than left to mislead.

Until a chapter is revised and marked again, judge the register by the rules
above rather than against a stored set of numbers: plain technical statements,
one main claim per sentence, certainty bounded to what was measured, and
paragraph shapes that vary with what the paragraph is doing.
