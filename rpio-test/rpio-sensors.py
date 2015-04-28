import RPIO
import time

#pin numbers
proximity1Pin = 16
proximity2Pin = 20

# set pins to use GPIO numbering
RPIO.setmode(RPIO.BCM)
#GPIO.setwarnings(False)

#pin setup
RPIO.setup(proximity1Pin, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(proximity2Pin, RPIO.IN, pull_up_down=RPIO.PUD_UP)

#helpful global variables
proximity1 = False #0 or 1 if sensor is triggered
proximity2 = False #0 or 1 if sensor is triggered
chickenCount = 0 #current number of chickens in coop




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


	

#def proximity2_callback(gpio_id, val):
#	global proximity2
#	proximity2 += 1
#	print("gpio %s: %s\n" % (gpio_id, val))
#	#print "proximity2: " + str(proximity2)




RPIO.add_interrupt_callback(proximity1Pin, proximity1_callback, threaded_callback=True, debounce_timeout_ms=200)

RPIO.add_interrupt_callback(proximity2Pin, proximity2_callback, threaded_callback=True, debounce_timeout_ms=200)




#add_interrupt_callback(gpio_id, callback, edge='both', pull_up_down=RPIO.PUD_OFF, threaded_callback=False, debounce_timeout_ms=None)
#print str(RPIO.sysinfo())
#print str(RPIO.version())



while True:
	try:
		print "Beginning count check loop"
		print "Current chicken count is " + str(chickenCount)
		print "proximity 1: " + str(proximity1)
		print "proximity 2: " + str(proximity2)
		RPIO.wait_for_interrupts(threaded=True)
		time.sleep(10.0)

#clean up GPIO usage when you quit with ctrl+C
	except KeyboardInterrupt:
		break

RPIO.cleanup()
