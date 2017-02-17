import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
print("Start")
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,GPIO.HIGH)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.HIGH)
GPIO.setup(19,GPIO.OUT)
GPIO.output(19,GPIO.HIGH)
for  num in range(0,5) :
    print("Number: ", num)
    time.sleep(1)
    GPIO.output(21,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    time.sleep(1)
    GPIO.output(21,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
print("End")
GPIO.output(21,GPIO.LOW)
GPIO.output(19,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
