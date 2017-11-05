from time import sleep
import os
import picamera
import pytumblr
from fractions import Fraction
import config

#create variables to hold commands 
makeVid = "convert -delay 50 image*.jpg animation.gif"

# AuthenticateS via OAuth, copy from https://api.tumblr.com/console/calls/user/info
client = pytumblr.TumblrRestClient(
  config.get_value('consumer_key'),
  config.get_value('consumer_secret'),
  config.get_value('token'),
  config.get_value('token_secret')
)

camera = picamera.PiCamera() #initiate picamera module and class
camera.resolution = (640, 480) #set resolution of picture here
camera.brightness = 60 #set brightness settings to help with dark photos
camera.annotate_foreground = picamera.Color(y=0.2, u=0, v=0) #set color of annotation 


#start camera preview                
camera.start_preview()

#display text over preview screen
camera.annotate_text = 'Get Ready!'
camera.annotate_text = '1'
#take 6 photos
for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
    sleep(0.75)
    if i == 1:
        camera.annotate_text = '2'
    elif i == 2:
        camera.annotate_text = '3'
    elif i == 3:
        camera.annotate_text = '4'
    elif i == 4:
        camera.annotate_text = '5'
    elif i == 5:
        camera.annotate_text = '6'
    elif i == 6:
        camera.annotate_text = '7'
    elif i == 7:
        camera.annotate_text = '8'
    elif i == 8:
        camera.annotate_text = '9'
    elif i == 9:
        camera.annotate_text = '10'
    if i == 10:
        break
camera.stop_preview() #stop preview 
os.system(makeVid) #send command to convert images to GIF
print('uploading') #let us know photo is about to start uploading

#upload photo to Tumblr
client.create_photo(
    'chasingbob',	#update to your username
	state="published",
	tags=["picamera", "raspberry pi"],
	data="animation.gif")

print("uploaded") #let us know GIF has been uploaded
            #turn on uploaded LED and play meow samples
