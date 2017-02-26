#!/usr/bin/python

# Import required Python libraries
import RPi.GPIO as GPIO
import time
pinList = [2]
def runOff():
    # Use BCM GPIO references instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # init list with pin numbers



    # loop through pins and set mode and state to 'low'

    for i in pinList:
        GPIO.setwarnings(False)
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)
    try:
        trigger()


    except KeyboardInterrupt:

      # Reset GPIO settings
      GPIO.cleanup()
    return "Turned Light Off"

def trigger() :
        for i in pinList:
          GPIO.output(i, GPIO.HIGH)
#         GPIO.cleanup()
          break
