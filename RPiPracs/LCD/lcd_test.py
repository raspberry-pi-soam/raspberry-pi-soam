from RPLCD.i2c import CharLCD
from time import sleep


lcd = CharLCD('PCF8574', 0x27)  # Change 0x27 if needed


lcd.write_string("hello from Team Rocket")
sleep(10)
lcd.clear()
lcd.write_string("hello from Anchal")
sleep(10)
lcd.clear()
lcd.write_string("hello from Sakshi")
sleep(10)
lcd.clear()
lcd.write_string("hello from Sanika")
sleep(10)
lcd.clear()
lcd.write_string("hello from Omkar")
sleep(10)
lcd.clear()
lcd.write_string("hello from Manash")
sleep(10)
lcd.clear()
