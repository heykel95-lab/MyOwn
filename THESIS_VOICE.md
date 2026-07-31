# Thesis Voice and Originality

Companion to [THESIS_WRITING_GUIDE.md](THESIS_WRITING_GUIDE.md). That file governs
what a chapter contains and what a claim may assert. This file governs how the
sentences sound, and it exists because a detector pass over Chapters 1 and 2
flagged specific, repeatable prose patterns.

**Read this before writing or rewriting any thesis prose.** Every example below
is real text from this thesis, not invented illustration.

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
A four-word sentence is allowed and lands hard. Use it after a long one.

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
- **Mark reused own work.** `backmatter/appendix_previous_campaign.tex` holds
  the earlier campaign. If any of that text appeared in a submitted report or
  paper, say so where it is introduced. Internal repetition across chapters is
  separately banned by THESIS_WRITING_GUIDE.md.
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
- `is a right-handed orthogonal system`, and any other sentence that defines a
  standard term
- `, and ` appearing three or more times in one sentence

Then check the paragraph as a whole:

- Does every paragraph contain at least one symbol, value, frame, or phase name?
- Are five consecutive sentences all 15–25 words?
- Did anything get longer instead of shorter?
- Does any compressed sentence now claim more certainty than the measurement
  supports?
