from tkinter import *
import time
root = Tk()
root.title("Sk. Salahuddin - Morning 01 Batch")
root.geometry("1000x320")
root.configure(bg="black")
date_label = Label(root, font=("Arial", 50), bg="black", fg="white")
date_label.pack(pady=10)
time_label = Label(root, font=("Arial", 120), bg="black", fg="#00ff00")
time_label.pack(pady=20)
def update():
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%d-%B-%Y %A")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update)
update()
root.mainloop()
