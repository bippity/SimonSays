##Lights up 3 LEDs when buttons are pressed

import RPi.GPIO as GPIO
import time

led1 = 12 ##GPIO18
led2 = 16 ##GPIO23
led3 = 36 ##GPIO16

button1 = 7 ##GPIO4
button2 = 11 ##GPIO17
button3 = 33 ##GPIO13

GPIO.setmode(GPIO.BOARD)

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

GPIO.setup(button1, GPIO.IN, GPIO.PUD_UP) ##Gives/turn on voltage for this pin
GPIO.setup(button2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, GPIO.PUD_UP)

'''def blink(number):
	if number == 1:
		GPIO.output(led1, True)
	else:
		GPIO.output(led1, False)

	if number == 2:
		GPIO.output(led2, True)
	else:
		GPIO.output(led2, False)
'''
while True:
	if GPIO.input(button1) == False:
		GPIO.output(led1, True)
	else:
		GPIO.output(led1, False)
	
	if GPIO.input(button2) == False:
		GPIO.output(led2, True)
	else:
		GPIO.output(led2, False)
	
	if GPIO.input(button3) == False:
		GPIO.output(led3, True)
	else:
		GPIO.output(led3, False)
	

##This part is never reached because it doesn't break out of while loop
print("Exit While loop")
GPIO.cleanup()
