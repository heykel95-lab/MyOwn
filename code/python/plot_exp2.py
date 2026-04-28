"""
plot_exp2.py
============
Reads exp2_virtual_wall.csv and plots wall distance and Cartesian force.

Usage:
    python3 plot_exp2.py
    python3 plot_exp2.py path/to/exp2_virtual_wall.csv
"""

import sys
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("exp2_virtual_wall.csv")
df = pd.read_csv(csv_path)

plt.figure()
plt.plot(df["time"], 1000.0 * df["d_wall"])
plt.xlabel("Time [s]")
plt.ylabel("Wall distance [mm]")
plt.title("Experiment 2: virtual-wall signed distance")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("exp2_wall_distance.pdf")

plt.figure()
plt.plot(df["time"], df["f_x"], label=r"$f_x$")
plt.plot(df["time"], df["f_y"], label=r"$f_y$")
plt.plot(df["time"], df["f_z"], label=r"$f_z$")
plt.xlabel("Time [s]")
plt.ylabel("Force [N]")
plt.title("Experiment 2: Cartesian force")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("exp2_cartesian_force.pdf")

print("Saved exp2_wall_distance.pdf and exp2_cartesian_force.pdf")
