sudo modprobe uinput
sudo chgrp uinput /dev/uinput
sudo chmod g+rw /dev/uinput
source ./.venv/bin/activate
exec python sumd.py