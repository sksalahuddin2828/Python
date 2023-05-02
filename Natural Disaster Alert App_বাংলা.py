import time
from twilio.rest import Client
import tkinter as tk
primary_color = "#2B4162"
secondary_color = "#F5F5F5"
heading_font = ("Helvetica", 24, "bold")
label_font = ("Helvetica", 16)
button_font = ("Helvetica", 16, "bold")
def check_for_alert():
    account_sid = 'your_twilio_account_sid' 
    auth_token = 'your_twilio_auth_token'  
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='সতর্কতাঃ ভাই! বৃষ্টি হবে পালান',  
        from_='(+1)_your_twilio_phone_number',
        to=phone_entry.get()
    )
    alert_status.set("Alert: Natural Disaster Detected")
def start():
    while True:
        check_for_alert()
        time.sleep(interval.get() * 60)
root = tk.Tk()
root.title("Sk. Salahuddin - Morning 01 Batch")
root.geometry('840x420')
root.configure(bg=secondary_color)
heading_label = tk.Label(root, text="প্রাকৃতিক দুর্যোগ সতর্কতা বার্তা", font=heading_font, fg=primary_color, bg=secondary_color)
heading_label.pack(pady=20)
phone_frame = tk.Frame(root, bg=secondary_color)
phone_frame.pack(pady=10)
phone_label = tk.Label(phone_frame, text="মোবাইল নম্বর:", font=label_font, fg=primary_color, bg=secondary_color)
phone_label.pack(side=tk.LEFT, padx=10)
phone_entry = tk.Entry(phone_frame, font=label_font)
phone_entry.pack(side=tk.LEFT)
phone_entry.insert(0, "মোবাইল নম্বর")
phone_entry.bind("<FocusIn>", lambda args: phone_entry.delete('0', 'end'))
phone_entry.bind("<FocusOut>", lambda args: phone_entry.insert(0, "মোবাইল নম্বর"))
disaster_frame = tk.Frame(root, bg=secondary_color)
disaster_frame.pack(pady=10)
disaster_label = tk.Label(disaster_frame, text="দুর্যোগের ধরন নির্বাচন করুন:", font=label_font, fg=primary_color, bg=secondary_color)
disaster_label.pack(side=tk.LEFT, padx=10)
disaster_checkboxes = [tk.Checkbutton(disaster_frame, text="বৃষ্টি", font=label_font, fg=primary_color, bg=secondary_color, padx=10),
                       tk.Checkbutton(disaster_frame, text="ঝড়ো বাতাস", font=label_font, fg=primary_color, bg=secondary_color, padx=10),
                       tk.Checkbutton(disaster_frame, text="ভূমিকম্প", font=label_font, fg=primary_color, bg=secondary_color, padx=10),
                       tk.Checkbutton(disaster_frame, text="সুনামি", font=label_font, fg=primary_color, bg=secondary_color, padx=10),
                       tk.Checkbutton(disaster_frame, text="ঝড়", font=label_font, fg=primary_color, bg=secondary_color, padx=10)
                       ]
for checkbox in disaster_checkboxes:
    checkbox.pack(side=tk.LEFT)
alert_status = tk.StringVar()
alert_status.set("No Alerts")
alert_label = tk.Label(root, textvariable=alert_status, font=label_font, fg=primary_color, bg=secondary_color)
alert_label.pack(pady=20)
interval_frame = tk.Frame(root, bg=secondary_color)
interval_frame.pack(pady=10)
interval_label = tk.Label(interval_frame, text="Check Interval (minutes):", font=label_font, fg=primary_color, bg=secondary_color)
interval_label.pack(side=tk.LEFT, padx=10)
interval = tk.Scale(interval_frame, from_=1, to=60, orient=tk.HORIZONTAL, length=200, font=label_font)
interval.pack(side=tk.LEFT)
start_button = tk.Button(root, text="বার্তা পাঠান", font=button_font, fg=primary_color, bg=secondary_color, command=start)
start_button.pack(pady=20)
root.mainloop()
