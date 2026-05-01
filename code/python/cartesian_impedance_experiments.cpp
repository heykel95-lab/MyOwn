#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>

#include <Eigen/Dense>
#include <Eigen/Geometry>

#include <franka/model.h>
#include <franka/robot.h>
#include <franka/robot_state.h>
#include <franka/duration.h>
#include <franka/exception.h>


// ============================================================
// Experiment selection
// ============================================================

enum class ExperimentType {
  SetPointLowStiffness,
  SetPointHighStiffness,
  Trajectory,
  ComplianceLowStiffness,
  ComplianceHighStiffness
};


// ============================================================
// Experiment parameter structure
// ============================================================

struct ExperimentConfig {
  Eigen::Vector3d p_d;

  double roll_d;
  double pitch_d;
  double yaw_d;

  double K1_p;
  double K2_p;
  double K3_p;

  double K1_R;
  double K2_R;
  double K3_R;

  bool use_trajectory;

  std::string csv_file_name;
};


// ============================================================
// Define experiment parameters
// ============================================================

ExperimentConfig getExperimentConfig(ExperimentType experiment) {
  ExperimentConfig config;

  switch (experiment) {

    case ExperimentType::SetPointLowStiffness:
      config.p_d << 0.45, 0.00, 0.35;

      config.roll_d  = 0.0;
      config.pitch_d = 0.0;
      config.yaw_d   = 0.0;

      config.K1_p = 800.0;
      config.K2_p = 800.0;
      config.K3_p = 800.0;

      config.K1_R = 30.0;
      config.K2_R = 30.0;
      config.K3_R = 30.0;

      config.use_trajectory = false;
      config.csv_file_name = "setpoint_low_stiffness.csv";
      break;


    case ExperimentType::SetPointHighStiffness:
      config.p_d << 0.45, 0.00, 0.35;

      config.roll_d  = 0.0;
      config.pitch_d = 0.0;
      config.yaw_d   = 0.0;

      config.K1_p = 2500.0;
      config.K2_p = 2500.0;
      config.K3_p = 2500.0;

      config.K1_R = 80.0;
      config.K2_R = 80.0;
      config.K3_R = 80.0;

      config.use_trajectory = false;
      config.csv_file_name = "setpoint_high_stiffness.csv";
      break;


    case ExperimentType::Trajectory:
      config.p_d << 0.45, 0.00, 0.35;

      config.roll_d  = 0.0;
      config.pitch_d = 0.0;
      config.yaw_d   = 0.0;

      config.K1_p = 1500.0;
      config.K2_p = 1500.0;
      config.K3_p = 1500.0;

      config.K1_R = 50.0;
      config.K2_R = 50.0;
      config.K3_R = 50.0;

      config.use_trajectory = true;
      config.csv_file_name = "trajectory_experiment.csv";
      break;


    case ExperimentType::ComplianceLowStiffness:
      config.p_d << 0.45, 0.00, 0.35;

      config.roll_d  = 0.0;
      config.pitch_d = 0.0;
      config.yaw_d   = 0.0;

      config.K1_p = 500.0;
      config.K2_p = 500.0;
      config.K3_p = 500.0;

      config.K1_R = 30.0;
      config.K2_R = 30.0;
      config.K3_R = 30.0;

      config.use_trajectory = false;
      config.csv_file_name = "compliance_low_stiffness.csv";
      break;


    case ExperimentType::ComplianceHighStiffness:
      config.p_d << 0.45, 0.00, 0.35;

      config.roll_d  = 0.0;
      config.pitch_d = 0.0;
      config.yaw_d   = 0.0;

      config.K1_p = 2500.0;
      config.K2_p = 2500.0;
      config.K3_p = 2500.0;

      config.K1_R = 80.0;
      config.K2_R = 80.0;
      config.K3_R = 80.0;

      config.use_trajectory = false;
      config.csv_file_name = "compliance_high_stiffness.csv";
      break;
  }

  return config;
}


// ============================================================
// Helper functions
// ============================================================

// Define function eigenToArray: convert an Eigen torque vector to a std::array.
std::array<double, 7> eigenToArray(
    const Eigen::Matrix<double, 7, 1>& tau) {

  std::array<double, 7> tau_array{};

  for (int i = 0; i < 7; ++i) {
    tau_array[i] = tau(i);
  }

  return tau_array;
}


// Define function limitTorques: limit each commanded joint torque.
Eigen::Matrix<double, 7, 1> limitTorques(
    const Eigen::Matrix<double, 7, 1>& tau) {

  const double tau_max = 87.0;

  Eigen::Matrix<double, 7, 1> tau_limited;

  for (int i = 0; i < 7; ++i) {
    tau_limited(i) = std::max(-tau_max, std::min(tau_max, tau(i)));
  }

  return tau_limited;
}


// Define function computeDesiredOrientation:
// compute R_d from desired roll, pitch, and yaw using the ZYX convention.
Eigen::Matrix3d computeDesiredOrientation(
    double roll_d,
    double pitch_d,
    double yaw_d) {

  Eigen::Matrix3d R_d =
      Eigen::AngleAxisd(yaw_d, Eigen::Vector3d::UnitZ()).toRotationMatrix() *
      Eigen::AngleAxisd(pitch_d, Eigen::Vector3d::UnitY()).toRotationMatrix() *
      Eigen::AngleAxisd(roll_d, Eigen::Vector3d::UnitX()).toRotationMatrix();

  return R_d;
}


// Define function computeOrientationError:
// compute the rotational error vector from desired and current orientations.
Eigen::Vector3d computeOrientationError(
    const Eigen::Matrix3d& R_d,
    const Eigen::Matrix3d& R_EE) {

  Eigen::Matrix3d dR = R_d.transpose() * R_EE;

  double cos_phi = (dR.trace() - 1.0) / 2.0;
  cos_phi = std::min(1.0, std::max(-1.0, cos_phi));

  double phi = std::acos(cos_phi);

  Eigen::Vector3d e_R;

  if (phi < 1e-6) {
    e_R.setZero();
  } else {
    e_R =
        phi / (2.0 * std::sin(phi)) *
        Eigen::Vector3d(dR(2, 1) - dR(1, 2),
                        dR(0, 2) - dR(2, 0),
                        dR(1, 0) - dR(0, 1));
  }

  return e_R;
}


// Define function updateDesiredPosition:
// use either a fixed set-point or a time-dependent trajectory.
Eigen::Vector3d updateDesiredPosition(
    const ExperimentConfig& config,
    double time) {

  Eigen::Vector3d p_d = config.p_d;

  if (config.use_trajectory) {
    p_d(0) = config.p_d(0) + 0.04 * std::sin(2.0 * M_PI * 0.25 * time);
    p_d(1) = config.p_d(1) + 0.03 * std::cos(2.0 * M_PI * 0.25 * time);
    p_d(2) = config.p_d(2) + 0.02 * std::sin(2.0 * M_PI * 0.15 * time);
  }

  return p_d;
}


// ============================================================
// Main controller
// ============================================================

int main(int argc, char** argv) {
  try {

    // Select the experiment case here.
    ExperimentType experiment = ExperimentType::SetPointLowStiffness;

    // Other possible selections:
    // ExperimentType experiment = ExperimentType::SetPointHighStiffness;
    // ExperimentType experiment = ExperimentType::Trajectory;
    // ExperimentType experiment = ExperimentType::ComplianceLowStiffness;
    // ExperimentType experiment = ExperimentType::ComplianceHighStiffness;

    ExperimentConfig config = getExperimentConfig(experiment);

    // Replace this with the robot IP address used in your setup.
    franka::Robot robot("172.16.0.2");

    // Load the robot model from libfranka.
    // The model is used to compute the Jacobian, gravity, and Coriolis terms.
    franka::Model model = robot.loadModel();

    // Compute the desired orientation R_d using the ZYX convention.
    Eigen::Matrix3d R_d =
        computeDesiredOrientation(config.roll_d,
                                  config.pitch_d,
                                  config.yaw_d);

    // Diagonal positional stiffness matrix in the desired end-effector frame.
    Eigen::Matrix3d Kp_EE =
        Eigen::Vector3d(config.K1_p,
                        config.K2_p,
                        config.K3_p).asDiagonal();

    // Diagonal rotational stiffness matrix in the desired end-effector frame.
    Eigen::Matrix3d KR_EE =
        Eigen::Vector3d(config.K1_R,
                        config.K2_R,
                        config.K3_R).asDiagonal();

    // Critical damping matrices in the desired end-effector frame.
    Eigen::Matrix3d Dp_EE =
        2.0 * Eigen::Vector3d(std::sqrt(config.K1_p),
                              std::sqrt(config.K2_p),
                              std::sqrt(config.K3_p)).asDiagonal();

    Eigen::Matrix3d DR_EE =
        2.0 * Eigen::Vector3d(std::sqrt(config.K1_R),
                              std::sqrt(config.K2_R),
                              std::sqrt(config.K3_R)).asDiagonal();

    // Express the stiffness and damping matrices in the base frame.
    Eigen::Matrix3d Kp_base = R_d * Kp_EE * R_d.transpose();
    Eigen::Matrix3d Dp_base = R_d * Dp_EE * R_d.transpose();

    Eigen::Matrix3d KR_base = R_d * KR_EE * R_d.transpose();
    Eigen::Matrix3d DR_base = R_d * DR_EE * R_d.transpose();

    // Open CSV file for logging experimental data.
    std::ofstream log_file(config.csv_file_name);

    // Write CSV header.
    log_file << "time,"
             << "p_EE_x,p_EE_y,p_EE_z,"
             << "p_d_x,p_d_y,p_d_z,"
             << "e_p_x,e_p_y,e_p_z,"
             << "e_R_x,e_R_y,e_R_z,"
             << "pdot_x,pdot_y,pdot_z,"
             << "omega_x,omega_y,omega_z,"
             << "f_x,f_y,f_z,"
             << "m_x,m_y,m_z,"
             << "tau_1,tau_2,tau_3,tau_4,tau_5,tau_6,tau_7"
             << "\n";

    // Initialize experiment time.
    double time = 0.0;

    // Real-time torque-control callback:
    // libfranka provides the current robot state at each control cycle, including
    // q, dq, and T_EE. The callback computes and returns the joint torque vector tau.
    robot.control([&](const franka::RobotState& state,
                      franka::Duration period) -> franka::Torques {

      // Update elapsed experiment time.
      time += period.toSec();

      // Map the current joint positions q from the robot state to an Eigen vector.
      Eigen::Map<const Eigen::Matrix<double, 7, 1>>
          q(state.q.data());

      // Map the current joint velocities dq from the robot state to an Eigen vector.
      Eigen::Map<const Eigen::Matrix<double, 7, 1>>
          dq(state.dq.data());

      // Compute the geometric Jacobian at the end-effector using the libfranka model.
      std::array<double, 42> jacobian_array =
          model.zeroJacobian(franka::Frame::kEndEffector, state);

      // Map the Jacobian array to a 6x7 Eigen matrix.
      Eigen::Map<const Eigen::Matrix<double, 6, 7>>
          J(jacobian_array.data());

      // Compute the Cartesian end-effector velocity from the joint velocities.
      Eigen::Matrix<double, 6, 1> xdot = J * dq;

      // Extract the linear velocity and angular velocity of the end-effector.
      Eigen::Vector3d pdot = xdot.head<3>();
      Eigen::Vector3d omega = xdot.tail<3>();

      // Map the current homogeneous end-effector transformation T_EE to an Eigen matrix.
      Eigen::Map<const Eigen::Matrix<double, 4, 4>>
          T_EE(state.O_T_EE.data());

      // Extract the current end-effector position p_EE and orientation R_EE.
      Eigen::Vector3d p_EE = T_EE.block<3, 1>(0, 3);
      Eigen::Matrix3d R_EE = T_EE.block<3, 3>(0, 0);

      // Update the desired position.
      // For set-point and compliance experiments, this stays constant.
      // For trajectory experiments, it changes with time.
      Eigen::Vector3d p_d = updateDesiredPosition(config, time);

      // Compute the Cartesian position error.
      Eigen::Vector3d e_p = p_d - p_EE;

      // Compute the rotational error.
      Eigen::Vector3d e_R = computeOrientationError(R_d, R_EE);

      // Compute the positional impedance force.
      Eigen::Vector3d f =
          Kp_base * e_p - Dp_base * pdot;

      // Compute the rotational impedance moment.
      Eigen::Vector3d m =
          KR_base * e_R - DR_base * omega;

      // Combine the Cartesian force and moment into one 6D force/moment vector.
      Eigen::Matrix<double, 6, 1> F;
      F.head<3>() = f;
      F.tail<3>() = m;

      // Map the Cartesian force/moment vector to joint torques using the Jacobian transpose.
      Eigen::Matrix<double, 7, 1> tau_task =
          J.transpose() * F;

      // Read the gravity compensation torque tau_g from the libfranka model.
      std::array<double, 7> gravity_array =
          model.gravity(state);

      // Read the Coriolis and centrifugal compensation torque tau_c from the libfranka model.
      std::array<double, 7> coriolis_array =
          model.coriolis(state);

      // Map the compensation terms to Eigen vectors.
      Eigen::Map<const Eigen::Matrix<double, 7, 1>>
          tau_g(gravity_array.data());

      Eigen::Map<const Eigen::Matrix<double, 7, 1>>
          tau_c(coriolis_array.data());

      // Compute the final commanded joint torque vector.
      Eigen::Matrix<double, 7, 1> tau =
          tau_task + tau_g + tau_c;

      // Limit the commanded torques before sending them to the robot.
      Eigen::Matrix<double, 7, 1> tau_limited =
          limitTorques(tau);

      // Log measured and computed quantities for later evaluation.
      log_file << std::fixed << std::setprecision(6)
               << time << ","
               << p_EE(0) << "," << p_EE(1) << "," << p_EE(2) << ","
               << p_d(0)  << "," << p_d(1)  << "," << p_d(2)  << ","
               << e_p(0) << "," << e_p(1) << "," << e_p(2) << ","
               << e_R(0) << "," << e_R(1) << "," << e_R(2) << ","
               << pdot(0) << "," << pdot(1) << "," << pdot(2) << ","
               << omega(0) << "," << omega(1) << "," << omega(2) << ","
               << f(0) << "," << f(1) << "," << f(2) << ","
               << m(0) << "," << m(1) << "," << m(2) << ","
               << tau_limited(0) << "," << tau_limited(1) << ","
               << tau_limited(2) << "," << tau_limited(3) << ","
               << tau_limited(4) << "," << tau_limited(5) << ","
               << tau_limited(6)
               << "\n";

      // Convert the limited Eigen torque vector to std::array and return it to libfranka.
      return franka::Torques(eigenToArray(tau_limited));
    });

  } catch (const franka::Exception& e) {
    std::cerr << e.what() << std::endl;
    return -1;
  }

  return 0;
}
