# SUMD-Joystick

This is a simple python script to read sumd values from the Raspberry PI GPIO serial
and output the data as a virtual joystick.

## Hardware

Connect your receivers "SUMD" pin to the GPIO Pin 10 of your Raspberry 5.
(Check the pinout for other versions). Connect the "+" to Pin 1 and the GND
to Pin 6. 

> :warning: **Make sure that your receiver runs at 3.3v as the pins of the Raspberry PI may not survive anything higher!**

## TX Setup

In your Transmitter find the "Telemetry" menu and set `SUMD at CH6` to `Yes`. If yours outputs on a different Pin adjust accordingly.

## Installation

```bash
git clone https://github.com/maddimax/sumd-joystick
cd sumd-joystick
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

## Using

You can test if everything works using the `test` flag:

```bash 
python sumd.py test
```

## Install

To finally install as a service edit the [sumd-joystick.service](sumd-joystick.service) file and change the paths according
to your setup. Then install the service 

```bash 
sudo cp sumd-joystick.service /etc/systemd/system/
```

And finally start it 

```bash 
sudo systemctl start sumd-joystick
```

To start it at boottime run 

```bash
sudo systemctl enable sumd-joystick
```

You can check if its working via 

```bash
journalctl -fu sumd-joystick
```
