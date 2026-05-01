Files included:

1. cartesian_impedance_controller_core.cpp
   Common controller code, matching the structure of Listing 3.1.

2. Experiment parameter files:
   - experiment_setpoint_low_stiffness.h
   - experiment_setpoint_high_stiffness.h
   - experiment_trajectory.h
   - experiment_compliance_low_stiffness.h
   - experiment_compliance_high_stiffness.h

How to select an experiment:

In cartesian_impedance_controller_core.cpp, replace

#include "experiment_setpoint_low_stiffness.h"

with the experiment file you want to run, for example

#include "experiment_trajectory.h"

The controller code stays unchanged. Only the selected parameter file changes the desired pose, stiffness values, trajectory settings, and CSV output file name.

Note:
This is a thesis-style code listing/template. In a complete buildable program, the robot object and callback context must be placed inside your actual main program structure.
