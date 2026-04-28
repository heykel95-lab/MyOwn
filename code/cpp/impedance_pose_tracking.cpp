/**
 * impedance_pose_tracking.cpp
 * ===========================
 * Experiment 1:
 * Fixed-point tracking with rotated stiffness directions.
 *
 * This experiment tracks one fixed Cartesian point p_des. The point defines
 * the centre of the virtual spring. The local stiffness matrix defines the
 * principal stiffness values, and W_local_to_base defines how those principal
 * directions are oriented in the robot base frame.
 *
 * Main equations:
 *   Kp_base = W_local_to_base * Kp_local * W_local_to_base.transpose()
 *   Dp_base = W_local_to_base * Dp_local * W_local_to_base.transpose()
 *   f       = Kp_base * (p_des - p_e) - Dp_base * p_dot
 *   tau     = J.transpose() * [f; 0] + tau_g + tau_c
 *
 * Output:
 *   exp1_rotated_tracking.csv
 */

#include <array>
#include <cmath>
#include <fstream>
#include <iostream>

#include <Eigen/Dense>
#include <franka/exception.h>
#include <franka/model.h>
#include <franka/robot.h>

namespace {

Eigen::Matrix3d rotationFromRPY(double roll, double pitch, double yaw) {
  Eigen::AngleAxisd Rx(roll, Eigen::Vector3d::UnitX());
  Eigen::AngleAxisd Ry(pitch, Eigen::Vector3d::UnitY());
  Eigen::AngleAxisd Rz(yaw, Eigen::Vector3d::UnitZ());
  return (Rz * Ry * Rx).toRotationMatrix();
}

std::array<double, 7> eigenToArray(const Eigen::Matrix<double, 7, 1>& v) {
  std::array<double, 7> out{};
  for (size_t i = 0; i < 7; ++i) {
    out[i] = v(i);
  }
  return out;
}

}  // namespace

int main(int argc, char** argv) {
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <robot-hostname-or-ip>\n";
    return -1;
  }

  try {
    franka::Robot robot(argv[1]);
    franka::Model model = robot.loadModel();

    // Desired fixed point: centre of the virtual spring.
    const Eigen::Vector3d p_des(0.50, 0.00, 0.40);

    // Local stiffness-frame orientation relative to the base frame.
    const double alpha = 20.0 * M_PI / 180.0;  // roll
    const double beta  = 30.0 * M_PI / 180.0;  // pitch
    const double gamma = 40.0 * M_PI / 180.0;  // yaw

    const Eigen::Matrix3d W_local_to_base = rotationFromRPY(alpha, beta, gamma);

    // Diagonal matrices in the local stiffness frame.
    Eigen::Matrix3d Kp_local = Eigen::Matrix3d::Zero();
    Kp_local.diagonal() << 1000.0, 300.0, 100.0;  // N/m

    Eigen::Matrix3d Dp_local = Eigen::Matrix3d::Zero();
    Dp_local.diagonal() << 2.0 * std::sqrt(1000.0),
                           2.0 * std::sqrt(300.0),
                           2.0 * std::sqrt(100.0);  // Ns/m

    // Full matrices used by the controller in the base frame.
    const Eigen::Matrix3d Kp_base =
        W_local_to_base * Kp_local * W_local_to_base.transpose();
    const Eigen::Matrix3d Dp_base =
        W_local_to_base * Dp_local * W_local_to_base.transpose();

    std::ofstream csv("exp1_rotated_tracking.csv");
    csv << "time,e_x,e_y,e_z,p_x,p_y,p_z,v_x,v_y,v_z,"
           "f_x,f_y,f_z,tau1,tau2,tau3,tau4,tau5,tau6,tau7\n";

    double time = 0.0;

    robot.control([&](const franka::RobotState& state,
                      franka::Duration period) -> franka::Torques {
      time += period.toSec();

      Eigen::Map<const Eigen::Matrix<double, 7, 1>> dq(state.dq.data());

      std::array<double, 42> jacobian_array =
          model.zeroJacobian(franka::Frame::kEndEffector, state);
      Eigen::Map<const Eigen::Matrix<double, 6, 7>> J(jacobian_array.data());

      Eigen::Matrix<double, 6, 1> xdot = J * dq;
      Eigen::Vector3d pdot = xdot.head<3>();

      Eigen::Map<const Eigen::Matrix<double, 4, 4>> T_EE(state.O_T_EE.data());
      Eigen::Vector3d p_e = T_EE.block<3, 1>(0, 3);

      Eigen::Vector3d e_p = p_des - p_e;
      Eigen::Vector3d f = Kp_base * e_p - Dp_base * pdot;

      Eigen::Matrix<double, 6, 1> F;
      F.head<3>() = f;
      F.tail<3>().setZero();

      Eigen::Matrix<double, 7, 1> tau_task = J.transpose() * F;

      std::array<double, 7> gravity_array = model.gravity(state);
      std::array<double, 7> coriolis_array = model.coriolis(state);
      Eigen::Map<const Eigen::Matrix<double, 7, 1>> tau_g(gravity_array.data());
      Eigen::Map<const Eigen::Matrix<double, 7, 1>> tau_c(coriolis_array.data());

      Eigen::Matrix<double, 7, 1> tau_cmd = tau_task + tau_g + tau_c;

      csv << time << "," << e_p(0) << "," << e_p(1) << "," << e_p(2)
          << "," << p_e(0) << "," << p_e(1) << "," << p_e(2)
          << "," << pdot(0) << "," << pdot(1) << "," << pdot(2)
          << "," << f(0) << "," << f(1) << "," << f(2);
      for (int i = 0; i < 7; ++i) {
        csv << "," << tau_cmd(i);
      }
      csv << "\n";

      return franka::Torques(eigenToArray(tau_cmd));
    });

  } catch (const franka::Exception& e) {
    std::cerr << e.what() << std::endl;
    return -1;
  }

  return 0;
}
