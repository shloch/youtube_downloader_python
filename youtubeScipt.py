from mhyt import yt_download

try:
    with open('config.videos.txt') as f:
        urls = f.readlines()
        print(urls)
        for url in urls:
            coupleUrlNom = url.split(' ')
            print('-------> downloading '  + coupleUrlNom[1])
            try:
                yt_download(coupleUrlNom[0],coupleUrlNom[1])
            except:
                print("Connection Error") #to handle exception
    f.close()
except:
     print("File opening Error")

