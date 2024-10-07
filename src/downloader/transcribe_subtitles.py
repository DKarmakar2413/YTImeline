import os

import pysrt

def extract_text_from_srt(file_path):
    subs = pysrt.open(file_path)
    transcript = " ".join([sub.text for sub in subs])
    return transcript



import srt

import webvtt

# Load a .vtt subtitle file
def extract_text_from_vtt(file_path):
    transcript = ""
    for caption in webvtt.read(file_path):
        transcript += caption.text + " "
    return transcript



import json

def extract_text_from_json3(file_path):
    transcript = ""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for entry in data.get('events', []):
            if 'segs' in entry:
                for segment in entry['segs']:
                    transcript += segment['utf8'] + " "
    return transcript




def extract_text_from_subtitle_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".vtt":
        return extract_text_from_vtt(file_path)
    elif ext == ".srt":
        return extract_text_from_srt(file_path)
    elif ext == ".json3":
        return extract_text_from_json3(file_path)
    else:
        raise ValueError(f"Unsupported subtitle format: {ext}")

# Check and prioritize subtitle formats
def get_transcript_from_subtitles(base_path, video_title):
    possible_extensions = ['.vtt', '.srt', '.json3']
    transcript = None

    # Search for subtitles in the preferred order
    for ext in possible_extensions:
        subtitle_file = os.path.join(base_path, f"{video_title}{ext}")
        if os.path.exists(subtitle_file):
            print(f"Found subtitle: {subtitle_file}")
            transcript = extract_text_from_subtitle_file(subtitle_file)
            break

    if transcript:
        return transcript
    else:
        raise FileNotFoundError(f"No suitable subtitle file found for {video_title} in {base_path}")

def save_transcript(transcript, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(transcript)

# Usage
transcript_text = get_transcript_from_subtitles("YTImeline/data/transcripts", "Dad Jokes | Don't laugh Challenge | Sam x Akila vs Andrew x Chloe | Raise Your Spirits")
save_transcript(transcript_text, "YTImeline/data/transcripts/example_video.txt")
