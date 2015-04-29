import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

m = GPIO.PWM(17, 50)

m.start(40)
time.sleep(2.0)
m.ChangeDutyCycle(60)
time.sleep(3.0)
m.stop()

GPIO.output(17, 0)

GPIO.cleanup()
