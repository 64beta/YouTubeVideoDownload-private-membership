import os
import yt_dlp

os.makedirs("downloads/videos", exist_ok=True)

def download_video(url):
    ydl_opts = {
        "cookiefile": "cookies.txt",
        "outtmpl": "downloads/videos/%(title)s.%(ext)s",
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "merge_output_format": "mp4",
        "ffmpeg_location": r"ffmpeg/ffmpeg.exe",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_link = input("Enter the video link: ")
    download_video(video_link)
