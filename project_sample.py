"""
	Author: Prakash Divakaran
	Code for IoT Fundamentals Project Scenario, turns on LED and buzz the buzzer
	
	Instructions:
	 -There are 15 blanks in this code. Fill them up with the appropriate value/code and run this code to get the 
	- The blanks are at lines 16, 17, 19, 27, 30, 36, 37, 66, 67, 68, 70, 71, 74, 75, 78
"""

import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

TRIG = ______
ECHO = ________
ledPin=26
buzzerPin = _______

url = "https://api.thingspeak.com/update"
api_key = "YOUR_API_KEY" #update your API Key here


print("Distance Measurement in progress")

GPIO.setup(TRIG, _________)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(__________, GPIO.OUT)


GPIO.output(TRIG, False) 
GPIO.output(ledPin, GPIO.LOW)
GPIO.output(buzzerPin, GPIO.LOW)
led_status = _______
buzzer_status = ______


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

        print "Distance: ",distance, "cm"

        GPIO.output(TRIG, False)

        if distance < _______:
                led_status = _____
                buzzer_status = _________
                print("Object is too close")
                GPIO.output(ledPin, ________)
                GPIO.output(buzzerPin, __________)

        else:
                led_status= ______
                buzzer_status= _________
                print("No object detected")
                GPIO.output(ledPin, GPIO.LOW)
                GPIO.output(buzzerPin, __________)


        #JSON payload
        payload = {'api_key':api_key, 'field1': distance, 'field2': "", 'field3':""}
        requests.get(url, params=payload)
        time.sleep(2)
