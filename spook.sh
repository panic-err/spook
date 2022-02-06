#!/bin/bash

DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo "Service started at ${DATE}" | systemd-cat -p info

while :
do
python3 /home/pi/spook/tkmain.py
done
