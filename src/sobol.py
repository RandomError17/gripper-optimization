from prbm_model import evaluate_design
from SALib.sample.sobol import sample
from SALib.analyze import sobol
import numpy as np

problem = {
    "num_vars": 4,
    "names": ["link_length_1","link_length_2","joint_stiffness","tendon_offset"],
    "bounds": [[0.030, 0.055],[0.015, 0.030],[0.26, 0.71],[0.002, 0.006]]
}

N = 1024
F = 130
l = 0.010
b = 0.012
param_values = sample(problem,N,calc_second_order=True)
theta1_min = 0
theta1_max = np.pi / 2

stress_outputs = []
grip_force_outputs = []

for row in param_values:

    link_length_1, link_length_2, joint_stiffness, tendon_offset = row

    worst_case_stress, minimum_grip_force = evaluate_design(link_length_1,link_length_2,joint_stiffness,tendon_offset,F,theta1_min,theta1_max,l,b)

    stress_outputs.append(worst_case_stress)
    grip_force_outputs.append(minimum_grip_force)

Y_stress = np.array(stress_outputs)
Y_grip_force = np.array(grip_force_outputs)

Si_stress = sobol.analyze(problem,Y_stress,calc_second_order=True)
Si_grip_force = sobol.analyze(problem,Y_grip_force,calc_second_order=True)

print(Si_stress)
print(Si_grip_force)