#import input
import kinematics
import math
import numpy as np

def main():
    np.set_printoptions(precision=4)
    np.set_printoptions(suppress=True)

    f = kinematics.ArticulatedArm()

    inverse = f.calculate_inverse(10, 0 , 0)
    print(np.degrees(np.array(inverse)))

    forward = f.calculate_forward(*inverse)
    print(forward[:3])


if __name__ == "__main__":
    main()
