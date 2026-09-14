"""Independent regression checks for the exact 5--9 s null-space analysis.

Uses real archived runs and small synthetic CSVs. Uses temporary synthetic inputs and an optional JSON report. Never changes the
analysis implementation or raw archive.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import importlib.util
import json
import math
import os
import sys
import tempfile
import types

import numpy as np

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
SCRIPT = DATA = COMPARISON_DATA = REPORT = TEMP_ROOT = None

CONDITIONS = ["MAIN_NS7_baseline_20N_200mm",
              "MAIN_NS7_damping_2p0_20N_200mm",
              "MAIN_NS8_ksigma_1p5_20N_200mm",
              "MAIN_NS8_ksigma_2p0_20N_200mm"]
EXPECTED = [
    {"excursion_rad": (0.13261424590916665, 0.015974350268640646),
     "net_displacement_rad": (0.13117569374975943, 0.015948936082968077),
     "sigma_gain": (-0.0021345063333333414, 0.0004707251263660354),
     "task_error_peak_mm": (1.2329157488341203, 0.06582741088027887),
     "nullspace_speed_peak_rad_s": (0.11946331266666667, 0.00667715982895792)},
    {"excursion_rad": (0.09929805533900014, 0.0039681235673134545),
     "net_displacement_rad": (0.09789733813446466, 0.0038402348616742798),
     "sigma_gain": (-0.0012569339999999967, 9.175295284621955e-05),
     "task_error_peak_mm": (1.228632092012848, 0.05189058084276039),
     "nullspace_speed_peak_rad_s": (0.080386674, 0.003433842103818401)},
    {"excursion_rad": (0.0050197591034999945, 8.399026886872481e-05),
     "net_displacement_rad": (0.0002536762176696863, 0.00029884548928315257),
     "sigma_gain": (6.666666666858372e-08, 7.821338333994296e-08),
     "task_error_peak_mm": (0.8886195248315337, 0.02446655261308275),
     "nullspace_speed_peak_rad_s": (0.013270905999999999, 0.0019538260979746896)},
    {"excursion_rad": (0.02944354160333337, 0.0024808493834116638),
     "net_displacement_rad": (-0.00018530407797765874, 0.0003296484587184597),
     "sigma_gain": (2.5999999995566608e-08, 2.4439312592275773e-07),
     "task_error_peak_mm": (0.9831069234446835, 0.05265261139482148),
     "nullspace_speed_peak_rad_s": (0.046685065666666664, 0.003342363798825219)},
]
EXPECTED_SIGMA = [{'sigma_start': (0.216511522, 5.447764587434356e-06),
  'sigma_end': (0.21437701566666667, 0.0004761158696633938),
  'sigma_minimum': (0.214376558, 0.00047598667821274217),
  'sigma_minimum_min': 0.214005362},
 {'sigma_start': (0.21650910666666667, 2.8251104993083762e-06),
  'sigma_end': (0.21525217266666666, 9.457445232901336e-05),
  'sigma_minimum': (0.21525122333333332, 9.378959160980012e-05),
  'sigma_minimum_min': 0.215149266},
 {'sigma_start': (0.216532229, 1.0847566547455328e-06),
  'sigma_end': (0.21653229566666668, 1.0081836803594997e-06),
  'sigma_minimum': (0.21653181633333335, 1.0479123691093842e-06),
  'sigma_minimum_min': 0.21653067},
 {'sigma_start': (0.21653388833333334, 4.692785242508514e-07),
  'sigma_end': (0.21653391433333333, 2.250118515323009e-07),
  'sigma_minimum': (0.21653332166666667, 3.072870536492818e-07),
  'sigma_minimum_min': 0.216532977}]

HASHES = [
    "f3938de24539f46233e3dd4f11cd9279f2ee50579ae8a71666a9caa9f9c8de24",
    "b056198c2bf035bd7b435b745a7b301afb626650345ad44ceec2f3c6876a44db",
    "681ce9ae9eb8fb70de84c1c02cf7c00bd884bf3a01e04baa01adcc871d4ad268",
    "d9bd745c6a9ba79f12138df71dd56b014825b876c3b778edb834ba26bb0530b3",
    "0b3717b9dc1f2b44a78ae7d8022e46c3cc55079f56e73dfcee48e0a08a79d3b6",
    "1facca14c498e5d44070155b5695b5a27b8e3c700d9105a850eb9861f75cb7a0",
    "46e40e6c74a9c52b9e70d64b4d91ac4958fd67329659dc1705dfb46118df6724",
    "fe2685270b324e3ce43e359fe2e84f8455a124c5b5aecd122a618fb3f5ea149f",
    "a5bdd487d7bb2144a53dc8bc8f3b4fae2a793e7f1e5d3fe8f0a45caaf5efea51",
    "8d0a1648ca05a45a3f4b71df5b49348669aa77311c9f8bdc0199ea68e96cf8cc",
    "fac81548338aa65227ef2368e15a09ba43c2be20022b457a91a302cc1cc61c47",
    "0805dcc238a7243dd81f2af5cb2033fd9a7be35ac3c15815f822d98587b9e083",
]
RESULTS = []


def check(name, operation):
    try:
        detail = operation()
        RESULTS.append({"check": name, "passed": True, "detail": detail})
    except Exception as error:
        RESULTS.append({"check": name, "passed": False,
                        "detail": f"{type(error).__name__}: {error}"})


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def close(value, target, label, tolerance=1e-12):
    require(math.isclose(float(value), target, rel_tol=1e-10,
                         abs_tol=tolerance), f"{label}: {value} != {target}")


def file_hash(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def synthetic_rows():
    names = ["time", "nullspace_speed", "sigma_current", "disturbance_scale",
             "disturbance_torque_scale"]
    names += [f"disturbance_force_base_{a}" for a in "xyz"]
    names += [f"tau_disturbance_{j}" for j in range(1, 8)]
    names += [f"e_p_{a}" for a in "xyz"]
    names += [f"nullspace_dq_{j}" for j in range(1, 8)]
    rows = []
    for i, time in enumerate([0, 5, 6, 7, 8, 9, 18]):
        row = dict.fromkeys(names, 0.0)
        row.update(time=time, disturbance_torque_scale=1.0)
        if 5 <= time <= 9:
            speed = [1, 2, 3, 2, 1][i - 1]
            row.update(nullspace_speed=speed, sigma_current=0.1 + i * 0.1,
                       disturbance_scale=1.0 if 5 < time < 9 else 0.0,
                       disturbance_force_base_x=20.0, tau_disturbance_1=2.0,
                       e_p_x=i * 0.001,
                       nullspace_dq_1=[1, 2, -3, -2, -1][i - 1])
        else:
            row.update(nullspace_speed=99.0, sigma_current=-100.0 * i,
                       disturbance_force_base_x=100.0, tau_disturbance_1=100.0,
                       e_p_x=100.0, nullspace_dq_1=99.0)
        rows.append(row)
    return rows


def synthetic_run(module, rows):
    with tempfile.TemporaryDirectory(prefix="synthetic-", dir=TEMP_ROOT) as folder:
        path = Path(folder) / "surface_grinding_controller_log.csv"
        with path.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        return module.read_run(folder)


def test_synthetic_success(module):
    run = synthetic_run(module, synthetic_rows())
    for key, target in {"excursion_rad": 8.0, "sigma_gain": 0.4,
                        "task_error_peak_mm": 5.0, "force_peak_N": 20.0,
                        "disturbance_tau_peak_Nm": 2.0,
                        "nullspace_speed_peak_rad_s": 3.0}.items():
        close(run[key], target, key)
    close(run["net_vector_rad"][0], -3.0, "net_vector_rad[0]")
    require(np.array_equal(run["relative_time"], np.arange(5)),
            "Synthetic curve does not span exact 0--4 s")
    return "Analytic trapezoids and all peak metrics exclude outside-window outliers."


def test_rejection(module, mutator):
    rows = synthetic_rows()
    mutator(rows)
    try:
        synthetic_run(module, rows)
    except ValueError as error:
        return str(error)
    raise AssertionError("Invalid input was accepted")



def verify_sigma_statistics(groups):
    for group, expected in zip(groups, EXPECTED_SIGMA):
        def statistics_check(group=group, expected=expected):
            out = {}
            for key in ["sigma_start", "sigma_end", "sigma_minimum"]:
                values = [run[key] for run in group["runs"]]
                mean, sd = expected[key]
                close(np.mean(values), mean, key + " mean", 1e-14)
                close(np.std(values, ddof=1), sd, key + " sample SD", 1e-14)
                out[key] = {"mean": float(np.mean(values)),
                            "sd": float(np.std(values, ddof=1))}
            close(min(run["sigma_minimum"] for run in group["runs"]),
                  expected["sigma_minimum_min"], "worst individual minimum", 1e-14)
            return out
        check(group["run_id"] + " absolute sigma statistics", statistics_check)
        for number, run in enumerate(group["runs"], start=1):
            def raw_trace_check(run=run, number=number, group=group):
                path = DATA / group["run_id"] / f"r{number:02}" / "surface_grinding_controller_log.csv"
                with path.open(newline="") as stream:
                    rows = [row for row in csv.DictReader(stream)
                            if 5.0 <= float(row["time"]) <= 9.0]
                sigma = np.array([float(row["sigma_current"]) for row in rows])
                relative = np.array([float(row["time"]) - 5.0 for row in rows])
                require(np.array_equal(run["sigma_trace"], sigma),
                        "Sigma trace differs from recorded samples")
                require(np.array_equal(run["relative_time"], relative),
                        "Trace timestamps differ from recorded time minus five")
                close(run["sigma_start"], sigma[0], "sigma start", 1e-15)
                close(run["sigma_end"], sigma[-1], "sigma end", 1e-15)
                close(run["sigma_minimum"], min(sigma), "raw per-trial minimum", 1e-15)
                close(run["sigma_end"] - run["sigma_start"], run["sigma_gain"],
                      "endpoint difference consistency", 1e-15)
                return {"samples": len(sigma), "raw_minimum": float(min(sigma))}
            check(group["run_id"] + f"/r{number:02} unresampled sigma trace", raw_trace_check)


def verify_sigma_summary(module, groups):
    old_summary = module.SUMMARY
    try:
        module.SUMMARY = str(TEMP_ROOT / "sigma-summary.csv")
        module.write_summary(groups)
        with Path(module.SUMMARY).open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        require(len(rows) == 4, "Summary should contain four conditions")
        for row, group, expected in zip(rows, groups, EXPECTED_SIGMA):
            require(row["run_id"] == group["run_id"], "Condition order changed")
            for key in ["sigma_start", "sigma_end", "sigma_minimum"]:
                mean, sd = expected[key]
                # Allow only the rounding introduced by CSV serialization.
                for column, target in [(key + "_mean", mean), (key + "_sd", sd)]:
                    close(float(row[column]), target, column,
                          5e-12 if column.endswith("_mean")
                          else max(1e-15, abs(target) * 5e-9))
            close(float(row["sigma_minimum_min"]), expected["sigma_minimum_min"],
                  "summary worst minimum", 1e-15)
        return "All seven absolute-sigma summary columns reproduce independent raw-sample statistics."
    finally:
        module.SUMMARY = old_summary


def verify_mean_of_minima(module, groups):
    # Different runs attain their minima at different times. The mean of their
    # individual minima is 0.1333..., while the minimum mean trace is 0.2.
    traces = [np.array([0.2, 0.1, 0.3]), np.array([0.2, 0.3, 0.1]),
              np.array([0.2, 0.2, 0.2])]
    group = dict(groups[0])
    group["runs"] = []
    for original, trace in zip(groups[0]["runs"], traces):
        run = dict(original)
        run.update(sigma_trace=trace, sigma_start=float(trace[0]),
                   sigma_end=float(trace[-1]), sigma_minimum=float(min(trace)),
                   sigma_gain=float(trace[-1] - trace[0]))
        group["runs"].append(run)
    old_summary = module.SUMMARY
    try:
        module.SUMMARY = str(TEMP_ROOT / "synthetic-minima-summary.csv")
        module.write_summary([group])
        with Path(module.SUMMARY).open(newline="") as stream:
            row = next(csv.DictReader(stream))
        expected = np.mean([min(trace) for trace in traces])
        wrong = min(np.mean(traces, axis=0))
        close(float(row["sigma_minimum_mean"]), expected,
              "mean of per-trial minima", 5e-12)
        require(abs(float(row["sigma_minimum_mean"]) - wrong) > 0.01,
                "Summary uses minimum of the mean trace")
        close(float(row["sigma_minimum_min"]), 0.1, "lowest individual minimum")
        return {"mean_per_trial_minimum": expected, "minimum_mean_trace": wrong}
    finally:
        module.SUMMARY = old_summary


def run_tests():
    if not SCRIPT.exists():
        raise SystemExit(f"Staged analysis is not available: {SCRIPT}")
    spec = importlib.util.spec_from_file_location("exact_window_analysis", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    groups = []
    for index, condition in enumerate(CONDITIONS):
        runs = [module.read_run(str(DATA / condition / f"r{i:02}"))
                for i in range(1, 4)]
        groups.append({"run_id": condition, "study": "damping" if index < 2 else "sigma",
                       "gain": [0, 2, 1.5, 2][index], "runs": runs})
    module.net_displacements(groups)

    for index, group in enumerate(groups):
        def check_statistics(group=group, expected=EXPECTED[index]):
            summary = {}
            for key, (mean, sd) in expected.items():
                values = [run[key] for run in group["runs"]]
                tolerance = 1e-15 if key == "sigma_gain" else 1e-12
                close(np.mean(values), mean, key + " mean", tolerance)
                close(np.std(values, ddof=1), sd, key + " SD", tolerance)
                summary[key] = {"mean": float(np.mean(values)),
                                "sd": float(np.std(values, ddof=1))}
            return summary
        check(group["run_id"] + " statistics", check_statistics)

        for run_number, run in enumerate(group["runs"], start=1):
            def check_curve(run=run):
                time = run["relative_time"]
                cumulative = run["cumulative_excursion"]
                close(time[0], 0.0, "first time")
                close(time[-1], 4.0, "last time")
                close(cumulative[0], 0.0, "initial cumulative")
                close(cumulative[-1], run["excursion_rad"], "final cumulative")
                require(np.all(np.diff(time) > 0), "Nonmonotonic time")
                require(np.all(np.diff(cumulative) >= 0), "Decreasing cumulative motion")
                require(np.linalg.norm(run["net_vector_rad"]) <= run["excursion_rad"] + 1e-8,
                        "Net-vector norm exceeds cumulative motion")
                return {"samples": len(time), "first": float(time[0]), "last": float(time[-1])}
            check(group["run_id"] + f"/r{run_number:02} curve", check_curve)

            def check_hash(index=index, run_number=run_number, condition=group["run_id"]):
                expected = HASHES[index * 3 + run_number - 1]
                relative = Path(condition) / f"r{run_number:02}" / "surface_grinding_controller_log.csv"
                for source in (DATA,) + ((COMPARISON_DATA,) if COMPARISON_DATA else ()):
                    require(file_hash(source / relative) == expected,
                            f"Raw log hash changed: {source / relative}")
                return expected
            check(group["run_id"] + f"/r{run_number:02} unchanged raw log", check_hash)

    check("Synthetic exact window and excluded outliers", lambda: test_synthetic_success(module))
    for name, mutation in [
        ("Missing 5 s sample", lambda rows: rows[1].update(time=5.01)),
        ("Missing 9 s sample", lambda rows: rows[5].update(time=8.99)),
        ("Nonmonotonic time", lambda rows: rows[3].update(time=5.5)),
        ("Duplicate time", lambda rows: rows[3].update(time=6.0)),
        ("Nonfinite time", lambda rows: rows[3].update(time=float("nan"))),
        ("Nonfinite sigma", lambda rows: rows[3].update(sigma_current=float("nan"))),
        ("Nonfinite projected velocity", lambda rows: rows[3].update(nullspace_dq_3=float("inf"))),
    ]:
        check(name, lambda mutation=mutation: test_rejection(module, mutation))
    verify_sigma_statistics(groups)
    check("Absolute sigma CSV summary", lambda: verify_sigma_summary(module, groups))
    check("Mean of trial minima differs from minimum mean trace",
          lambda: verify_mean_of_minima(module, groups))
    failed = [item for item in RESULTS if not item["passed"]]
    report = {"analysis": str(SCRIPT), "checks": len(RESULTS),
              "failed": len(failed), "results": RESULTS}
    if REPORT is not None:
        REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks": len(RESULTS), "failed": failed, "report": str(REPORT) if REPORT else None}, indent=2))
    return 1 if failed else 0


def main():
    global SCRIPT, DATA, COMPARISON_DATA, REPORT, TEMP_ROOT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--script", type=Path,
                        default=HERE.parent / "figures" / "make_nullspace_figure.py",
                        help="analysis script to verify")
    parser.add_argument("--results", type=Path,
                        default=HERE.parent / "experiments" / "results",
                        help="directory containing the twelve archived run logs")
    parser.add_argument("--comparison-results", type=Path,
                        help="optional mirrored run archive to check against the same hashes")
    parser.add_argument("--report", type=Path,
                        help="optional path for a detailed JSON report")
    args = parser.parse_args()
    SCRIPT = args.script.resolve()
    DATA = args.results.resolve()
    COMPARISON_DATA = (args.comparison_results.resolve()
                       if args.comparison_results is not None else None)
    REPORT = args.report.resolve() if args.report is not None else None
    previous_cache = os.environ.get("MPLCONFIGDIR")
    with tempfile.TemporaryDirectory(prefix="nullspace-window-tests-") as folder:
        TEMP_ROOT = Path(folder)
        os.environ["MPLCONFIGDIR"] = str(TEMP_ROOT / "mpl-cache")
        # The numerical functions do not use the plot style. Keep this test
        # independent of LaTeX/font configuration and unrelated figure outputs.
        style = types.ModuleType("make_figures")
        for name, value in {"SERIES_BLACK": "black", "SERIES_RED": "red",
                            "SERIES_BLUE": "blue", "SERIES_YELLOW": "yellow",
                            "FIGURES": str(TEMP_ROOT)}.items():
            setattr(style, name, value)
        style.save = lambda *args, **kwargs: None
        style.axis_legend = lambda *args, **kwargs: None
        sys.modules["make_figures"] = style
        try:
            return run_tests()
        finally:
            if previous_cache is None:
                os.environ.pop("MPLCONFIGDIR", None)
            else:
                os.environ["MPLCONFIGDIR"] = previous_cache


if __name__ == "__main__":
    sys.exit(main())
