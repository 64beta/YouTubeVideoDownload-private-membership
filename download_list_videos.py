import os
import yt_dlp

os.makedirs("downloads/listVideos", exist_ok=True)

def get_ydl_opts():
    return {
        "cookiefile": "cookies.txt",
        "outtmpl": "downloads/listVideos/%(title)s.%(ext)s",
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "merge_output_format": "mp4",
        "ffmpeg_location": r"ffmpeg/ffmpeg.exe",
        "ratelimit": None,
        "skip_unavailable_fragments": False,
    }

def download_single_video(url):
    while True:
        try:
            with yt_dlp.YoutubeDL(get_ydl_opts()) as ydl:
                ydl.download([url])
            print(f"\n✓ Finished: {url}")
            break

        except Exception as e:
            print("\n----------------------------------")
            print("Token / Cookie expired OR error:")
            print(e)
            print("----------------------------------")

            answer = input("Should I continue if You have changed my cookies? (y/n): ").lower()

            if answer == "n":
                print("exit()")
                exit()

            print("continue...\n")

def download_from_file(file_path):
    if not os.path.exists(file_path):
        print("links.txt not found!")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        links = [line.strip() for line in f if line.strip()]

    print(f"{len(links)} links found. Starting...\n")

    for idx, url in enumerate(links, start=1):
        print(f"\n▶️  {idx}. Downloading video:")
        print(url)
        download_single_video(url)


if __name__ == "__main__":
    download_from_file("links.txt")
