import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import matplotlib.pyplot as plt


# Setup I2C and ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0)


# Prepare lists to store data
times = []
voltages = []


start_time = time.time()


plt.ion()  # Turn interactive mode on for live plot
fig, ax = plt.subplots()


while True:
    current_time = time.time() - start_time
    voltage = chan.voltage


    # Append data
    times.append(current_time)
    voltages.append(voltage)


    # Plot data
    ax.clear()
    ax.plot(times, voltages, label="Voltage (V)")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title("ADS1015 Voltage Readings")
    ax.legend()
    plt.pause(0.1)


    time.sleep(0.5)
