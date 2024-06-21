import serial

class SumDReceiver:
    MAX_CHANNEL_NUMBER=16 

    def __init__(self) -> None:
        self.ser = serial.Serial('/dev/ttyAMA0',
                        baudrate=115200,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE)
        self.channels = [1500]*self.MAX_CHANNEL_NUMBER

    def getChannels(self):
        return self.channels
    
    def checkCrc(self, crc, value):
        crc ^= value << 8

        for i in range(0, 8):
            if (crc & 0x8000) > 0:
                crc =(crc << 1) ^ 0x1021
            else:
                crc = crc << 1
        return crc & 0xFFFF

    def update(self):
        state = 0
        inFailsafe = 0
        numberOfChannels = 0
        buf = b''

        while True:
            data = self.ser.read()
            buf += data

            if state == 0:
                if data[0] == 0xA8:
                    state = 1
                continue

            if state == 1:
                if data[0] == 0x01 or data[0] == 0x81:
                    if data[0] == 0x81:
                        inFailsafe = True
                    state = 2
                    continue

            if state == 2:
                if data[0] >= 2 and data[0] <= self.MAX_CHANNEL_NUMBER:
                    numberOfChannels = data[0]

                    channelData = self.ser.read(2*numberOfChannels)
                    buf = buf + channelData
                    channels = []
                    for i in range(0, numberOfChannels):
                        channels.append(
                            (channelData[(i*2)] << 5) + (channelData[i*2+1] >> 3)
                        )
                    self.channels = channels
                    buf = buf + self.ser.read(2)
                    crc = 0
                    for v in buf:
                        crc = self.checkCrc(crc, v)

                    return crc == 0
            state = 0
