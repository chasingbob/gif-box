import RPi.GPIO as GPIO
from time import sleep

button = 18

while True:
    input_state = GPIO.input(button)
    if input_state == True:
        print('Button Pressed')
        
    sleep(0.2)

