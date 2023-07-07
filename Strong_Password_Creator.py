from tkinter import *
import random, string

def generate_password():
    password_length = random.randint(16, 22)
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(password_characters, k=password_length))

    generated_password.set(password)

root = Tk()
root.geometry("400x280")
root.title("Password Generator")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("Generate a strong password:")

generate_button = Button(root, text="Generate", command=generate_password).pack()

generated_password = StringVar()
generated_password_label = Label(root, textvariable=generated_password)
generated_password_label.pack()

root.mainloop()
