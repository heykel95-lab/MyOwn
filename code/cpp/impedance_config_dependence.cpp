/**
 * impedance_config_dependence.cpp
 * ===============================
 * Experiment 4: configuration dependence of joint torques.
 *
 * The same Cartesian wrench is applied at different robot configurations.
 * Because J = J(q), the torque vector tau = J^T(q) F changes with q.
 */

#include <array>
#include <iostream>
#include <vector>

#include <Eigen/Dense>
#include <franka/exception.h>
#include <franka/model.h>
#include <franka/robot.h>

int main(int argc, char** argv) {
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <robot-hostname-or-ip>\n";
    return -1;
  }

  try {
    franka::Robot robot(argv[1]);
    franka::Model model = robot.loadModel();

    std::vector<std::array<double, 7>> configurations = {
        {0.0, -M_PI/4, 0.0, -3*M_PI/4, 0.0, M_PI/2, M_PI/4},
        {0.0, -M_PI/6, 0.0, -2*M_PI/3, 0.0, M_PI/2, M_PI/4},
        {M_PI/6, -M_PI/4, 0.0, -3*M_PI/4, 0.0, M_PI/2, M_PI/4}
    };

    // Example Cartesian force in base x-direction.
    Eigen::Matrix<double, 6, 1> F;
    F << -1.0, 0.0, 0.0, 0.0, 0.0, 0.0;

    for (size_t c = 0; c < configurations.size(); ++c) {
      // In a full implementation, move_to_config(robot, configurations[c])
      // is called here before reading the Jacobian at the configuration.

      franka::RobotState state = robot.readOnce();
      std::array<double, 42> jacobian_array =
          model.zeroJacobian(franka::Frame::kEndEffector, state);
      Eigen::Map<const Eigen::Matrix<double, 6, 7>> J(jacobian_array.data());

      Eigen::Matrix<double, 7, 1> tau = J.transpose() * F;

      std::cout << "Configuration " << (c + 1) << ": ";
      for (int i = 0; i < 7; ++i) {
        std::cout << tau(i) << " ";
      }
      std::cout << "Nm\n";
    }

  } catch (const franka::Exception& e) {
    std::cerr << e.what() << std::endl;
    return -1;
  }

  return 0;
}
