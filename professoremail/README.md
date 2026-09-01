# Professor email figures

`Professor_Email_Figures.pdf` is the document prepared for the professor email.
It contains the existing contact-sequence wrench comparison, the prepared
quasi-static `t`-mode check and its measured-results section, followed by the
controller state flow, Cartesian impedance block diagram, surface-contact
sequence, and Cartesian pose-hold flowchart. Each item occupies its own section
and page.

The plot compares absolute commanded and model-estimated \(F_n\) and
\(M_{t_1}\) during Contact Establishment for `P2_t1_pos_p000/r04`, with the
compliance centre at the TCP. The grey interval from 4 to 5 seconds supplies
the stationary means. The commanded wrench is resolved on the configured
surface axes. Libfranka supplies the estimated spatial wrench on stiffness
frame \(K\), expressed in the base frame.

The plot starts directly from Libfranka's absolute estimator output using
`external_wrench = robot_state.O_F_ext_hat_K`; its first and last three entries
are logged as `external_force` and `external_moment`. The plotted scalars are
projections of these direct vector values, not separate raw estimator
variables. They do not use the clearance-referenced signals formed by
subtracting the stored pre-contact wrench. Since \(K\) coincides with the TCP
in this run, the plotted components are
\(F_{n,\mathrm{est}}=n_s^\top{}^{O}f_{\mathrm{ext},K}\) and
\(M_{t_1,\mathrm{est}}=t_1^\top({}^{O}m_{\mathrm{ext},K}
-p_{\mathrm{TCP}}\times{}^{O}f_{\mathrm{ext},K})\). They are compared with
the corresponding absolute commanded components.

The stationary values are `Fn_cmd = -80.312 N`,
`Fn_est = -78.451 N`, `Mt1_cmd = +0.635 N m`, and
`Mt1_est = +0.604 N m`. The estimate differs from the command by `2.32%` for
normal force and `4.87%` for tangent-1 moment. Both comparisons are consistent
in sign and magnitude for this single trace.

Regenerate the plot from the thesis repository root with:

```sh
python3 professoremail/plot_fn_mt1_comparison.py \
  ../Thesis_Final_Control/experiments/results/P2_t1_pos_p000/r04/logs/surface_grinding_controller_log.csv \
  ../Thesis_Final_Control/experiments/results/P2_t1_pos_p000/r04/params_effective/surface.conf \
  --out-dir professoremail
```

Then compile the combined document from the same directory:

```sh
pdflatex -interaction=nonstopmode -output-directory professoremail \
  professoremail/Professor_Email_Figures.tex
```

The plot source also writes `fn_mt1_commanded_vs_estimated.csv`. It contains
the plotted pairs at the controller timestamps. The untouched controller
record used to create it is included as
`P2_t1_pos_p000_r04_controller_log.csv`.

The PDF records the effective Contact Establishment set-up beside the plot:
`Kp = [2000, 2000, 350] N/m`, `KR = [5, 5, 50] N m/rad`, automatically
calculated `Dp = [231.2, 177.9, 112.1] N s/m`, and
`DR = [1.5, 1.9, 1.2] N m s/rad`, all ordered as `[t1, t2, n]`. The compliance
centre is at the TCP:
`r_c = p_c - p_TCP = [0, 0, 0] mm` in the configured surface basis.
The entry-to-end rotation about \(t_1\) is `-7.27 deg`. The pressure centre was
not measured. The `8.09 mm` lever shown in the discussion is therefore a
quasi-static force/moment equivalent, not a measured contact location.

## Dedicated t-mode consistency test

The dedicated test is kept separate from the earlier contact-sequence plot.
`t_mode_consistency_overlay.txt` makes the setup impedance decoupled at the TCP,
disables null-space torque, uses configured damping, and sets
`Kp_normal = 1000 N/m` and `KR_tangent1 = 15 N m/rad`. The accepted nominal
checks are `20.0 N` at `20 mm` and `1.309 N m` at `5 deg`.

Create the controller setup once from the thesis repository root:

```sh
mkdir -p ../Thesis_Final_Control/experiments/setups/T_MODE_CONSISTENCY
cp professoremail/t_mode_consistency_overlay.txt \
  ../Thesis_Final_Control/experiments/setups/T_MODE_CONSISTENCY/overlay.txt
cp professoremail/t_mode_consistency_about.txt \
  ../Thesis_Final_Control/experiments/setups/T_MODE_CONSISTENCY/about.txt
```

The recorded consistency run is:

```sh
./experiments/run.sh T_MODE_CONSISTENCY 1
```

Mode `t` was selected at the startup menu. The achieved stationary increments
were about `23 mm` along the surface normal and `5.2 deg` about tangent 1. The
normal load remained applied during the rotation.

Generate the result plot, CSV and LaTeX section from the thesis repository:

```sh
python3 professoremail/analyse_t_mode_consistency.py \
  ../Thesis_Final_Control/experiments/results/T_MODE_CONSISTENCY/r01
pdflatex -interaction=nonstopmode -output-directory professoremail \
  professoremail/Professor_Email_Figures.tex
```

The analysis refuses logs that do not confirm `t` mode or the prepared
decoupled parameters. It uses the untouched baseline for normal force. It
transports the base-relative moment to the TCP, then subtracts the loaded
pre-rotation baseline to isolate the moment increment. It retains the
surface-frame component signs and reports the quasi-static spring prediction,
logged command, model estimate, baseline noise, signal-to-noise ratio and
agreement status. The result is a one-run consistency check, not a
repeatability claim.

### Explicit K-frame repeat

The prepared T_MODE_KFRAME_REPEAT setup retains the same stiffnesses and zero
compliance-centre shift. It uses automatic damping with factor 1.0 and
null-space mode 0. The damping calculated at t-mode entry is stored in the CSV
and reported in the professor-email text. The rebuilt controller additionally
logs K_F_ext_hat_K rotated into the base axes and the measured K-to-TCP offset.
The analysis uses that explicitly K-referenced moment for the repeat and
cross-checks it against the simultaneously logged O_F_ext_hat_K signal.
Follow professoremail/T_MODE_KFRAME_REPEAT_PROTOCOL.md for the timed hand
motions, first-trial check and optional three-trial analysis.

### Manual-damping consistency trial

The completed T_MODE_MANUAL_D_REPEAT trial reproduces the original manual
damping while retaining the explicit K-frame wrench diagnostics. It uses
DR_t1=10.01 N m s/rad, rc=0 and null-space mode 0. The professor-email result
uses the stationary force interval from 8 to 13 s and the stationary moment
interval from 28.5 to 31 s. Both component checks are consistent.
`T_MODE_MANUAL_D_REPEAT_r01_controller_log.csv` is the untouched controller
CSV for this measured trial; `t_mode_consistency_summary.csv` contains the
plateau values used in the table.

## First-plot Contact Establishment diagnostic

The proposed `T_MODE_MOMENT_DIAGNOSTIC` is not used for the first plot. That
hand-operated hold checks a different controller state. The first plot is
repeated with `P2_t1_pos_p000/r04` through the automatic `s` sequence. Its
original gains, automatic damping factor 1.9, null-space mode 3 and zero
compliance-centre lever remain unchanged.

Analyse the archived trial with:

```sh
python3 professoremail/analyse_contact_moment_diagnostic.py \
  ../Thesis_Final_Control/experiments/results/P2_t1_pos_p000/r04
```

The professor-email plot uses the absolute TCP-referenced moment.
