import io 
from pytube import YouTube


def convertir_video(url):
    yt = YouTube(url)
    yt.streams.filter(res="1080p", fps="60fps")
    