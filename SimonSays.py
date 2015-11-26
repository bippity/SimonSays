import RPi.GPIO as GPIO
import time
import random
import os

##Setting up LEDs/Buttons
led1 = 12 ##GPIO18
led2 = 16 ##GPIO23
led3 = 36 ##GPIO16
button1 = 7 ##GPIO4
button2 = 11 ##GPIO17
button3 = 33 ##GPIO13

try:
	gameOver = False
	pattern = ""
	userInput = ""
	level = 1

	##Initializes the GPIO pins and creates highscore.txt if nonexistent
	def initialize():
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(led1, GPIO.OUT)
		GPIO.setup(led2, GPIO.OUT)
		GPIO.setup(led3, GPIO.OUT)
		GPIO.setup(button1, GPIO.IN, GPIO.PUD_UP)
		GPIO.setup(button2, GPIO.IN, GPIO.PUD_UP)
		GPIO.setup(button3, GPIO.IN, GPIO.PUD_UP)
		if os.path.isfile("highscore.txt") == False:
			scoreFile = open("highscore.txt", "w+")
			scoreFile.write(str(0))
	
	##Generates a random pattern for lights to blink
	def genPattern():
    		global pattern
    		pattern = ""
    		for i in range(0, level):
        		pattern += str(random.randint(1,3))

   		##print(pattern)
	
	##Plays the pattern with a delay of "s" seconds
	def playPattern(s, delay):
    		for i in pattern:
        		##print("Blinking LED " + i)
        		if delay == True:
				blink(i, s)
			else:
				noDelayBlink(i, s)
    
	##Blinks the specified LED for "s" seconds and a delay after finishing
	def blink(number, s):
    		if number == "1":
        		GPIO.output(led1, True)
        		time.sleep(s)
        		GPIO.output(led1, False)
    		if number == "2":
        		GPIO.output(led2, True)
        		time.sleep(s)
        		GPIO.output(led2, False)
    		if number == "3":
        		GPIO.output(led3, True)
        		time.sleep(s)
        		GPIO.output(led3, False)
    		time.sleep(.2)
	##Does the same as blink() except no delay at the end
	def noDelayBlink(number, s):
		if number =="1":
			GPIO.output(led1, True)
			time.sleep(s)
			GPIO.output(led1, False)
		if number == "2":
			GPIO.output(led2, True)
			time.sleep(s)
			GPIO.output(led2, False)
		if number == "3":
			GPIO.output(led3, True)
			time.sleep(s)
			GPIO.output(led3, False)

	##Awaits for the player's/button input
	def waitForInput():
		global pattern
		global userInput
		while len(userInput) < len(pattern):
			if GPIO.input(button1) == False:
				userInput += "1"
				blink("1", .2)
				print("LED 1 is pressed")
				time.sleep(.1)
			if GPIO.input(button2) == False:
				userInput += "2"
				blink("2", .2)
				print("LED 2 is pressed")
				time.sleep(.1)
			if GPIO.input(button3) == False:
				userInput += "3"
				blink("3", .2)
				print("LED 3 is pressed")
				time.sleep(.1)

	##Display a 3-2-1 pattern to show that level is about to start
	def begin():
		GPIO.output(led1, True)
		GPIO.output(led2, True)
		GPIO.output(led3, True)
		time.sleep(1)
		GPIO.output(led3, False)
		time.sleep(1)
		GPIO.output(led2, False)
		time.sleep(1)
		GPIO.output(led1, False)
		time.sleep(1)

	##Convert the patterns into integers and compare
	def checkInputMatch(input):
		global pattern
		userPattern = int(input)
		genPattern = int(pattern)
		return userPattern == genPattern
	
	##Plays a "success" pattern -flashes all lights twice
	def playSuccess():
		GPIO.output(led1, True)
		GPIO.output(led2, True)
		GPIO.output(led3, True)
		time.sleep(.1)
		GPIO.output(led1, False)
		GPIO.output(led2, False)
		GPIO.output(led3, False)
		time.sleep(.1)
		GPIO.output(led1, True)
		GPIO.output(led2, True)
		GPIO.output(led3, True)
		time.sleep(.1)
		GPIO.output(led1, False)
		GPIO.output(led2, False)
		GPIO.output(led3, False)
		time.sleep(.1)
		
	##Plays a random pattern showing that the player failed
	def playFail():
		global level
		level = 20
		genPattern()
		playPattern(.05, False)

	##Main function
	initialize()
	while gameOver == False:
		print("LEVEL: " + str(level))
		begin()
		genPattern()
		playPattern(.5, True)
		waitForInput()
		if checkInputMatch(userInput) == False:
			print("GAME OVER")
			print("Your score: " + str(level-1))
		
			##Initialize highscore from text file
			scoreFile = open("highscore.txt", "rw+")
			highscore = int(scoreFile.readline())

			if level > highscore:
				highscore = level-1
				scoreFile.seek(0,0)
				scoreFile.write(str(highscore))
			print("High Score: " + str(highscore))
			scoreFile.close()
			playFail()
			gameOver = True	
		else:
			level = level + 1
			playSuccess()
		
		userInput = ""

##Cleans up GPIO pins/board when program exits
finally:
	GPIO.cleanup()
