import RPi.GPIO as GPIO
from time import sleep
import os

import picamera
import pytumblr
from fractions import Fraction
import config

#create variables to hold commands 
make_vid = "convert -delay 50 image*.jpg animation.gif"

yellow_led = 27
red_led = 17
button = 18


print('setup...')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)

# AuthenticateS via OAuth, copy from https://api.tumblr.com/console/calls/user/info
client = pytumblr.TumblrRestClient(
    config.get_value('consumer_key'),
    config.get_value('consumer_secret'),
    config.get_value('token'),
    config.get_value('token_secret')
)

print('camera...')

camera = picamera.PiCamera() #initiate picamera module and class
camera.resolution = (640, 480) #set resolution of picture here
camera.brightness = 60 #set brightness settings to help with dark photos


print('ready...')

try:
    while True:
        input_state = GPIO.input(button)
        if input_state == True:
            print('Button Pressed')
            sleep(0.2)
            #if pressed blink yellow LED at two speeds
            for i in range(3):
                GPIO.output(yellow_led, True)
                sleep(1)
                GPIO.output(yellow_led, False)
                sleep(1)
            for i in range(3):
                GPIO.output(yellow_led, True)
                sleep(.25)
                GPIO.output(yellow_led, False)
                sleep(.25)

            print('taking gif')

            for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
                sleep(0.75)
                if i == 6:
                    break

            print('done taking gif')

            for i in range(2):
                GPIO.output(red_led, True)
                sleep(.25)
                GPIO.output(red_led, False)
                sleep(.25)
            
            os.system(make_vid) #send command to convert images to GIF

            client.create_photo(
                    'chasingbob',
            	    state="published",
            	    tags=["picamera", "raspberry pi", "test"],
            	    data="animation.gif")

            print('done uploading...')

            for i in range(2):
                GPIO.output(red_led, True)
                sleep(.25)
                GPIO.output(red_led, False)
                sleep(.25)

        

except KeyboardInterrupt:
    print('Program stopped')