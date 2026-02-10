import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(to:str,subject:str,body:str):
    smtp_host="smtp.gmail.com"
    smtp_port=587

    sender_email="g.ashutosh2501@gmail.com"
    sender_password=os.getenv("SMTP_APP_PASSWORD")

    message=MIMEMultipart()
    message["From"]=sender_email
    message["To"]=to
    message["Subject"]=subject

    message.attach(MIMEText(body,"plain"))

    with smtplib.SMTP(smtp_host,smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email,sender_password)
        server.send_message(message)

    return {"status":"email sent via smtp"}