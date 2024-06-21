from sumdreceiver import SumDReceiver
from joystickemu import Joystick

receiver = SumDReceiver()
joystick = Joystick()

nLoops = 100000000000

def loop():
    global nLoops
    if not receiver.update():
        print('E')
        return
    joystick.update(receiver.getChannels())
    if nLoops > 1000:
        print('\n')
        print(receiver.getChannels())
        nLoops = 0
    if nLoops % 50 == 0:
        print('.', end='', flush=True)
    nLoops = nLoops + 1

def main():
    print("Virtual Joystick v0.1")
    while True:
        loop()
    return 0

exit(main())