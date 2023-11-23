# convert text to speech
import pyttsx3
# object
engine = pyttsx3.init()

# see your computer voice options
"""
for voice in engine.getProperty("voices"):
    print(voice)
"""

voices = engine.getProperty("voices")
engine.saveProperty("voice", voices[1].id)

# function to convert text to speech

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

# input
text = input("Enter text convert to speech: ")

# calling the function
Speak(text)


