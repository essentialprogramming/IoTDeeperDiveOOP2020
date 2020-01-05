# ThingSpeak Update Using MQTT
# Copyright 2016, MathWorks, Inc

# This is an example of publishing to multiple fields simultaneously.
# Connections over standard TCP, websocket or SSL are possible by setting
# the parameters below.
#
# CPU and RAM usage is collected every 20 seconds and published to a
# ThingSpeak channel using an MQTT Publish
#
# This example requires the Paho MQTT client package which
# is available at: http://eclipse.org/paho/clients/python

from __future__ import print_function
import paho.mqtt.publish as publish

from bme280 import readBME280All
from time import sleep

###   Start of user configuration   ###   

#  ThingSpeak Channel Settings

# The ThingSpeak Channel ID
# Replace this with your Channel ID
channelID = "<< Dein Channel ID >>"

# The Write API Key for the channel
# Replace this with your Write API key
apiKey = "<< Dein API Key >>"

#  MQTT Connection Methods

# Set useUnsecuredTCP to True to use the default MQTT port of 1883
# This type of unsecured MQTT connection uses the least amount of system resources.
useUnsecuredTCP = True

# Set useUnsecuredWebSockets to True to use MQTT over an unsecured websocket on port 80.
# Try this if port 1883 is blocked on your network.
useUnsecuredWebsockets = False

# Set useSSLWebsockets to True to use MQTT over a secure websocket on port 443.
# This type of connection will use slightly more system resources, but the connection
# will be secured by SSL.
useSSLWebsockets = False

###   End of user configuration   ###

# The Hostname of the ThinSpeak MQTT service
mqttHost = "mqtt.thingspeak.com"

# Set up the connection parameters based on the connection type
if useUnsecuredTCP:
    tTransport = "tcp"
    tPort = 1883
    tTLS = None

if useUnsecuredWebsockets:
    tTransport = "websockets"
    tPort = 80
    tTLS = None

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    tPort = 443
        
# Create the topic string
topic = "channels/" + channelID + "/publish/" + apiKey

# Run a loop which calculates the system performance every
#   20 seconds and published that to a ThingSpeak channel
#   using MQTT.
while(True):
   
 
    # get the system performance data
    
    temperature, pressure, humidity = readBME280All();
    # build the payload string
    print ("Temperature in C %5.2f  Humidity in Percentage %5.2f  Air Pressure in hPa %5.2f" %(temperature, humidity, pressure))
    tPayload = "field1=" + str(temperature) + "&field2=" + str(humidity) + "&field3=" + str(pressure)
    # attempt to publish this data to the topic 
    try:
        publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)

    except (KeyboardInterrupt):
        break
    except:     
        pass 
