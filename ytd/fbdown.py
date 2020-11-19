from __future__ import unicode_literals
import youtube_dl
import json

with youtube_dl.YoutubeDL() as ydl:
    url = ydl.extract_info('https://www.youtube.com/watch?v=JaO6fPA99Hg&t=1450s&ab_channel=iCoder', download=False)
    print(url["formats"][-1]["url"])
