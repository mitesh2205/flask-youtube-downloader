#importing the module
import pytube

# import pytube

url = 'https://www.youtube.com/watch?v=3lhQX5GvMe8&ab_channel=MusicHub'

youtube = pytube.YouTube(url)
videos = youtube.streams
i = 0
for video in videos:
    print(str(i+ " " + str(video)))
    i+=1

stream_num = int(input("Enter Stream Number:"))
download_video = videos[stream_num -1]
download_video.download()

print("video is downloaded")
