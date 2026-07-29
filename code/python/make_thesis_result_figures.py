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
    fig.savefig(output_dir / name, bbox_inches="tight")
    plt.close(fig)


def stiffness_figure(rows: list[dict[str, str]], output_dir: Path) -> None:
    selected = [
        row
        for row in rows
        if row["run_id"].startswith("A2_KRtan") and admissible(row)
    ]
    buckets: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in selected:
        buckets[int(row["run_id"].split("_")[-1])].append(row)

    fig, axes = plt.subplots(1, 3, figsize=(9.5, 3.0))
    panels = (
        ("align_improve_real_deg", "alignment improvement [deg]"),
        ("force_steady_N", "model-estimated normal load [N]"),
        ("tau_norm_max_Nm", "peak commanded torque norm [Nm]"),
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
            capsize=3,
            color="#2a78d6",
            linewidth=1.5,
        )
        ax.set_xlabel(r"$K_{R,\mathrm{tangent}}$ [Nm/rad]")
        ax.set_ylabel(ylabel)
        ax.grid(alpha=0.3)
    fig.suptitle("Influence of tangential rotational stiffness", fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    save(fig, output_dir, "A2_stiffness_sweep.pdf")


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
        ("B2_pole_normal", "configured-normal sweep", "#2a78d6", "o"),
        ("B3_pole_tangent_", r"$t_1$ sweep", "#eb6834", "^"),
        ("B4_pole_tangent2", r"$t_2$ sweep", "#1baf7a", "s"),
    )
    coordinates = (
        ("pole_cmd_x_mm", r"compliance-centre offset along $t_1$ [mm]"),
        ("pole_cmd_y_mm", r"compliance-centre offset along $t_2$ [mm]"),
        ("pole_cmd_z_mm", "compliance-centre normal offset [mm]"),
    )

    fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.4), sharey=True)
    for ax, (coordinate, xlabel) in zip(axes, coordinates):
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
                ms=7,
                mew=0.8,
                mec="white",
                linestyle="none",
                label=label,
            )
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
        ax.plot(grid, np.polyval(coefficients, grid), color="#52514e", linewidth=1.5)
        if degree == 2:
            stationary = -coefficients[1] / (2.0 * coefficients[0])
            note = (
                f"$R^2$ = {r_squared:.3f}\n"
                f"fitted maximum {stationary:+.0f} mm"
            )
        else:
            note = (
                f"$R^2$ = {r_squared:.3f}\n"
                f"{coefficients[0]:+.3f} deg/mm"
            )
        ax.annotate(
            note,
            xy=(0.04, 0.94),
            xycoords="axes fraction",
            va="top",
            fontsize=8,
        )
        ax.axhline(0.0, color="0.55", linewidth=1)
        ax.set_xlabel(xlabel)
        ax.grid(alpha=0.3)

    axes[0].set_ylabel("alignment improvement relative to physical plane [deg]")
    axes[0].legend(fontsize=8, loc="lower right", frameon=False)
    fig.suptitle("Alignment response by compliance-centre coordinate", fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    save(fig, output_dir, "B_pole_component.pdf")


def surface_figure(rows: list[dict[str, str]], output_dir: Path) -> None:
    points = []
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
            points.append(point)

    measured = np.asarray(points)
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

    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    limit = np.max(np.abs(response))
    contour = ax.contourf(
        xx,
        yy,
        zz,
        levels=np.linspace(-limit, limit, 15),
        cmap="RdBu_r",
        extend="both",
    )
    ax.contour(xx, yy, zz, levels=[0.0], colors="0.25", linewidths=1.2)
    ax.plot(
        x,
        y,
        "o",
        ms=5,
        mfc="none",
        mec="#0b0b0b",
        mew=0.9,
        linestyle="none",
        label="measured runs",
    )
    ax.plot(
        [x_stationary],
        [y_stationary],
        "*",
        ms=15,
        color="#0b0b0b",
        linestyle="none",
        label=(
            "model-predicted stationary point "
            f"({x_stationary:+.0f}, {y_stationary:+.0f}) mm"
        ),
    )
    colourbar = fig.colorbar(contour, ax=ax)
    colourbar.set_label("alignment improvement relative to physical plane [deg]")
    ax.set_xlabel(r"compliance-centre offset along $t_1$ [mm]")
    ax.set_ylabel(r"compliance-centre offset along $t_2$ [mm]")
    ax.set_title(
        f"Additive quadratic fit, $R^2$ = {r_squared:.3f} over "
        f"{len(measured)} runs; shaded only near measured runs",
        fontsize=9,
    )
    ax.legend(fontsize=7, loc="lower right", framealpha=0.9)
    ax.grid(False)
    save(fig, output_dir, "B_pole_surface.pdf")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metrics", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    arguments = parser.parse_args()

    with arguments.metrics.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    stiffness_figure(rows, arguments.output_dir)
    component_figure(rows, arguments.output_dir)
    surface_figure(rows, arguments.output_dir)


if __name__ == "__main__":
    main()
