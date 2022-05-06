import time
import requests
import board
import adafruit_dht
 

dhtDevice = adafruit_dht.DHT11(board.D4)
url = "https://api.thingspeak.com/update"
api_key = "YOUR_API_KEY"

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.2f} C    Humidity: {}% ".format(temperature_c, humidity)
        payload = {'api_key' : api_key, 'field1' : temperature_c, 'field2': humidity}
        r = requests.get(url, params=payload)
    except RuntimeError as error:
   
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(2.0)
                   
