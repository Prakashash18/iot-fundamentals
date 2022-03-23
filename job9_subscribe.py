import paho.mqtt.subscribe as subscribe
import json

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channel_ID = "1682262"

# The hostname of the ThingSpeak MQTT broker.
mqtt_host = "mqtt3.thingspeak.com"

# Your MQTT credentials for the device
mqtt_client_ID = "DBcuBQM8BSkgOCYmKiEQPSc"
mqtt_username  = "DBcuBQM8BSkgOCYmKiEQPSc"
mqtt_password  = "Al6WOpe+WiH12NjlCTKEvITY"

# Create the topic string.
topic = "channels/" + channel_ID + "/subscribe"

while True:
        msg = subscribe.simple(topic, hostname=mqtt_host, client_id=mqtt_client$
        msg2 = json.loads(msg.payload)
        print("The temperature is {0} degree C and humidity is {1} percent".for$

