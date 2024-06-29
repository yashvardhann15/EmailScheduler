import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time


sender_email = ""  # Replace with your email

password = ""  # Replace with your App Password. Visit https://myaccount.google.com/apppasswords

def send_email(receiver_email):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Daily Report"
    msg['From'] = sender_email
    msg['To'] = receiver_email

# Replace with your HTML content. Note: All the css should be inline in the HTML and JS can't be used.
    html = r"""  
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome Page</title>
        </head>
        <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f5f5f5; color: #333;">
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; text-align: center; padding: 20px;">
                <div style="background-color: #4CAF50; color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                    <h1 style="margin: 0; font-size: 36px;">Welcome to Our Website!</h1>
                    <p style="margin: 10px 0 20px; font-size: 18px;">We're glad to have you here. Explore and enjoy your stay.</p>
                    <a href="#" style="display: inline-block; padding: 10px 20px; margin-top: 10px; font-size: 16px; color: #4CAF50; background-color: white; border-radius: 5px; text-decoration: none; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">Get Started</a>
                </div>
            </div>
        </body>
        </html>

    """

    part2 = MIMEText(html, 'html')
    msg.attach(part2)


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")




emails = ["@gmail.com", "@gmail.com"]   # Replace with the email addresses you want to send the email to

def send_emails_to_all():
    for email in emails:
        send_email(email)
schedule.every().day.at("12:10").do(send_emails_to_all)  # Replace with the time you want to send the email at

while True:
    schedule.run_pending()
    time.sleep(1)
    


