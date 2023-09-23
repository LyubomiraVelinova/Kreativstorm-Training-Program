# Importing necessary libraries
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import schedule
import logging

# Configure logging
logging.basicConfig(filename='email_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email server settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'custom.demo.email@gmail.com'
EMAIL_PASSWORD = 'ebhylihgrbjwgyww'

# List of recipients
CLIENT_EMAILS = ['lyubomira_mihova@abv.bg', 'lyubomiramihova@gmail.com']

# Report files directory
REPORTS_DIR = 'reports/'


def send_daily_reports():
    # Setting up a connection to the email server (gmail)
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        for email in CLIENT_EMAILS:
            # Building the message content
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = email
            msg['Subject'] = 'Just exercising'
            body = 'This message is only for training use. There is nothing important in it!!!'
            msg.attach(MIMEText(body))

            for filename in os.listdir(REPORTS_DIR):
                filepath = os.path.join(REPORTS_DIR, filename)
                with open(filepath, 'rb') as f:
                    part = MIMEApplication(f.read(), Name=os.path.basename(filepath))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(filepath)}"'
                    msg.attach(part)

            # Sending the email
            server.sendmail(
                from_addr=EMAIL_ADDRESS,
                to_addrs=email,
                msg=msg.as_string()
            )
            logging.info(f'Send report to {email}.')
    except Exception as e:
        logging.error(f'Error: {str(e)}')  # Log errors
    finally:
        server.quit()


# send_daily_reports()
schedule.every().day.at('10:00').do(send_daily_reports)
