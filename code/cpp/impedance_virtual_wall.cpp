/**
 * impedance_virtual_wall.cpp
 * ==========================
 * Experiment 2: compliant interaction with a virtual wall.
 *
 * This file uses the same local/base indexing style as the thesis:
 *   Kp_local: diagonal stiffness in the wall/local frame
 *   Kp_base : full stiffness matrix expressed in the robot base frame
 *
 * The wall frame is defined by two tangential directions t1, t2 and one
 * normal direction n. For an axis-aligned wall, W_local_to_base = I.
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

    // Wall geometry in base frame.
    const Eigen::Vector3d p0(0.50, 0.00, 0.40);
    const Eigen::Vector3d t1(1.0, 0.0, 0.0);
    const Eigen::Vector3d t2(0.0, 1.0, 0.0);
    const Eigen::Vector3d n(0.0, 0.0, 1.0);

    Eigen::Matrix3d W_local_to_base;
    W_local_to_base.col(0) = t1;
    W_local_to_base.col(1) = t2;
    W_local_to_base.col(2) = n;

    // Local wall-frame stiffness: free tangential, stiff normal.
    Eigen::Matrix3d Kp_local = Eigen::Matrix3d::Zero();
    Kp_local.diagonal() << 50.0, 50.0, 1000.0;  // N/m

    Eigen::Matrix3d Dp_local = Eigen::Matrix3d::Zero();
    Dp_local.diagonal() << 14.14, 14.14, 63.25;  // Ns/m

    const Eigen::Matrix3d Kp_base =
        W_local_to_base * Kp_local * W_local_to_base.transpose();
    const Eigen::Matrix3d Dp_base =
        W_local_to_base * Dp_local * W_local_to_base.transpose();

    std::ofstream csv("exp2_virtual_wall.csv");
    csv << "time,d_wall,p_x,p_y,p_z,v_x,v_y,v_z,f_x,f_y,f_z,"
           "tau1,tau2,tau3,tau4,tau5,tau6,tau7\n";

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

      const double d = n.transpose() * (p_e - p0);
      Eigen::Vector3d e_p = -d * n;  // desired signed distance is zero

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

      csv << time << "," << d
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
