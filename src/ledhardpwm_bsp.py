#!/usr/bin/python3
import wiringpi
import time

PIN = 12

wiringpi.wiringPiSetupPhys()

wiringpi.pinMode(PIN,2)

maxreps = 10
repetitions = 0

while repetitions < maxreps:
	for i in range(0,1001,50):
		wiringpi.pwmWrite(PIN, i)
		time.sleep(0.1)
	for i in range(0,1001,50):
		wiringpi.pwmWrite(PIN, 1000-i)
		time.sleep(0.1)	
	
	repetitions += 1

wiringpi.pwmWrite(PIN,0)



 
