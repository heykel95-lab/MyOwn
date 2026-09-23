# Figure references in the thesis

Updated: 2026-09-23, after applying the agreed corrections. Figure numbers in
the inventory refer to the rebuilt `Thesis.pdf`.

The audit followed the active inputs from `Thesis.tex`, excluding comments and
archived appendices. It matched the 25 figure environments against the compiled
List of Figures and checked explicit references outside figure environments.
Multiple labels attached to one figure were counted as one figure. Captions,
labels and List of Figures entries were not counted as running-text references.
The surrounding paragraphs were then reviewed for the figure's contribution.

**Result: all 25 figures are referenced.** All figure references found
in the active text resolve to an included figure. There are no numbered figures
in the active appendices or Chapter 6.

## Corrections applied

- **Former Figure 2.2 removed.** The moment-decomposition equation and the
  supporting/opposing normal-force moment sketch explain the mechanism.
  The removed source is preserved as `figures/withdrawn/moment_bookkeeping.tex`.
  Former Figures 2.3 and 2.4 are now Figures 2.2 and 2.3, respectively.
- **Figure 3.8 retained and referenced.** The statement that switching modes
  leaves the Cartesian reference and impedance unchanged now identifies the
  loop in the figure.
- **Figure 5.2 retained and referenced.** The normal-force comparison now
  identifies the figure beside the prediction and measured means.
- **Figure 5.3 retained and referenced.** The rotational-impedance plausibility
  statement now identifies the moment comparison. Force and moment assess
  different impedance relations, so these two figures retain distinct purposes.

The other 22 figures have identifiable roles in their surrounding explanation
or results. Figures 3.4, 3.5 and 3.7 have brief reference sentences, but the
adjacent equations and paragraphs supply the specific explanation. They
respectively show tool geometry, the clearance criterion and reference
generation; sharing the tool geometry does not make them duplicates.

The final build has 120 pages, with no undefined references or overfull boxes.
The changed pages and the retained Figure 3.8 were rendered and visually checked.

## Complete inventory

Reference locations below use the line numbers in each chapter's current `.tex`
source. The count includes only explicit running-text cross-references.

| Figure | References | Reference lines | Contribution and assessment |
|---|---:|---|---|
| 1.1 | 1 | Chapter 1: 26 | Separates surface-reference mismatch from desired/achieved orientation mismatch. Keep. |
| 2.1 | 1 | Chapter 2: 91 | Relates the coordinate frames and end-effector position error. Keep. |
| 2.2 | 1 | Chapter 2: 1065 | Builds the combined angular direction and perpendicular CoC displacement in three views. Keep. |
| 2.3 | 1 | Chapter 2: 1263 | Shows how reversing the tangential displacement changes the normal-force moment. Keep. |
| 3.1 | 1 | Chapter 3: 30 | Gives the overall operating-state flow and controller selection. Keep. |
| 3.2 | 1 | Chapter 3: 60 | Connects references, feedback, Cartesian impedance and additive torque terms. Keep. |
| 3.3 | 2 | Chapter 3: 44, 124 | Expands the surface-contact sequence and its connection to Contact-Impedance Hold. Keep. |
| 3.4 | 1 | Chapter 3: 258 | Shows the calibrated tool-face offsets and four corners used by the clearance calculation. Keep. |
| 3.5 | 1 | Chapter 3: 360 | Illustrates why the closest tool corner determines clearance. Keep. |
| 3.6 | 1 | Chapter 3: 393 | Distinguishes corner, edge and face cases for selecting the tool point. Keep. |
| 3.7 | 1 | Chapter 3: 549 | Makes the tool-point and TCP reference construction spatially explicit. Keep. |
| 3.8 | 1 | Chapter 3: 636 | Shows selectable null-space modes, live switching and pose capture. Keep; now explicitly referenced. |
| 4.1 | 2 | Chapter 4: 41, 106 | Shows the physical set-up and distinguishes it from the configured surface reference. Keep. |
| 4.2 | 1 | Chapter 4: 387 | Defines the entry offset and contact-end angular error against the calibrated normal. Keep. |
| 5.1 | 1 | Chapter 5: 40 | Compares commanded and model-estimated wrench during Contact Establishment. Keep. |
| 5.2 | 1 | Chapter 5: 68 | Supports the discussed translational impedance plausibility assessment. Keep; now explicitly referenced. |
| 5.3 | 1 | Chapter 5: 90 | Supports the discussed rotational impedance plausibility assessment. Keep; now explicitly referenced. |
| 5.4 | 1 | Chapter 5: 123 | Shows the TCP-centred baseline angular errors. Keep. |
| 5.5 | 1 | Chapter 5: 158 | Shows the rotational-stiffness comparison discussed in Case B. Keep. |
| 5.6 | 1 | Chapter 5: 190 | Shows the smaller angular-error variation across the tested translational stiffnesses. Keep. |
| 5.7 | 1 | Chapter 5: 224 | Shows the dependence on tangential CoC position and entry direction. Keep. |
| 5.8 | 2 | Chapter 5: 282, 304 | Connects angular-error histories to estimated force and moment and supports the settling comparison. Keep. |
| 5.9 | 2 | Chapter 5: 344, 414 | Compares cumulative motion across all seven joints for four null-space settings. Keep. |
| 5.10 | 1 | Chapter 5: 371 | Compares Jacobian conditioning during the same disturbance. Keep. |
| 5.11 | 1 | Chapter 5: 394 | Shows measured joint-1 motion over time and trial spread. Keep; its role differs from the cumulative seven-joint measure. |

Chapter sources:

- [Chapter 1](chapters/01_introduction.tex)
- [Chapter 2](chapters/02_theoretical_background.tex)
- [Chapter 3](chapters/03_software_implementation.tex)
- [Chapter 4](chapters/04_experimental_setup_and_evaluation.tex)
- [Chapter 5](chapters/05_results_and_discussion.tex)
