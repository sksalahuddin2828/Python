from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from pygame import mixer

mixer.init()

# If you want to listen to the director's audio on your computer, use his link here with the directory:
mixer.music.load('D:/Na Rakha Kichu Kotha.mp3') 

def play_song():
    mixer.music.play()

def stop_song():
    mixer.music.stop()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def set_volume(volume):
    mixer.music.set_volume(float(volume) / 100)

window = ThemedTk(theme="arc")   # set theme="" --> plastik / elegance / radiance / clearlooks / equilux / arc
window.geometry('252x88')  # set dimensions of the window
window.title('Music Player')

playButton = ttk.Button(window, text="Play", command=play_song)
playButton.grid(column=0, row=1)

stopButton = ttk.Button(window, text="Stop", command=stop_song)
stopButton.grid(column=1, row=1)

pauseButton = ttk.Button(window, text="Pause", command=pause)
pauseButton.grid(column=2, row=1)

resumeButton = ttk.Button(window, text="Resume", command=resume)
resumeButton.grid(column=1, row=2)

volumeLabel = ttk.Label(window, text="Volume:")
volumeLabel.grid(column=0, row=0)

volumeScale = ttk.Scale(window, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
volumeScale.set(50)  # Set initial volume to 50
volumeScale.grid(column=1, row=0, columnspan=3, sticky="we")

window.mainloop()
