from tkinter import *
import random, string

def generate_password():
    password_strength = strength.get()
    password_length = length.get()

    if password_strength == "Weak":
        if password_length < 6:
            password_length = 6
        password = ''.join(random.choices(string.ascii_letters, k=password_length))
    elif password_strength == "Medium":
        if password_length < 8:
            password_length = 8
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
    else:
        if password_length < 10:
            password_length = 10
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))

    generated_password.set(password)

root = Tk()
root.geometry("400x280")
root.title("Password Generator")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("Choose the strength and length of your password:")

strength = StringVar()
strength.set("Weak")

strength_label = Label(root, text="Strength:").pack()
strength_option = OptionMenu(root, strength, "Weak", "Medium", "Strong")
strength_option.pack()

length_label = Label(root, text="Length:").pack()
length = IntVar()
length.set(8)
length_entry = Entry(root, textvariable=length).pack()

generate_button = Button(root, text="Generate", command=generate_password).pack()

generated_password = StringVar()
generated_password_label = Label(root, textvariable=generated_password)
generated_password_label.pack()

root.mainloop()
