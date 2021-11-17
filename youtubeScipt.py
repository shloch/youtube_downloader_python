from mhyt import yt_download
import os

def already_download(fileName):
    directory_files = os.listdir()
    return (fileName in directory_files)

def launch_download():
    try:
        with open('config.videos.txt') as f:
            urls = f.readlines()
            print(urls)
            for url in urls:
                coupleUrlNom = url.split(' ')
                if(already_download(coupleUrlNom[1].strip()) == False):  
                    print()    
                    print('------- downloading '  + coupleUrlNom[1].strip() + '--------')
                    try:
                        yt_download(coupleUrlNom[0],coupleUrlNom[1].strip())
                    except:
                        print("Connection Error") #to handle exception
                else:
                    print()
                    print('- ' + coupleUrlNom[1].strip() + ' <==== Already Downloaded')
        f.close()
    except:
         print("File opening Error")

'''
def rename_files():
    all_files = os.listdir()
    for f in all_files:
        split_names = f.split('\n')
        if (len(split_names) > 1):
            try:
                os.rename(f, split_names[0])
            except:
                print("could not rename file " + f)
'''


launch_download()

