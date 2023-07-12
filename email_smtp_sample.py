import csv
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
receiver_email = 'abdulrehmancs17@gmail.com'
sender_email = 'malikarj98@gmail.com'
subject = 'Test Email'
message = 'Hello, this is a test email.'

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Add the message body
msg.attach(MIMEText(message, 'plain'))

# SMTP server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'Malik AR-J'
smtp_password = 'sqaswldietivnsno'

try:
    # Create a SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # server.starttls()  # Enable secure connection
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully.')
except Exception as e:
    print('Error sending email:', str(e))