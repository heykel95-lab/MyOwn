#pragma once

#include <string>
#include <Eigen/Dense>

// Desired end-effector position.
Eigen::Vector3d p_d(0.45, 0.0, 0.35);

// Desired orientation angles in radians.
double roll_d  = 0.0;
double pitch_d = 0.0;
double yaw_d   = 0.0;

// Positional stiffness values along the desired end-effector x-, y-, and z-axes.
double K1_p = 2500.0;
double K2_p = 2500.0;
double K3_p = 2500.0;

// Rotational stiffness values about the desired end-effector x-, y-, and z-axes.
double K1_R = 80.0;
double K2_R = 80.0;
double K3_R = 80.0;

// Trajectory settings.
// If use_trajectory is false, the desired position remains constant.
bool use_trajectory = false;

double trajectory_amplitude_x = 0.0;
double trajectory_amplitude_y = 0.0;
double trajectory_amplitude_z = 0.0;

double trajectory_frequency_x = 0.0;
double trajectory_frequency_y = 0.0;
double trajectory_frequency_z = 0.0;

// CSV output file.
std::string csv_file_name = "compliance_high_stiffness.csv";
