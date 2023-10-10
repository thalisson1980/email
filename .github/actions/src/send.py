import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import os

# Set up your SMTP email credentials
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
smtp_username = os.environ.get('SMTP_USERNAME')
smtp_password = os.environ.get('SMTP_PASSWORD')

# Recipient email address
recipient_email = os.environ.get('RECIPIENT')

# Subject and message body for the email
subject = 'Response Needed'
message_body = '''
Dear recipient,

Please respond to this email with one of the following options:

- Reply with 'Yes' to approve.
- Reply with 'No' to deny.

Thank you,
Your Sender
'''

# Create the email
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message_body, 'plain'))

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully with subject: 'Response Needed'")
except Exception as e:
    print(f"Error: {str(e)}")
