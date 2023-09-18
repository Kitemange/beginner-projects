from pytube import YouTube
import webbrowser


#create a youtube object
url = input("Place the url you want to download: ")
#The 'yt'object is created by passing te video url as argument to the youtube constructor
yt = YouTube(url)

#Download the video
print('Downloading...')  #Printing this so that it is visible while downloading.
#open youtube video while downloading for confirmation
webbrowser.open(url)
video_stream= yt.streams.filter(progressive=True).first().download()   #Filtering for progressive streams only and getting first one
