import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

port_in = 3
port_out = 5
port_out2 = 7

gpio.setup(port_in,gpio.IN)
gpio.setup(port_out,gpio.OUT)
gpio.setup(port_out2,gpio.OUT)
last = 0

try :
	while True :
		gpio.output(port_out,gpio.LOW)
		time.sleep(0.1)

		
		gpio.output(port_out,gpio.HIGH)
		time.sleep(0.0001)
		gpio.output(port_out,gpio.LOW)
		time.sleep(0.0001)
		start = time.time()

		while gpio.input(port_in) == 0:
			start = time.time()


		while gpio.input(port_in) == 1:
			stop = time.time()

	
		distance = (stop - start) * 34000 / 2
		print distance
		gpio.output(port_out2,gpio.LOW)
		if distance < 30 :
			print "*****************"
			gpio.output(port_out2,gpio.HIGH)
except KeyboardInterrupt:
	gpio.cleanup()
gpio.cleanup()
