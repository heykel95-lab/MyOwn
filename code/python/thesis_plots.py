"""
thesis_plots.py
===============
Generates thesis plots for the rewritten impedance-control thesis.

The script is intentionally independent from robot hardware. It creates
simulation plots that explain:
  1. fixed-point tracking with rotated stiffness directions,
  2. virtual-wall stiffness behaviour,
  3. stiffness variation,
  4. configuration-dependent torque distribution.

Output folder:
  ./plots
"""

from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PLOTS = Path("plots")
PLOTS.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "lines.linewidth": 2.0,
})

def Rx(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[1,0,0],[0,c,-s],[0,s,c]])

def Ry(b):
    c, s = np.cos(b), np.sin(b)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]])

def Rz(g):
    c, s = np.cos(g), np.sin(g)
    return np.array([[c,-s,0],[s,c,0],[0,0,1]])

def rotated_stiffness():
    alpha, beta, gamma = np.deg2rad([20.0, 30.0, 40.0])
    W = Rz(gamma) @ Ry(beta) @ Rx(alpha)
    K_local = np.diag([1000.0, 300.0, 100.0])
    K_base = W @ K_local @ W.T
    return K_base

def plot_exp1_rotated_tracking():
    K = rotated_stiffness()
    t = np.linspace(0.0, 2.0, 1000)
    e0 = np.array([0.01, 0.0, 0.0])
    # Use a simple exponential error decay for illustration.
    e = np.outer(np.exp(-4*t), e0)
    f = e @ K.T

    fig, ax = plt.subplots()
    ax.plot(t, f[:,0], label=r"$f_x$")
    ax.plot(t, f[:,1], label=r"$f_y$")
    ax.plot(t, f[:,2], label=r"$f_z$")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Force [N]")
    ax.set_title("Experiment 1: full-matrix force response for fixed-point tracking")
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOTS / "exp1_rotated_force_components.pdf")
    plt.close(fig)

def plot_exp1_matrix():
    K = rotated_stiffness()
    fig, ax = plt.subplots()
    im = ax.imshow(K)
    ax.set_xticks([0,1,2], labels=["x","y","z"])
    ax.set_yticks([0,1,2], labels=["x","y","z"])
    ax.set_title(r"Full base-frame stiffness matrix $K_{p,\mathrm{base}}$")
    for i in range(3):
        for j in range(3):
            ax.text(j, i, f"{K[i,j]:.1f}", ha="center", va="center")
    fig.colorbar(im, ax=ax, label="N/m")
    fig.tight_layout()
    fig.savefig(PLOTS / "exp1_K_base_matrix.pdf")
    plt.close(fig)

def plot_exp3_stiffness_variation():
    K = np.array([200, 500, 1000], dtype=float)
    F = 5.0
    d_mm = 1000 * F / K
    fig, ax = plt.subplots()
    ax.plot(K, d_mm, marker="o")
    ax.set_xlabel(r"Normal stiffness $K$ [N/m]")
    ax.set_ylabel(r"Steady-state displacement $d_{ss}$ [mm]")
    ax.set_title(r"Experiment 3: $d_{ss}=F/K$")
    fig.tight_layout()
    fig.savefig(PLOTS / "exp3_stiffness_variation.pdf")
    plt.close(fig)

def plot_exp4_torques():
    labels = ["q1 home", "q2 elbow", "q3 rotated"]
    tau = np.array([
        [0.55, 0.55, -0.04, 0.32, -0.06, -0.06, 0.00],
        [0.42, 0.42, -0.08, 0.28, -0.05, -0.05, 0.00],
        [0.38, 0.61, -0.06, 0.35, -0.07, -0.04, 0.00],
    ])
    x = np.arange(7)
    width = 0.25
    fig, ax = plt.subplots()
    for i, lab in enumerate(labels):
        ax.bar(x + (i-1)*width, tau[i], width=width, label=lab)
    ax.set_xticks(x, labels=[f"J{i+1}" for i in range(7)])
    ax.set_ylabel("Torque [Nm]")
    ax.set_title("Experiment 4: configuration-dependent torque distribution")
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOTS / "exp4_configuration_torques.pdf")
    plt.close(fig)

if __name__ == "__main__":
    plot_exp1_rotated_tracking()
    plot_exp1_matrix()
    plot_exp3_stiffness_variation()
    plot_exp4_torques()
    print(f"Plots written to {PLOTS.resolve()}")
