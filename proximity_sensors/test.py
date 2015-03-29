import RPi.GPIO as GPIO
import time

#pin numbers
proximity1Pin = 23
proximity2Pin = 24

#helpful global variables
proximity1 = 0
proximity2 = 0
chickenCount = 0

#setup
GPIO.setmode(GPIO.BCM)

#detecting low voltage (movement detection)
GPIO.add_event_detect( proximity1Pin, GPIO.FALLING, callback=proximity1Low )
GPIO.add_event_detect( proximity2Pin, GPIO.FALLING, callback=proximity2Low )

#detecting high voltage (chicken past sensor)
GPIO.add_event_detect( proximity1Pin, GPIO.RISING, callback=proximity1High )
GPIO.add_event_detect( proximity2Pin, GPIO.RISING, callback=proximity2High )

#callback function for sensor1
def proximity1Low(proximity1Pin):
	proximity1 += 1

	#proximity1 hit first
	if proximity1 > proximity2:
		#wait for chicken to hit proximity2:
		t = time.clock()
		while True:
			if proximity2 == 1:
				break
			if (t-time.clock()) >= 10:
				break

		#wait for the High functions to reset global variables
		t = time.clock()
		while True:
			if ( proximity1 == 0 && proximity2 == 0 ):
				chickenCount -= 1
				break
			if (t-time.clock()) >= 10:
				break
				


		#case chicken hits proximity2 => wait for both sensors to read high, decrement chickenCount
		#case chicken walks away =>
		#case false detection =>
	
def proximity2Low(proximity2Pin):
	proximity2 += 1

	#proximity2 hit first
	if proximity2 > proximity1:
		#wait for chicken to hit proximity1:
		t = time.clock()
		while True:
			if proximity1 == 1:
				break
			if (t-time.clock()) >= 10:
				break

		#wait for the High functions to reset global variables
		t = time.clock()
		while True:
			if ( proximity1 == 0 && proximity2 == 0 ):
				chickenCount += 1
				break
			if (t-time.clock()) >= 10:
				break



		#case chicken hits proximity1 => wait for both sensors to read high, increment chickenCount
		#case chicken walks away =>
		#case false detection =>
def proximity1High(proximity1Pin):
	proximity1 -= 1

def proximity2High(proximity2Pin):
	proximity2 -= 1	
	
GPIO.cleanup()

if __name__ == "__main__":
