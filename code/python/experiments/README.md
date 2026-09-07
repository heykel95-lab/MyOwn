# Run records for the two generated figures

The thesis includes five figures drawn by a script rather than typeset in
`pgfplots`: `figures/MAIN_D_wrench.pdf`,
`figures/MAIN_NS_nullspace_automatic.pdf` and the three
`figures/MAIN_WR_*.pdf`. This directory holds exactly the run records those
scripts read and cannot find elsewhere in the repository, so all five redraw
from a checkout with no argument and no access to the lab machine. The
remaining inputs, one wrench CSV and one controller log, are committed under
`professoremail/`.

    python3 ../figures/plot_coc_case.py \
        'P2_t1_pos_m040/r01=CoC Position, $r_{c,t_2} = -40$ mm' \
        'P2_t1_pos_p000/r01=CoC at TCP, $r_{c,t_2} = 0$' \
        'P2_t1_pos_p040/r01=CoC Position, $r_{c,t_2} = 40$ mm' \
        --axis t1 --out MAIN_E_wrench --out-dir OUT

    python3 ../figures/make_nullspace_figure.py --out-dir OUT

`results/` is where both scripts resolve by default, so `--results` is only
needed if the records are moved elsewhere. Install the pinned environment from
`../figures/requirements.txt` first; an older matplotlib reproduces every number
but redraws the figures slightly differently, which
`../figures/README.md` describes.

## What is here

| Path | Read by | Purpose |
|---|---|---|
| `results/P2_t1_pos_{m040,p000,p040}/r01/logs/surface_grinding_controller_log.csv` | `plot_coc_case.py` | the three Case-D contact traces |
| `results/P2_t1_pos_{m040,p000,p040}/r01/params_effective/*.conf` | `plot_coc_case.py` | the surface tilt the traces are resolved on |
| `results/MAIN_NS{7,8}_*_20N_200mm/r0{1,2,3}/surface_grinding_controller_log.csv` | `make_nullspace_figure.py` | twelve pose-hold runs, three per condition |
| `results/T_MODE_MANUAL_D_REPEAT/r01/params_effective/*.conf` | `make_wrench_evaluation_figures.py` | the parameters of the plausibility run |
| `results/T_MODE_MANUAL_D_REPEAT/r01/terminal.log` | `make_wrench_evaluation_figures.py` | confirms the setup-impedance hold; the analysis refuses a run without it |
| `derived/MAIN_NS_automatic_summary.csv` | written, not read | the table `make_nullspace_figure.py` regenerates |

The Case-D records come from `Thesis_Final_Control`, the null-space records from
`MyController`. `code/AGENTS.md` explains why the two are not interchangeable.
The derived table is committed as generated output rather than as an input: a
regeneration overwrites it, so `git diff` reports any drift between the archive
and the numbers Section 5.5 reports. It was byte-identical to the lab
machine's copy when the records were placed here.

## What is deliberately not here

The archives these came from are far larger: 171 run directories in
`Thesis_Final_Control` and 6.4 GB of results in `MyController`. Only the files
the two scripts open were copied, so this directory stays at roughly 343 MB
rather than carrying an archive the thesis does not draw on.

That excludes, for the Case-D trials, the `r02` and `r03` repetitions, which the
reported figure does not use, and the set-up PDFs beside each log. For the
null-space runs it excludes `surface_grinding_controller_sigma_debug.csv`, the
per-run `terminal.log`, and the `meta.txt`, `overlay.txt`, `about.txt` and
`provenance.txt` stamps.

It also excludes, by a standing rule rather than for size,
`MyController`'s measured plane and tool-axis calibration files:
`plane_calibration_*`, `plane_profile.txt`, `tool_axis_calibration_*`,
`tool_mount_status.txt` and `tool_profile.txt`. These are not to be published.
`make_nullspace_figure.py` reads none of them, so their absence costs nothing.
