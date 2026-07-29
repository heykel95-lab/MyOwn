#!/usr/bin/env python3
"""
evaluate_contact_alignment.py
=============================

Offline analysis of a surface-contact alignment trial.  The reader accepts the
current FULL-Working-Clean log schema and the earlier experiment schema used by
the historical coupled-pole campaign.

What it computes
----------------
1. Magnitudes over time of the clearance-relative controller error, commanded
   Cartesian force, bias-corrected external-force estimate (when logged), and
   commanded joint torque.
2. Set-up-window selection from ``phase == 2`` in current logs.  A
   bias-corrected external-force threshold narrows this to an estimated-contact
   subset when available; otherwise the window remains explicitly
   contact-unverified.  A user time can override the selection.
3. Rotation-vector magnitude at the beginning and end of the selected window.
   In current logs this is rotation away from the frozen clearance orientation,
   not a tool-axis-to-surface alignment angle.
4. Before--after TCP displacement and, when the current schema provides
   ``tool_contact_*``, displacement of the selected physical tool feature.
Outputs
-------
- A printed summary table of all scalar metrics.
- PNG figures: clearance-relative rotation error, TCP/selected-feature
  displacement, commanded Cartesian force, bias-corrected external-force
  magnitude, and commanded joint torque (written next to the CSV unless
  --outdir is given).

Usage
-----
    python evaluate_contact_alignment.py current_run.csv

    python evaluate_contact_alignment.py run.csv --contact-time 2.0

    # compare several settings into one table:
    python evaluate_contact_alignment.py test1.csv test2.csv test3.csv

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


def _first_xyz(df, *prefixes):
    """Return the first complete xyz group and the prefix that was selected."""
    for prefix in prefixes:
        cols = [f"{prefix}_x", f"{prefix}_y", f"{prefix}_z"]
        if all(c in df.columns for c in cols):
            return df[cols].to_numpy(dtype=float), prefix
    return None, None


def load_log(path):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    if "time" not in df.columns:
        raise KeyError("CSV has no 'time' column")
    return df


def select_analysis_window(
        df, time, fallback_force_norm, threshold, contact_time, phase_value):
    """Return ``(start, stop, source)`` for current or legacy logs.

    Phase 2 starts at geometric clearance, not force contact.  When the current
    bias-corrected external force is present, its norm is used only to select an
    estimated-contact subset within phase 2.
    """
    if contact_time is not None:
        return int(np.searchsorted(time, contact_time)), len(time), "user time"
    if "phase" in df.columns:
        phase = df["phase"].to_numpy(dtype=int)
        indices = np.flatnonzero(phase == phase_value)
        if len(indices):
            start, stop = int(indices[0]), int(indices[-1]) + 1
            f_external, _ = _first_xyz(df, "force_after_contact")
            if f_external is not None:
                above = np.flatnonzero(
                    _norm(f_external[start:stop]) >= threshold)
                if len(above):
                    return (start + int(above[0]), stop,
                            f"phase {phase_value}, bias-corrected "
                            "external-force threshold")
            return (start, stop,
                    f"phase {phase_value} set-up/clearance "
                    "(contact unverified)")
        return None, len(time), f"phase {phase_value} absent"
    above = np.where(fallback_force_norm >= threshold)[0]
    if len(above) == 0:
        return None, len(time), "not found"
    return int(above[0]), len(time), "legacy force threshold"


# --------------------------------------------------------------------------- #
# Per-file analysis
# --------------------------------------------------------------------------- #
def analyse(path, args):
    df = load_log(path)
    t = df["time"].to_numpy(dtype=float)

    p_EE = _xyz(df, "p_EE")
    e_R = _xyz(df, "e_R")
    f_cmd = _xyz(df, "f")
    tau_cols = [c for c in df.columns if c.startswith("tau_cmd")]
    tau = df[tau_cols].to_numpy(dtype=float) if tau_cols else np.zeros((len(t), 1))

    f_cmd_norm = _norm(f_cmd)
    eR_norm = _norm(e_R)
    tau_norm = _norm(tau)
    f_external, external_force_source = _first_xyz(
        df, "force_after_contact", "external_force", "f_ext")
    f_external_norm = (
        _norm(f_external) if f_external is not None
        else np.full(len(t), np.nan)
    )

    p_feature, feature_source = _first_xyz(df, "tool_contact")

    c0, c1, window_source = select_analysis_window(
        df, t, f_cmd_norm, args.contact_force_threshold,
        args.contact_time, args.phase_value)
    if c0 is None:
        raise ValueError(f"no valid analysis window: {window_source}")
    elif args.verbose:
        print(f"[{os.path.basename(path)}] analysis window from {window_source}; "
              f"feature source: {feature_source or 'not logged'}.")
        if external_force_source is not None:
            print("external-force estimate source:", external_force_source)

    # Clearance-reference controller error at the ends of the selected window.
    start_stop = min(c1, c0 + args.window)
    end_start = max(c0, c1 - args.window)
    eR_start = float(np.median(eR_norm[c0:start_stop]))
    eR_end = float(np.median(eR_norm[end_start:c1]))
    delta_eR_control = eR_start - eR_end

    p_tcp_start = np.median(p_EE[c0:start_stop], axis=0)
    p_tcp_end = np.median(p_EE[end_start:c1], axis=0)
    tcp_displacement = float(np.linalg.norm(p_tcp_end - p_tcp_start))
    if p_feature is not None:
        p_feature_start = np.median(p_feature[c0:start_stop], axis=0)
        p_feature_end = np.median(p_feature[end_start:c1], axis=0)
        feature_displacement = float(
            np.linalg.norm(p_feature_end - p_feature_start))
    else:
        feature_displacement = float("nan")

    deg = 180.0 / np.pi
    metrics = {
        "file": os.path.basename(path),
        "eR_clearance_start_deg": eR_start * deg,
        "eR_clearance_end_deg": eR_end * deg,
        "delta_eR_control_deg": delta_eR_control * deg,
        "tcp_displacement_mm": tcp_displacement * 1000.0,
        "feature_displacement_mm": feature_displacement * 1000.0,
        "f_cmd_max_N": float(np.max(f_cmd_norm[c0:c1])),
        "f_external_delta_max_N": (
            float(np.nanmax(f_external_norm[c0:c1]))
            if np.any(np.isfinite(f_external_norm[c0:c1]))
            else float("nan")
        ),
        "tau_cmd_max_Nm": float(np.max(tau_norm[c0:c1])),
    }

    if not args.no_plots:
        _plots(path, args, t, eR_norm, f_cmd_norm, f_external_norm,
               tau_norm, c0, window_source, p_EE, p_feature, deg)

    return metrics


def _plots(path, args, t, eR_norm, f_cmd_norm, f_external_norm, tau_norm,
           c0, window_source, p_EE, p_feature, deg):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    base = os.path.splitext(os.path.basename(path))[0]
    outdir = args.outdir or os.path.dirname(os.path.abspath(path))
    os.makedirs(outdir, exist_ok=True)

    # 1) clearance-relative controller rotation error vs time
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(t, eR_norm * deg, lw=1.5)
    if c0 > 0:
        ax.axvline(t[c0], ls="--", color="k", lw=1,
                   label="analysis-window start")
        ax.legend()
    ax.set_xlabel("time [s]"); ax.set_ylabel(r"$\|e_R\|$ [deg]")
    ax.set_title("Controller rotation error relative to clearance orientation")
    fig.tight_layout(); fig.savefig(os.path.join(outdir, f"{base}_eR.png"), dpi=150)
    plt.close(fig)

    # 2) displacement relative to the analysis-window start
    fig, ax = plt.subplots(figsize=(7, 3.5))
    tcp_relative = _norm(p_EE - p_EE[c0]) * 1000.0
    ax.plot(t, tcp_relative, lw=1.5, label="TCP displacement [mm]")
    if p_feature is not None:
        feature_relative = _norm(p_feature - p_feature[c0]) * 1000.0
        ax.plot(t, feature_relative, lw=1.2,
                label="selected-feature displacement [mm]")
    if c0 > 0:
        ax.axvline(t[c0], ls="--", color="k", lw=1)
    ax.set_xlabel("time [s]"); ax.legend()
    ax.set_title("Displacement relative to analysis-window start")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, f"{base}_displacement.png"), dpi=150)
    plt.close(fig)

    # 3) Cartesian-force and commanded joint-torque diagnostics
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(t, f_cmd_norm, lw=1.5, label=r"$\|f_{\rm cmd}\|$ [N]")
    if np.any(np.isfinite(f_external_norm)):
        ax.plot(t, f_external_norm, lw=1.2,
                label=r"$\|\Delta f_{\rm ext}\|$ [N]")
    ax.plot(t, tau_norm, lw=1.5, label=r"$\|\tau_{\rm cmd}\|$ [Nm]")
    if c0 > 0:
        ax.axvline(t[c0], ls="--", color="k", lw=1)
    ax.set_xlabel("time [s]"); ax.legend()
    ax.set_title(f"Force and joint-torque diagnostics ({window_source})")
    fig.tight_layout(); fig.savefig(os.path.join(outdir, f"{base}_force_torque.png"), dpi=150)
    plt.close(fig)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", nargs="+", help="one or more log CSV files")
    ap.add_argument("--contact-time", type=float, default=None,
                    help="analysis-window start time [s] (overrides phase selection)")
    ap.add_argument("--phase-value", type=int, default=2,
                    help="phase integer used as the current-log analysis window "
                         "(default: 2 = set_up)")
    ap.add_argument("--contact-force-threshold", type=float, default=3.0,
                    help="bias-corrected external-force threshold within phase "
                         "2, or legacy force fallback [N]")
    ap.add_argument("--window", type=int, default=50,
                    help="samples used for before/after medians")
    ap.add_argument("--outdir", default=None, help="directory for the PNG plots")
    ap.add_argument("--no-plots", action="store_true", help="skip the figures")
    ap.add_argument("--verbose", action="store_true",
                    help="also print analysis-window and signal-source details")
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
    print("\nColumns: eR_clearance_* and delta_eR_control are controller-error "
          "metrics, not physical surface-alignment angles; tcp_displacement "
          "and feature_displacement are before--after geometric metrics; "
          "f_cmd and tau_cmd are commanded peaks; "
          "f_external_delta is the bias-corrected external-force-estimate peak.")


if __name__ == "__main__":
    main()
