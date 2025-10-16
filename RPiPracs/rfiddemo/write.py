import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
print("Looking for cards")
print("Press Ctrl+c to STOP")
try:
    text=input('Enter New Data:')
    print("Now place your tag to write	")
    reader.write(text)
    print("Data Written Successfully	")
finally:
    GPIO.cleanup()











    
# SDA - 24
# SCK - 23
# MOSI - 19
# MISO - 21 
# GND - 6 , VCC / 3.3V - 1
# RST - 22
# apt-get update & upgrade
# sudo raspi-config > SPI
# sudo reboot 
# sudo apt-get install python3-dev python3-pip
# sudo pip3 install spidev
# sudo pip3 install mfrc522
# run write.py then read.py
#welcome message
