import pytumblr
import config

# Authenticates via OAuth, copy from https://api.tumblr.com/console/calls/user/info
client = pytumblr.TumblrRestClient(
    config.get_value('consumer_key'),
    config.get_value('consumer_secret'),
    config.get_value('token'),
    config.get_value('token_secret')
)

client.create_photo(
    config.get_value('user_name'), 
    state="published",
    tags=["raspberrypi", "picamera"],
    data="mmm.gif"
)
print("uploaded")