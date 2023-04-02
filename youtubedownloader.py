from pytube import YouTube
import calendar
import time

current_GMT = time.gmtime()
isnextvideo = True
newfile = "DownloadedYoutubeVid"+str(calendar.timegm(current_GMT))+".txt"

while (isnextvideo):
    link=input("Paste the link of the Youtube video you want to download: ")
    yt = YouTube(link)
    yt.streams.get_highest_resolution().download(output_path="./DownloadedVideos")

    Downloaded_video = {"author": yt.author,
                    "Title": yt.title,
                      }
    f = open(newfile,"a")
    f.write("Author: "+yt.author)
    f.write("Description: "+yt.title)
    print("Downloaded videos can be found in /DownloadedVideos... Thanks!")
    newvideo =input("Do you want to download another video? (y/n): ")
    #Condition to know if the download of more videos is requested
    if newvideo == "y":
        isnextvideo= True
    else:
        isnextvideo = False
        

