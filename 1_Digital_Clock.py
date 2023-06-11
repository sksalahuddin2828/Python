from tkinter import *
import time
import calendar

root = Tk()
root.title("Sk. Salahuddin - Morning 01 Batch")
root.geometry("700x370")
root.configure(bg="#272727")
date_formats = ["%B %d, %Y"]
#"%d-%m-%Y",
#"%b %d, %Y",
# "Today is %A, %B %d, %Y",
# "Happy %A, %B %d, %Y",
# "It's %A, %B %d, %Y",
# "The date is %A, %B %d, %Y"
date_format = date_formats[0]
date_label = Label(root, font=("Helvetica", 35), bg="#272727", fg="#fff", text="")
date_label.pack(pady=(30, 10))
time_label = Label(root, font=("Helvetica", 80, "bold"), bg="#272727", fg="#F39C12", text="")
time_label.pack(pady=10)
day_of_week_label = Label(root, font=("Helvetica", 18), bg="#272727", fg="#fff", text="")
day_of_week_label.pack()
month_label = Label(root, font=("Helvetica", 18), bg="#272727", fg="#fff", text="")
month_label.pack()
year_label = Label(root, font=("Helvetica", 18), bg="#272727", fg="#fff", text="")
year_label.pack()
def update():
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime(date_format)
    day_of_week = calendar.day_name[time.localtime().tm_wday]
    month = calendar.month_name[time.localtime().tm_mon]
    year = time.strftime("%Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    day_of_week_label.config(text=day_of_week)
    month_label.config(text=month)
    year_label.config(text=year)
    root.after(1000, update)
update()
root.mainloop()
