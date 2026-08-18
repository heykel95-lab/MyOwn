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
| `MAIN_E_frame.pdf` | `MAIN_F_frame.pdf` | `make_coc_figures.py` |
| `MAIN_D_wrench.pdf` | `MAIN_E_wrench.pdf` | `plot_coc_case.py` |
| `MAIN_D_diagnostics.pdf` | `MAIN_E_diagnostics.pdf` | `plot_setup_diagnostics.py` |
| `MAIN_DQ_metric_comparison.pdf` | same name | `compare_angle_metrics.py` |
| `MAIN_NS_nullspace_automatic.pdf` | same name | `make_nullspace_figure.py` |

`make_coc_figures.py` also writes `MAIN_D_contact.pdf`, `MAIN_G_toolaxis.pdf`
and `MAIN_H_magnitude.pdf`, which are in `figures/` as `MAIN_A_contact.pdf`,
`MAIN_F_toolaxis.pdf` and `MAIN_G_magnitude.pdf` but are no longer included by
any chapter.

The four Chapter 5 figures drawn in `pgfplots` — the Case-A bars, the Case-D
panels, the Case-D-against-Case-F comparison and the Case-G panels — have no
generator here. They are `.tex` sources in `figures/` and are drawn from the
means already tabulated in the thesis.

## Running them

`make_coc_figures.py` needs no data. Its values are the means reported in
Chapter 5, written into the file, so it runs anywhere:

    python3 make_coc_figures.py --out-dir /path/to/output

The other four read logged CSV from `experiments/results/` in the repository
they came from, and only run beside that data:

    python3 plot_setup_diagnostics.py --out-dir OUT
    python3 compare_angle_metrics.py --out-dir OUT
    python3 plot_coc_case.py \
        "P2_t1_pos_m040/r01=centre -40 mm" \
        "P2_t1_pos_p000/r01=centre 0 mm" \
        "P2_t1_pos_p040/r01=centre +40 mm" \
        --axis t1 --out MAIN_E_wrench --out-dir OUT
    python3 make_nullspace_figure.py

`plot_coc_case.py` takes its trials on the command line; the three above are
the ones the reported figure uses. `plot_setup_diagnostics.py` has its two
trials as defaults in the file.

`figure_style.py` and `extract_metrics.py` are imported by the
`Thesis_Final_Control` scripts. `make_figures.py` is imported by
`make_nullspace_figure.py` for its colours and its `save` helper; the figures
`make_figures.py` writes when run on its own belong to the superseded set and
are not in the thesis.

## The one edit

`compare_angle_metrics.py` labelled its first series `EE-inferred angular
deviation`, a term banned in the thesis. The published PDF was corrected by
patching the file itself, so the script and the figure had drifted apart. The
label here reads `Alignment angle from end-effector pose`, matching the figure.
Regenerating that figure now carries the same text as the published one; before
this edit it would have reintroduced the banned term. The two files are not
byte-identical, because the published PDF was patched in place and its objects
were renumbered, but the drawing and every string in it are the same.
