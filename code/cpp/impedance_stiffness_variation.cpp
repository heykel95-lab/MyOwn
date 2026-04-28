/**
 * impedance_stiffness_variation.cpp
 * =================================
 * Experiment 3: stiffness variation.
 *
 * The normal/local stiffness value is varied while the same controller
 * structure is kept:
 *   Kp_base = W_local_to_base * Kp_local * W_local_to_base.transpose()
 *
 * This file demonstrates how increasing stiffness reduces steady-state
 * displacement but increases Cartesian force and joint torque demand.
 */

#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>

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

  const std::vector<double> normal_stiffness_values = {200.0, 500.0, 1000.0};

  try {
    franka::Robot robot(argv[1]);
    franka::Model model = robot.loadModel();

    const Eigen::Vector3d p0(0.50, 0.00, 0.40);
    const Eigen::Vector3d n(0.0, 0.0, 1.0);
    const Eigen::Matrix3d W_local_to_base = Eigen::Matrix3d::Identity();

    for (double k_stiff : normal_stiffness_values) {
      Eigen::Matrix3d Kp_local = Eigen::Matrix3d::Zero();
      Kp_local.diagonal() << 50.0, 50.0, k_stiff;

      Eigen::Matrix3d Dp_local = Eigen::Matrix3d::Zero();
      Dp_local.diagonal() << 2.0 * std::sqrt(50.0),
                             2.0 * std::sqrt(50.0),
                             2.0 * std::sqrt(k_stiff);

      const Eigen::Matrix3d Kp_base =
          W_local_to_base * Kp_local * W_local_to_base.transpose();
      const Eigen::Matrix3d Dp_base =
          W_local_to_base * Dp_local * W_local_to_base.transpose();

      std::ofstream csv("exp3_k" + std::to_string(static_cast<int>(k_stiff)) + ".csv");
      csv << "time,d_wall,f_z,tau1,tau2,tau3,tau4,tau5,tau6,tau7\n";

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
        Eigen::Vector3d e_p = -d * n;

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

        csv << time << "," << d << "," << f(2);
        for (int i = 0; i < 7; ++i) {
          csv << "," << tau_cmd(i);
        }
        csv << "\n";

        if (time > 3.0) {
          return franka::MotionFinished(franka::Torques(eigenToArray(tau_cmd)));
        }
        return franka::Torques(eigenToArray(tau_cmd));
      });
    }

  } catch (const franka::Exception& e) {
    std::cerr << e.what() << std::endl;
    return -1;
  }

  return 0;
}
