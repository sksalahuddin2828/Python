# pip install pygame

import os
import pygame
from pygame import mixer
from tkinter import Tk, filedialog

# Initialize the mixer
pygame.mixer.init()

# Create a Tkinter window to select audio files
root = Tk()
root.withdraw()

# Function to select a file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")])
    if file_path:
        play_music(file_path)

# Function to play the selected file
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Main loop
while True:
    print("1. Select a file")
    print("2. Stop music")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        select_file()
    elif choice == "2":
        stop_music()
    elif choice == "3":
        break

# Quit the mixer
pygame.mixer.quit()
