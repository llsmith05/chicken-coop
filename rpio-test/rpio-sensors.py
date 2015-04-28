import RPIO
import time

#pin numbers
proximity1Pin = 20
proximity2Pin = 20

# set pins to use GPIO numbering
#RPIO.setmode(RPIO.BCM)
#GPIO.setwarnings(False)

#pin setup
RPIO.setup(proximity1Pin, RPIO.IN)
#RPIO.setup(proximity2Pin, RPIO.IN, pull_up_down=RPIO.PUD_UP)

#helpful global variables
proximity1 = 0 #0 or 1 if sensor is triggered
proximity2 = 0 #0 or 1 if sensor is triggered
chickenCount = 0 #current number of chickens in coop




def proximity1_callback(proximity1, val):
	proximity1 += 1
	print("gpio %s: %s\n" % (gpio_id, val))



RPIO.add_interrupt_callback(proximity1Pin, proximity1_callback, edge='rising', pull_up_down=RPIO.PUD_UP, threaded_callback=True, debounce_timeout_ms=200)







#add_interrupt_callback(gpio_id, callback, edge='both', pull_up_down=RPIO.PUD_OFF, threaded_callback=False, debounce_timeout_ms=None)





while True:
	try:
		print "Beginning count check loop"
		print "Current chicken count is " + str(chickenCount)

		time.sleep(10.0)

#clean up GPIO usage when you quit with ctrl+C
	except KeyboardInterrupt:
		RPIO.cleanup()
		break
