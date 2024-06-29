

# Automated Daily Email Reports
This project automates the sending of daily email reports using Python. It leverages `smtplib` for email sending and `schedule` for task scheduling.

## Features

- Sends a daily email containing a welcome message with inline-styled HTML content.
- Uses `smtplib` to connect to SMTP server (e.g., Gmail) securely.
- Utilizes `schedule` library to schedule and automate email sending at a specified time daily.

## Requirements

- Python 3.x
- `smtplib` library
- `schedule` library

## Installation

1. Clone the repository.
2. Install dependencies:
   - `pip install schedule`
3. Update sender_email and password variables in send_email.py with your email credentials(Not Google account password). Replace with your App Password. Visit https://myaccount.google.com/apppasswords

4. Add recipient email addresses to emails list in send_email.py.

## Usage
1. Modify the HTML content in send_email.py to customize the email body. Keep CSS inline, do not add JS scripts.
2. Adjust the scheduled time in send_email.py using schedule.every().day.at("HH:MM").do(send_emails_to_all).
3. The code should be running at sending time.
