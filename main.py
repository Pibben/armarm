#import input
import kinematics
import math
import numpy as np

def main():
    f = kinematics.ArticulatedArm()
    forward = f.calculate_forward(math.radians(0), math.radians(1), math.radians(1))
    np.set_printoptions(precision=4)
    np.set_printoptions(suppress=True)
    print(forward)
    inverse = f.calculate_inverse(forward[0], forward[1], forward[2])
    print(np.array(inverse))

if __name__ == "__main__":
    main()
