import paho.mqtt.client as mqtt

# Einen Client kreieren
client = mqtt.Client("node")

# Mit dem lokalen Broker an Port 1883 verbinden:
client.connect("localhost")

# topic ist die Nachrichtenwarteschlange, der zweite Parameter der payload
# Parameter 3: QoS (0: at most once 1: at least once 2: exactly once)
# Parameter 4: retained? (diese Nachrich wird jedem Subscriber auf jeden Fall
# zugesandt)

client.publish("oop2020/test", "Diese Nachricht bekommen alle zu sehen", 1, True)
client.publish("oop2020/test", "Hallo liebe Tutorialbesucher", 1, False)
client.publish("oop2020/test", "Ich hoffe, alle geniessen die Arbeit", 1, False)

