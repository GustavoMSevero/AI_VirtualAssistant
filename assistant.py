import pyttsx3 # pip install pyttxs3
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def timeNow():
    time = datetime.datetime.now().strftime("%I:%M")
    speak(time)

def dateToday():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)


# speak("Hi! i'm JARVIS, an virtual assistant.")
timeNow()
dateToday()