#pip install putybe

from pytube import YouTube
 
youtube_video_url = 'https://www.youtube.com/watch?v=RnXYmCXX9dw&ab_channel=DevNB'
 
try:
    yt_obj = YouTube(youtube_video_url)
 
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
 
    # download the highest quality video
    filters.get_highest_resolution().download()
    print('La video a bien ete telecharger ')
except Exception as e:
    print(e)
    download(output_path='le chemin a stocker la video', filename='yt_video.mp4')