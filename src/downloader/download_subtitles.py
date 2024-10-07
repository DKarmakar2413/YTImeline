import subprocess

def download_subtitles(video_url, save_path, preferred_lang="en"):
    """
    Downloads subtitles for a given YouTube video URL in .vtt format.

    Parameters:
    video_url (str): The URL of the YouTube video.
    save_path (str): The directory path where subtitles will be saved.
    preferred_lang (str): Language code for the subtitles (default: 'en').

    Returns:
    str: Path to the downloaded subtitle file, if successful.
    """
    # Create a command for downloading subtitles
    command = [
        "yt-dlp",
        "--sub-lang", preferred_lang,  # Preferred subtitle language (e.g., 'en' for English)
        "--write-sub",                 # Download subtitles
        "--skip-download",             # Skip downloading the actual video
        "--sub-format", "vtt",         # Preferred subtitle format
        "-o", f"{save_path}/%(title)s.%(ext)s",  # Save with the video title name
        video_url
    ]

    try:
        # Run the command using subprocess
        subprocess.run(command, check=True)
        print(f"Subtitles downloaded successfully for {video_url}")
        return save_path
    except subprocess.CalledProcessError as e:
        print(f"Failed to download subtitles: {e}")
        return None
