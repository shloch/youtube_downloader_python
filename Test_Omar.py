#Télécharger la bibliothèque pytube3  "pip install pytube3"
#Importer la bibliothèque "import pytube" 
#Copier le URL de la video Youtube "url = 'https://www.youtube.com/watch?v=5EurHP1DCJg'"
#Rediriger le ficher "video.download('/Downloads')"
from os import close
from mhyt import yt_download

with open('Videos.txt') as f:
    lines = f.readlines()
    #print(lines)
    yt_download(lines[0],lines[1])
close()
#yt_download(str(f.read(),'utf-8'))


