import os
import yt_dlp

def download_playlist(playlist_url):
    ydl_opts_info = {
        "cookiefile": "cookies.txt",
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
        playlist_title = info_dict.get("title", "Playlist")

    playlist_folder = os.path.join("downloads", "playlists", playlist_title)
    os.makedirs(playlist_folder, exist_ok=True)

    ydl_opts_download = {
        "cookiefile": "cookies.txt",
        "outtmpl": os.path.join(playlist_folder, "%(title)s.%(ext)s"),
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "merge_output_format": "mp4",
        "ffmpeg_location": r"ffmpeg/ffmpeg.exe",
    }

    with yt_dlp.YoutubeDL(ydl_opts_download) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist_link = input("Enter the playlist link: ")
    download_playlist(playlist_link)
