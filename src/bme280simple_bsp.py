from bme280 import readBME280All
from time import sleep

print( "---- STARTEN DER MESSWERTERFASSUNG VOM BME280 ----")
while True:

	temperature,pressure,humidity = readBME280All()
	print( "Temperatur : " + str(temperature) + " C" )
	print( "Luftdruck : " + str(pressure) + " hPa" )
	print( "Feuchtigkeit : " + str(humidity) + " %" )
	print( "--------------------------------------------------" );
	sleep(2)
