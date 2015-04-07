import RPi.GPIO as GPIO
import time
import Adafruit_MCP9808.MCP9808 as MCP9808

#pin numbers
proximity1Pin = 20
proximity2Pin = 16
lightPin = 26
doorOpenPin = 25 #check that this is accurate
doorClosePin = 11 #same here

# set pins to use GPIO numbering
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#pin setup
GPIO.setup(proximity1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(proximity2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(lightPin, GPIO.IN)
GPIO.setup(doorOpenPin, GPIO.OUT)
GPIO.setup(doorClosePin, GPIO.OUT)

#helpful global variables
proximity1 = 0
proximity2 = 0
chickenCount = 0
doorStatus = 0

#convert C to F for temp sensor
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

#temp sensor creation and initialization
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

def lightStatus(lightPin):
	#Read light level and return 1 for dark, 0 for light
	return 1

def closeDoor(doorClosePin):
	#turn on door motor
	GPIO.output(doorClosePin,1)
	#wait a couple seconds for it to complete
	time.sleep(2.0)
	#turn off motor
	GPIO.output(doorClosePin,0)
	return None

def openDoor(doorOpenPin):
	#turn on door motor
	GPIO.output(doorOpenPin,1)
	#wait a couple seconds for it to complete
	time.sleep(2.0)
	#turn off motor
	GPIO.output(doorOpenPin,0)
	return None

#proximity
GPIO.add_event_detect(proximity1Pin, GPIO.BOTH, callback=proximity1, bouncetime=300)
GPIO.add_event_detect(proximity2Pin, GPIO.BOTH, callback=proximity2, bouncetime=300)



while True:
	if (chickenCount == 5 && lightStatus() == 1 && doorStatus = 0)
		closeDoor()
		doorStatus = 1
	if (lightStatus() == 0 && doorStatus = 1)
		openDoor()
		doorStatus = 0
	time.sleep(60.0)

GPIO.cleanup()
