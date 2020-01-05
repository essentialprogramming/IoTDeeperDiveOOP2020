#!/usr/bin/python3


from smbus2 import SMBus # i2c
import time


i2cbus = SMBus(1)
adr = 0x48

def read(cmd):
	write = i2cbus.write_byte_data(adr,cmd, 0)
	read = i2cbus.read_byte(adr)
	return read

print("Alle Ausgaben entsprechen Rohwerte von 0..255")

for i in range(100):
	licht = read(0x41)
	print("Lichtwiderstand " + str(licht))

	temp = read(0x42)
	print("Temperatur " + str(temp))

	ain2 = read(0x43)
	print("Analogeingang " + str(ain2))

	poti = read(0x40)
	print("Poti-Spannung  " + str(poti)) 

	time.sleep(2)
