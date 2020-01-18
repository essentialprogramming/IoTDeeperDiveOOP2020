#!/usr/bin/python3
# Mehr Info zu gpiozero auf https://gpiozero.readthedocs.io
from gpiozero import LED 
from time import sleep

# Die Nummerierung der Pins erfolgt 
# anhand der Position am Board

led = LED(26) 
 
for i in range(10):
	print("Schleifendurchgang ", i+1)
	led.on()	
	print("An")
	sleep(0.5)
	led.off()
	sleep(0.5)
	print("Aus")

