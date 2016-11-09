import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

port_in = 3
port_out = 5

gpio.setup(port_in,gpio.IN)
gpio.setup(port_out,gpio.OUT)

try :

except KeyboardInterrupt:
	gpio.cleanup()
gpio.cleanup()
