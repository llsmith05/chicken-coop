import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

doorOpenPin = 17 #check that this is accurate
doorClosePin = 18 #same here


GPIO.setup(doorOpenPin, GPIO.OUT)
GPIO.setup(doorClosePin, GPIO.OUT)

chickenCount = 0
doorStatus = 0

def closeDoor(doorClosePin):
	print "Closing"
	#turn on door motor
	GPIO.output(doorClosePin,1)
	#wait a couple seconds for it to complete
	time.sleep(2.0)
	#turn off motor
	GPIO.output(doorClosePin,0)
	return None

def openDoor(doorOpenPin):
	print "Opening"
	#turn on door motor
	GPIO.output(doorOpenPin,1)
	#wait a couple seconds for it to complete
	time.sleep(2.0)
	#turn off motor
	GPIO.output(doorOpenPin,0)
	return None

while True:
	openDoor(doorOpenPin)
	time.sleep(10.0)
	closeDoor(doorClosePin)
	time.sleep(10.0)
