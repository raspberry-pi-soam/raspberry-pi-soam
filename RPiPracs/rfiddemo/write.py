import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
#welcome message
print("Looking for cards")
print("Press Ctrl+c to STOP")
try:
    text=input('Enter New Data:')
    print("Now place your tag to write	")
    reader.write(text)
    print("Data Written Successfully	")
finally:
    GPIO.cleanup()