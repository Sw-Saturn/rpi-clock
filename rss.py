import feedparser

RSS_NIKKEI="https://assets.wor.jp/rss/rdf/nikkei/news.rdf"
feed = feedparser.parse(RSS_NIKKEI)

for i in feed.entries:
    title = i.title
    print(title)