"""
Your peripheral nervous system (PNS) is one of two main parts of your body’s nervous system.
Your PNS feeds information into your brain from most of your senses. It carries signals that allow you to move your muscles.
Your PNS also delivers signals that your brain uses to control vital, unconscious processes like your heartbeat and breathing.

"""

import pyttsx3
import webbrowser

# sapi5 is a Peripheral Nervous System (PNS) in Microsoft Windows. It's like a brain
# It works for Peripheral devices like keyboard, mouse, speaker etc etc.
neuron = pyttsx3.init("sapi5")

while True:
    # receive a input from user == when user input in this terminal
    com = input("Enter your text: ").lower()
    
    # when get a input from user then check this conditions
    if "youtube" in com:
        neuron.say("opening YouTube")
        neuron.runAndWait()
        webbrowser.open("https://www.youtube.com/")

    if "search" in com:
        neuron.say("search for what ")
        neuron.runAndWait()
        search=input("").lower()
        neuron.say(f"OK, I'm searching for {search}")
        neuron.runAndWait()
        webbrowser.open(f"https://www.google.com/search?q={search}")
        
#--------------------------------------------------------------------------------------------

import pyttsx3
import webbrowser

search = pyttsx3.init("sapi5")
 
while True:
    user_input = input("Enter your text: ").lower()

    if "youtube" in user_input:
        search.say("Opening YouTube, just wait a while")
        search.runAndWait()
        webbrowser.open("https://www.youtube.com/")

    if "search" in user_input:
        search.say("What do you want to search from Google?")
        search.runAndWait()
        search_items = input("Give your search keyword: ").lower()
        search.say("Opening your search itmes, just wait a while")
        search.runAndWait()
        webbrowser.open(f"https://www.google.com/search?q={search_items}")

    else:
        print("Opps! Try again")
