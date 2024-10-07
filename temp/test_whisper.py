import whisper

# Load the Whisper model (choose a smaller model if limited resources)
model = whisper.load_model("base")  # Options: tiny, base, small, medium, large

# Transcribe the sample audio file
result = model.transcribe("C:\MY FILES\ASMR.mp3")

# Print the transcribed text and word-level timestamps
print("Transcribed Text:\n", result['text'])
print("\nWord-level Timestamps:\n", result['segments'])
