# coding: UTF-8
from dotenv import load_dotenv
load_dotenv(verbose=True)

import os

consumer_key= os.getenv("consumer_key") # 環境変数の値をAPに代入
consumer_secret=os.getenv("consumer_secret")
access_token=os.getenv("access_token")
access_secret=os.getenv("access_secret")
