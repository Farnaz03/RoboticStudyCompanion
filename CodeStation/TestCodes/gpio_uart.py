### GPIO 14 TXD & GPIO 15 RXD

import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1) # open the serial port
time.sleep(1) # wait for the Nextion display to initialize

ser.write('t0.txt="Hello World!"'.encode('utf-8')) # send the text to the Nextion display
ser.write(0xff) # end of command character
ser.write(0xff)
ser.write(0xff)

ser.close() # close the serial port

#https://github.com/WiringPi/WiringPi-Python
# import wiringpi
# wiringpi.wiringPiSetup()
# serial = wiringpi.serialOpen('/dev/ttyS0',9600)
# wiringpi.serialPuts(serial,'hello world!')