class ServoController:
    def __init__(self, address):
        self.address = address
        self.pwm = None
        self.pwm.setPWMFreq(60)

    def set(self, port, value):
        self.pwm.setPWM(port, 0, value)

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
    def __init__(self, calibration, controller, port):
        self.calibration = calibration
        self.controller = controller
        self.port = port

    def setDegree(self, degrees):
        value = self.calibration.degreesToValue(degrees)
        self.controller.set(self.port, value)