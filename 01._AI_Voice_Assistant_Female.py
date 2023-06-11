import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
# Artificial Intelligence actually access the Webbrowser
import webbrowser
import time
import ecapture as ec
import pywhatkit
# OS can access your operating system
import os
import subprocess
import wolframalpha
# Json save everything like a database
import json 
import requests

print('Sk. Salahuddin - Morning 01 Batch')

engine = pyttsx3.init('sapi5')

# Set the voice to a female voice
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def esshan():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening!")

def takeCommand():
    record = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening...")
        audio = record.listen(source)

        try:
            statement = record.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("I didn't hear you, please say that again")
            return "none"
        return statement.lower()

esshan()
speak("Opening, Please wait for a few seconds")

if __name__=='__main__':
    while True:
        speak("What can i do for you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "turn off" in statement:
            speak ('See you later and take care, bye!')
            break

        if 'wikipedia' in statement:
            speak('Searching the wiki')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("according to the wiki")
            speak(results)

        elif 'time' in statement:
            clock_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"Your local time is {clock_time} in Bangladesh Time")

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://youtube.com")
            speak("Opening YouTube, just wait for a while")
            time.sleep(3)

        elif 'play' in statement:
            song = statement.replace("play", "")
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif 'open facebook' in statement:
            webbrowser.open_new_tab("https://facebook.com")
            speak("Opening Facebook, just wait for a while")
            time.sleep(3)

        elif 'open twitter' in statement:
            webbrowser.open_new_tab("https://twitter.com")
            speak("Opening Twitter, just wait for a while")
            time.sleep(3)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Opening Google Chrome, just wait for a while")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Opening Gmail, just wait for a while")
            time.sleep(5)
