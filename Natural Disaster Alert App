# More design will come very soon -- I already tring to learn form Stanford University CA United States
# Natural_Disaster_Alert_System App -- This Desktop Application will be in many language, so any country user can use it for his/her own language
# Also this app web version release will in May 2024
# Then we can send SMS in evry person Cell/Mobile Phone within a micro seconds more than 700 million peoples together

import tkinter as tk
import time
from twilio.rest import Client
def check_for_alert():
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Alert: Natural Disaster Detected',
        from_='your twilio phone number'
        to=phone_entry.get()
    )
    alert_status.set("Alert: Natural Disaster Detected")
def start():
    while True:
        check_for_alert()
        time.sleep(interval.get() * 60)
root = tk.Tk()
root.title("প্রাকৃতিক দুর্যোগ সতর্কতা বার্তা")
root.geometry('700x280')
phone_label = tk.Label(root, text="Phone Number:", font=("Arial Bold", 12))
phone_label.grid(row=0, column=0, pady=(20,0))
phone_entry = tk.Entry(root, font=("Arial", 12))
phone_entry.grid(row=0, column=1, pady=(20,0))
disaster_label = tk.Label(root, text="Select Disaster Types:", font=("Arial Bold", 12))
disaster_label.grid(row=1, column=0, pady=10)
disaster_checkboxes = [tk.Checkbutton(root, text="Rain", font=("Arial", 12), padx=10),
                       tk.Checkbutton(root, text="Earthquake", font=("Arial", 12), padx=10),
                       tk.Checkbutton(root, text="Tsunami", font=("Arial", 12), padx=10),
                       tk.Checkbutton(root, text="Storm", font=("Arial", 12), padx=10)]
for i, checkbox in enumerate(disaster_checkboxes):
    checkbox.grid(row=1, column=i+1)
interval_label = tk.Label(root, text="Alert Interval (in minutes):", font=("Arial Bold", 12))
interval_label.grid(row=2, column=0, pady=10)
interval = tk.Scale(root, from_=1, to=60, orient=tk.HORIZONTAL, font=("Arial", 12))
interval.grid(row=2, column=1)
alert_status = tk.StringVar()
alert_status.set("No Alert")
alert_label = tk.Label(root, textvariable=alert_status, font=("Arial Bold", 16))
alert_label.grid(row=3, column=0, columnspan=2, pady=20)
start_button = tk.Button(root, text="Start", font=("Arial Bold", 12), command=start)
start_button.grid(row=4, column=0, columnspan=2, pady=20)
root.mainloop()
