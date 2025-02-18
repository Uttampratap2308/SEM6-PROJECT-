# send_alert.py
import smtplib

def send_alert():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    message = 'Subject: Security Alert!\n\nPossible Attack Detected!'
    server.sendmail('your_email@gmail.com', 'alert_receiver@gmail.com', message)
    server.quit()
    print("Alert Email Sent.")
