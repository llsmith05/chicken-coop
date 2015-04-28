import RPi.GPIO as GPIO
import time

#pin numbers
proximity1Pin = 23
proximity2Pin = 24

#helpful global variables
proximity1 = False
proximity2 = False
chickenCount = 0

#setup
GPIO.setmode(GPIO.BCM)

#callback function for sensor1
def proximity1_callback(proximity1Pin):
	#object not detected
	if GPIO.input(proximity1Pin):
		#reset the global variable 
		proximity1 = False #or should it be !proximity1 ?
		print "decrementing proximity1"

	#object detected
	else:
		#increment the proximity 1 variable
		proximity1 = True
		print "incrementing proximity1"
		exception = False

		#proximity1 hit first
		if (proximity1 == True && proximity2 == False):
			#wait for chicken to hit proximity2:
			print "waiting for proximity2 to trigger..."
			t = time.time()
			while True:
				if proximity2 == True:
					print "proximity 2 triggered"
					print "now waiting for both sensors to reset"
					break
				#only wait for 10s, and throw an exception
				if (t-time.time()) >= 10:
					exception = True
					print "you took too long to activate proximity2, throwing exception"
					break

			#wait for the High functions to reset global variables
			t = time.time()
			while True:
				#don't do anything to chickenCount if there was an exception
				if ( exception ):
					print "exception detected... exiting proximity1 callback function"
					break
				#wait for both sensors to reset their variables
				if ( proximity1 == False && proximity2 == False ):
					#this indicates a chicken leaving
					print "both sensors were reset! decrementing chickencount"
					chickenCount -= 1
					break
				#only wait for 10s, throw exception
				if (t-time.time()) >= 10:
					exception = True
					print "you took too long to reset the sensors, throwing exception"
					break
		
def proximity2_callback(proximity2Pin):
	#object not detected
	if GPIO.input(proximity2Pin):
		#reset the global variable >>> this is probably bad
		proximity2 = False
		print "decrementing proximity2"

	#object detected
	else:
		#increment the proximity 2 variable
		proximity2 = True
		print "incrementing proximity 2"
		exception = False

		#proximity2 hit first
		if (proximity2 == True && proximity1 == False):
			#wait for chicken to hit proximity1:
			print "waiting for proximity1 to trigger..."
			t = time.time()
			while True:
				if proximity1 == True:
					print "proximity 1 triggered"
					print "now waiting for both sensors to reset"
					break
				#only wait for 10s, and throw an exception
				if (t-time.time()) >= 10:
					exception = True
					print "you took too long to activate proximity1, throwing exception"
					break

			#wait for the High functions to reset global variables
			t = time.time()
			while True:
				#don't do anything to chickenCount if there was an exception
				if ( exception ):
					print "exception detected in proximity2 callback...exiting"
					break
				#wait for both sensors to reset their variables
				if ( proximity1 == False && proximity2 == False ):
					#this indicates a chicken entering
					print "both variables were reset, incrementing chickenCount"
					chickenCount += 1
					break
				#only wait for 10s, throw exception
				if (t-time.time()) >= 10:
					exception = True
					print "took too long to reset the sensors...exiting proximity2 callback
					break

#detecting change in voltage (movement through sensor)
GPIO.add_event_detect(proximity1Pin, GPIO.BOTH, callback=proximity1_callback, bouncetime=300)
GPIO.add_event_detect(proximity2Pin, GPIO.BOTH, callback=proximity2_callback, bouncetime=300)






	
GPIO.cleanup()

if __name__ == "__main__":
