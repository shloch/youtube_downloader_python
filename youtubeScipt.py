from mhyt import yt_download
import os


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


def rename_files():
    all_files = os.listdir()
    print(all_files)
    for f in all_files:
        split_names = f.split('\n')
        if (len(split_names) > 1):
            try:
                os.rename(f, split_names[0])
            except:
                print("could not rename file " + f)


#os.rename('geeks.txt', 'PythonGeeks.txt')
rename_files()

