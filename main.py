from pytube import YouTube

def download_ytvid_as_mp3():
    video_url = input("Enter the URL of the YouTube video: ")
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    filename = f"{yt.title}.mp3"
    video.download(filename=filename)
    print(f"Download complete: {filename}")

download_ytvid_as_mp3()
