import settings
from twitter import *
from requests_oauthlib import OAuth1Session
from samplebase import SampleBase
from rgbmatrix import graphics
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import subprocess
import re
from datetime import datetime

def create_oath_session():
    oath = OAuth1Session(
    settings.consumer_key,
    settings.consumer_secret,
    settings.access_token,
    settings.access_secret
    )
    return oath


def clock(self):
    offscreen_canvas = self.matrix.CreateFrameCanvas()
    font = graphics.Font()
    font_time = graphics.Font()
    # font.LoadFont("../../../fonts/mplus_h12r.bdf")
    font_time.LoadFont("./fonts/21-Adobe-Helvetica.bdf")
    # font.LoadFont("../../../fonts/15-Adobe-Helvetica.bdf")
    font.LoadFont("./fonts/16-Adobe-Helvetica-Bold.bdf")

    timeColor = graphics.Color(61, 147, 215)
    d = datetime.now()
    time_text = d.strftime("%H:%M")
    # logger.debug(my_text)
    offscreen_canvas.Clear()
    # len = graphics.DrawText(offscreen_canvas, font, 4, 12, textColor, date_text)
    len1 = graphics.DrawText(offscreen_canvas, font_time, 14, 30, timeColor, time_text)

    # time.sleep(0.01)
    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


if __name__ == '__main__':
    oauth = OAuth(settings.access_token,settings.access_secret,settings.consumer_key,settings.consumer_secret)
    tw_api = Twitter(auth=oauth)
    friends = tw_api.friends.ids(screen_name='Sw_Saturn',count=500)
    friends_ids = ','.join(map(str, friends['ids']))

    stream = TwitterStream(auth=oauth, secure=True)
    for tweet in stream.statuses.filter(follow=friends_ids):
        clock()
        #print(tweet['text'])
        if 'user' in tweet and tweet['user']['id'] in friends['ids']:
            #with open('tweet.txt','w')as f:
            #    f.write('@'+tweet['user']['screen_name']+' '+tweet['text'])
            twText = tweet['user']['name']+' @'+tweet['user']['screen_name']+' '+tweet['text']+' '
            twText = re.sub('\n', " ", twText)
            twText=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", twText)
            subprocess.call('sudo convert -background none +antialias -fill "#9057FF" -font /usr/share/fonts/truetype/jfdot/JF-Dot-jiskan16s.ttf -pointsize 16 -gravity north label:"{0}" /home/pi/rpi-clock/tw.png'.format(twText),shell=True)
            #subprocess.call('sudo convert -background none +antialias -fill "#b09bd1" -font /usr/share/fonts/opentype/A-OTF-ShinGoPro-Regular.otf -pointsize 28 -gravity north label:"{0}" /home/pi/rpi-clock/tw.png'.format(twText),shell=True)
            subprocess.call('sudo python3 image-scroller.py --led-no-hardware-pulse 1 --led-chain=4 -i tw.png -b 80',shell=True)
