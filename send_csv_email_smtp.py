import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read sender email from CSV file
sender_file = 'sender_emails.csv'
sender_df = pd.read_csv(sender_file)
sender_email = sender_df['Email'][0]
smtp_password = sender_df['Password'][0]

# Read receiver emails, subject, and body from Excel file
receiver_file = 'receiver_emails.csv'
receiver_df = pd.read_csv(receiver_file)

# Read server details from CSV file
server_file = 'server_details.csv'
server_df = pd.read_csv(server_file)

for (receiver_index, receiver_row), (server_index, server_row) in zip(receiver_df.iterrows(), server_df.iterrows()):
    receiver_email = receiver_row['Email']
    subject = receiver_row['Subject']
    body = receiver_row['Body']

    smtp_server = server_row['SMTP Server']
    smtp_port = server_row['Port']

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add the message body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create a SMTP session
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable secure connection
            server.login(sender_email, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print('Email sent successfully using', smtp_server)
    except Exception as e:
        print('Error sending email using', smtp_server, ':', str(e))
