"""
plot_exp1.py
============
Reads exp1_rotated_tracking.csv and plots the measured force components.

Usage:
    python3 plot_exp1.py
    python3 plot_exp1.py path/to/exp1_rotated_tracking.csv
"""

import sys
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("exp1_rotated_tracking.csv")
df = pd.read_csv(csv_path)

plt.figure()
plt.plot(df["time"], df["f_x"], label=r"$f_x$")
plt.plot(df["time"], df["f_y"], label=r"$f_y$")
plt.plot(df["time"], df["f_z"], label=r"$f_z$")
plt.xlabel("Time [s]")
plt.ylabel("Force [N]")
plt.title("Experiment 1: fixed-point tracking with rotated stiffness")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("exp1_rotated_tracking_forces.pdf")
print("Saved exp1_rotated_tracking_forces.pdf")
