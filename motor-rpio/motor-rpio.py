import RPIO
from RPIO import PWM
import time


#check that these are right
doorOpenPin = 17
doorClosePin = 18

#only BCM numbering is supported; also, there's no setmode function
#RPIO.setmode(RPIO.BCM)

###############
##Avoid channels 0, 1, 2, 3, 6, 7. The GPU uses 1, 3, 6, 7. The frame buffer uses 0 and the SD card uses 2.
##channels 4,5 okay
##can we just use one channel?
##default subcycle time is 20 ms

PWM.setup()
PWM.init_channel(4, subcycle_time_us=20000)

#RPIO.setup(doorOpenPin, RPIO.OUT)
#RPIO.setup(doorClosePin, RPIO.OUT)

PWM.cleanup()
