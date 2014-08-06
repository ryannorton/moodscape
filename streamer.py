from twython import TwythonStreamer
from datetime import datetime
import os
import pytz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MoodScape.settings')
from app.models import Tweet

class MyStreamer(TwythonStreamer):
    
    # counts each tweet - used for debugging   
    count = 0
    
    def on_success(self, data):
        
        # only include tweets with all necessary data
        if ('coordinates' in data 
            and 'user' in data
            and data['user']['screen_name'] is not None 
            and data['coordinates'] is not None
        ):
            # view progress in console - used for debugging
            print self.count, data['coordinates']['coordinates']
            
            self.count += 1
            
            # create and store tweet object in database
            Tweet.objects.get_or_create(
                text=data['text'], 
                lat=data['coordinates']['coordinates'][0], 
                lon=data['coordinates']['coordinates'][1],
                user='@' + data['user']['screen_name'], 
                date=datetime.now(tz=pytz.timezone("America/Denver"))
            )

            # collect n number of tweets - used for testing
            if self.count >= 100:	
            	self.disconnect()

    def on_error(self, status_code, data):
        print status_code

def main():

    # extract keys for Twitter API authorization
    keyfile = open('appkeys.txt')
    keys = keyfile.read().split('\n')
    keyfile.close()
    APP_KEY = keys[0]
    APP_SECRET = keys[1]
    OAUTH_TOKEN = keys[2]
    OAUTH_TOKEN_SECRET = keys[3]
    
    # initialize Twitter's public streaming API
    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
    # only include tweets with location data
    stream.statuses.filter(locations='-180,-90,180,90')

main()

