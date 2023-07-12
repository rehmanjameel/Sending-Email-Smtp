import csv

# Create sender email CSV file
sender_file = 'sender_emails.csv'
sender_email = [{'First Name': 'first_name', 'Last Name': 'last_name', 'Email': 'malikarj98@gmail.com',
                 'Password': 'sqaswldietivnsno'}]

with open(sender_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['First Name', 'Last Name', 'Email', 'Password'])
    writer.writeheader()  # Write header
    writer.writerows(sender_email)  # Write sender emails

# Create receiver email CSV file
receiver_file = 'receiver_emails.csv'
receiver_emails = [{'First Name': 'first_name', 'Last Name': 'last_name', 'Email': 'abdulrehmancs17@gmail.com',
                    'Subject': 'Test Subject', 'Body': 'This is a test email.'},
                   {'First Name': 'first_name', 'Last Name': 'last_name', 'Email': 'abdulrehmancs17@gmail.com',
                    'Subject': 'Test Subject 121', 'Body': 'This is a test email.121'},
                   {'First Name': 'first_name', 'Last Name': 'last_name', 'Email': 'abdulrehmancs17@gmail.com',
                    'Subject': 'Test Subject 11', 'Body': 'This is a test email.11'}
                   ]

with open(receiver_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['First Name', 'Last Name', 'Email', 'Subject', 'Body'])
    writer.writeheader()  # Write header
    writer.writerows(receiver_emails)  # Write receiver emails, subject, and body

# Create server details CSV file
server_file = 'server_details.csv'
servers = [
    {'Server': 'google.com', 'SMTP Server': 'smtp.gmail.com', 'Port': 587},
    {'Server': 'icloud.com', 'SMTP Server': 'smtp.gmail.com', 'Port': 587},
    {'Server': 'icloud.com', 'SMTP Server': 'smtp.gmail.com', 'Port': 587}
]

with open(server_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Server', 'SMTP Server', 'Port'])
    writer.writeheader()  # Write header
    writer.writerows(servers)  # Write server details
