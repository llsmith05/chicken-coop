import RPi.GPIO as GPIO
import time
import Adafruit_MCP9808.MCP9808 as MCP9808

#convert C to F for temp sensor
def c_to_f(c):
	return c * 9.0 / 5.0 + 32.0

# set pins to use GPIO numbering
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

# IO pin variables
ir_pin_inner = 13
ir_pin_outer = 19

#temp sensor
sensor = MCP9808.MCP9808()
sensor.begin()

# set up pins
GPIO.setup(ir_pin_inner, GPIO.IN)
GPIO.setup(ir_pin_outer, GPIO.IN)

#read temp sensor
def getTemp():
    return temp

while True:
    temp = sensor.readTemp()
#    print 'Temp is {1:0.3F}*F'.format(temp, c_to_f(temp))
