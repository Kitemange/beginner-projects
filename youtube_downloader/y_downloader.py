import youtube_dl

#create a youtube downloader dictionary ydl_opts
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
    'outtmpl': '%(title)s.%(ext)s',
}
tdl = youtube_dl.YoutubeDL(ydl_opts)

#download the video
url=input("Enterthe url to the youtube video: ")
tdl.download([url])
