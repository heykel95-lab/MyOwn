#!/usr/bin/env python3
"""Generate the principal Chapter 5 figures from an extracted metrics CSV."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# The thesis loads \usepackage{lmodern}.  Using LaTeX for all plot text makes
# labels and mathematics use the same Latin Modern fonts as the document.
plt.rcParams.update(
    {
        "text.usetex": True,
        "text.latex.preamble": r"\usepackage{lmodern}\usepackage{amsmath}",
        "font.family": "serif",
        "font.serif": ["Latin Modern Roman"],
        "font.size": 9.5,
        "axes.labelsize": 9.5,
        "axes.titlesize": 9.5,
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "legend.fontsize": 8.5,
        "axes.linewidth": 0.8,
        "lines.linewidth": 1.4,
        "lines.markersize": 5.5,
        "grid.color": "0.85",
        "grid.linewidth": 0.6,
        "grid.alpha": 0.8,
        "axes.unicode_minus": False,
        "savefig.facecolor": "white",
    }
)


BLUE = "#0072B2"
ORANGE = "#D55E00"
GREEN = "#009E73"
INK = "#303030"
LIGHT_INK = "#8A8A8A"


DATA_FLAGS = {
    "not-converged",
    "no-setup-phase",
    "no-general-log",
    "tip-mismatch",
    "task-disturbed",
}


def number(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "nan"))
    except ValueError:
        return float("nan")


def admissible(row: dict[str, str]) -> bool:
    flags = {item.split("(")[0] for item in row.get("flags", "").split(";")}
    return not bool(flags & DATA_FLAGS)


def save(fig: plt.Figure, output_dir: Path, name: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_dir / name,
        bbox_inches="tight",
        pad_inches=0.04,
        metadata={"Creator": "Matplotlib with LaTeX/Latin Modern"},
    )
    plt.close(fig)


def grouped_mean_sd(
    x: np.ndarray, y: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return one mean and sample SD for each distinct x coordinate."""
    x_values = np.unique(x)
    means = np.array([np.mean(y[x == value]) for value in x_values])
    errors = np.array(
        [
            np.std(y[x == value], ddof=1) if np.sum(x == value) > 1 else 0.0
            for value in x_values
        ]
    )
    return x_values, means, errors


def remove_top_and_right_spines(ax: plt.Axes) -> None:
    for name in ("top", "right"):
        ax.spines[name].set_visible(False)


def stiffness_figure(rows: list[dict[str, str]], output_dir: Path) -> None:
    selected = [
        row
        for row in rows
        if row["run_id"].startswith("A2_KRtan") and admissible(row)
    ]
    buckets: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in selected:
        buckets[int(row["run_id"].split("_")[-1])].append(row)

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(6.45, 2.75),
        constrained_layout=True,
    )
    panels = (
        (
            "align_improve_real_deg",
            r"Physical-plane improvement, $\Delta\theta_{\mathrm{align,phys}}$ ($^\circ$)",
        ),
        ("force_steady_N", r"Estimated normal load (N)"),
    )
    for ax, (key, ylabel) in zip(axes, panels):
        x_values = sorted(buckets)
        means = [np.mean([number(row, key) for row in buckets[x]]) for x in x_values]
        errors = [
            np.std([number(row, key) for row in buckets[x]], ddof=1)
            for x in x_values
        ]
        ax.errorbar(
            x_values,
            means,
            yerr=errors,
            marker="o",
            capsize=3.5,
            color=BLUE,
            markerfacecolor="white",
            markeredgewidth=1.2,
        )
        ax.set_xlabel(r"$K_{R,t_1}=K_{R,t_2}$ ($\mathrm{N\,m/rad}$)")
        ax.set_ylabel(ylabel)
        ax.set_xticks(x_values)
        ax.grid(axis="y")
        remove_top_and_right_spines(ax)
    save(fig, output_dir, "A2_stiffness_sweep.pdf")


def settling_figure(rows: list[dict[str, str]], output_dir: Path) -> None:
    selected = [
        row
        for row in rows
        if row["run_id"].startswith("G2_equilibrium") and admissible(row)
    ]
    selected.sort(key=lambda row: number(row, "setup_duration_s"))

    duration = np.rint(
        np.array([number(row, "setup_duration_s") for row in selected])
    )
    tip = np.array([number(row, "tip_final_deg") for row in selected])
    drift = np.array(
        [number(row, "tip_drift_last20pct_deg") for row in selected]
    )
    load = np.array([number(row, "force_final_N") for row in selected])

    fig, axes = plt.subplots(
        1,
        3,
        figsize=(6.45, 2.55),
        constrained_layout=True,
    )
    panels = (
        (tip, r"Final tip angle ($^\circ$)", False),
        (drift, r"Final-fifth tip drift ($^\circ$)", True),
        (load, r"Final estimated normal load (N)", False),
    )
    for ax, (values, ylabel, logarithmic) in zip(axes, panels):
        ax.plot(
            duration,
            values,
            "-o",
            color=BLUE,
            markerfacecolor="white",
            markeredgewidth=1.2,
        )
        ax.set_xlabel("Set-up duration (s)")
        ax.set_ylabel(ylabel)
        ax.set_xticks(duration.astype(int))
        if logarithmic:
            ax.set_yscale("log")
        ax.grid(axis="y", which="major")
        remove_top_and_right_spines(ax)

    save(fig, output_dir, "G2_equilibrium.pdf")


def pole_points(
    rows: list[dict[str, str]], prefix: str, coordinate: str
) -> tuple[np.ndarray, np.ndarray]:
    points = [
        (number(row, coordinate), number(row, "align_improve_real_deg"))
        for row in rows
        if row["run_id"].startswith(prefix) and admissible(row)
    ]
    points = [(x, y) for x, y in points if np.isfinite(x) and np.isfinite(y)]
    if not points:
        return np.array([]), np.array([])
    return np.array([point[0] for point in points]), np.array(
        [point[1] for point in points]
    )


def component_figure(rows: list[dict[str, str]], output_dir: Path) -> None:
    series = (
        ("B2_pole_normal", "configured-normal sweep", BLUE, "o"),
        ("B3_pole_tangent_", r"$t_1$ sweep", ORANGE, "^"),
        ("B4_pole_tangent2", r"$t_2$ sweep", GREEN, "s"),
    )
    coordinates = (
        ("pole_cmd_x_mm", r"Offset along $t_1$ (mm)"),
        ("pole_cmd_y_mm", r"Offset along $t_2$ (mm)"),
        ("pole_cmd_z_mm", r"Normal offset (mm)"),
    )

    fig = plt.figure(figsize=(6.45, 5.0), constrained_layout=True)
    grid_spec = fig.add_gridspec(2, 2)
    axes = (
        fig.add_subplot(grid_spec[0, 0]),
        fig.add_subplot(grid_spec[0, 1]),
        fig.add_subplot(grid_spec[1, :]),
    )
    panel_labels = (r"\textbf{(a)}", r"\textbf{(b)}", r"\textbf{(c)}")

    all_response = np.array(
        [
            number(row, "align_improve_real_deg")
            for row in rows
            if row["run_id"].startswith(("B1_", "B2_", "B3_", "B4_"))
            and admissible(row)
        ]
    )
    all_response = all_response[np.isfinite(all_response)]
    response_padding = 0.08 * np.ptp(all_response)
    response_limits = (
        np.min(all_response) - response_padding,
        np.max(all_response) + response_padding,
    )

    legend_handles = []
    legend_labels = []
    for panel_index, (ax, (coordinate, xlabel)) in enumerate(
        zip(axes, coordinates)
    ):
        all_x: list[np.ndarray] = []
        all_y: list[np.ndarray] = []
        for prefix, label, colour, marker in series:
            x, y = pole_points(rows, prefix, coordinate)
            if not x.size:
                continue
            ax.plot(
                x,
                y,
                marker,
                color=colour,
                ms=3.2,
                alpha=0.24,
                linestyle="none",
            )
            x_group, mean, error = grouped_mean_sd(x, y)
            handle = ax.errorbar(
                x_group,
                mean,
                yerr=error,
                marker=marker,
                color=colour,
                markerfacecolor="white",
                markeredgewidth=1.0,
                capsize=2.5,
                linestyle="none",
                label=label,
            )
            if panel_index == 0:
                legend_handles.append(handle)
                legend_labels.append(label)
            all_x.append(x)
            all_y.append(y)

        x = np.concatenate(all_x)
        y = np.concatenate(all_y)
        degree = 1 if coordinate == "pole_cmd_z_mm" else 2
        coefficients = np.polyfit(x, y, degree)
        fitted = np.polyval(coefficients, x)
        r_squared = 1.0 - np.sum((y - fitted) ** 2) / np.sum(
            (y - np.mean(y)) ** 2
        )
        grid = np.linspace(np.min(x), np.max(x), 200)
        ax.plot(grid, np.polyval(coefficients, grid), color=INK)
        if degree == 2:
            stationary = -coefficients[1] / (2.0 * coefficients[0])
            note = (
                f"$R^2={r_squared:.3f}$\n"
                f"stationary: ${stationary:+.0f}\\,\\mathrm{{mm}}$"
            )
        else:
            note = (
                f"$R^2={r_squared:.3f}$\n"
                f"slope: ${coefficients[0]:+.3f}^\\circ/\\mathrm{{mm}}$"
            )
        ax.annotate(
            note,
            xy=(0.97, 0.96),
            xycoords="axes fraction",
            ha="right",
            va="top",
            bbox={"facecolor": "white", "edgecolor": "0.8", "pad": 2.5},
        )
        ax.text(
            0.02,
            0.96,
            panel_labels[panel_index],
            transform=ax.transAxes,
            va="top",
        )
        ax.axhline(0.0, color=LIGHT_INK, linewidth=0.9)
        ax.set_xlabel(xlabel)
        ax.set_ylim(response_limits)
        ax.grid(axis="y")
        remove_top_and_right_spines(ax)

    axes[0].set_ylabel(r"Physical-plane improvement ($^\circ$)")
    axes[2].set_ylabel(r"Physical-plane improvement ($^\circ$)")
    axes[1].tick_params(labelleft=False)
    fig.legend(
        legend_handles,
        legend_labels,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.02),
        ncol=3,
        frameon=False,
    )
    save(fig, output_dir, "B_pole_component.pdf")


def surface_figure(rows: list[dict[str, str]], output_dir: Path) -> None:
    fit_points = []
    held_out_points = []
    for row in rows:
        if not row["run_id"].startswith(("B1_", "B2_", "B3_", "B4_")):
            continue
        if not admissible(row):
            continue
        point = (
            number(row, "pole_cmd_x_mm"),
            number(row, "pole_cmd_y_mm"),
            number(row, "align_improve_real_deg"),
        )
        if all(np.isfinite(value) for value in point):
            if row["run_id"].startswith("B1_"):
                held_out_points.append(point)
            else:
                fit_points.append(point)

    measured = np.asarray(fit_points)
    held_out = np.asarray(held_out_points)
    x, y, response = measured[:, 0], measured[:, 1], measured[:, 2]
    design = np.column_stack([x, x**2, y, y**2, np.ones(len(measured))])
    coefficients, residuals, *_ = np.linalg.lstsq(design, response, rcond=None)
    fitted = design @ coefficients
    r_squared = 1.0 - np.sum((response - fitted) ** 2) / np.sum(
        (response - np.mean(response)) ** 2
    )
    x_stationary = -coefficients[0] / (2.0 * coefficients[1])
    y_stationary = -coefficients[2] / (2.0 * coefficients[3])

    grid_x = np.linspace(np.min(x) - 10, np.max(x) + 10, 240)
    grid_y = np.linspace(np.min(y) - 10, np.max(y) + 10, 240)
    xx, yy = np.meshgrid(grid_x, grid_y)
    zz = (
        coefficients[0] * xx
        + coefficients[1] * xx**2
        + coefficients[2] * yy
        + coefficients[3] * yy**2
        + coefficients[4]
    )
    distance_squared = np.min(
        (xx[..., None] - x) ** 2 + (yy[..., None] - y) ** 2, axis=-1
    )
    zz = np.ma.masked_where(distance_squared > 45.0**2, zz)

    fig, ax = plt.subplots(
        figsize=(6.25, 4.35),
        constrained_layout=True,
    )
    limit = np.max(np.abs(response))
    contour = ax.contourf(
        xx,
        yy,
        zz,
        levels=np.linspace(-limit, limit, 17),
        cmap="RdBu_r",
        vmin=-limit,
        vmax=limit,
        extend="both",
    )
    ax.contour(xx, yy, zz, levels=[0.0], colors=INK, linewidths=1.1)
    ax.plot(
        x,
        y,
        "o",
        ms=4.5,
        mfc="none",
        mec=INK,
        mew=0.8,
        linestyle="none",
        label="Fitted settings",
    )
    ax.plot(
        held_out[:, 0],
        held_out[:, 1],
        "D",
        ms=5.0,
        mfc="white",
        mec=GREEN,
        mew=1.0,
        linestyle="none",
        label="Held-out E1 setting",
    )
    ax.plot(
        [x_stationary],
        [y_stationary],
        "*",
        ms=12,
        color=INK,
        linestyle="none",
        label="Predicted stationary point",
    )
    ax.annotate(
        (
            f"$R^2={r_squared:.3f}$, $n={len(measured)}$\n"
            f"stationary: $({x_stationary:+.0f},"
            f"{y_stationary:+.0f})\\,\\mathrm{{mm}}$"
        ),
        xy=(0.03, 0.97),
        xycoords="axes fraction",
        va="top",
        bbox={"facecolor": "white", "edgecolor": "0.8", "pad": 3.0},
    )
    colourbar = fig.colorbar(contour, ax=ax, pad=0.02)
    colourbar.set_label(r"Physical-plane improvement ($^\circ$)")
    ax.set_xlabel(r"Offset along $t_1$ (mm)")
    ax.set_ylabel(r"Offset along $t_2$ (mm)")
    ax.legend(loc="lower right", framealpha=0.92)
    ax.grid(False)
    save(fig, output_dir, "B_pole_surface.pdf")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metrics", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    arguments = parser.parse_args()

    with arguments.metrics.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    settling_figure(rows, arguments.output_dir)
    stiffness_figure(rows, arguments.output_dir)
    component_figure(rows, arguments.output_dir)
    surface_figure(rows, arguments.output_dir)


if __name__ == "__main__":
    main()
