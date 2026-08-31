# T-mode K-frame consistency repeat

This repeat keeps the stiffnesses from the first t-mode run and keeps the
compliance centre at the TCP. Automatic damping is enabled with factor 1.0;
the active values are calculated from the operational-space inertia at t-mode
entry and recorded in the CSV. Null-space mode 0 removes the secondary
joint-space torque. The controller also logs both Franka wrench
representations, plus the measured offset from stiffness frame K to the TCP.

## Run the first trial

From the final-controller repository:

    cd ~/Desktop/Thesis_Final_Control
    ./experiments/run.sh T_MODE_KFRAME_REPEAT 1

Select t at the startup menu. Do not press g or p during the run. Watch the
controller time and perform these actions:

1. 0.5--3.0 s: leave the tool untouched and clear of the surface.
2. 3.5--7.5 s: push slowly by approximately 20 mm along the surface normal.
3. 8.0--12.0 s: hold the normal displacement stationary.
4. 12.0--17.0 s: keep the same normal displacement without rotating.
5. 17.0--21.0 s: keep the normal displacement and rotate approximately 5 deg
   about positive tangent 1.
6. 22.0--28.0 s: hold both displacement and rotation stationary.
7. 28.0--34.0 s: release the tool and leave it untouched.

At these gains, 20 mm corresponds to approximately 20 N and 5 deg corresponds
to approximately 1.31 N m. Exact manual targets are unnecessary because the
analysis uses the achieved pose errors.

## Analyse the first trial

From the thesis repository:

    cd ~/Desktop/MyOwn-thesis
    python3 professoremail/analyse_t_mode_consistency.py \
      ../Thesis_Final_Control/experiments/results/T_MODE_KFRAME_REPEAT/r01

The output must identify K_F_ext_hat_K as the estimator source. It prints the
calculated damping values, the measured K-to-TCP offset and the RMS residuals
between the independently logged O- and K-frame wrench representations. The
same damping values are written to the summary CSV and the professor-email
text. Inspect the plot before taking further trials.

If the first trace has clean stationary intervals, repeat the same procedure:

    cd ~/Desktop/Thesis_Final_Control
    ./experiments/run.sh T_MODE_KFRAME_REPEAT 2
    ./experiments/run.sh T_MODE_KFRAME_REPEAT 3

Then analyse all three:

    cd ~/Desktop/MyOwn-thesis
    python3 professoremail/analyse_t_mode_consistency.py \
      ../Thesis_Final_Control/experiments/results/T_MODE_KFRAME_REPEAT/r01 \
      ../Thesis_Final_Control/experiments/results/T_MODE_KFRAME_REPEAT/r02 \
      ../Thesis_Final_Control/experiments/results/T_MODE_KFRAME_REPEAT/r03

The command regenerates the plot, summary CSV and LaTeX results section used by
the professor-email PDF.
