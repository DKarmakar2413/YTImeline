from pathlib import Path

# Define paths
base_path = "YTImeline/data/subtitles"
Path(base_path).mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist

# Sample YouTube video URL
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download subtitles
download_subtitles(video_url, base_path)


# video title 
import subprocess
import os

def get_video_title_from_url(url):
    # Use yt-dlp to get the video title
    command = f'yt-dlp --get-title {url}'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.strip() if result.returncode == 0 else None

# Call the function to get the title from a YouTube video URL
video_url = "https://www.youtube.com/watch?v=abc123"
video_title = get_video_title_from_url(video_url)
print("Extracted Video Title:", video_title)

# Use the title to search for subtitle files
transcript = get_transcript_from_subtitles("YTImeline/data/transcripts", video_title)
