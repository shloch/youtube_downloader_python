#Télécharger la bibliothèque pytube3  "pip install pytube3"
#Importer la bibliothèque "import pytube" 
#Copier le URL de la video Youtube "url = 'https://www.youtube.com/watch?v=5EurHP1DCJg'"
#Rediriger le ficher "video.download('/Downloads')"
from mhyt import yt_download
from urllib.request import urlopen

f = urlopen("Videos.txt")

yt_download(str(f.read(),'utf-8'))


