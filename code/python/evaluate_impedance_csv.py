import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Load CSV log file
# ------------------------------------------------------------
file_path = "impedance_experiment_log.csv"
data = pd.read_csv(file_path)


# ------------------------------------------------------------
# Compute error norms
# ------------------------------------------------------------
data["e_p_norm"] = np.sqrt(
    data["e_p_x"]**2 +
    data["e_p_y"]**2 +
    data["e_p_z"]**2
)

data["e_R_norm"] = np.sqrt(
    data["e_R_x"]**2 +
    data["e_R_y"]**2 +
    data["e_R_z"]**2
)


# ------------------------------------------------------------
# Evaluation time window for steady-state error
# Here: final 20% of the experiment
# ------------------------------------------------------------
t_final = data["time"].iloc[-1]
steady_state_start = 0.8 * t_final

steady_state_data = data[data["time"] >= steady_state_start]


# ------------------------------------------------------------
# Maximum errors
# ------------------------------------------------------------
e_p_max = data["e_p_norm"].max()
e_R_max = data["e_R_norm"].max()


# ------------------------------------------------------------
# Steady-state errors
# Mean error over final 20% of experiment
# ------------------------------------------------------------
e_p_ss = steady_state_data["e_p_norm"].mean()
e_R_ss = steady_state_data["e_R_norm"].mean()


# ------------------------------------------------------------
# Overshoot calculation for each error component
# Overshoot is evaluated after the first zero crossing.
# ------------------------------------------------------------
def compute_overshoot(time, error):
    error = np.asarray(error)

    # Find first zero crossing
    zero_crossings = np.where(np.diff(np.sign(error)) != 0)[0]

    if len(zero_crossings) == 0:
        return 0.0

    first_crossing_index = zero_crossings[0]

    # Overshoot is the maximum absolute error after the first zero crossing
    overshoot = np.max(np.abs(error[first_crossing_index:]))

    return overshoot


overshoot_ep_x = compute_overshoot(data["time"], data["e_p_x"])
overshoot_ep_y = compute_overshoot(data["time"], data["e_p_y"])
overshoot_ep_z = compute_overshoot(data["time"], data["e_p_z"])

overshoot_eR_x = compute_overshoot(data["time"], data["e_R_x"])
overshoot_eR_y = compute_overshoot(data["time"], data["e_R_y"])
overshoot_eR_z = compute_overshoot(data["time"], data["e_R_z"])


# ------------------------------------------------------------
# Maximum commanded torque for each joint
# ------------------------------------------------------------
tau_max = {}

for i in range(1, 8):
    tau_max[f"tau_{i}_max"] = data[f"tau_{i}"].abs().max()


# ------------------------------------------------------------
# Print evaluation results
# ------------------------------------------------------------
print("Evaluation Results")
print("------------------")
print(f"Maximum positional error:      {e_p_max:.6f} m")
print(f"Steady-state positional error: {e_p_ss:.6f} m")
print()
print(f"Maximum rotational error:      {e_R_max:.6f} rad")
print(f"Steady-state rotational error: {e_R_ss:.6f} rad")
print()
print("Position overshoot:")
print(f"  e_p_x overshoot: {overshoot_ep_x:.6f} m")
print(f"  e_p_y overshoot: {overshoot_ep_y:.6f} m")
print(f"  e_p_z overshoot: {overshoot_ep_z:.6f} m")
print()
print("Rotational overshoot:")
print(f"  e_R_x overshoot: {overshoot_eR_x:.6f} rad")
print(f"  e_R_y overshoot: {overshoot_eR_y:.6f} rad")
print(f"  e_R_z overshoot: {overshoot_eR_z:.6f} rad")
print()
print("Maximum commanded joint torques:")
for key, value in tau_max.items():
    print(f"  {key}: {value:.6f} Nm")


# ------------------------------------------------------------
# Plot position error components
# ------------------------------------------------------------
plt.figure()
plt.plot(data["time"], data["e_p_x"], label=r"$e_{p,x}$")
plt.plot(data["time"], data["e_p_y"], label=r"$e_{p,y}$")
plt.plot(data["time"], data["e_p_z"], label=r"$e_{p,z}$")
plt.xlabel("Time [s]")
plt.ylabel("Position error [m]")
plt.title("Position Error")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Plot position error norm
# ------------------------------------------------------------
plt.figure()
plt.plot(data["time"], data["e_p_norm"], label=r"$\|e_p\|$")
plt.xlabel("Time [s]")
plt.ylabel("Position error norm [m]")
plt.title("Position Error Norm")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Plot rotational error components
# ------------------------------------------------------------
plt.figure()
plt.plot(data["time"], data["e_R_x"], label=r"$e_{R,x}$")
plt.plot(data["time"], data["e_R_y"], label=r"$e_{R,y}$")
plt.plot(data["time"], data["e_R_z"], label=r"$e_{R,z}$")
plt.xlabel("Time [s]")
plt.ylabel("Rotational error [rad]")
plt.title("Rotational Error")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Plot rotational error norm
# ------------------------------------------------------------
plt.figure()
plt.plot(data["time"], data["e_R_norm"], label=r"$\|e_R\|$")
plt.xlabel("Time [s]")
plt.ylabel("Rotational error norm [rad]")
plt.title("Rotational Error Norm")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Plot Cartesian forces
# ------------------------------------------------------------
plt.figure()
plt.plot(data["time"], data["f_x"], label=r"$f_x$")
plt.plot(data["time"], data["f_y"], label=r"$f_y$")
plt.plot(data["time"], data["f_z"], label=r"$f_z$")
plt.xlabel("Time [s]")
plt.ylabel("Force [N]")
plt.title("Cartesian Impedance Forces")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Plot Cartesian moments
# ------------------------------------------------------------
plt.figure()
plt.plot(data["time"], data["m_x"], label=r"$m_x$")
plt.plot(data["time"], data["m_y"], label=r"$m_y$")
plt.plot(data["time"], data["m_z"], label=r"$m_z$")
plt.xlabel("Time [s]")
plt.ylabel("Moment [Nm]")
plt.title("Cartesian Impedance Moments")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Plot commanded joint torques
# ------------------------------------------------------------
plt.figure()

for i in range(1, 8):
    plt.plot(data["time"], data[f"tau_{i}"], label=rf"$\tau_{i}$")

plt.xlabel("Time [s]")
plt.ylabel("Joint torque [Nm]")
plt.title("Commanded Joint Torques")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
