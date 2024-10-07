import whisper

model = whisper.load_model("base")  # You can choose "small", "medium", "large", etc. based on your needs.
print("Model loaded. Checking device...")
print(f"Device: {model.device}")
