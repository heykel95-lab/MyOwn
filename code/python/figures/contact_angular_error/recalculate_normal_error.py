"""Recalculate main contact angular errors from archived controller records.

All 93 contact trials have terminal reports containing entry and end normal-error
vectors to 0.01 degrees. Use those consistent records for grouped statistics.
Raw CSV logs are archived for these trials. Three representative trials
are independently reconstructed below for the existing time-history figure.

The archive includes full normal-error vectors but no measured R_EE matrices.
Those vectors were calculated online from R_EE and the calibrated tool axis.
We recover the entry tool normal from that full vector, transport it with the
measured EE relative rotation e_R(t), and independently calculate the shortest
normal-to-normal rotation at every recorded Contact Establishment sample.
The result is checked against the negative of the logged full normal error.
No scalar subtraction of entry angle and contact response is used.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation

def find_control_root() -> Path:
    """Find the control archive beside a parent checkout, or accept --root."""
    for parent in (Path.cwd(), *Path(__file__).resolve().parents):
        candidate = parent / "Thesis_Final_Control"
        if (candidate / "experiments" / "results").is_dir():
            return candidate
    return Path("Thesis_Final_Control")


ROOT = find_control_root()
POSITIONS = [-100, -90, -80, -40, -20, -10, 0, 10, 20, 40, 80, 90, 100]
TAG = lambda p: f"{'m' if p < 0 else 'p'}{abs(p):03d}"
RUNS = ["P6_zero_p000", "A_rot_t1_15", "A_rot_t1_50",
        "B_trans_t1_0300", "B_trans_t1_0800"] + [
    f"P2_t1_{direction}_{TAG(p)}" for direction in ("pos", "neg") for p in POSITIONS]
TRACE_RUNS = ["P2_t1_pos_m040", "P2_t1_pos_p000", "P2_t1_pos_p040"]


def params(directory: Path) -> dict[str, float]:
    values = {}
    for file in directory.glob("*.conf"):
        for raw in file.read_text().splitlines():
            line = raw.split("#")[0].strip()
            if "=" in line:
                key, val = map(str.strip, line.split("=", 1))
                try:
                    values[key] = float(val)
                except ValueError:
                    pass
    return values


def unit(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)


def frame_from_params(p: dict[str, float]) -> np.ndarray:
    rx = Rotation.from_euler("x", p["surface_tilt_x_deg"], degrees=True).as_matrix()
    ry = Rotation.from_euler("y", p["surface_tilt_y_deg"], degrees=True).as_matrix()
    n = unit(ry @ rx @ np.array([0., 0., 1.]))
    hint = np.array([p[f"surface_tangent1_hint_base_{a}"] for a in "xyz"])
    t1 = unit(hint - np.dot(hint, n) * n)
    return np.column_stack([t1, np.cross(n, t1), n])


def shortest_vector(reference: np.ndarray, current: np.ndarray) -> np.ndarray:
    """Shortest rotation reference -> each current normal, base-frame radians."""
    cross = np.cross(np.broadcast_to(reference, current.shape), current)
    sin_angle = np.linalg.norm(cross, axis=1)
    dot = np.clip(current @ reference, -1., 1.)
    angle = np.arctan2(sin_angle, dot)
    if np.any((sin_angle < 1e-12) & (dot < 0)):
        raise ValueError("Antiparallel normals make shortest rotation axis ambiguous")
    scale = np.divide(angle, sin_angle, out=np.ones_like(angle), where=sin_angle > 1e-12)
    return cross * scale[:, None]


def sha256(file: Path) -> str:
    return hashlib.sha256(file.read_bytes()).hexdigest()


def process(root: Path, out: Path, run: str, repeat: str) -> tuple[dict, dict]:
    trial = root / "experiments" / "results" / run / repeat
    logs = list((trial / "logs").glob("*.csv"))
    if len(logs) != 1:
        raise ValueError(f"Expected one archived CSV: {trial}, found {len(logs)}")
    log = logs[0]
    p = params(trial / "params_effective")
    frame = frame_from_params(p)
    reference = -frame[:, 2]
    assert p["tool_axis_target_sign"] == -1.0
    columns = pd.read_csv(log, nrows=0).columns
    state = "phase" if "phase" in columns else "state"
    metric = "angular_deviation" if "angular_deviation_t1_deg" in columns else "alignment_error"
    component_columns = ([f"{metric}_{axis}_deg" for axis in ("t1", "t2", "normal")])
    total_column = "angular_deviation_deg" if "angular_deviation_deg" in columns else "alignment_angle_deg"
    needed = ["time", state, *component_columns, total_column] + [
        f"{prefix}_{axis}" for prefix in ("e_R", "p_EE", "external_force", "external_moment") for axis in "xyz"]
    d = pd.read_csv(log, usecols=needed)
    d = d.loc[d[state] == 2].reset_index(drop=True)
    if len(d) < 4000:
        raise ValueError(f"Incomplete five-second contact phase: {trial}")
    t = d["time"].to_numpy()
    t = t - t[0]
    # Online record describes tool normal -> configured inward normal.
    online = d[component_columns].to_numpy()
    theta_entry_base = -np.radians(online[0]) @ frame.T
    entry_tool_normal = Rotation.from_rotvec(theta_entry_base).apply(reference)
    e_r = d[[f"e_R_{a}" for a in "xyz"]].to_numpy()
    # e_R is Log(R_reference R_EE(t)^T) in base coordinates. Account for
    # sub-sample capture timing by retaining the first logged e_R vector.
    held_tool_normal = Rotation.from_rotvec(e_r[0]).apply(entry_tool_normal)
    tool_normals = Rotation.from_rotvec(-e_r).apply(held_tool_normal)
    theta_base = shortest_vector(reference, tool_normals)
    theta_surface = np.degrees(theta_base @ frame)
    # These are independent full-vector consistency checks, not tests of a
    # scalar angle subtraction. Use a tolerance ten times finer than the
    # 0.01-degree reporting precision and record the actual residual.
    reconstruction_error = float(np.max(np.abs(theta_surface + online)))
    if reconstruction_error > 1e-3:
        raise ValueError(f"Full 3D reconstruction differs in {run}/{repeat}: {reconstruction_error} deg")
    total = np.linalg.norm(theta_surface, axis=1)
    if np.max(np.abs(total - d[total_column])) > 1e-3:
        raise ValueError(f"Total normal-angle mismatch: {run}/{repeat}")
    # Use directly logged normal vector for reported precision. The independent
    # recomputation agrees to substantially better precision than reporting.
    theta = -online
    total = d[total_column].to_numpy()
    old_gamma = np.degrees(e_r @ frame)
    force = d[[f"external_force_{a}" for a in "xyz"]].to_numpy()
    moment = d[[f"external_moment_{a}" for a in "xyz"]].to_numpy()
    position = d[[f"p_EE_{a}" for a in "xyz"]].to_numpy()
    fn = force @ frame[:, 2]
    mt1 = (moment - np.cross(position, force)) @ frame[:, 0]
    row = dict(run_id=run, repeat=repeat, samples=len(d),
               duration_s=float(t[-1]), log_path=str(log), log_sha256=sha256(log),
               reconstruction_max_abs_deg=reconstruction_error)
    for i, axis in enumerate(("t1", "t2", "n")):
        row[f"entry_{axis}_deg"] = float(theta[0, i])
        row[f"final_{axis}_deg"] = float(theta[-1, i])
        row[f"change_{axis}_deg"] = float(theta[-1, i] - theta[0, i])
        row[f"old_gamma_{axis}_deg"] = float(old_gamma[-1, i])
    row.update(entry_total_deg=float(total[0]), final_total_deg=float(total[-1]),
               final_second_fn_est_N=float(np.mean(fn[t >= t[-1] - 1.])),
               final_second_moment_t1_est_Nm=float(np.mean(mt1[t >= t[-1] - 1.])),
               reduction_abs_t1_deg=float(abs(theta[0, 0]) - abs(theta[-1, 0])),
               crossed_t1_zero=bool(np.sign(theta[0, 0]) != np.sign(theta[-1, 0])))
    if run in TRACE_RUNS and repeat == "r01":
        trace = pd.DataFrame(dict(t_contact_s=t, theta_err_t1_deg=theta[:, 0],
            theta_err_t2_deg=theta[:, 1], total_error_deg=total,
            fn_est_N=fn, moment_t1_est_Nm=mt1,
            old_gamma_t1_deg=old_gamma[:, 0],
            tool_normal_x=tool_normals[:, 0], tool_normal_y=tool_normals[:, 1],
            tool_normal_z=tool_normals[:, 2]))
        trace.to_csv(out / f"trace_{run}_{repeat}.csv", index=False, float_format="%.12g")
        # Descriptive times only: first time after which error remains within
        # 0.1 degrees of its own endpoint, and the 90% change crossing.
        outside = np.flatnonzero(np.abs(theta[:, 0] - theta[-1, 0]) > .1)
        row["within_0p1deg_of_endpoint_after_s"] = float(t[outside[-1] + 1]) if len(outside) and outside[-1] < len(t)-1 else 0.
        span = theta[-1, 0] - theta[0, 0]
        crossing = np.flatnonzero((theta[:, 0] - theta[0, 0]) / span >= .9)
        row["first_90pct_endpoint_change_s"] = float(t[crossing[0]]) if len(crossing) else None
    provenance = dict(run_id=run, repeat=repeat, source_log_sha256=row["log_sha256"],
        archive_provenance=(trial / "provenance.txt").read_text(),
        surface_frame=frame.tolist(), calibrated_tool_axis_ee=[p[f"tool_axis_ee_{a}"] for a in "xyz"],
        reconstructed_entry_tool_normal_base=entry_tool_normal.tolist(), params=p)
    return row, provenance


def report_endpoint(root: Path, run: str, repeat: str, old_metrics: pd.DataFrame) -> tuple[dict, dict]:
    trial = root / "experiments" / "results" / run / repeat
    report = trial / "terminal.log"
    content = report.read_text(errors="replace")
    match = re.search(r"deviation components.*?before=\[(.*?)\].*?after=\[(.*?)\]", content)
    if not match:
        raise ValueError(f"No full normal-vector endpoint report in {report}")
    entry = -np.array([float(v) for v in match[1].split(",")])
    final = -np.array([float(v) for v in match[2].split(",")])
    total = re.search(r"(?:deviation|alignment):\s*before=([-\d.]+).*?after=([-\d.]+)", content)
    duration = re.search(r"stop:.*?\|\s*t=([-\d.]+)\s*s", content)
    old = old_metrics[(old_metrics.run_id == run) & (old_metrics.repeat == repeat)].iloc[0]
    if int(old["exit_status"]) != 0 or "stop: time | t=5.0 s" not in content:
        raise ValueError(f"Incomplete contact trial: {report}")
    p = params(trial / "params_effective")
    frame = frame_from_params(p)
    assert p["tool_axis_target_sign"] == -1.0
    row = dict(run_id=run, repeat=repeat, duration_s=float(duration[1]),
        source_kind="terminal_normal_vector_endpoints", source_resolution_deg=0.01,
        report_path=str(report), report_sha256=sha256(report))
    for i, axis in enumerate(("t1", "t2", "n")):
        row[f"entry_{axis}_deg"] = float(entry[i])
        row[f"final_{axis}_deg"] = float(final[i])
        row[f"change_{axis}_deg"] = float(final[i]-entry[i])
        source_axis = "normal" if axis == "n" else axis
        row[f"old_gamma_{axis}_deg"] = float(old[f"contact_rotation_{source_axis}_deg"])
        # The previously extracted metrics must independently reproduce every
        # report component. This validates all selected sources without fabrication.
        assert abs(entry[i] + float(old[f"deviation_before_{axis}"])) < 1e-9
        assert abs(final[i] + float(old[f"deviation_after_{axis}"])) < 1e-9
    row.update(entry_total_deg=float(total[1]), final_total_deg=float(total[2]),
        reduction_abs_t1_deg=float(abs(entry[0])-abs(final[0])),
        crossed_t1_zero=bool(np.sign(entry[0]) != np.sign(final[0])))
    provenance = dict(run_id=run, repeat=repeat, report_sha256=row["report_sha256"],
        archive_provenance=(trial / "provenance.txt").read_text(),
        surface_frame=frame.tolist(),
        calibrated_tool_axis_ee=[p[f"tool_axis_ee_{a}"] for a in "xyz"], params=p)
    return row, provenance


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--control-root", "--root", type=Path, default=ROOT)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    rows, provenance, trace_rows = [], [], []
    prior = pd.read_csv(args.control_root / "experiments" / "derived" / "metrics.csv")
    for run in RUNS:
        for repeat in ("r01", "r02", "r03"):
            row, source = report_endpoint(args.control_root, run, repeat, prior)
            rows.append(row)
            provenance.append(source)
            if run in TRACE_RUNS and repeat == "r01":
                trace_row, _ = process(args.control_root, args.out, run, repeat)
                trace_row["report_entry_difference_t1_deg"] = row["entry_t1_deg"]-trace_row["entry_t1_deg"]
                trace_row["report_final_difference_t1_deg"] = row["final_t1_deg"]-trace_row["final_t1_deg"]
                trace_rows.append(trace_row)
        print(run, flush=True)
    data = pd.DataFrame(rows)
    assert len(data) == 3 * len(RUNS)
    data.to_csv(args.out / "per_trial_results.csv", index=False, float_format="%.12g")
    metric_columns = [c for c in data if c.endswith("_deg") or c.endswith("_N") or c.endswith("_Nm")]
    summaries = []
    for run, d in data.groupby("run_id", sort=False):
        result = dict(run_id=run, n=len(d))
        for column in metric_columns:
            result[column + "_mean"] = float(d[column].mean())
            result[column + "_sd"] = float(d[column].std(ddof=1))
        summaries.append(result)
    grouped = pd.DataFrame(summaries)
    grouped.to_csv(args.out / "grouped_results.csv", index=False, float_format="%.12g")
    (args.out / "grouped_results.json").write_text(json.dumps(summaries, indent=2))
    (args.out / "source_provenance.json").write_text(json.dumps(provenance, indent=2))
    trace_data = pd.DataFrame(trace_rows)
    trace_data.to_csv(args.out / "representative_trace_endpoints.csv", index=False, float_format="%.12g")
    # Independently verify source trial selection against the original
    # contact-rotation column that generated Chapter 5, including endpoints.
    comparison = trace_data.merge(prior[["run_id", "repeat", "contact_rotation_t1_deg"]], on=["run_id", "repeat"], validate="one_to_one")
    delta = float(np.max(np.abs(comparison.old_gamma_t1_deg - comparison.contact_rotation_t1_deg)))
    assert delta < 1e-8
    audit = dict(trials=len(data), groups=len(grouped), repeats_per_group=3,
        maximum_full_3d_reconstruction_difference_deg=float(trace_data.reconstruction_max_abs_deg.max()),
        maximum_old_gamma_endpoint_difference_deg=delta,
        shortest_contact_duration_s=float(data.duration_s.min()),
        longest_contact_duration_s=float(data.duration_s.max()),
        angular_definition="theta_err: shortest rotation -n_s -> R_EE(t) n_Tool,EE, base-frame vector, resolved on t1",
        logged_definition="angular_deviation: shortest rotation R_EE(t) n_Tool,EE -> -n_s, resolved on surface axes",
        source_precision="grouped statistics use original terminal report endpoints, rounded online to 0.01 degree; three raw trace normal angles have 9 decimal places in degree and e_R 9 decimal places in radians",
        endpoint="grouped statistics use contact-entry and contact-end vectors from each controller terminal report; traces use first and last phase==2 samples, matching original gamma endpoint",
        raw_log_coverage="All selected trials have archived CSV logs via Git LFS and terminal vector endpoints; three representative traces are reconstructed here",
        endpoint_band_time_definition="First recorded contact time after which theta_err,t1 stays within +/-0.1 degree of its own last recorded value through contact end, inclusive",
        endpoint_band_half_width_deg=0.1,
        endpoint_band_time_TCP_s=float(trace_data.loc[trace_data.run_id == "P2_t1_pos_p000", "within_0p1deg_of_endpoint_after_s"].iloc[0]),
        endpoint_band_time_plus40mm_s=float(trace_data.loc[trace_data.run_id == "P2_t1_pos_p040", "within_0p1deg_of_endpoint_after_s"].iloc[0]),
        calibration_uncertainty="unquantified; robot orientation and fixed tool normal estimate physical alignment subject to calibration and tool-mount error")
    audit["endpoint_band_time_difference_s"] = audit["endpoint_band_time_TCP_s"] - audit["endpoint_band_time_plus40mm_s"]
    (args.out / "audit.json").write_text(json.dumps(audit, indent=2))
    print(grouped[["run_id", "entry_t1_deg_mean", "final_t1_deg_mean", "final_t1_deg_sd", "old_gamma_t1_deg_mean"]].to_string(index=False))
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
