#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# Die Nummerierung der Pins erfolgt 
# anhand der Position am Board
GPIO.setmode(GPIO.BOARD)

# LED an Pin 26
LEDPIN = 26 
 
# LEDPIN ist Ausgabe-Port
GPIO.setup(LEDPIN, GPIO.OUT)

for i in range(10):
	print("Schleifendurchgang ", i+1)
	GPIO.output(LEDPIN, GPIO.HIGH)
	print("An")
	time.sleep(0.5)
	GPIO.output(LEDPIN, GPIO.LOW)
	time.sleep(0.5)
	print("Aus")

GPIO.cleanup()


 
