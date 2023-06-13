import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class ListenerThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            self.signal.emit(text)
        except sr.UnknownValueError:
            self.signal.emit("")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Voice Assistant")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Assistant is ready.", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 50, 200, 30)

        self.button = QPushButton("Start Listening", self)
        self.button.setGeometry(100, 100, 100, 30)
        self.button.clicked.connect(self.start_listening)

        self.listener_thread = ListenerThread()
        self.listener_thread.signal.connect(self.process_input)

        self.synthesizer = pyttsx3.init()

    def start_listening(self):
        self.listener_thread.start()

    def process_input(self, text):
        if "open youtube" in text.lower():
            self.speak("Opening YouTube...")
            pywhatkit.playonyt("")  # Add the keyword or video title you want to search for on YouTube

        elif "open facebook" in text.lower():
            self.speak("Opening Facebook...")
            pywhatkit.search("Facebook")

        elif "play" in text.lower() and "on youtube" in text.lower():
            query = text.lower().replace("play", "").replace("on youtube", "").strip()
            self.speak(f"Playing {query} on YouTube...")
            pywhatkit.playonyt(query)

        elif text.lower() == "hello":
            self.speak("Hello there!")

        elif text.lower() == "what's your name":
            self.speak("I am your creative voice assistant.")

        elif text.lower() == "exit":
            self.speak("Goodbye!")
            sys.exit()

        else:
            self.speak("Sorry, I couldn't understand you.")

    def speak(self, text):
        self.synthesizer.say(text)
        self.synthesizer.runAndWait()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

#----------------------------------------------

import webbrowser

def process_input(self, text):
    if "open youtube" in text.lower():
        self.speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in text.lower():
        self.speak("Opening Facebook...")
        webbrowser.open("https://www.facebook.com")

    elif "play" in text.lower() and "on youtube" in text.lower():
        query = text.lower().replace("play", "").replace("on youtube", "").strip()
        self.speak(f"Playing {query} on YouTube...")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    elif text.lower() == "hello":
        self.speak("Hello there!")

    elif text.lower() == "what's your name":
        self.speak("I am your creative voice assistant.")

    elif text.lower() == "exit":
        self.speak("Goodbye!")
        sys.exit()

    else:
        self.speak("Sorry, I couldn't understand you.")

