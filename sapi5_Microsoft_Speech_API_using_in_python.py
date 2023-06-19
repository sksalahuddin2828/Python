# The Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications.
# SAPI5 or sapi5 = 5 is version name

import pyttsx3

name = pyttsx3.init("sapi5")
name.say("Hello World!")
name.runAndWait()

#-------------Talking Again and Again!---------------

import pyttsx3

while True:
    name = pyttsx3.init("sapi5")
    name.say("Hello World!")
    name.runAndWait()
    
#------Talking Again and Again from User Input!------

import pyttsx3
_ = input("Enter a name: ")

while True:
    name = pyttsx3.init("sapi5")
    name.say(_)
    name.runAndWait()
