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
double K1_p = 500.0;
double K2_p = 500.0;
double K3_p = 500.0;

// Rotational stiffness values about the desired end-effector x-, y-, and z-axes.
double K1_R = 30.0;
double K2_R = 30.0;
double K3_R = 30.0;

// Positional damping values along the desired end-effector x-, y-, and z-axes.
double D1_p = 44.72;
double D2_p = 44.72;
double D3_p = 44.72;

// Rotational damping values about the desired end-effector x-, y-, and z-axes.
double D1_R = 10.95;
double D2_R = 10.95;
double D3_R = 10.95;

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
std::string csv_file_name = "compliance_low_stiffness.csv";
