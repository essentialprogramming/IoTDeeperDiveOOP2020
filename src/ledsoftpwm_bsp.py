#!/usr/bin/python3
from time import sleep
import RPi.GPIO as GPIO 

PIN = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT) 

pwm=GPIO.PWM(PIN, 100);
pwm.start(0) 


maxreps = 10
repetitions = 0

while repetitions < maxreps:
	for i in range(0,100,4):
		pwm.ChangeDutyCycle(i)	
		sleep(0.1)
	for i in range(0,101,4):
		pwm.ChangeDutyCycle(100-i)
		sleep(0.1)	
	
	repetitions += 1

GPIO.cleanup


 
