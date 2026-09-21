Contact angular error: source records, calculation and numerical interpretation
===============================================================================

Definition
----------
theta_err(t) is the base-frame vector for the shortest rotation from the
inward configured surface normal -n_s to the calibrated tool-face normal
R_EE(t) n_Tool,EE. Its first-tangent component is theta_err,t1(t). At contact
entry it is the measured angular offset theta_meas,t1. Positive/negative
directions therefore remain those already used for the entry angular offset.

The comparison uses the original calibrated/configured surface reference.
It estimates physical angular misalignment subject to calibration and tool
mount errors. The calibration uncertainty is unquantified. The t1 component
can be zero while the total angle between the two normals remains nonzero.

The final controller already calculated the full shortest normal rotation
online. Its angular_deviation_t1_deg/t 2_deg/normal_deg columns describe the
reverse direction, from the measured tool normal to the inward configured
normal. Negating this vector gives theta_err. For older names the corresponding
fields are alignment_error_t1_deg/t 2_deg/normal_deg. No scalar subtraction of
entry angle and contact response is used anywhere in the reported calculation.

Authoritative controller implementation:
surface_grinding_controller/src/control/cartesian_impedance.cpp:
 currentToolAxisInBase, surfaceToolAxisInBase, toolSurfaceAlignmentErrorBase.
surface_grinding_controller/src/runtime/control_loop.cpp:
 row.angular_deviation_surface = R_base_surface.transpose() *
 toolSurfaceAlignmentErrorBase(params, R_EE, R_base_surface).
surface_grinding_controller/src/report/csv_logging.cpp:
 degree conversion and angular_deviation_* fields.
The same normal formula exists in the recorded ae 031 cd code revision.

Data availability and endpoint convention
----------------------------------------
The selected main-contact archive has 93 trials across 31 unique settings.
Each setting has three repetitions. All 93 controller terminal.log reports
contain full normal-error components at contact entry and at contact end,
reported to 0.01 degrees. All selected raw CSV logs are available from the
Thesis_Final_Control archive through Git LFS. Three representative r01 trials
supply the existing time histories.
The script never imputes missing measurements or obtains them from old gamma.

For consistency, every grouped mean and sample standard deviation uses the
entry/final normal-vector values in the original controller terminal reports,
including the three trials whose complete CSVs are available. The terminal
report's final vector describes the contact-end orientation. It is not a
final-second average. Reported values are rounded to 0.01 degrees before the
three-repetition statistics are calculated. Each individual reported endpoint
therefore carries up to 0.005 degree rounding uncertainty, in addition to the
unquantified calibration/mount uncertainty. A displayed SD of 0.00 means the
archived rounded values coincide, not that physical uncertainty is absent.

The representative time traces use all recorded phase==2 samples, with time
shifted by the first such sample. Each available trace runs from 0 to 5.001 s,
and the archived controller report identifies the nominal duration as 5.0 s.
Do not resample or interpolate to manufacture a different endpoint. The old
gamma audit uses the last recorded phase==2 e_R sample, exactly reproducing
the original metrics.csv endpoint. Force/moment final-second values use the
recorded interval t_contact >= last_t_contact -1 s and include both endpoints.

All 93 selected contact trials retain exactly these calibration parameters:
 tool_axis_ee = (0.026387069, -0.006678514, 0.999629492)
 tool_axis_target_sign = -1
 surface_tilt_x_deg = -1.585191335
 surface_tilt_y_deg = 0.988473281
 surface_tangent1_hint_base = (1,0,0)
The script reads the archived params_effective values separately for each trial.
Null-space calibration records are not used for the contact trials.

Independent consistency checks
------------------------------
For the three complete CSVs, the script reconstructs the entry tool normal
from the full logged entry normal vector. It then transports that normal with
the measured EE relative rotation e_R(t), accounting for the first logged
e_R sample. It freshly calculates the shortest vector between the configured
normal and that reconstructed tool normal at every sample. This independent
full 3D reconstruction matches the negated logged normal vector within
0.000078 degrees. Raw R_EE matrices are not themselves stored in these CSVs.
The original online normal vectors are retained as the reported data.
The raw endpoint versus terminal report differences for the three traces lie
within the 0.005 degree report rounding interval. All 93 terminal components
also exactly match the earlier extracted metrics.csv records. The three
recomputed old gamma endpoints match the original extracted metric to 2 e-15
degrees. audit.json and representative_trace_endpoints.csv preserve the checks.

Files and reproducibility
-------------------------
Installed location in thesis:
 code/python/figures/contact_angular_error/

recalculate_normal_error.py:
 Run with Python plus numpy, pandas and scipy. It discovers a sibling
 Thesis_Final_Control archive or accepts --root PATH. --out PATH selects
 the destination. Without --out it writes beside the script.

grouped_results.csv / grouped_results.json:
 31 rows, one per run_id. Columns include n, entry_t1_deg_mean/sd,
 final_t1_deg_mean/sd, final_total_deg_mean/sd. Unrounded arithmetic results
 are retained for reproducibility, but audience-facing values use 2 decimals.

per_trial_results.csv:
 93 rows with original report endpoints, source paths, SHA256 hashes,
 source resolution and old_gamma_* audit columns.

trace_P2_t1_pos_{m040,p000,p040}_r01.csv:
 Full recorded traces. Columns t_contact_s, theta_err_t1_deg,
 theta_err_t 2_deg, total_error_deg, fn_est_N, moment_t1_est_Nm,
 old_gamma_t1_deg and reconstructed tool_normal_x/y/z.

representative_trace_endpoints.csv:
 Full-precision trace endpoint values, exact file hashes, geometric audit
 differences, report rounding differences, final-second wrench means and
 optional endpoint-change timing checks. Those checks do not automatically
 define a new settling-time metric in the thesis.

source_provenance.json:
 Every selected report hash, original run provenance and archived parameters.

wider_coc_source_audit.json:
 Checks all 12 added +/-80 mm trials against corresponding +/-40 mm settings.
 Only compliance_center_offset_ee_y differs. All reports end by the five-second
 timer and have exit status zero. Plot r_c,t2 is -1000 * offset_ee_y in mm.

Main numerical interpretation
-----------------------------
Baseline final t1 error, mean +/- sample SD in degrees:
 entry 0.69: +1.65 +/-0.01
 entry+9.31: +1.75 +/-0.00
 entry-9.41: +1.41 +/-0.06
Both tilted conditions reduce the magnitude of the calibrated-reference t1
error. The negative condition crosses that component's zero. The nominal-zero
condition instead increases its error. Final-error magnitude reductions from
group means are 81.2% and 85.0% for the positive and negative tilted conditions.
These percentages describe the calibrated-reference t1 component.

Rotational stiffness 5/15/50 N m/rad gives final errors 1.75/2.04/6.58 degrees.
The rise from 5 to 50 is 4.83 degrees. Higher rotational stiffness leaves a
larger residual error in the tested direction.

Tangential translational stiffness 300/800/2000 N/m gives final errors
1.68/1.69/1.75 degrees. The span is 0.07 degrees, not the old gamma span 0.03.

CoC positions[-100,-90,-80,-40,-20,-10,0,10,20,40,80,90,100]mm give
positive-entry angular errors
[31.77,10.52,9.35,9.13,8.33,1.89,1.75,1.68,1.60,1.48,1.17,1.11,0.83] degrees,
and negative-entry angular errors
[2.76,2.48,2.23,1.99,1.86,1.82,1.41,0.94,-4.40,-9.24,-9.56,-11.91,-33.98] degrees.
All means and sample SD use three report endpoints. Original points are
unchanged. The largest sample SD is 1.33 degrees at -100 mm, positive entry.
Across-position entry means are 9.33/-9.38 degrees.

The +/-90 and +/-100 mm conditions were acquired on 2026-09-21 in a later
session with the same saved calibration and impedance parameters. Their raw
logs, saved settings, validation and provenance are under
Thesis_Final_Control/experiments/coc_extension and experiments/results.
The smallest positive-entry mean is 0.83 degrees at +100 mm, 52.6% below
TCP. The negative-entry minimum remains 0.94 degrees at +10 mm, 33.7% below
TCP. Percentages use unrounded means. See coc_extension_source_audit.json.

For representative r01 traces at-40/TCP/+40 mm, final t1 errors are
9.11717/1.749733/1.486307 degrees. Total normal-angle magnitudes are
9.39224/3.33981/3.06789 degrees. Final-second model-estimated normal forces
are-82.8608/-79.0240/-78.0291 N, preserving rounded-83/-79/-78 N labels.
The final-second estimated TCP moments are 4.0692/0.7317/-2.5401 N m.

The endpoint-band time is the first recorded contact time after which
theta_err,t1 stays within +/-0.1 degree of its own last recorded value through
contact end, inclusive. It is 2.489 s for the +40 mm trace and 3.601 s for the
TCP trace, a difference of 1.112 s. Display approximately 2.5 s and 3.6 s,
and 1.1 s earlier. This reports entry into a specified endpoint band, without
claiming that the curve is perfectly constant thereafter. At 2.304 s the
+40 mm error is still 2.62 degrees, so the old 2.3 s steady-level claim should
not be retained. There is a brief undershoot near 2.4 s.
