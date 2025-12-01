# YouTube Private / Membership / Playlist Downloader

A simple Python tool for downloading:
- Private YouTube videos (using cookies)
- Membership-only videos
- Full playlists (each playlist gets its own folder)
- Highest quality MP4 (video + audio merged)

This tool uses **yt-dlp** + **FFmpeg**
No API key is required.

---

## Features

- Download private & members-only videos
- Playlist downloader with automatic folder creation
- Best quality MP4 merge
- Supports 720p / 1080p / 4K (if available)
- Works on Windows, Linux, macOS
- Only requires `cookies.txt`

---

## Installation

### 1. Install Python packages

```bash
pip install yt-dlp
```

---

## 2. Install FFmpeg

Download the **full build** from:

🔗 https://www.gyan.dev/ffmpeg/builds/

Download this file:

```
ffmpeg-git-full.7z
```

Extract the archive.  
Inside the extracted folder, open the **bin** directory and locate:

```
ffmpeg.exe
```

Copy this file into your project like this:

```
ffmpeg/
    ffmpeg.exe
```

Only **ffmpeg.exe** is required — you can ignore the other `.exe` files.


---

## Adding Cookies (Required for private/members-only videos)

Install this extension:
https://github.com/kairi003/Get-cookies.txt-Locally

Export cookies in **Netscape format**, then save as:

```
cookies.txt
```

Make sure `cookies.txt` is inside the project folder.

---

## ▶Usage

### Download a **single video**
```bash
python download_video.py
```

### Download a **playlist**
```bash
python download_playlist.py
```

---

## Output Structure

```
downloads/
   videos/
      video-name.mp4
   playlists/
      Playlist Name/
         video1.mp4
         video2.mp4
```

---

## Project Structure

```
YouTubeDownloader/
│
├── downloads/
│   ├── videos/
│   └── playlists/
│
├── ffmpeg/
│   └── ffmpeg.exe
│
├── cookies.txt
├── download_video.py
├── download_playlist.py
└── README.md
```
---
This project was created for users who want a simple, clean, and reliable way to download private, members-only, or full playlist videos from YouTube without dealing with complex tools or browser plugins.