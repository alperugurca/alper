import sys
import yt_dlp


def needmusic(url=None):
    """Download audio from YouTube video."""
    url = url or (sys.argv[1] if len(sys.argv) > 1 else None)
    if not url:
        print("Usage: needmusic <youtube_url>")
        return
    ydl_opts = {"format": "bestaudio/best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def needvideo(url=None):
    """Download video from YouTube."""
    url = url or (sys.argv[1] if len(sys.argv) > 1 else None)
    if not url:
        print("Usage: needvideo <youtube_url>")
        return
    ydl_opts = {"format": "best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])