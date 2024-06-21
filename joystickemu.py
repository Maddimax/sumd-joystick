import uinput

class Joystick:
    def __init__(self) -> None:
        events = (
            uinput.ABS_X + (1100, 1900, 0, 0),
            uinput.ABS_Y + (1100, 1900, 0, 0),
            uinput.ABS_GAS + (1100, 1900, 0, 0),
            uinput.ABS_RUDDER + (1100, 1900, 0, 0),
            uinput.ABS_RX + (1100, 1900, 0, 0),
            uinput.ABS_RY + (1100, 1900, 0, 0),
        )
        self.device = uinput.Device(
            events,
            vendor=0x045e,
            product=0x028e,
            version=0x110,
            name="Graupner GR12",
        )
    def update(self, channels):
        self.device.emit(uinput.ABS_GAS, channels[0], syn=False)
        
        self.device.emit(uinput.ABS_X, channels[1], syn=False)
        self.device.emit(uinput.ABS_Y, channels[2])

        self.device.emit(uinput.ABS_RUDDER, channels[3])

        self.device.emit(uinput.ABS_RX, channels[4], syn=False)
        self.device.emit(uinput.ABS_RY, channels[5])