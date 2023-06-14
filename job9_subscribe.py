import paho.mqtt.subscribe as subscribe
import json

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channel_ID = "<YOUR-CHANNEL-ID>"

# The hostname of the ThingSpeak MQTT broker.
mqtt_host = "mqtt3.thingspeak.com"

# Your MQTT credentials for the device
mqtt_client_ID = "<YOUR_CLIENT_ID>"
mqtt_username  = "<YOUR_USERNAME>"
mqtt_password  = "<YOUR_PASSWORD>"

# Create the topic string.
topic = "channels/" + channel_ID + "/subscribe"

while True:
        msg = subscribe.simple(topic, hostname=mqtt_host, client_id=mqtt_client_ID, auth={'username':mqtt_username, 'password':mqtt_password}) 
        msg2 = json.loads(msg.payload)
        print("The temperature is {0} degree C and humidity is {1} percent".format(msg2['field1'], msg2['field2']))

