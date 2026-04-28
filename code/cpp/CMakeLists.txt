cmake_minimum_required(VERSION 3.10)
project(cartesian_impedance_thesis CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")

find_package(Franka REQUIRED)
find_package(Eigen3 REQUIRED)

# Experiment 1: fixed-point tracking with rotated stiffness directions
add_executable(impedance_pose_tracking impedance_pose_tracking.cpp)
target_link_libraries(impedance_pose_tracking Franka::Franka Eigen3::Eigen)

# Experiment 2: virtual wall interaction
add_executable(impedance_virtual_wall impedance_virtual_wall.cpp)
target_link_libraries(impedance_virtual_wall Franka::Franka Eigen3::Eigen)

# Experiment 3: stiffness variation
add_executable(impedance_stiffness_variation impedance_stiffness_variation.cpp)
target_link_libraries(impedance_stiffness_variation Franka::Franka Eigen3::Eigen)

# Experiment 4: configuration dependence
add_executable(impedance_config_dependence impedance_config_dependence.cpp)
target_link_libraries(impedance_config_dependence Franka::Franka Eigen3::Eigen)
