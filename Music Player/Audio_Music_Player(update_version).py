# Now you can increase or decrease the volume here, you can also select multiple songs at once and listen to your favorite songs, delete and add songs as needed.
# Remember only this files *.mp3;*.wav;*.ogg;*.mp4;*.avi;*.mkv;*.flv;*.mov;*.wmv;*.webm

import os
import pygame
from tkinter import Tk, filedialog, messagebox
from tkinter import ttk
from tkinter import Listbox

# Initialize the mixer
pygame.mixer.init()

# Create a Tkinter window to select media files
root = Tk()
root.withdraw()

# Global variables
current_file = ""
playlist = []
current_index = 0
is_playing = False
volume = 0.5  # Default volume

# Function to select a file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[
        ("Audio/Video Files", "*.mp3;*.wav;*.ogg;*.mp4;*.avi;*.mkv;*.flv;*.mov;*.wmv;*.webm")
    ])
    if file_path:
        add_to_playlist(file_path)

# Function to add a file to the playlist
def add_to_playlist(file_path):
    playlist.append(file_path)
    playlist_box.insert("end", os.path.basename(file_path))

# Function to remove a file from the playlist
def remove_from_playlist():
    selected_index = playlist_box.curselection()
    if selected_index:
        playlist.pop(selected_index[0])
        playlist_box.delete(selected_index)

# Function to clear the playlist
def clear_playlist():
    global current_index
    playlist.clear()
    playlist_box.delete(0, "end")
    stop_music()
    current_index = 0

# Function to play the selected file or playlist
def play_music(file_path=None):
    global current_file, current_index, is_playing

    if not file_path:
        selected_index = playlist_box.curselection()
        if not selected_index:
            messagebox.showinfo("Error", "No file selected.")
            return
        current_index = selected_index[0]
        file_path = playlist[current_index]

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    current_file = file_path
    is_playing = True

    update_status()

# Function to pause/resume the music
def pause_resume_music():
    global is_playing

    if is_playing:
        pygame.mixer.music.pause()
        is_playing = False
    else:
        pygame.mixer.music.unpause()
        is_playing = True

    update_status()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    update_status()

# Function to rewind the music
def rewind_music():
    pygame.mixer.music.rewind()

# Function to fast forward the music
def fast_forward_music(seconds):
    current_time = pygame.mixer.music.get_pos() / 1000
    new_time = current_time + seconds
    pygame.mixer.music.set_pos(new_time)

# Function to set the volume
def set_volume(volume_level):
    global volume
    volume = float(volume_level)
    pygame.mixer.music.set_volume(volume)

# Function to update the status label
def update_status():
    global current_file, current_index, is_playing

    if current_file:
        status_label.config(text=f"Now playing: {os.path.basename(current_file)}")
    else:
        status_label.config(text="")

    if is_playing:
        play_pause_button.config(text="Pause")
    else:
        play_pause_button.config(text="Resume")

    playlist_box.selection_clear(0, "end")
    playlist_box.selection_set(current_index)

# Main GUI window
window = Tk()
window.title("Media Player")

# Create buttons
select_button = ttk.Button(window, text="Select File", command=select_file)
play_pause_button = ttk.Button(window,text="Play", command=play_music)
stop_button = ttk.Button(window, text="Stop", command=stop_music)
rewind_button = ttk.Button(window, text="Rewind", command=rewind_music)
fast_forward_button = ttk.Button(window, text="Fast Forward", command=lambda: fast_forward_music(10))

# Create playlist controls
playlist_label = ttk.Label(window, text="Playlist")
playlist_box = Listbox(window, selectbackground="#3498db", selectforeground="white")
remove_button = ttk.Button(window, text="Remove", command=remove_from_playlist)
clear_button = ttk.Button(window, text="Clear", command=clear_playlist)

# Create volume control
volume_label = ttk.Label(window, text="Volume")
volume_scale = ttk.Scale(window, from_=0.0, to=1.0, orient="horizontal", command=set_volume)
volume_scale.set(volume)  # Set initial volume value

# Create status label
status_label = ttk.Label(window, text="", anchor="center")

# Position the buttons and widgets
select_button.grid(row=0, column=0, padx=10, pady=10)
play_pause_button.grid(row=0, column=1, padx=10, pady=10)
stop_button.grid(row=0, column=2, padx=10, pady=10)
rewind_button.grid(row=0, column=3, padx=10, pady=10)
fast_forward_button.grid(row=0, column=4, padx=10, pady=10)
playlist_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
playlist_box.grid(row=2, column=0, rowspan=4, columnspan=5, padx=10, pady=10, sticky="nsew")
remove_button.grid(row=2, column=5, padx=5, pady=10, sticky="w")
clear_button.grid(row=3, column=5, padx=5, pady=10, sticky="w")
volume_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
volume_scale.grid(row=6, column=1, columnspan=4, padx=10, pady=5, sticky="we")
status_label.grid(row=7, column=0, columnspan=6, padx=10, pady=5, sticky="we")

# Configure grid weights
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)

# Start the GUI event loop
window.mainloop()

# Quit the mixer
pygame.mixer.quit()
