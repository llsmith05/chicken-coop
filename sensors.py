import RPi.GPIO as GPIO
import time
import Adafruit_MCP9808.MCP9808 as MCP9808

#pin numbers
proximity1Pin = 23
proximity2Pin = 24

# set pins to use GPIO numbering
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#pin setup
GPIO.setup(proximity1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(proximity2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#helpful global variables
proximity1 = 0
proximity2 = 0
chickenCount = 0

#convert C to F for temp sensor
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0


#temp sensor
sensor = MCP9808.MCP9808()
sensor.begin()

#read temp sensor
def getTemp():
        temp = sensor.readTempC()
        return temp

#callback function for sensor1
def proximity1(proximity1Pin):
	if GPIO.input(proximity1Pin):
		print "No object at sensor 1"
	else:
		print "Object detected at sensor 1"
def proximity2(proximity2Pin):
	if GPIO.input(proximity2Pin):
		print "No object at sensor 2"
	else:
		print "Object detected at sensor 2"

#proximity
GPIO.add_event_detect(proximity1Pin, GPIO.BOTH, callback=proximity1)
GPIO.add_event_detect(proximity2Pin, GPIO.BOTH, callback=proximity2)



while True:
       print "."
       time.sleep(1.0)

GPIO.cleanup()
