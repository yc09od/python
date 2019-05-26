import RPi.GPIO as gpio
import time

class Motor:
    ## link1 is left + , link3 is right +
    ## link2 is left - , link4 is right -
    link_1 = -1
    link_2 = -1
    link_3 = -1
    link_4 = -1
    default_value = [0,0,0,0]
    forward_value = [1,0,1,0]
    backward_value = [0,1,0,1]
    turn_left_value = [1,0,1,0]
    turn_right_value = [0,1,0,1]

    def __init__(self, ports):
        self.link_1 = ports[0]
        self.link_2 = ports[1]
        self.link_3 = ports[2]
        self.link_4 = ports[3]
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.link_1, gpio.OUT)
        gpio.setup(self.link_2, gpio.OUT)
        gpio.setup(self.link_3, gpio.OUT)
        gpio.setup(self.link_4, gpio.OUT)

    def intToGpio(self, i):
        print(i)
        if i == 0:
            return gpio.LOW
        else:
            return gpio.HIGH

    def setPort(self, values):
        index = 0
        gpio.output(self.link_1, self.intToGpio(values[index]))
        index += 1
        gpio.output(self.link_2, self.intToGpio(values[index]))
        index += 1
        gpio.output(self.link_3, self.intToGpio(values[index]))
        index += 1
        gpio.output(self.link_4, self.intToGpio(values[index]))

    def stop(self):
        self.setPort(self.default_value)

    def forward(self, t):
        self.setPort(self.forward_value)
        time.sleep(t)
        self.stop()

    def backward(self, t):
        self.setPort(self.backward_value)
        time.sleep(t)
        self.stop()

    def turn_left(self, t):
        self.setPort(self.turn_left_value)
        time.sleep(t)
        self.stop()

    def turn_right(self, t):
        self.setPort(self.turn_right_value)
        time.sleep(t)
        self.stop()

    def release_port(self):
        gpio.cleanup()
