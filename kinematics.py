import math
import numpy as np

class Link:
    def __init__(self, alpha, a, d, servo):
        self.alpha = alpha
        self.a = a
        self.d = d
        self.servo = servo

    def get_rot_z_theta(self, theta):
        return np.matrix([[math.cos(theta), -math.sin(theta), 0, 0],
                          [math.sin(theta),  math.cos(theta), 0, 0],
                          [              0,                0, 1, 0],
                          [              0,                0, 0, 1]])

    def get_trans_z_d(self):
        return np.matrix([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, self.d],
                          [0, 0, 0, 1]])

    def get_trans_x_a(self):
        return np.matrix([[1, 0, 0, self.a],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])

    def get_rot_z_alpha(self):
        return np.matrix([[1,                    0,                     0, 0],
                          [0, math.cos(self.alpha), -math.sin(self.alpha), 0],
                          [0, math.sin(self.alpha),  math.cos(self.alpha), 0],
                          [0,                    0,                     0, 1]])

    def calculate(self, theta):
        return self.get_rot_z_theta(theta) * self.get_trans_z_d() * self.get_trans_x_a() * self.get_rot_z_alpha()



class ArticulatedArm:
    def __init__(self):
        l1 = 8
        l2 = 20
        l3 = 25

        self.L1 = Link(math.radians(90), 0, l1, None)
        self.L2 = Link(math.radians(180 ), l2, 0, None)
        self.L3 = Link(math.radians(-90), l3, 0, None)

    def calculate_forward(self, theta1, theta2, theta3):
        m = self.L1.calculate(theta1) * self.L2.calculate(theta2) * self.L3.calculate(theta3)

        return np.squeeze(np.asarray(m @ np.array([0, 0, 0, 1])))

    def calculate_inverse(self, X, Y, Z):
        def angle_from_sides(a, b, c):
            return math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

        R2 = X ** 2 + Y ** 2
        R = math.sqrt(R2)

        Zprim = Z - self.L1.d

        S2 = Zprim ** 2 + R2
        S = math.sqrt(S2)

        theta0 = math.atan2(Y, X)
        theta1 = angle_from_sides(self.L2.a, S, self.L3.a)
        theta2 = math.pi - angle_from_sides(self.L2.a, self.L3.a, S)
        theta_h = math.atan2(Zprim, R)

        return tuple([theta0, theta1 + theta_h, theta2])
