import pytube
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc'

youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download('../Video')