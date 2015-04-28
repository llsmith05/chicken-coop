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
proximity1 = 0 #0 or 1 if sensor is triggered
proximity2 = 0 #0 or 1 if sensor is triggered
chickenCount = 0 #current number of chickens in coop




def proximity1_callback(gpio_id, val):
	global proximity1
	proximity1 += 1
	print("gpio %s: %s\n" % (gpio_id, val))

def proximity2_callback(gpio_id, val):
	global proximity2
	proximity2 += 1
	print("gpio %s: %s\n" % (gpio_id, val))
	#print "proximity2: " + str(proximity2)




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
