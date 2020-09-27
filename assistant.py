import pyttsx3 # pip install pyttxs3
import datetime
import speech_recognition as sr

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

def voiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query


# speak("Hi! i'm JARVIS, an virtual assistant.")
# timeNow()
# dateToday()
# wish()
voiceCommand()
