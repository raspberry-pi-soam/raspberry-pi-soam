from RPLCD.i2c import CharLCD
from time import sleep
# gnd - 6
# vcc - 4
# sda - 3
# scl - 5
# sudo raspi-config > I2C
# sudo reboot and update, upgrade apt
# sudo apt install i2c-tools python3-smbus python3-pip
# sudo pip3 install RPLCD
# i2cdetect -y 1 & check for 27 or any other number

lcd = CharLCD('PCF8574', 0x27)  # Change 0x27 if needed


lcd.write_string("hello from Team Rocket")
sleep(10)
lcd.clear()
