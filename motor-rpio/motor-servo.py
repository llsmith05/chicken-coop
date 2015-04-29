import time
from RPIO import PWM

servo = PWM.Servo()

doorOpenPin = 17
doorClosePin = 18

def doorOpen():
	servo.set_servo(doorOpenPin, 1000)
	time.sleep(3.0)
	servo.stop_servo(doorOpenPin)

while True:
	try:
		print "beginning servo loop"
		doorOpen()
		time.sleep(5.0)
	except KeyboardInterrupt:
		break

servo.stop_servo(doorOpenPin)
PWM.cleanup()
