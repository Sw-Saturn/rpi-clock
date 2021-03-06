import settings
from twitter import *
from requests_oauthlib import OAuth1Session
# from samplebase import SampleBase
# from rgbmatrix import graphics
# from rgbmatrix import RGBMatrix, RGBMatrixOptions
import subprocess
import re
import time
from datetime import datetime

def create_oath_session():
    oath = OAuth1Session(
    settings.consumer_key,
    settings.consumer_secret,
    settings.access_token,
    settings.access_secret
    )
    return oath



if __name__ == '__main__':
    oauth = OAuth(settings.access_token,settings.access_secret,settings.consumer_key,settings.consumer_secret)
    tw_api = Twitter(auth=oauth)
    friends = tw_api.friends.ids(screen_name='Sw_Saturn',count=500)
    friends_ids = ','.join(map(str, friends['ids']))
    init = True
    stream = TwitterStream(auth=oauth, secure=True)
    for tweet in stream.statuses.filter(track=["#kosenconf"]):
        #print(tweet['text'])
        # if 'user' in tweet and tweet['user']['id'] in friends['ids']:
        #with open('tweet.txt','w')as f:
        #    f.write('@'+tweet['user']['screen_name']+' '+tweet['text'])
        twText = tweet['user']['name']+' @'+tweet['user']['screen_name']+' '+tweet['text']+' '
        twText = re.sub('\n', " ", twText)
        twText=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", twText)
        subprocess.call('sudo convert -background none +antialias -fill "#9057FF" -font /usr/share/fonts/truetype/jfdot/JF-Dot-jiskan16s.ttf -pointsize 16 -gravity north label:"{0}" /home/pi/rpi-clock/tw.png'.format(twText),shell=True)
        #subprocess.call('sudo convert -background none +antialias -fill "#b09bd1" -font /usr/share/fonts/opentype/A-OTF-ShinGoPro-Regular.otf -pointsize 28 -gravity north label:"{0}" /home/pi/rpi-clock/tw.png'.format(twText),shell=True)
        if not init:
            proc.wait()
        proc = subprocess.Popen('sudo python3 image-scroller.py --led-no-hardware-pulse 1 --led-chain=4 -i tw.png -b 80'.split(),shell=False)
        init = False
