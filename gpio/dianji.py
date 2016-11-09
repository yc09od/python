import RPi.GPIO as gpio
import time
import signal
import atexit

gpio.setmode(gpio.BOARD)

port_out = 3

gpio.setup(port_out,gpio.OUT)
p = gpio.PWM(port_out,50)
p.start(0)

try :
	for i in range(0,181,10):
		p.ChangeDutyCycle(2.5 + 10 * i /180)
		time.sleep(0.02)
		p.ChangeDutyCycle(0)
		time.sleep(0.2)
	print 'change'
	for i in range(181,0,-10):
		p.ChangeDutyCycle(2.5 + 10 * i /180)
		time.sleep(0.02)
		p.ChangeDutyCycle(0)
		time.sleep(0.2)

except KeyboardInterrupt:
	gpio.cleanup()
p.start(0)
gpio.cleanup()
