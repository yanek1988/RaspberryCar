#!/usr/bin/env bash

# make sure script is executed with sudo

# service bluetooth restart
hciconfig hci0 up

LOGFILE=/home/pi/raspberrycar.log
LISTENERFILE=/home/pi/obd.log
PROJECTPATH=/home/pi/projects/RaspberryCar/

LISTENERRUNNING=`ps aux |grep listener.py |wc -l`
echo `date` >> "$LOGFILE"

if [[ "$LISTENERRUNNING" == "2" ]]; then
        echo "DEBUG: listener already running - no action needed" >> "$LOGFILE"
        exit 0;
fi

hcitool scan > /tmp/scan.log
cat /tmp/scan.log >> "$LOGFILE"
MACADDRESS=`cat /tmp/scan.log |grep 'OBD\|Vgate' |awk '{print $1}'`

if [[ "$MACADDRESS" == "" ]]; then
	echo "ERROR: unable to get mac address of OBD device" >> "$LOGFILE"
	exit 0;
fi

sleep 5
rfcomm connect 0 "$MACADDRESS" 1 >> "$LOGFILE" 2>&1 &

sleep 10
cd "$PROJECTPATH" && python3 listener.py -m adv >> "$LISTENERFILE" 2>&1 &

exit 0;

