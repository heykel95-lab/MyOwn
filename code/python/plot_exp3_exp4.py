"""
plot_exp3_exp4.py
=================
Creates analysis plots for Experiment 3 and Experiment 4.

Experiment 3:
  compares steady-state displacement d_ss = F/K.

Experiment 4:
  illustrates configuration-dependent torque distributions.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
})

# Experiment 3
K = np.array([200.0, 500.0, 1000.0])
F = 5.0
d_mm = 1000.0 * F / K

plt.figure()
plt.plot(K, d_mm, marker="o")
plt.xlabel("Stiffness [N/m]")
plt.ylabel("Steady-state displacement [mm]")
plt.title(r"Experiment 3: $d_{ss}=F/K$")
plt.tight_layout()
plt.savefig("exp3_displacement_vs_stiffness.pdf")

# Experiment 4
tau = np.array([
    [0.55, 0.55, -0.04, 0.32, -0.06, -0.06, 0.00],
    [0.42, 0.42, -0.08, 0.28, -0.05, -0.05, 0.00],
    [0.38, 0.61, -0.06, 0.35, -0.07, -0.04, 0.00],
])
labels = ["q1", "q2", "q3"]
x = np.arange(7)
width = 0.25

plt.figure()
for i, lab in enumerate(labels):
    plt.bar(x + (i - 1)*width, tau[i], width=width, label=lab)
plt.xticks(x, [f"J{i+1}" for i in range(7)])
plt.ylabel("Torque [Nm]")
plt.title(r"Experiment 4: $\tau=J^T(q)F$")
plt.legend()
plt.tight_layout()
plt.savefig("exp4_torque_distribution.pdf")

print("Saved exp3_displacement_vs_stiffness.pdf and exp4_torque_distribution.pdf")
