import evdev
import threading

def find_device(name):
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    for device in devices:
        if device.name == name:
            return device

    return None


class Input:
    def __init__(self, func):
        self.dev = find_device('3Dconnexion SpaceNavigator')
        self.t = None
        self.func = func

    def reset(self):
        self.values = [0, 0, 0, 0, 0, 0]
        self.emit()

    def emit(self):
        labels = ['X', 'Y', 'Z', 'RX', 'RY', 'RZ']
        self.func(dict(zip(labels, self.values)))

    def run(self):
        self.reset()

        for event in self.dev.read_loop():
            if event.type == evdev.ecodes.EV_REL:
                self.values[event.code] = event.value / 350.0

            if event.type == evdev.ecodes.EV_SYN:
                if self.t:
                    self.t.cancel()
                self.emit()
                self.t = threading.Timer(0.1, self.reset)
                self.t.start()
