# import input
import kinematics
import numpy as np

class Controller:
    def __init__(self):
        np.set_printoptions(precision=4)
        np.set_printoptions(suppress=True)

        self.arm = kinematics.ArticulatedArm()
        self.coords = np.array([0, 0, 0])

    def run(self, delta_coords):
        self.coords = self.coords + delta_coords
        print("Input: ", self.coords)
        inverse = self.arm.calculate_inverse(self.coords)

        print("Inverse: ", np.degrees(np.array(inverse)))

        forward = self.arm.calculate_forward(*inverse)

        print("Forward: ", forward[:3])


def main():
    c = Controller()

    c.run(np.array([10, 0, 0]))
    c.run(np.array([1, 0, 0]))
    c.run(np.array([2, 0, 0]))


if __name__ == "__main__":
    main()
