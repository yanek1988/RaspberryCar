# Raspberry Car

Library for car's computer for the following functions:
* Store car's data from OBD II
* (NOT SUPPORTED YET) Store GPS locations
* (NOT SUPPORTED YET) Show GPS Navigartion on the screen

Required components:
* Raspberry Pi Model B Revision 2.0
* OBD II ELM 327 BLUETOOTH
* Bluetooth dongle for RaspberryPi

Software:
* Raspbian
* Python 3

# Installation

### RaspberryPi

* Install Raspbian
* `mkdir projects && cd projects && git clone ...`
* Add `sh /home/pi/projects/RaspberryCar/setup/autostart.sh` to `/etc/rc.local`
* [OPTIONAL] Add `*/5 * * * * /home/pi/projects/RaspberryCar/setup/autostart.sh` to `sudo crontab -e`

### Car

* Place OBD adapter to car's slot
* Turn on your RaspberryPi


