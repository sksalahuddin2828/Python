import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import wikipedia
import webbrowser

search = pyttsx3.init()
print("Sk. Salahuddin - Morning 01 Batch: +8801767902828")
"""
Change voice "by default" 0 is Male voices and 1 is Female voices
If you install multiple voices then check voices index
"""
def speak(text):
    voices = search.getProperty("voices")
    search.setProperty("voice", voices[3].id)
    search.setProperty("rate", 200)
    search.say(text)
    search.runAndWait()

def takeCommand():
    lang_convert = Translator()
    record = sr.Recognizer()
    with sr.Microphone() as source:
        record.adjust_for_ambient_noise(source, duration=0.7)
        print("Listening...")
        audio = record.listen(source, timeout=None, phrase_time_limit=7)
        try:
            user_input = record.recognize_google(audio, language='en-IN')
            speak("You said: " + user_input)
            print(f"user said: {user_input}\n")
            translated = lang_convert.translate(user_input, dest='en').text

        except sr.UnknownValueError:
            speak("I didn't hear you, please say that again")
            return "none"
        except sr.RequestError:
            speak("Sorry, I'm having trouble processing your request. Please try again later.")
            return "none"
        except Exception as e:
            speak("Sorry, an error occurred. Please try again;{0}".format(e))
            print("Sorry, an error occurred. Please try again;{0}".format(e))
            return "none"
        return translated.lower()


def ip_address():
    speak("Checking your Internet Protocol (IP) address, please wait for a moment!")
    url: str = "https://checkip.amazonaws.com"
    request = requests.get(url)
    ip: str = request.text
    print(f"Your IP Address: {ip}")
    speak(f"Your IP Address is: {ip}")

def open_wikipedia():
    speak("Opening Wikipedia")
    webbrowser.open("https://www.wikipedia.org/")


speak("Welcome, Sk. Salahuddin")

while True:
    user_input = takeCommand().lower()

    if "olivia" in user_input:
        speak("Hello! How can I assist you?")

    elif any(exit_word in user_input for exit_word in ["exit", "close", "off", "good bye", "bye", "ok bye", "turn off", "shut down", "no thanks"]):
        speak('Take care and see you later')
        clockTime_night()
        speak('Bye!')
        break

    speak("Please wait")

    if "ip address" in user_input or "internet protocol" in user_input or "ip" in user_input:
        ip_address()

    elif "opening wikipedia" in user_input:
        open_wikipedia()

    else:
        speak("Sorry, I didn't understand that command. Please try again!")
