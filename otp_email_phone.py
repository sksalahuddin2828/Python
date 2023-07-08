import os
import math
import random
import smtplib

digits = "0123456789"

def generate_otp():
    otp = ""
    for i in range(6):
        otp += digits[math.floor(random.random()*10)]
    return otp

def send_otp_phone(phone_number, otp):
    # Logic to send the OTP to the user's phone number
    print(f"Sending OTP {otp} to phone number: {phone_number}")

def send_otp_email(email, otp):
    # Logic to send the OTP to the user's email address
    msg = f"{otp} is your OTP. Please verify it."
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your_Gmail_Account", "Your_app_password")
    s.sendmail('&&&&&&&&&&&', email, msg)
    s.quit()
    print(f"Sending OTP {otp} to email address: {email}")

def verify_otp(entered_otp, generated_otp):
    if entered_otp == generated_otp:
        return True
    else:
        return False

# Usage example
phone_number = "+1234567890"  # Replace with the actual phone number
email_id = "example@gmail.com"  # Replace with the actual email address

# Generate OTP and send it to the user's phone number
otp_phone = generate_otp()
send_otp_phone(phone_number, otp_phone)

# Generate OTP and send it to the user's email
otp_email = generate_otp()
send_otp_email(email_id, otp_email)

# Prompt the user to choose the verification method
verification_method = input("Choose the verification method (1 - Phone, 2 - Email): ")

# Prompt the user to enter the OTP
entered_otp = input("Enter the OTP: ")

# Verify the entered OTP based on the chosen method
if verification_method == "1":
    if verify_otp(entered_otp, otp_phone):
        print("OTP verification successful!")
    else:
        print("OTP verification failed.")
elif verification_method == "2":
    if verify_otp(entered_otp, otp_email):
        print("OTP verification successful!")
    else:
        print("OTP verification failed.")
else:
    print("Invalid verification method selected.")
