import math

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

L1 = 0.10       # meters
L2 = 0.05       # meters
theta1 = 0      # radians
theta2 = 0      # radians

x, y = compute_tip_position(L1, theta1, L2, theta2)

print("Tip position:", (x, y))
print("Expected:", (L1 + L2, 0))
