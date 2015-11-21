'''Reaction.py
This is called the Reaction Game. 
http://www.raspberrypi.org/learning/python-quick-reaction-game/worksheet/
'''

import RPi.GPIO as GPIO
import time
import random


##Gets the 2 players' names
left_name = raw_input('Left player name is ')
right_name = raw_input('Right player name is ')

names = [left_name, right_name]

GPIO.setmode(GPIO.BOARD)
##GPIO.setwarnings(False)

led = 16
right_button = 32
left_button = 7

GPIO.setup(led, GPIO.OUT)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)

GPIO.output(led, True)
time.sleep(5)
GPIO.output(led, False)

while True:
	if GPIO.input(left_button) == False:
		print(names[0] + " won")
		break
	if GPIO.input(right_button) == False:
		print(names[1] + " won")
		break

GPIO.cleanup()
