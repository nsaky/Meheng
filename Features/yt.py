import urllib.request
import re
import webbrowser
from pytube import YouTube

def search_yt(keyword):
    try:
        url="https://www.youtube.com/results?search_query="+keyword
        webbrowser.open(url)
        return f"Searching on Youtube, {keyword}"
    except:
        return "Problem Searching that on YouTube, at the moment"

def get_video_url(keyword):
    html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+keyword)
    video_ids=re.findall(r"watch\?v=(\S{11})",html.read().decode())
    url=("https://www.youtube.com/watch?v="+video_ids[0])
    return url

def play_yt_video(keyword):
    try:
        webbrowser.open(get_video_url(keyword))
        keyword=keyword.replace("_"," ")
        return f"Playing Youtube Video on the topic of {keyword}"
    except:
        return "Problem Playing that video on YouTube, at the moment."
