# T-mode manual-damping repeat

This repeat reproduces the impedance parameters of the original t-mode trial
while retaining the explicit K-frame wrench diagnostics. The active gains in
the surface basis [t1,t2,n] are:

    Kp = [2000, 2000, 1000] N/m
    Dp = [10, 10, 175] N s/m
    KR = [15, 5, 50] N m/rad
    DR = [10.01, 10.01, 10] N m s/rad

Automatic damping is disabled. The compliance-centre shift and null-space
torque are also disabled, so rc=0 and null-space mode 0.

## Run the trial

From the final-controller repository:

    cd ~/Desktop/Thesis_Final_Control
    ./experiments/run.sh T_MODE_MANUAL_D_REPEAT 2

Select t at the startup menu. Do not press g or p. Use the controller time for
the following actions:

1. 0.5--3.0 s: leave the tool untouched.
2. 3.5--7.5 s: push slowly by approximately 20 mm along the surface normal.
3. 8.0--13.0 s: hold the normal displacement stationary.
4. 13.0--17.0 s: maintain the same push without rotating.
5. 17.0--22.0 s: rotate approximately 5 deg about positive tangent 1.
6. 22.0--31.0 s: maintain the displacement and angle. Apply only the
   counter-torque needed to prevent the controller from returning.
7. 31.0--34.0 s: release the tool.

The stronger manual rotational damping should be felt during the rotation.
The stationary comparison should begin only after the rotational transient.
Use 28.5--31 s when that interval is visibly stationary.

## Analyse the trial

From the thesis repository:

    cd ~/Desktop/MyOwn-thesis
    python3 professoremail/analyse_t_mode_consistency.py \
      ../Thesis_Final_Control/experiments/results/T_MODE_MANUAL_D_REPEAT/r02 \
      --force-window 8 13 \
      --moment-baseline-window 13 17 \
      --moment-window 28.5 31

The output must identify K_F_ext_hat_K as the estimator source and report
DR_used_t1=10.01 N m s/rad.
