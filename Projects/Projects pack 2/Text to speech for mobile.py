from gtts import gTTS
import os

# Input text to be spoken
text_to_speak = input("Enter text to convert to speech: ")

# Create a gTTS object
tts = gTTS(text=text_to_speak, lang="en")

# Save the speech as an MP3 file
tts.save("output.mp3")

# Play the saved MP3 file
os.system("mpv output.mp3")
