import time
import requests
import board
import adafruit_dht
 

dhtDevice = adafruit_dht.DHT11(board.D4)
url = "https://api.thingspeak.com/update"


while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.2f} C    Humidity: {}% ".format(temperature_c, humidity$
        payload = {'api_key' : 'J7ZLU278U2M2XJJU', 'field1' : temperature_c, 'f$
        r = requests.get(url, params=payload)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(2.0)
                   
