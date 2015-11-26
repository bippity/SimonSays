import RPi.GPIO as GPIO
import time
import random

##Setting up LEDs/Buttons/
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
GPIO.setup(button1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, GPIO.PUD_UP)

#Instantialize highscore from text file
scoreFile = open("highscore.txt", "rw")
highscore = int(scoreFile.readline())
scoreFile.close()

gameOver = False
pattern = ""
userInput = ""
level = 1

def genPattern():
    global pattern
    pattern = ""
    for i in range(0, level):
        pattern += str(random.randint(1,3))

    print(pattern)

def playPattern():
    print("LEVEL: " + str(level))
    for i in pattern:
        print("Blinking LED " + i)
        blink(i)
    

def blink(number):
    if number == "1":
        GPIO.output(led1, True)
        time.sleep(.5)
        GPIO.output(led1, False)
    if number == "2":
        GPIO.output(led2, True)
        time.sleep(.5)
        GPIO.output(led2, False)
    if number == "3":
        GPIO.output(led3, True)
        time.sleep(.5)
        GPIO.output(led3, False)
    time.sleep(.3)

def waitForInput():
	global pattern
	global userInput
	while len(userInput) < len(pattern):
		if GPIO.input(button1) == False:
			userInput += "1"
			blink("1")
			print("LED 1 is pressed")
			time.sleep(.1)
		if GPIO.input(button2) == False:
			userInput += "2"
			blink("2")
			print("LED 2 is pressed")
			time.sleep(.1)
		if GPIO.input(button3) == False:
			userInput += "3"
			blink("3")
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


##Main function
while gameOver == False:
	begin()
	genPattern()
	playPattern()
	waitForInput()
	if checkInputMatch(userInput) == False:
		print("GAME OVER")
		print("Your score: " + str(level-1))
		if level > highscore:
			highscore = level-1
			scoreFile = open("highscore.txt", "rw+")
			scoreFile.seek(0,0)
			scoreFile.write(str(highscore))
		print("High Score: " + str(highscore))
		gameOver = True	
	else:
		level = level + 1
		GPIO.output(led1, True)
		GPIO.output(led2, True)
		GPIO.output(led3, True)
		time.sleep(1.5)
		GPIO.output(led1, False)
		GPIO.output(led2, False)
		GPIO.output(led3, False)
		
	userInput = ""
