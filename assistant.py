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

def wish():
    speak("Welcome back sir!")
    speak("The time is")
    timeNow()
    speak("Today is")
    dateToday()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good efternon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")

    speak("JARVIS at your service sir. How can i help you?")


# speak("Hi! i'm JARVIS, an virtual assistant.")
# timeNow()
# dateToday()
wish()