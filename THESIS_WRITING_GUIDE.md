# Thesis Writing Guide

This file is the standing editorial guide for this thesis. Update it whenever a
new recurring preference, technical convention, or evidence rule is agreed.
The current thesis contains one combined Results and Discussion chapter.
The completed first contact-alignment campaign is also preserved in
`backmatter/appendix_previous_campaign.tex`. Keep it as comparison evidence
while the calibrated-plane, axis-specific campaign is being recorded. Do not
replace the main results with planned or empty sections; update the main
chapter only after new measurements have been checked.

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

## Roles of the chapters

- Introduction: define the contact-alignment problem, relevant literature gap,
  scope, and substantial contributions.
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

Use clear technical English rather than rhetorical or promotional language.
Avoid expressions such as:

- “the answer is visible before any fitting”;
- “a sweep is worth nothing until…”;
- “costs alignment and buys nothing”;
- “this is the substantive question”;
- “surprisingly”, “remarkably”, “clearly”, or “as can easily be seen”;
- repeated “This demonstrates that…” constructions.

Prefer the sequence:

measured value → comparison → interpretation → limitation.

Do not over-academize simple statements. Prefer “The measured alignment
increased as rotational stiffness decreased” over inflated wording.

Use British spelling consistently, including `centre`, `behaviour`, and
`optimisation`, except in literal software identifiers.

## Figures and tables

Keep figure and table captions short, preferably one line and normally below
about 12 words. Use a descriptive noun phrase that identifies the plotted
quantity, comparison, geometry, or parameter set.

Good examples:

- `Set-up settling at 4, 8, and 12 s.`
- `Paired tangent-axis stiffness results (n=5 per setting).`
- `Alignment response by compliance-centre coordinate.`
- `Phase-specific automatic-damping policy.`

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
changed together. In the completed Case-D campaign,
\(K_{R,t_1}=K_{R,t_2}\) was assigned the common values 5, 15, and
50 Nm/rad. These data establish the effect of the paired setting and must not
be described as an isolated \(t_1\)- or \(t_2\)-axis effect.

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

## Evidence and claims

Never invent measurements, repetitions, fitted values, confidence intervals,
p-values, contact locations, timing bounds, or safety conclusions.

Distinguish:

1. measured observation;
2. model-based interpretation;
3. hypothesis requiring another experiment.

Use `model-estimated external wrench` for
`O_F_ext_hat_K`. Do not call it a directly measured wrench. A location inferred
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

Avoid absolute normal-coordinate claims. Use:

> Within the investigated configuration and parameter range, the normal
> compliance-centre coordinate provided little additional explanatory power
> after accounting for the two in-plane coordinates.

If damping was not varied, report only that no sustained oscillation was
observed with the selected damping. Do not claim a measured damping effect.

Keep the null-space theory and implementation, but do not claim experimentally
improved singularity conditioning until matched controlled trials exist.

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
- Distinguish the virtual-centre lever
  \(r_c=p_{\mathrm{TCP}}-p_c\) from the physical-contact lever
  \(r_C=p_C-p_{\mathrm{TCP}}\).
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

- robot, tool, surface, fixture, and relevant software stack;
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

The principal experimental conclusions are:

1. Lowering the paired tangent-axis rotational stiffness
   \(K_{R,t_1}=K_{R,t_2}\) increased contact-induced alignment over the tested
   range. Report the corresponding estimated normal-load range without
   claiming formal equivalence or an isolated effect of either tangent axis.
2. Both in-plane compliance-centre coordinates strongly influenced alignment.
3. The in-plane response was non-monotonic, and unsuitable placements reduced
   alignment or rotated the tool away from the desired orientation.
4. The normal compliance-centre coordinate added substantially less
   explanatory information over the investigated range.

Basic settling, formulation-equivalence, and repeatability checks support the
measurements but should not dominate the conclusion.

## Energy, passivity, and stability

Do not include an energy-based experimental objective, energy metric, or
energy-monitoring proposal unless it is directly relevant to a performed study.
Do not restore a standalone stability or passivity chapter. Algebraic symmetry
and positive-(semi)definiteness may be stated where needed, but they do not
prove closed-loop stability or passivity of the sampled
robot–controller–environment system.

## Final editorial checklist

Before accepting a revision:

- search for question-driven headings and literal research questions;
- search for Git, repository, development-history, and draft-comparison terms;
- search for proposal language outside Future Work;
- check configured versus physical plane terminology;
- check `estimated` versus `measured` force/wrench terminology;
- check experiment counts, repetitions, units, and parameter values;
- check predicted versus experimentally confirmed results;
- check Abstract, Kurzfassung, Results, and Conclusion for identical certainty;
- remove duplicated theory and unsupported causal claims;
- compile both `Thesis.tex` and `Professor_Draft.tex`;
- resolve undefined references and overfull boxes;
- visually inspect changed pages.

The final test for every sentence is whether it belongs in a robotics/control
thesis whose reader knows nothing about the author’s repository, coding
history, or earlier drafts.
