import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637
Display = tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
Display.clear()
Display.brightness(1)
while(True):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    currenttime = 1234
    currenttime = f"{hour:02d}{minute:02d}"  # currenttime = "1305"
    Display.show(currenttime, colon=(second % 2 == 1))
    time.sleep(1)
#VCC -> GPIO (Pin 4)
#GND -> GPIO (Pin 14)
#CLK -> GPIO23 (Pin 16)
#Di0 -> GPIO24 (Pin 18)
#sudo apt update
#sudo apt upgrade
#steps to write in exam
#1.Connection of wires
#2.dowload tm1637.py script from https://github.com/mcauser/micropython-tm1637.git
#3.clock.py
#4.place tm1637.py and clock.py in same folder
