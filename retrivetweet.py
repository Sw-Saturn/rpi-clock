import settings
from twitter import *
from requests_oauthlib import OAuth1Session
import subprocess
import re

def create_oath_session():
    oath = OAuth1Session(
    settings.consumer_key,
    settings.consumer_secret,
    settings.access_token,
    settings.access_secret
    )
    return oath


def tweetReply(oath,text):
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    params = {'status': text}
    req = oath.post(url,params)
    if req.status_code == 200:
        print('tweet succeed!')
        print(text)
    else:
        print('tweet failed')


def init():
    tw_id = "dmz_ai"
    return Twitter(auth=OAuth(settings.access_token,settings.access_secret,settings.consumer_key,settings.consumer_secret)),tw_id


if __name__ == '__main__':
    oauth = OAuth(settings.access_token,settings.access_secret,settings.consumer_key,settings.consumer_secret)
    tw_api = Twitter(auth=oauth)
    friends = tw_api.friends.ids(screen_name='Sw_Saturn',count=50)
    friends_ids = ','.join(map(str, friends['ids']))

    stream = TwitterStream(auth=oauth, secure=True)
    for tweet in stream.statuses.filter(follow=friends_ids):
        print(tweet['text'])
        if 'user' in tweet and tweet['user']['id'] in friends['ids']:
            #with open('tweet.txt','w')as f:
            #    f.write('@'+tweet['user']['screen_name']+' '+tweet['text'])
            twText = tweet['user']['name']+' @'+tweet['user']['screen_name']+' '+tweet['text']+' '
            twText = re.sub('\n', " ", twText)
            subprocess.call('sudo convert -background black -fill white -font /usr/share/fonts/truetype/jfdot/JF-Dot-jiskan24.ttf -pointsize 26 label:"{0}" /home/pi/rpi-clock/tw.jpg'.format(twText),shell=True)
            subprocess.call('sudo python3 image-scroller.py --led-no-hardware-pulse 1 --led-chain=4 -i tw.jpg -b 80',shell=True)
