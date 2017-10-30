#!/usr/bin/env bash

# make sure script is executed with sudo

# service bluetooth restart
hciconfig hci0 up

MACADDRESS=`hcitool scan |grep HTC |awk '{print $1}'`
sleep 5
rfcomm connect 0 "$MACADDRESS" 1 >> /home/pi/blue.log 2>&1 &

sleep 5
cd /home/pi/projects/RaspberryCar/ && python3 raspberrycar.py > /home/pi/obd.txt 2>&1

exit 0;
