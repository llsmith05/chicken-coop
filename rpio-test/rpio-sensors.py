import RPIO
import time

#pin numbers
proximity1Pin = 16
proximity2Pin = 21

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
	proximity1 += 1
	print("gpio %s: %s\n" % (gpio_id, val))
	print "proximity1: " + str(proximity1)

def proximity2_callback(gpio_id, val):
	proximity2 += 1
	print("gpio %s: %s\n" % (gpio_id, val))
	print "proximity2: " + str(proximity2)

x = [4, 17, 18, 27, 22, 23, 24, 25, 5, 12, 6, 13, 19, 26, 16, 20, 21]
def findthepin():
	while x != []:
		i = x.pop()
		RPIO.add_interrupt_callback(i, proximity1_callback, threaded_callback=True, debounce_timeout_ms=10)
		RPIO.add_interrupt_callback(i, proximity2_callback, threaded_callback=True, debounce_timeout_ms=10)



#add_interrupt_callback(gpio_id, callback, edge='both', pull_up_down=RPIO.PUD_OFF, threaded_callback=False, debounce_timeout_ms=None)
print str(RPIO.sysinfo())
print str(RPIO.version())
findthepin()
while True:
	try:
		print "Beginning count check loop"
		print "Current chicken count is " + str(chickenCount)
		print "proximity 1: " + str(proximity1)
		print "proximity 2: " + str(proximity2)
		time.sleep(10.0)

#clean up GPIO usage when you quit with ctrl+C
	except KeyboardInterrupt:
		break

RPIO.cleanup()
