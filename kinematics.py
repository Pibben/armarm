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



class ArticulatedArmForward:
    def __init__(self):
        l1 = 8
        l2 = 20
        l3 = 25

        self.L1 = Link(math.radians(90), 0, l1, None)
        self.L2 = Link(math.radians(0), l2, 0, None)
        self.L3 = Link(math.radians(-90), l3, 0, None)

    def calculate(self, theta1, theta2, theta3):
        m = self.L1.calculate(theta1) * self.L2.calculate(theta2) * self.L3.calculate(theta3)

        return m @ np.array([0, 0, 0, 1])