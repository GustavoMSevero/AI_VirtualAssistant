import pyttsx3 # pip install pyttxs3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hi! i'm JARVIS, an virtual assistant.")