# pip install SpeechRecognition pyttsx3

import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
synthesizer = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return "none"

def speak(text):
    synthesizer.say(text)
    synthesizer.runAndWait()

while True:
    user_input = listen()

    if user_input.lower() == "hello":
        speak("Hello there!")
    elif user_input.lower() == "what's your name":
        speak("I am your creative voice assistant.")
    elif user_input.lower() == "exit":
        speak("Goodbye!")
        break
    else:
        speak("Sorry, I couldn't understand you.")
