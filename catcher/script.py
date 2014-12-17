import time
from datetime import date
import picamera
import RPi.GPIO as GPIO

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
# Set GPIO to output
GPIO.setup(32, GPIO.OUT, initial=False)

camera = picamera.PiCamera()

n = 1

while (n < 10000) :
	now = time.strftime("%d-%m-%Y--%H:%M:%S")
	name = "catch-" + now + ".jpg"
	camera.capture("out/" + name)
	n+=1
	time.sleep(5)

