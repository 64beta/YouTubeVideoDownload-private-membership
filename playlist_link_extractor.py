import yt_dlp

def extract_playlist_links(playlist_url):
    ydl_opts = {
        "cookiefile": "cookies.txt",
        "extract_flat": True,
        "skip_download": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)

    entries = info.get("entries", [])
    video_links = [f"{e['url']}" for e in entries if "url" in e]
    return video_links


def save_links_to_file(links, filename="links.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")


if __name__ == "__main__":
    playlist_url = input("Enter playlist URL: ")
    links = extract_playlist_links(playlist_url)
    save_links_to_file(links)
