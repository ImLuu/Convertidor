from pytube import YouTube

url = "https://www.youtube.com/watch?v=WPTap0YCWI8"
yt = YouTube(url)
yt = yt.streams.get_audio_only()
yt.download()
