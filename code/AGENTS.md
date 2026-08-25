# Working rules for `code/`

**These instructions apply to every coding agent.** `code/CLAUDE.md` holds the
same text, regenerated from this file by `sync_agent_docs.ps1` and by the
pre-commit hook. **Edit this file, never `code/CLAUDE.md`.**

Controller and analysis source for the thesis. The prose rules in
[../THESIS_VOICE.md](../THESIS_VOICE.md) do **not** apply here — that file
governs thesis sentences, not comments or identifiers. Write code comments
normally.

## What this code is

This directory is thesis evidence, not a product. `backmatter/appendix_code.tex`
reproduces listings from these files, and Chapters 3–5 describe their behaviour
as fact. Two consequences:

- **Changing behaviour changes what the thesis claims.** Before altering a
  control law, gain, frame convention, sign, or metric definition, check whether
  a chapter states the current behaviour. If it does, the text has to move with
  the code, or the change must not be made.
- **Do not silently modernise.** Refactoring for its own sake breaks the
  correspondence between a listing in the appendix and the file it came from.

`code/cpp/` holds the real-time controller: `cartesian_impedance_controller_core.cpp`
is the core law, the `experiment_*.h` headers hold per-experiment parameter sets,
and the `impedance_*.cpp` files are the individual experiment programs.

`code/python/` holds post-hoc analysis of logged CSV. `evaluate_contact_alignment.py`
produces the alignment metrics reported in Chapter 5, and
`make_thesis_result_figures.py` generates the principal Chapter 5 figures.
(`cartesian_impedance_experiments.cpp` sits in this directory despite being C++.)

`code/python/figures/` holds the generators for the plots the thesis actually
includes, recovered from the two experiment repositories. The figures were
renamed by hand after they were generated, so the scripts still write the old
case letters; `code/python/figures/README.md` carries the name map and is the
first thing to read before changing a plot.

## Which controller is authoritative

Two controller repositories exist on the author's machine and they are **not**
equal in standing. Getting this wrong silently attributes the reported results
to the wrong implementation.

- **`Thesis_Final_Control/surface_grinding_controller` is the final
  controller.** Every contact experiment reported in the thesis — the
  calibrated-plane campaign, Cases A to H, the centre-of-compliance work — was
  run with it. It is the authority on the impedance law, the phase structure,
  the compliance-centre conventions, and the set-up evaluation. On the lab
  machine it also holds the campaign archive under `experiments/results/`,
  \(171\) run directories over the \(57\) reported settings, and the
  `experiments/derived/metrics.csv` that the contact figure scripts read.
  **A clone shows neither**: its `.gitignore` excludes
  `experiments/results/**/*.csv` for size and `experiments/derived/` entirely,
  so a session away from the lab machine sees run metadata without the logs and
  must not conclude the records were never kept.
- **`MyController` is superseded and must not be cited for the contact
  results.** The one part of it still in use is the **null-space pose-hold
  experiment under the internally commanded disturbance**, whose run records
  under `MyController/experiments/results/` are the source of the null-space
  values in Chapters 5 and 6 and of `MAIN_NS_nullspace_automatic.pdf`.
  `MyController/experiments/derived/metrics.csv` belongs to the superseded
  generation: it carries no `P2_` rows and does not reproduce any reported
  contact figure.
- **`code/cpp/` in this repository is older still.** It is the pose-tracking,
  virtual-wall and stiffness-variation controller from the earlier experiments,
  not the calibrated-plane controller. Do not read a contact-campaign
  convention out of it.

The practical consequence: a sign, gain, frame or metric convention for the
contact results is checked against `Thesis_Final_Control`, and a null-space
convention against `MyController`. A convention read from the wrong one is a
factual error in the thesis, not a stylistic one.

## Conventions that must match the thesis

These are stated in the text and cannot drift:

- Wrench ordering is force followed by moment.
- Position error is desired minus current: `e_p = p_d - p_EE`.
- Rotational error is `ΔR = R_EE^T R_d`, mapped to the base frame by
  left-multiplication with `R_EE`.
- The compliance-centre displacement is `r_c = p_c - p_TCP`; the tool-geometry
  lever to the selected tool point is `r_Tool = p_Tool - p_TCP`. They are different points and
  never interchangeable. The names `r_C` and `p_C` were replaced because one
  letter of case is not a readable distinction; do not reintroduce them.
- Six singular values belong to the 6×7 Jacobian, `σ_min = σ_6`; `v_7` is the
  structural null direction at full row rank.
- Control and logging rates are 1 kHz.

`O_F_ext_hat_K` is a **model-estimated** external wrench, never a measured one.
Keep that distinction in variable names and comments.

## Analysis scripts

- An analysis script must not invent, interpolate, or impute a measurement. If a
  run is missing, it is missing.
- Metric definitions are reported in Chapter 4. Changing how a metric is
  computed invalidates the numbers already written into Chapters 4 and 5 — say
  so rather than quietly re-running.
- Numbers produced here end up in the thesis, so keep the reported precision
  within what three repetitions support.

## Plot scripts

Plot styling follows [../FIGURE_STYLE.md](../FIGURE_STYLE.md). The settled
matplotlib setup lives at the top of `make_thesis_result_figures.py`: `usetex`
on with `lmodern`, Latin Modern Roman serif, 9.5 pt labels, 8.5 pt ticks, and a
colour-blind-safe palette. Match it rather than introducing a second style.

Export vector PDF at approximately final printed width, and inspect the result
inside the compiled document rather than as a standalone file.

## Attribution

Where a file descends from the libfranka examples, keep the attribution — the
thesis cites `libfrankaCartesianExample`, and the appendix text should say which
listings derive from it rather than presenting them as written from scratch.
