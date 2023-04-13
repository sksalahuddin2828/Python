from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%H:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)

Label(master, font=("Arial", 30), text="Digital Clock", fg="white", bg="black").pack()
clock = Label(master, font=("Arial", 100), bg="black", fg="white")
clock.pack()

get_time()
master.mainloop()
