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

def get_weather(city):
    # API URL with your API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=99e68c086c34059f58d3349bd4fb694c&units=metric'

    # Send an HTTP GET request to the API and get the response
    response = requests.get(url)

    # Check if the API call was successful
    if response.status_code == 200:
        # Parse the JSON response to get the weather information
        weather = response.json()

        # Extract the relevant weather information from the JSON response
        temperature = weather['main']['temp']
        humidity = weather['main']['humidity']
        description = weather['weather'][0]['description']

        # Return the weather report for the city
        return f"The temperature in {city} is {temperature} Kelvin. The humidity is {humidity}% and the weather is {description}."
    else:
        # Return an error message if the API call was not successful
        return "Unable to get the weather report. Please try again later."
    
get_weather("khulna")

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

speak("Opening, Please wait for a seconds")
esshan()

if __name__=='__main__':
    while True:
        speak("What can i do for you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "turn off" in statement:
            speak('See you later!')
            break

        if 'wikipedia' in statement:
            speak('Searching the wiki')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("according to the wiki")
            speak(results)

        elif 'weather' in statement:
            speak("Sure, which city?")
            city = takeCommand()
            weather_report = get_weather(city)
            speak(weather_report)

        elif 'time' in statement:
            now = datetime.datetime.now()
            date = now.strftime('%Y-%m-%d')
            clock = now.strftime('%I:%M %p')
            speak(f"Today's date is {date} and the current time is {clock}")

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
