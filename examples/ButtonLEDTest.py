import RPi.GPIO as GPIO
import time

led = 18 ##GPIO24
button = 7 ##GPIO4

GPIO.setmode(GPIO.BOARD)
##GPIO.output(led, False) ##Initialize everything (Make sure everything is off first)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP) ##Gives/turn on voltage for this pin

while True:
	if GPIO.input(button) == False:
		print("Button pressed")
		GPIO.output(led, True)
	else:
		GPIO.output(led, False)
	

print("Exit While loop")
GPIO.cleanup()
