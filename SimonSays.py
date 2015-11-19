import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) ##GPIO pin 4
GPIO.setup(33, GPIO.OUT) ##GPIO pin 27
GPIO.setup(15, GPIO.OUT) ##GPIO pin 22

pattern = ""
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
    levelUp()
    

def blink(number):
    if number == "1":
        GPIO.output(7, True)
        time.sleep(.5)
        GPIO.output(7, False)
    if number == "2":
        GPIO.output(33, True)
        time.sleep(.5)
        GPIO.output(33, False)
    if number == "3":
        GPIO.output(15, True)
        time.sleep(.5)
        GPIO.output(15, False)
    time.sleep(.5)

def levelUp():
    global level
    level = level + 1

genPattern()
playPattern()
genPattern()
playPattern()
genPattern()
playPattern()
genPattern()
playPattern()
genPattern()
playPattern()

GPIO.cleanup()
