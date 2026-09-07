# Generators for the Chapter 5 and appendix plots

Every generated plot the thesis includes is produced by a script in this
directory. They were recovered from the two experiment repositories on the lab
machine, `Thesis_Final_Control/analysis/` and
`MyController/experiments/analysis/`, and copied here unchanged apart from the
one edit noted at the end.

They had appeared lost because the figures were **renamed by hand** after they
were generated. A search of either repository for a current file name returns
nothing; the scripts still write the old case letters. The map below is the
missing link, and every row was checked by regenerating the figure and
comparing it against the file in `figures/`.

## Which script writes which figure

| Figure in `figures/` | Written by the script as | Script |
|---|---|---|
| `MAIN_B_KR.pdf` | `MAIN_A_KR.pdf` | `make_coc_figures.py` |
| `MAIN_C_KP.pdf` | `MAIN_B_KP.pdf` | `make_coc_figures.py` |
| `MAIN_H_direction.pdf` | `MAIN_C_direction.pdf` | `make_coc_figures.py` |
| `MAIN_D_sign.pdf` | `MAIN_E_sign.pdf` | `make_coc_figures.py` |
| `MAIN_D_wrench.pdf` | `MAIN_E_wrench.pdf` | `plot_coc_case.py` |
| `MAIN_D_diagnostics.pdf` | `MAIN_E_diagnostics.pdf` | `plot_setup_diagnostics.py` |
| `MAIN_DQ_metric_comparison.pdf` | same name | `compare_angle_metrics.py` |
| `MAIN_DQ_metric_summary.pdf` | same name | `compare_angle_metrics.py --summary-only` |
| `MAIN_NS_nullspace_automatic.pdf` | same name | `make_nullspace_figure.py` |

`make_coc_figures.py` also writes `MAIN_D_contact.pdf`, `MAIN_G_toolaxis.pdf`
and `MAIN_H_magnitude.pdf`, which are in `figures/` as `MAIN_A_contact.pdf`,
`MAIN_F_toolaxis.pdf` and `MAIN_G_magnitude.pdf` but are no longer included by
any chapter. It also writes `MAIN_F_frame.pdf`, retained in `figures/` as
`MAIN_E_frame.pdf`; the corresponding definition-frame experiment is no
longer reported. `plot_angle_descent.py` writes `MAIN_DQ_descent.pdf`, which is in
`figures/` and is likewise no longer included; it is kept here so that every
generated file in `figures/` has its generator.

`MAIN_D_diagnostics.pdf` joined that set on 2026-08-19. Its appendix section
was removed because it reached the same conclusion as the chapter's
`MAIN_D_wrench.pdf` — a similar commanded normal force at both outer Case-D
positions and a moment about \(t_1\) of opposite sign — with the two remaining
surface-frame components adding no distinction the thesis relies on. The file
and `plot_setup_diagnostics.py` stay, so the generator is still here if the
section is ever restored.

The thesis includes `MAIN_DQ_metric_summary.pdf` in place of the older
two-panel metric-comparison plot. The summary mode uses the archived derived
metrics without requiring the absent raw time-series files and avoids the
clipped label in the older figure.

The four Chapter 5 figures drawn in `pgfplots` — the Case-A bars, the Case-D
panels, the Case-D-against-Case-F comparison and the Case-G panels — have no
generator here. They are `.tex` sources in `figures/` and are drawn from the
means already tabulated in the thesis.

## Environment

The committed PDFs were drawn with **matplotlib 3.9.2**, read from the
`/Creator` and `/Producer` metadata of the files themselves rather than from a
record of the session. `requirements.txt` pins it:

    python3 -m venv .venv && . .venv/bin/activate
    pip install -r requirements.txt

The version matters more than it looks. Under matplotlib 3.1.2 every script
below still runs, every printed number is identical, and the curves are the
same, but two things in the drawing change. The tick locator chooses fewer
ticks, so a panel of `MAIN_D_wrench.pdf` carries ticks every 5 rather than
every 2.5. And the net-displacement label in panel (c) of
`MAIN_NS_nullspace_automatic.pdf` renders as `-0.006` rather than the `0.006`
in the committed file: `_net_value_label()` writes U+2212, which the committed
figure's embedded face silently drops. Section 5.5 reads
`the measured net displacement was negative, so its absolute value was 0.006`,
which is written against the committed rendering. Regenerating that figure in a
pinned environment keeps the sentence and the label in step; regenerating it in
an older one does not.

## Running them

`make_coc_figures.py` reads the campaign metrics. On the lab machine, pass the
authoritative derived file explicitly:

    python3 make_coc_figures.py \
        --metrics /path/to/Thesis_Final_Control/experiments/derived/metrics.csv \
        --out-dir /path/to/output

The other four read logged CSV from `experiments/results/` in the repository
they came from, and only run beside that data:

    python3 plot_setup_diagnostics.py --out-dir OUT
    python3 compare_angle_metrics.py \
        --results /path/to/Thesis_Final_Control/experiments/results \
        --metrics /path/to/Thesis_Final_Control/experiments/derived/metrics.csv \
        --out-dir OUT
    python3 plot_coc_case.py \
        'P2_t1_pos_m040/r01=CoC Position, $r_{c,t_2} = -40$ mm' \
        'P2_t1_pos_p000/r01=CoC at TCP, $r_{c,t_2} = 0$' \
        'P2_t1_pos_p040/r01=CoC Position, $r_{c,t_2} = 40$ mm' \
        --axis t1 --out MAIN_E_wrench \
        --results /path/to/Thesis_Final_Control/experiments/results \
        --out-dir OUT
    python3 make_nullspace_figure.py \
        --results /path/to/MyController/experiments/results \
        --out-dir OUT

`plot_coc_case.py` takes its trials on the command line; the three above are
the ones the reported figure uses. `plot_setup_diagnostics.py` has its two
trials as defaults in the file.

`figure_style.py` and `extract_metrics.py` are imported by the
`Thesis_Final_Control` scripts. `make_figures.py` is imported by
`make_nullspace_figure.py` for its colours and its `save` helper; the figures
`make_figures.py` writes when run on its own belong to the superseded set and
are not in the thesis.

## What Chapter 5 needs

Chapter 5 includes six figures. Four are `pgfplots` sources in `figures/` whose
coordinates are written into the `.tex` file, so they carry their own data and
redraw wherever the thesis compiles:

  * `results_case_a_bars.tex`
  * `results_case_b_stiffness.tex`
  * `results_case_c_stiffness.tex`
  * `results_case_d_panels.tex`

The other two are drawn here and read run records that are not in this
repository:

| Figure | Script | Reads |
|---|---|---|
| `MAIN_D_wrench.pdf` | `plot_coc_case.py` | `Thesis_Final_Control/experiments/results/P2_t1_pos_{m040,p000,p040}/r01/`, about 27 MB: each trial's `logs/*.csv` and its `params_effective/` |
| `MAIN_NS_nullspace_automatic.pdf` | `make_nullspace_figure.py` | `MyController/experiments/results/MAIN_NS{7,8}_*_20N_200mm/r0{1,2,3}/surface_grinding_controller_log.csv`, twelve files of about 27 MB each |

A checkout on its own therefore redraws four of the six. The remaining two need
the directories above copied across, and the `--results` argument then points
at wherever they were put.

Two cautions when copying the null-space records. `MyController`'s
`plane_calibration_*`, `plane_profile.txt`, `tool_axis_calibration_*`,
`tool_mount_status.txt` and `tool_profile.txt` are not to be published, and
`make_nullspace_figure.py` reads none of them, so they can be left behind.
And `MyController/experiments/analysis/make_nullspace_figure.py` is the
superseded two-panel generator; the copy in this directory is the authoritative
one.

## What the null-space script gained

`make_nullspace_figure.py` originally reported one redundant-motion quantity,
the integral of the projected joint-velocity magnitude, which Chapter 4 now
calls the **cumulative projected null-space motion**. That integral is a path
length, so it cannot distinguish a configuration that was displaced from one
that moved back and forth and ended where it started -- the difference between
the two sigma settings turns on exactly that.

The script now also integrates the projected joint velocity **without** the
magnitude, giving the net displacement \(\Delta q_{\mathrm{null}}\), and
resolves every run onto one signed axis in `net_displacements()`. The axis
comes from the condition without null-space torque: the recorded null direction
`sigma_n_best_*` is written only while the conditioning term is selecting a
sign, so it is zero throughout the runs that have no conditioning torque, and
the direction has to be recovered from the motion itself. At full row rank the
null space is one dimensional, so every net displacement lies along that one
axis. Two columns were added to `derived/MAIN_NS_automatic_summary.csv`:
`net_displacement_mean_rad` and `net_displacement_sd_rad`.

Running it against `MyController/experiments/results/` reproduces every
null-space value in Chapters 5 and 6.

The run records are not in this repository: the four reported conditions are
roughly \(320\,\mathrm{MB}\) of logged CSV inside a \(6.4\,\mathrm{GB}\)
archive, so they stay on the lab machine and the figure is committed as a PDF.
`--results` and `--out-dir` are therefore the normal way to run this script,
since the checkout holding it is not the checkout holding the data. Any machine
with a copy of `MyController/experiments/results/` reproduces
`MAIN_NS_nullspace_automatic.pdf` exactly.

The script and the committed PDF had drifted apart once before: the labels were
corrected in the script while the PDF in `figures/` was left as generated by an
earlier version, so the figure still read
\(\Delta\sigma_{\min,\mathrm{dist}}\), \(\Delta\eta_{\mathrm{dist}}\),
`Net Redundant Displacement` and `Peak Cartesian Position Error` against a
Section 5.5 that had moved to \(\Delta\sigma_{\min}\), \(\Delta\eta\) and
\(\lVert e_p\rVert_{\max}\). Regenerate the PDF in the same turn as a label
edit; a label change that is not rebuilt is invisible until someone reads the
compiled figure against the paragraph beside it.

## Plot-label edits

`compare_angle_metrics.py` labelled its first series `EE-inferred angular
deviation`, a term banned in the thesis. The published PDF was corrected by
patching the file itself, so the script and the figure had drifted apart. The
label here reads `Alignment angle from end-effector pose`, matching the figure.
Regenerating that figure now carries the same text as the published one; before
this edit it would have reintroduced the banned term. The two files are not
byte-identical, because the published PDF was patched in place and its objects
were renumbered, but the drawing and every string in it are the same.

`make_coc_figures.py` labels the data-independent direction comparison with the
configured orientation-offset notation used by the thesis. Its horizontal axis
therefore uses `Configured Orientation-Offset Direction` and
\(\theta_{\mathrm{offset}}\), not the withdrawn commanded-rotation wording.
