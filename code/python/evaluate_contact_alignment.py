#!/usr/bin/env python3
"""
evaluate_contact_alignment.py
=============================

Offline analysis of a table-contact *passive self-alignment* trial logged by the
Cartesian impedance controller. It computes every metric used in the thesis and
emits the figures that replace the placeholder plots.

What it computes
----------------
1. Magnitudes over time: ||e_R||, ||e_p||, ||f||, ||m||, ||tau||.
2. Contact detection (force threshold, or a user-given --contact-time).
3. Orientation error before / after contact and the reduction  Delta e_R.
4. Instantaneous screw axis / pole from the measured twist (Chasles):
        p_ISA = (omega x v) / ||omega||^2          (relative to the TCP)
        p_pole = p_EE + p_ISA                       (absolute, base frame)
   Samples with ||omega|| below a threshold are discarded (unreliable).
5. Pole error relative to the tool edge:
        e_P     = || p_pole - p_edge ||
        d_ISA_e = || (p_edge - p_pole_axis_point) x a_ISA ||
6. Least-squares identification of the effective translation-rotation impedance
   ("big moment equation"):
        M_C = K_rt_eff dx_C + D_rt_eff v_C + K_R_eff dtheta + D_R_eff omega
   with the contact moment moved to the edge by  M_C = m - r_C x f .
7. Optional commanded-vs-measured wrench check  r_check = ||m + m_ext|| / ||m||
   (only if f_ext_* / m_ext_* columns are present in the CSV).

Outputs
-------
- A printed summary table of all scalar metrics.
- PNG figures: orientation error vs time, pole scatter vs edge, force/torque vs
  time (written next to the CSV unless --outdir is given).

Usage
-----
    python evaluate_contact_alignment.py run.csv \
        --edge 0.50 0.00 0.20 --normal 0 0 1

    python evaluate_contact_alignment.py run.csv --contact-time 2.0

    # compare several settings into one table:
    python evaluate_contact_alignment.py test1.csv test2.csv test3.csv \
        --edge 0.50 0.00 0.20

Requires: numpy, pandas, matplotlib.
"""

import argparse
import os
import sys
import numpy as np

try:
    import pandas as pd
except ImportError:
    sys.exit("This script needs pandas (pip install pandas).")

# matplotlib is only needed for the plots; import lazily so metrics still work
# on a headless machine without a display backend configured.


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def _xyz(df, prefix):
    """Return an (N,3) array from columns prefix_x, prefix_y, prefix_z."""
    cols = [f"{prefix}_x", f"{prefix}_y", f"{prefix}_z"]
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise KeyError(f"missing columns {missing}")
    return df[cols].to_numpy(dtype=float)


def _norm(a):
    return np.linalg.norm(a, axis=1)


def load_log(path):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    if "time" not in df.columns:
        raise KeyError("CSV has no 'time' column")
    return df


def detect_contact(time, f_norm, threshold, contact_time):
    """Return the index where contact starts."""
    if contact_time is not None:
        return int(np.searchsorted(time, contact_time))
    above = np.where(f_norm >= threshold)[0]
    if len(above) == 0:
        return None
    return int(above[0])


def instantaneous_poles(p_EE, pdot, omega, omega_min):
    """Per-sample absolute pole and screw-axis direction (Chasles).

    Returns (poles_abs, axis_dir, valid_mask).
    """
    w_norm = _norm(omega)
    valid = w_norm > omega_min
    poles = np.full_like(p_EE, np.nan)
    axis = np.full_like(omega, np.nan)
    # p_ISA = (omega x v) / |omega|^2, relative to the TCP
    cross = np.cross(omega[valid], pdot[valid])
    p_isa_rel = cross / (w_norm[valid] ** 2)[:, None]
    poles[valid] = p_EE[valid] + p_isa_rel
    axis[valid] = omega[valid] / w_norm[valid][:, None]
    return poles, axis, valid


def pole_errors(poles, axis, p_EE, pdot, omega, valid, p_edge, omega_min):
    """e_P (point distance) and d_ISA_e (edge-to-axis distance) per valid sample."""
    e_P = np.full(len(p_EE), np.nan)
    d_axis = np.full(len(p_EE), np.nan)
    e_P[valid] = _norm(poles[valid] - p_edge)
    # screw-axis point = p_EE + (omega x v)/|omega|^2 = poles (already absolute)
    rel = p_edge[None, :] - poles[valid]
    d_axis[valid] = _norm(np.cross(rel, axis[valid]))
    return e_P, d_axis


def least_squares_effective(df, c0, c1, p_edge):
    """Identify [K_rt, D_rt, K_R, D_R] (each 3x3) from the contact window.

    Model per sample i:
        M_C,i = K_rt dx_C,i + D_rt v_C,i + K_R dtheta_i + D_R omega_i
    with M_C,i = m_i - r_C x f_i  (moment about the edge).
    dx_C   : TCP displacement since contact start (sliding/translation)
    v_C    : linear velocity (pdot)
    dtheta : orientation error vector e_R relative to its value at contact start
    omega  : angular velocity
    """
    sl = slice(c0, c1)
    p_EE = _xyz(df, "p_EE")[sl]
    e_R = _xyz(df, "e_R")[sl]
    pdot = _xyz(df, "pdot")[sl]
    omega = _xyz(df, "omega")[sl]
    f = _xyz(df, "f")[sl]
    m = _xyz(df, "m")[sl]

    dx_C = p_EE - p_EE[0]                 # translation since contact start
    dtheta = e_R - e_R[0]                 # rotation since contact start
    r_C = p_edge[None, :] - p_EE          # TCP -> edge, per sample
    M_C = m - np.cross(r_C, f)            # moment transferred to the edge

    # Regressor phi_i = [dx_C, v_C, dtheta, omega]  (12,)
    Phi = np.hstack([dx_C, pdot, dtheta, omega])      # (N,12)
    Y = M_C                                            # (N,3)
    # Solve  Y = Phi A^T  ->  A^T = pinv(Phi) Y
    A_T, *_ = np.linalg.lstsq(Phi, Y, rcond=None)      # (12,3)
    A = A_T.T                                           # (3,12)
    blocks = {
        "K_rt_eff": A[:, 0:3],
        "D_rt_eff": A[:, 3:6],
        "K_R_eff": A[:, 6:9],
        "D_R_eff": A[:, 9:12],
    }
    # fit quality
    resid = Y - Phi @ A_T
    ss_res = float(np.sum(resid ** 2))
    ss_tot = float(np.sum((Y - Y.mean(axis=0)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    M_trans = (dx_C @ blocks["K_rt_eff"].T)
    M_rot = (dtheta @ blocks["K_R_eff"].T)
    blocks["R2"] = r2
    blocks["M_trans_mean_norm"] = float(np.mean(_norm(M_trans)))
    blocks["M_rot_mean_norm"] = float(np.mean(_norm(M_rot)))
    return blocks


def wrench_check(df, sl):
    """r_check = ||m + m_ext|| / ||m|| over the window, if m_ext is logged."""
    if "m_ext_x" not in df.columns:
        return None
    m = _xyz(df, "m")[sl]
    m_ext = _xyz(df, "m_ext")[sl]
    num = _norm(m + m_ext)
    den = _norm(m)
    den = np.where(den < 1e-9, np.nan, den)
    return float(np.nanmean(num / den))


# --------------------------------------------------------------------------- #
# Per-file analysis
# --------------------------------------------------------------------------- #
def analyse(path, args):
    df = load_log(path)
    t = df["time"].to_numpy(dtype=float)

    p_EE = _xyz(df, "p_EE")
    e_p = _xyz(df, "e_p")
    e_R = _xyz(df, "e_R")
    pdot = _xyz(df, "pdot")
    omega = _xyz(df, "omega")
    f = _xyz(df, "f")
    m = _xyz(df, "m")
    tau_cols = [c for c in df.columns if c.startswith("tau_cmd")]
    tau = df[tau_cols].to_numpy(dtype=float) if tau_cols else np.zeros((len(t), 1))

    f_norm, m_norm, eR_norm, tau_norm = _norm(f), _norm(m), _norm(e_R), _norm(tau)

    p_edge = np.asarray(args.edge, dtype=float)

    c0 = detect_contact(t, f_norm, args.contact_force_threshold, args.contact_time)
    if c0 is None:
        print(f"[{os.path.basename(path)}] no contact detected "
              f"(||f|| never exceeds {args.contact_force_threshold} N).")
        c0 = 0
    c1 = len(t)

    # Orientation error before / after.
    eR_before = float(np.median(eR_norm[max(0, c0 - args.window):c0])) if c0 > 0 \
        else float(eR_norm[0])
    eR_after = float(np.median(eR_norm[-args.window:]))
    delta_eR = eR_before - eR_after

    # Instantaneous poles over the contact window.
    poles, axis, valid = instantaneous_poles(
        p_EE[c0:c1], pdot[c0:c1], omega[c0:c1], args.omega_min)
    e_P, d_axis = pole_errors(poles, axis, p_EE[c0:c1], pdot[c0:c1],
                              omega[c0:c1], valid, p_edge, args.omega_min)
    e_P_valid = e_P[~np.isnan(e_P)]
    d_valid = d_axis[~np.isnan(d_axis)]

    # Least-squares effective impedance.
    fit = least_squares_effective(df, c0, c1, p_edge)
    r_check = wrench_check(df, slice(c0, c1))

    deg = 180.0 / np.pi
    metrics = {
        "file": os.path.basename(path),
        "eR_before_deg": eR_before * deg,
        "eR_after_deg": eR_after * deg,
        "delta_eR_deg": delta_eR * deg,
        "e_P_mm": (np.median(e_P_valid) * 1000.0) if len(e_P_valid) else float("nan"),
        "d_ISA_mm": (np.median(d_valid) * 1000.0) if len(d_valid) else float("nan"),
        "f_max_N": float(np.max(f_norm[c0:c1])),
        "m_max_Nm": float(np.max(m_norm[c0:c1])),
        "tau_max_Nm": float(np.max(tau_norm[c0:c1])),
        "fit_R2": fit["R2"],
        "M_trans/M_rot": (fit["M_trans_mean_norm"] /
                          fit["M_rot_mean_norm"]) if fit["M_rot_mean_norm"] else float("nan"),
        "r_check": r_check if r_check is not None else float("nan"),
    }

    if not args.no_plots:
        _plots(path, args, t, eR_norm, f_norm, tau_norm, c0,
               poles, valid, p_edge, deg)

    if args.verbose:
        print(f"\n=== {os.path.basename(path)} : effective impedance ===")
        np.set_printoptions(precision=3, suppress=True)
        for k in ("K_rt_eff", "D_rt_eff", "K_R_eff", "D_R_eff"):
            print(f"{k} =\n{fit[k]}")
    return metrics


def _plots(path, args, t, eR_norm, f_norm, tau_norm, c0, poles, valid,
           p_edge, deg):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    base = os.path.splitext(os.path.basename(path))[0]
    outdir = args.outdir or os.path.dirname(os.path.abspath(path))
    os.makedirs(outdir, exist_ok=True)

    # 1) orientation error vs time
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(t, eR_norm * deg, lw=1.5)
    if c0 > 0:
        ax.axvline(t[c0], ls="--", color="k", lw=1, label="contact")
        ax.legend()
    ax.set_xlabel("time [s]"); ax.set_ylabel(r"$\|e_R\|$ [deg]")
    ax.set_title("Orientation error during contact")
    fig.tight_layout(); fig.savefig(os.path.join(outdir, f"{base}_eR.png"), dpi=150)
    plt.close(fig)

    # 2) pole scatter relative to the edge (projected on x-z)
    pv = poles[valid]
    if len(pv):
        fig, ax = plt.subplots(figsize=(4.5, 4.5))
        ax.scatter(pv[:, 0], pv[:, 2], s=8, alpha=0.4, label="instantaneous poles")
        ax.scatter([p_edge[0]], [p_edge[2]], c="r", marker="x", s=80, label="edge")
        ax.set_xlabel("x [m]"); ax.set_ylabel("z [m]")
        ax.set_aspect("equal", "datalim"); ax.legend()
        ax.set_title("Pole cluster vs. tool edge")
        fig.tight_layout(); fig.savefig(os.path.join(outdir, f"{base}_pole.png"), dpi=150)
        plt.close(fig)

    # 3) force / torque vs time
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(t, f_norm, lw=1.5, label=r"$\|f\|$ [N]")
    ax.plot(t, tau_norm, lw=1.5, label=r"$\|\tau\|$ [Nm]")
    if c0 > 0:
        ax.axvline(t[c0], ls="--", color="k", lw=1)
    ax.set_xlabel("time [s]"); ax.legend()
    ax.set_title("Contact force and commanded torque")
    fig.tight_layout(); fig.savefig(os.path.join(outdir, f"{base}_force_torque.png"), dpi=150)
    plt.close(fig)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", nargs="+", help="one or more log CSV files")
    ap.add_argument("--edge", nargs=3, type=float, default=[0.0, 0.0, 0.0],
                    metavar=("X", "Y", "Z"),
                    help="tool edge / desired pole position in the base frame [m]")
    ap.add_argument("--normal", nargs=3, type=float, default=[0.0, 0.0, 1.0],
                    metavar=("NX", "NY", "NZ"), help="surface normal (unit)")
    ap.add_argument("--contact-time", type=float, default=None,
                    help="force contact start time [s] (overrides force detection)")
    ap.add_argument("--contact-force-threshold", type=float, default=3.0,
                    help="||f|| threshold for contact detection [N]")
    ap.add_argument("--omega-min", type=float, default=0.02,
                    help="minimum ||omega|| for a reliable pole [rad/s]")
    ap.add_argument("--window", type=int, default=50,
                    help="samples used for before/after medians")
    ap.add_argument("--outdir", default=None, help="directory for the PNG plots")
    ap.add_argument("--no-plots", action="store_true", help="skip the figures")
    ap.add_argument("--verbose", action="store_true",
                    help="also print the effective stiffness/damping matrices")
    args = ap.parse_args()

    rows = []
    for path in args.csv:
        try:
            rows.append(analyse(path, args))
        except Exception as exc:  # noqa: BLE001
            print(f"[{os.path.basename(path)}] error: {exc}")

    if not rows:
        return
    summary = pd.DataFrame(rows).set_index("file")
    pd.set_option("display.float_format", lambda v: f"{v:.3f}")
    pd.set_option("display.width", 200)
    print("\n==================== SUMMARY ====================")
    print(summary.to_string())
    print("\nColumns: eR_*_deg orientation error; delta_eR_deg reduction; "
          "e_P_mm pole-to-edge; d_ISA_mm axis-to-edge; *_max peaks; "
          "fit_R2 least-squares quality; M_trans/M_rot moment split; "
          "r_check wrench consistency (NaN if m_ext not logged).")


if __name__ == "__main__":
    main()
