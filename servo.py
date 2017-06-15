import Adafruit_PCA9685

class ServoController:
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)

    def set(self, port, value):
        self.pwm.set_pwm(port, 0, value)

class Calibration:
    def __init__(self, neg90, zero, pos90):
        self.neg90 = neg90
        self.zero = zero
        self.pos90 = pos90

    def degreesToValue(self, degrees):
        if degrees > 0.0:
            k = (self.pos90 - self.zero) / 90.0
        else:
            k = (self.zero - self.neg90) / 90.0
        return k * degrees + self.zero

class Servo:
    def __init__(self, calibration, controller, port, min, max):
        self.calibration = calibration
        self.controller = controller
        self.port = port
        self.min = min
        self.max = max

    def setDegree(self, degrees):
        value = self.calibration.degreesToValue(degrees)
        self.setRaw(value)

    def setRaw(self, value):
        if value > self.max:
            value = self.max
        if value < self.min:
            value = self.min

        self.controller.set(self.port, value)
