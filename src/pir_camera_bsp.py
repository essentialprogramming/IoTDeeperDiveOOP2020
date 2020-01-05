
#!/usr/bin/python3
import picamera, sys, time
import RPi.GPIO as GPIO

PIR_PIN = 7
SLEEP_TIME = 10
LED_PIN = 26

GPIO.setmode(GPIO.BOARD)
cam = picamera.PiCamera()
cam.resolution = (1920, 1080)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

def bewegungsmeldung(pin):
		tme = time.strftime("%Y_%m_%d-%H:%M:%S")
		cam.capture("Foto-%s.jpg" %tme)
		GPIO.output(LED_PIN, GPIO.HIGH)
		print("Foto gespeichert")
		time.sleep(SLEEP_TIME)
		GPIO.output(LED_PIN, GPIO.LOW)
		return

GPIO.add_event_detect(PIR_PIN, GPIO.RISING)
GPIO.add_event_callback(PIR_PIN, bewegungsmeldung)

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
	cam.close()
	sys.exit()

