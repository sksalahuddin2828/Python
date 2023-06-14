# Frist read carefully instraction in comments here :-)

import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "email.alert.your@gmail.com"  # email.alert.Your Email like Gmail, Yahoo Mail etc
    msg['from'] = user

    # generate this password from tour Gmail App Password option
    # --> other name --> Email alerts --> click generate keys like here or down below
    password = "abcdefghijklmnopqr"  
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    email_alert("Hey", "Hello world", "your@gmail.com")  # enter your gmail or email here
