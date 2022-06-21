import smtplib
from email.mime.text import MIMEText


def send_email(email, height, average_height, count):
    from_email = "udemystudent45@gmail.com"
    from_password = "afnxrchxyhuwtxtj"
    to_email = email

    subject = "Height Data"
    message = f"Hey there, your height is <strong>{height} cm</strong> " \
              f"The average among <strong>{count}</strong> users is <strong>{average_height} cm</strong>"

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
