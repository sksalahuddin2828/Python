from tkinter import *
import tkinter.font as font
import random

def startGame():
    global displayed_word_color
    if timer == 60:
        countdown()
    next_word()

def resetGame():
    global timer, score
    timer = 60
    score = 0
    game_score.config(text="Your Score: " + str(score))
    color_entry.delete(0, END)
    color_entry.config(state=NORMAL)
    start_button.config(state=DISABLED)
    reset_button.config(state=DISABLED)
    countdown()

def next_word():
    global displayed_word_color
    if timer > 0:
        color_entry.delete(0, END)
        displayed_word_color = random.choice(colors)
        displayed_word_text = random.choice(colors)
        display_words.config(text=displayed_word_text, fg=displayed_word_color)

def check_word(event):
    global score
    if timer > 0:
        if displayed_word_color.lower() == color_entry.get().lower():
            score += 1
        game_score.config(text="Your Score: " + str(score))
        color_entry.delete(0, END)
        next_word()

def countdown():
    global timer
    if timer > 0:
        timer -= 1
        time_left.config(text="Game Ends in: " + str(timer) + "s")
        time_left.after(1000, countdown)
        color_entry.config(state=NORMAL)
        start_button.config(state=DISABLED)
        reset_button.config(state=DISABLED)
    else:
        color_entry.config(state=DISABLED)
        start_button.config(state=NORMAL)
        reset_button.config(state=NORMAL)

colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]

timer = 60
score = 0
displayed_word_color = ''

my_window = Tk()
my_window.title("Color Game")

app_font = font.Font(family='Helvetica', size=12)

game_desp = "Game Description: Enter the color of the words displayed below. \n And Keep in mind not to enter the word text itself"
myFont = font.Font(family='Helvetica')

game_description = Label(my_window, text=game_desp, font=app_font, fg="grey")
game_description.pack()

game_score = Label(my_window, text="Your Score: " + str(score), font=(font.Font(size=16)), fg="green")
game_score.pack()

display_words = Label(my_window, font=(font.Font(size=28)), pady=10)
display_words.pack()

time_left = Label(my_window, text="Game Ends in: -", font=(font.Font(size=14)), fg="orange")
time_left.pack()

color_entry = Entry(my_window, width=30)
color_entry.pack(pady=10)
color_entry.bind("<Return>", check_word)

btn_frame = Frame(my_window, width=80, height=40, bg='red')
btn_frame.pack(side=BOTTOM)

start_button = Button(btn_frame, text="Start", width=20, fg="black", bg="pink", bd=0, padx=20, pady=10, command=startGame)
start_button.grid(row=0, column=0)

reset_button = Button(btn_frame, text="Reset", width=20, fg="black", bg="light blue", bd=0, padx=20, pady=10, command=resetGame)
reset_button.grid(row=0, column=1)

my_window.geometry('600x300')
my_window.mainloop()
