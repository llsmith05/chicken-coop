#import RPi.GPIO as GPIO
import RPIO
import time
import Adafruit_MCP9808.MCP9808 as MCP9808
from flask import Flask, render_template, url_for

app = Flask(__name__)

#pin numbers
proximity1Pin = 20
proximity2Pin = 16
doorOpenPin = 17
doorClosePin = 18

# set pins to use RPIO numbering
RPIO.setmode(RPIO.BCM)
#RPIO.setwarnings(False)

#pin setup
RPIO.setup(proximity1Pin, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(proximity2Pin, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(doorOpenPin, RPIO.OUT)
RPIO.setup(doorClosePin, RPIO.OUT)

#helpful global variables
proximity1 = False #False if object not detected, True if object detected
proximity2 = False #False if object not detected, True if object detected
chickenCount = 0 #current number of chickens in coop
doorStatus = 0 #0 for closed, 1 for open

#convert C to F for temp sensor
#Returns as Fahrenheit int
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

#temp sensor creation and initialization
sensor = MCP9808.MCP9808()
sensor.begin()

#read temp sensor
#returns temp in Celsius as int
def getTemp():
        temp = sensor.readTempC()
        return temp

#callback function for sensor1
def proximity1_callback(gpio_id, val):
	global proximity1
	global proximity2
	global chickenCount

	exception = False

	#object not detected
	if(val == 1):
		#reset the corresponding global variable
		proximity1 = False
		print "reseting proximity1"

	#object detected
	#NOTE: think about putting '&& proximity1 == False' in the conditional
	elif(val == 0):
		#indicate a change in state
		proximity1 = True
		print "\nproximity1 activated; changing state variable\n"

		#proximity1 hit first
		if( proximity1 == True and proximity2 == False ):
			
			#wait for chicken to trigger proximity2
			print "waiting for proximity2 to trigger..."
			t = time.time()
			while True:
				if( proximity2 == True ):
					print "\nproximity2 triggered\n"
					print "now waiting for both sensors to reset"
					break
				if( (time.time()-t) >= 5 ):
					exception = True
					print "took to long to activate proximity2, throwing exception"
					break

			#wait for the globals to reset
			t = time.time()
			while True:
				#don't do anything to chickenCount if exception
				if( exception ):
					print "exception detected, exiting proximity1_callback"
					break

				#wait for both sensors to reset their variables
				if( proximity1 == False and proximity2 == False ):
					print "both sensors were reset! decrementing chickenCount"
					chickenCount -= 1
					break

				#only wait 5 sec
				if( (time.time()-t) >= 5 ):
					exception = True
					print "took too long to reset the sensors, throwing exception"
					break
	else:
		exception = True

	if(exception == True):
		proximity1 = False
		proximity2 = False

		
#sensor 2 callback function
def proximity2_callback(gpio_id, val):
	global proximity1
	global proximity2
	global chickenCount

	exception = False

	#object not detected
	if(val == 1):
		#reset the corresponding global variable
		proximity2 = False
		print "reseting proximity2"

	#object detected
	#NOTE: think about putting '&& proximity2 == False' in the conditional
	elif(val == 0):
		#indicate a change in state
		proximity2 = True
		print "\nproximity2 activated; changing state variable\n"

		#proximity2 hit first
		if( proximity2 == True and proximity1 == False ):
			
			#wait for chicken to trigger proximity1
			print "waiting for proximity1 to trigger..."
			t = time.time()
			while True:
				if( proximity1 == True ):
					print "\nproximity1 triggered\n"
					print "now waiting for both sensors to reset"
					break
				if( (time.time()-t) >= 5 ):
					exception = True
					print "took to long to activate proximity1, throwing exception"
					break

			#wait for the globals to reset
			t = time.time()
			while True:
				#don't do anything to chickenCount if exception
				if( exception ):
					print "exception detected, exiting proximity2_callback"
					break

				#wait for both sensors to reset their variables
				if( proximity2 == False and proximity1 == False ):
					print "both sensors were reset! incrementing chickenCount"
					chickenCount += 1
					break

				#only wait 5 sec
				if( (time.time()-t) >= 5 ):
					exception = True
					print "took too long to reset the sensors, throwing exception"
					break
	else:
		exception = True

	if( exception == True ):
		proximity1 = False
		proximity2 = False


def closeDoor(doorClosePin):
	#turn on door motor
	RPIO.output(doorClosePin,1)
	#wait a couple seconds for it to complete
	time.sleep(0.5)
	#turn off motor
	RPIO.output(doorClosePin,0)
	return None

def openDoor(doorOpenPin):
	#turn on door motor
	RPIO.output(doorOpenPin,1)
	#wait a couple seconds for it to complete
	time.sleep(0.5)
	#turn off motor
	RPIO.output(doorOpenPin,0)
	return None

def getCount():
	return chickenCount

def getDoorStatus():
	return doorStatus

#interrupt detection for both IR sensors
RPIO.add_interrupt_callback(proximity1Pin, proximity1_callback, threaded_callback=True, debounce_timeout_ms=200)

RPIO.add_interrupt_callback(proximity2Pin, proximity2_callback, threaded_callback=True, debounce_timeout_ms=200)


#################################
#NOT SURE WHERE THIS SHOULD GO
RPIO.wait_for_interrupts(threaded=True)


@app.route("/")
def coophome():
	#get temperature
	temp = c_to_f(getTemp())
	chickens = getCount()
	door = getDoorStatus()
	#pass temp, chickens and door to the HTML template
	return render_template('main.html', temp=temp, chickenCount=chickens, doorStatus=door)

@app.route("/door")
def doorToggle():
	global doorStatus
	if (doorStatus == 0):
		#if door is closed, open it
		openDoor(doorOpenPin);
		print "Opening door"
		#set status as open
		doorStatus = 1
		#returning to console for debugging
		return "Opened!"
	else:
		#if door is open
		closeDoor(doorClosePin);
		print "Closing door"
		#set status
		doorStatus = 0
		#returning to console for debugging
		return "Closed!"

#run Flask app; replace debug=True with host='0.0.0.0' for external server access
if __name__ == "__main__":
	app.run(host='0.0.0.0')

# while True:
# 	print "Beginning count check loop"
# 	print "Current chicken count is " + str(chickenCount)
# 	if (doorStatus == 1):
# 		print "Opening door"
# 		openDoor(doorOpenPin)
# 		doorStatus = 0

# 	if (chickenCount >= 5 and doorStatus == 0):
# 		print "Closing door"
# 		closeDoor(doorClosePin)
# 		doorStatus = 1
# 	time.sleep(10.0)

#clean up RPIO usage when you quit with ctrl+C
#except KeyboardInterrupt:
RPIO.cleanup()
