import imaplib
import email
from email.header import decode_header
import time
import os

# Set up your Outlook email credentials
email_address = os.environ.get('SMTP_USERNAME')
password = os.environ.get('SMTP_PASSWORD')

# Connect to the Outlook email server
while True:
    try:
        imap = imaplib.IMAP4_SSL('outlook.office365.com')
        imap.login(email_address, password)

        # Select the inbox folder
        imap.select('inbox')

        # Search for emails with a specific subject or criteria
        criteria = '(SUBJECT "check test")'
        status, email_ids = imap.search(None, criteria)

        if email_ids[0]:
            # Get the most recent email (you may need to adjust this logic)
            latest_email_id = email_ids[0].split()[-1]

            # Fetch the email content
            status, email_data = imap.fetch(latest_email_id, '(RFC822)')
            raw_email = email_data[0][1].decode('utf-8')

            # Parse the email content
            msg = email.message_from_string(raw_email)

            # You can then extract and process the response from the email
            subject = decode_header(msg["Subject"])[0][0]

            # Process the response and determine the next steps based on the content
            if "Yes" in subject:
                print("Received a 'Yes' response")
                response = "approved"
            elif "No" in subject:
                print("Received a 'No' response")
                response = "denied"
            else:
                response = "unknown"  # Handle other cases if needed

            # Close the IMAP connection
            imap.logout()

            # Print the response (you can customize how you use this response)
            print(response)

        # Add a delay (e.g., check every minute)
        time.sleep(60)

    except Exception as e:
        print(f"Error: {str(e)}")
