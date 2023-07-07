import os
import pygame
from tkinter import Tk, filedialog
from tkinter import ttk

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

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Function to unpause the music
def unpause_music():
    pygame.mixer.music.unpause()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Function to rewind the music
def rewind_music():
    pygame.mixer.music.rewind()

# Function to fast forward the music
def fast_forward_music(seconds):
    current_time = pygame.mixer.music.get_pos() / 750  # Change value 1000
    new_time = current_time + seconds
    pygame.mixer.music.set_pos(new_time)

# Function to repeat the music
def repeat_music():
    pygame.mixer.music.play(-1)  # -1 indicates infinite loop

# Main GUI window
window = Tk()
window.title("Music Player")

# Create buttons
select_button = ttk.Button(window, text="Select File", command=select_file)
play_button = ttk.Button(window, text="Play", command=lambda: play_music(file_path_entry.get()))
pause_button = ttk.Button(window, text="Pause", command=pause_music)
unpause_button = ttk.Button(window, text="Unpause", command=unpause_music)
stop_button = ttk.Button(window, text="Stop", command=stop_music)
rewind_button = ttk.Button(window, text="Rewind", command=rewind_music)
fast_forward_button = ttk.Button(window, text="Fast Forward", command=lambda: fast_forward_music(10))
repeat_button = ttk.Button(window, text="Repeat", command=repeat_music)

# Create file path entry
file_path_entry = ttk.Entry(window, width=50)

# Position the buttons and entry
select_button.grid(row=0, column=0, padx=10, pady=10)
play_button.grid(row=0, column=1, padx=10, pady=10)
pause_button.grid(row=0, column=2, padx=10, pady=10)
unpause_button.grid(row=0, column=3, padx=10, pady=10)
stop_button.grid(row=0, column=4, padx=10, pady=10)
rewind_button.grid(row=1, column=0, padx=10, pady=10)
fast_forward_button.grid(row=1, column=1, padx=10, pady=10)
repeat_button.grid(row=1, column=2, padx=10, pady=10)
file_path_entry.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()

# Quit the mixer
pygame.mixer.quit()
