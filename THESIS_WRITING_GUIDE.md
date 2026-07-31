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
- **contact point** for the physical point the tool touches, \(p_C\), with
  \(r_C=p_C-p_{\mathrm{TCP}}\). It is a different point and the two are
  never used for one another.
- **pole** is implementation vocabulary from the parameter names. Keep it in
  equation labels and parameter keys, not in the running text.
- **tilt** for the commanded angular offset and for the axis it acts about: a
  `tilt about t1`, the `tilted axis`, the `tilted-axis stiffness`. Not
  `excitation`, which is borrowed from system identification and describes an
  input signal rather than a commanded orientation, and not `mismatch`, which
  implies an unwanted discrepancy where the angle is deliberate.

Do not build a name out of the state a quantity happens to be in. The centre of
compliance is held constant from first contact, so it was being called the
`frozen pole` throughout, which names a behaviour and an implementation detail
instead of the thing. State the behaviour once, where the quantity is
introduced, and use the plain name thereafter. The same applies to a
`frozen lever` or a `frozen reference`: say that it is held constant, then call
it the lever.

Symbols follow the same rule. One point, one subscript: \(p_c\), \(r_c\),
\(K_c\), \(D_c\).

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

Dimensionless entries are `[-]`. A quantity whose rows differ, such as a
Jacobian, says which is which: `[m/rad] linear, [-] angular`.

## Software identifiers in the text

Do not print long configuration or field names in the running text. A name
carrying two or more underscores is a file-format detail rather than a
scientific quantity, and it reads as source code instead of prose. State what
the setting does:

- `the pole is frozen at first contact`, not the parameter name that sets it;
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

## Evidence and claims

Never invent measurements, repetitions, fitted values, confidence intervals,
p-values, contact locations, timing bounds, or safety conclusions.

Distinguish:

1. measured observation;
2. model-based interpretation;
3. hypothesis requiring another experiment.

Trace every geometric metric through its measurement chain. The controller
reconstructs the tool axis from the EE pose and a nominal tool-to-EE transform.
Because the mounted tool can rotate approximately ±2° about \(y_{EE}\), call
this quantity the **EE-inferred tool axis**, not a directly measured physical
tool-face axis. Do not rename \(y_{EE}\) as \(t_2\) without transforming it
into the calibrated surface frame. State that the current angular results
describe the combined robot–gripper–tool response and cannot separate
controller compliance from gripper compliance. A visually or physically flat
tool may coexist with a changing EE-inferred angle.

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

The principal experimental conclusions of the calibrated-plane campaign are:

1. Compliance-centre placement dominates the alignment response, and its
   favourable sign is opposite for the two surface tangents. The unfavourable
   sign removes the correction rather than reducing it.
2. Raising the rotational stiffness of the excited axis reduces alignment over
   the tested range. Because the tangent entries were varied separately, report
   this per axis and not as a common paired setting.
3. Reducing the translational stiffness perpendicular to the excited axis
   improves alignment about \(t_2\) only, and a high rotational stiffness
   removes that benefit.
4. Displacing the compliance centre along the surface normal produced no change
   beyond the interpretation threshold over the investigated range.
5. Alignment is larger for a mismatch about \(t_2\) than about \(t_1\), and
   commanding the same mismatch about the tool-face axes places the response
   near the linear combination of the tangent components, which attributes the
   asymmetry to the surface frame rather than to the face geometry.

Report the \(t_2\) results as lower bounds. Unmeasured tool motion within the
gripper can conceal correction that occurred but cannot create it.

Basic settling, formulation-equivalence, and repeatability checks support the
measurements but should not dominate the conclusion.

The conclusion states what every experimental case showed, one entry per case,
in the case order used in the results chapter. A case that produced a null or
bounding result is reported as such rather than omitted.

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
- retain the EE-inferred metric and the operator-observed contact state as
  separate outcomes when tool-to-gripper motion is unmeasured;
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

## Final editorial checklist

Before accepting a revision:

- search for question-driven headings and literal research questions;
- search the running text for names carrying two or more underscores;
- search for `frozen`, and for any name built from a quantity's state;
- search for `excitation` and `mismatch` where a commanded tilt is meant;
- check that one quantity carries one name and one symbol throughout;
- search the symbol list for `mixed` and for units written without a space;
- check that the contents lists the figures, tables and symbols;
- check that list items begin with a capital letter;
- check that the conclusion covers every experimental case;
- check that each reported comparison also states its relation;
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
