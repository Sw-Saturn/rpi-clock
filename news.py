import subprocess
import feedparser

RSS_URL = "https://www3.nhk.or.jp/rss/news/cat0.xml"

news = feedparser.parse(RSS_URL)
#print(news)

for entry in news.entries:
    title = entry.title
    summary  = entry.summary
    #print(title)
    #print(summary)
    out = title+' '
    subprocess.call('sudo convert -background black -fill "#e8ad35" -font /usr/share/fonts/truetype/jfdot/JF-Dot-jiskan24.ttf -pointsize 30 label:"{0}" /home/pi/rpi-clock/news.png'.format(out),shell=True)
    subprocess.call('sudo python3 image-scroller.py --led-chain=1 --led-cols=64 -i news.png -b 80 --led-no-hardware-pulse 1',shell=True)
