import math
import numpy as np

GAMMA = 0.85
K_THETA = 2.66
E = 9.2e6 

def compute_theta2(F, r, k):
    theta2 = (F * r) / k
    return theta2

def compute_tip_force(k, theta2, L2):
    F_tip = (k * theta2) / L2
    return F_tip

def compute_tip_position(L1, theta1, L2, theta2):
    elbow_x = L1 * math.cos(theta1)
    elbow_y = L1 * math.sin(theta1)

    tip_x = elbow_x + L2 * math.cos(theta1 + theta2)
    tip_y = elbow_y + L2 * math.sin(theta1 + theta2)

    return tip_x, tip_y    

def compute_flexure_stress(k, theta2, l, b):
    h = ((12 * k * l) / (GAMMA * K_THETA * E * b)) ** (1 / 3)
    M = k * theta2
    c = h / 2
    I = (b * h**3) / 12
    stress = (M * c) / I

    return stress

def evaluate_configuration(L1, L2, k, r, F, theta1, l, b):
    theta2 = compute_theta2(F, r, k)
    F_tip = compute_tip_force(k, theta2, L2)
    tip_position = compute_tip_position( L1, theta1, L2, theta2)
    stress = compute_flexure_stress(k, theta2, l, b)

    return theta2, F_tip, tip_position, stress

def evaluate_design(L1, L2, k, r, F, theta1_min, theta1_max, l, b):
    theta1_values = np.linspace(theta1_min, theta1_max, 5)

    stresses = []
    grip_forces = []

    for theta1 in theta1_values:

        theta2, F_tip, tip_position, stress = evaluate_configuration(L1, L2, k, r, F, theta1, l, b)
        stresses.append(stress)
        grip_forces.append(F_tip)

    worst_case_stress = max(stresses)
    minimum_grip_force = min(grip_forces)

    return worst_case_stress, minimum_grip_force
