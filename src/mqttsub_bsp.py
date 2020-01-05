import paho.mqtt.client as mqtt

# Callback für Verbindungsaufbau
def on_connect(client, userdata, flags, rc):
    print("Verbindung aufgebaut mit Fehlercode " + str(rc))
    client.subscribe("oop2020/test")

# Callback für Nachrichtenempfang
def on_message(client, userdata, msg):
    print("Neue Nachricht im Topic " + msg.topic + "   Inhalt: " + str(msg.payload))

# MQTT Client anlegen
client = mqtt.Client()
# Callbackhandler zuweisen
client.on_connect = on_connect
client.on_message = on_message

# Verbindung zum Broker aufbauen
client.connect("localhost", 1883, 60)

# Auf eingehende Nachrichten warten
client.loop_forever()
