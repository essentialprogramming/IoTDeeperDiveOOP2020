#!/usr/bin/python3

import sys
from time import sleep
import RPi.GPIO as GPIO
import requests

# Leuchtdauer bei Bewegungserkennung
LED_ON_TIME = 10 
# Verwendete LED
LEDPIN = 26
# PIR Sensor
PIRPIN = 7

# Verwendet werden die physikalischen Pins
GPIO.setmode(GPIO.BOARD)
# Keine Warnungen wie "Port ist bereits belegt"
GPIO.setwarnings(False)
# LEDPIN ist Ausgabeport
GPIO.setup(LEDPIN, GPIO.OUT)

# PIRPIN greift den Status des PIR-Sensors ab
GPIO.setup(PIRPIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Ereignisbehandlung, wenn Bewegung erkannt
def bewegung_erkannt(pin):
	print("Bewegung registriert")
        # Code fuer IFTTT-Post
	data = requests.post("https://maker.ifttt.com/trigger/bewegungerkannt/with/key/<< eigener Key >>")
	print (data.text) 	
	# LED an bei Bewegungserkennung
	GPIO.output(LEDPIN, GPIO.HIGH)
	sleep(LED_ON_TIME)
	GPIO.output(LEDPIN, GPIO.LOW)
	return

# Ausloesung der Ereignisse durch 
# aufsteigende Signalflanken
GPIO.add_event_detect(PIRPIN, GPIO.RISING)
GPIO.add_event_callback(PIRPIN, bewegung_erkannt)


print("CONTROL-C beendet das Programm")

try:
	while True: # Endlosschleife
		sleep(0.5)
except KeyboardInterrupt: # Schleifenende bei Interrupt
	GPIO.cleanup() 
	sys.exit()


