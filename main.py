#import input
import kinematics
import math

def main():
    f = kinematics.ArticulatedArmForward()
    print(f.calculate(0, math.radians(0), math.radians(-1)))

if __name__ == "__main__":
    main()
