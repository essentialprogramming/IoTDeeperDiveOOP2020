#!/usr/bin/python3

import sys
from time import sleep
import RPi.GPIO as GPIO

# Zeit, während der die LED leuchtet
SLEEP_TIME = 10 
# Verwendete LED an Pin 26
LEDPIN = 26

# Verwendet werden die physikalischen Pins
GPIO.setmode(GPIO.BOARD)
# LEDPIN ist Ausgabeport
GPIO.setup(LEDPIN, GPIO.OUT)

# Pin 7 greift den Status des PIR-Sensors ab
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Callback bei Statusänderungen am PIR 
def bewegung_erkannt(pin):
	print("Bewegung registriert")
	# LED an bei Bewegungserkennung
	GPIO.output(LEDPIN, GPIO.HIGH)
	sleep(SLEEP_TIME)
	GPIO.output(LEDPIN, GPIO.LOW)
	return

# Auslösung der Ereignisse durch 
# aufsteigende Signalflanken
GPIO.add_event_detect(7, GPIO.RISING)
GPIO.add_event_callback(7, bewegung_erkannt)

print("CONTROL-C beendet das Programm")
try:
	while True: # Enbdlosschleife
		sleep(0.5)
except KeyboardInterrupt: # Schleifenende bei Interrupt
	GPIO.cleanup() 
	sys.exit()


