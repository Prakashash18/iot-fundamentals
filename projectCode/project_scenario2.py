"""
	Author: Prakash Divakaran
	Code for IoT Fundamentals Project Scenario 2, turns on LED and buzzes buzzer
	
	Instructions:

	- Fill in the missing blanks in line 29, 36, 69, 74, 81 with the appropriate code / value

"""

import RPi.GPIO as GPIO
import time
import requests


api_key = "Write API Key here !" #update your API Key here

url = "https://api.thingspeak.com/update"
led_status = 0
buzzer_status = 0
GPIO.setmode(GPIO.BCM)

TRIG=23
ECHO=24
ledPin=26
buzzerPin = ____

print("Distance Measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(__________, GPIO.OUT)


GPIO.output(TRIG, False) 
GPIO.output(ledPin, GPIO.LOW)
GPIO.output(buzzerPin, GPIO.LOW)

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
                buzzer_status=1
                print("Object is too close")
                GPIO.output(ledPin, GPIO.HIGH)
                GPIO.output(buzzerPin, __________)

        else:
                led_status=0
                buzzer_status=0
                print("No object detected")
                GPIO.output(ledPin, GPIO.LOW)
                GPIO.output(buzzerPin, __________)


        #JSON payload
        payload = {'api_key':api_key, 'field1': distance, 'field2': led_status, 'field3':buzzer_status}
        requests.get(url, params=payload)
        time.sleep(2)
