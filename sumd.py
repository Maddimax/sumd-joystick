import sys
from sumdreceiver import SumDReceiver
from joystickemu import Joystick

receiver = SumDReceiver()
joystick = Joystick()

nLoops = 100000000000

def loop(test):
    global nLoops
    updateSuccess = receiver.update()
    rxChannels = receiver.getChannels()
    if updateSuccess:
        joystick.update(rxChannels)
    if test:
        print(f"Channels: {rxChannels}, Ok: {updateSuccess}")
    else:
        if not updateSuccess:
            print('.', end='', flush=True)
        if nLoops > 1000:
            print('\n')
            print(receiver.getChannels())
            nLoops = 0
        if nLoops % 50 == 0:
            print('.', end='', flush=True)
        nLoops = nLoops + 1

def main():
    print("Virtual Joystick v0.1")
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    while True:
        loop(test)

exit(main())