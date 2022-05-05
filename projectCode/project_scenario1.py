"""
	Author: Prakash Divakaran
	Code for IoT Fundamentals Project Scenario 1, only turns on LED
"""

import RPi.GPIO as GPIO
import time
import requests


api_key = "Write API Key here !" #update your API Key here


"""
Instructions:

	- Fill in the missing blank in line 63 with the appropriate code / value

"""

url = "https://api.thingspeak.com/update"
led_status = 0
GPIO.setmode(GPIO.BCM)

TRIG=23
ECHO=24
ledPin=26

print("Distance Measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(TRIG, False) 
GPIO.output(ledPin, GPIO.LOW)
print("Preparing sensor")
time.sleep(2)

while 1:
        #send wave
        GPIO.output(TRIG, True)
        time.sleep(0.00001) #10 microsecond delay
        GPIO.output(TRIG, False)

        #read wave
        while GPIO.input(ECHO)==0:
                pulse_start = time.time()

        while GPIO.input(ECHO)==1:
                pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = 34300 * pulse_duration/2

        distance = round(distance,2)

        print("Distance: ",distance, "cm")

        GPIO.output(TRIG, False)

        if distance < _______:
                led_status=1
                print("Object is too close")
                GPIO.output(ledPin, GPIO.HIGH)
        else:
                led_status=0
                print("No object detected")
                GPIO.output(ledPin, GPIO.LOW)

        #JSON payload
        payload = {'api_key':api_key, 'field1': distance, 'field2': led_status}
        requests.get(url, params=payload)
        time.sleep(2)
