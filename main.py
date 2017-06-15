import input
import servo
#import kinematics
#import numpy as np

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
    controller = servo.ServoController()
    s0 = servo.Servo(None, controller, 0, 320, 550)
    s1 = servo.Servo(None, controller, 1, 320, 550)
    s2 = servo.Servo(None, controller, 2, 22
    0, 550)

    value = {0: 400.0, 1: 400.0, 2:400.0}

    def pi(d):
        print(d)

    def serve(d):
        value[0] -= d['RZ']*2.0
        value[1] -= d['RX']
        value[2] -= d['Z']
        print(d['Z'], value[2])
        s0.setRaw(int(value[0]))
        s1.setRaw(int(value[1]))
        s2.setRaw(int(value[2]))

    i = input.Input(serve)
    i.run()
#    c = Controller()

#    c.run(np.array([10, 0, 0]))
#    c.run(np.array([1, 0, 0]))
#    c.run(np.array([2, 0, 0]))


if __name__ == "__main__":
    main()
