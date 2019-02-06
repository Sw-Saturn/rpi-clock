#!/bin/sh

sudo systemctl stop twitter.service
cd /home/pi/rpi-clock
sudo /usr/bin/python3 /home/pi/rpi-clock/news.py
sudo systemctl start twitter.service
