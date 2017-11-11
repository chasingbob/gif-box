import RPi.GPIO as GPIO
from time import sleep

button = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    input_state = GPIO.input(button)
    if input_state == True:
        print('Button Pressed')
        
    sleep(0.2)

