from app import models, views
from app import app
import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, mensaje, asunto):

    email_domo = "teamdomorestaurantes@gmail.com"
    passw = "yuyfufiubxaeclpz"
    message = MIMEText(mensaje)
    message['Subject'] = asunto
    message['From'] = "teamdomorestaurantes@gmail.com"
    message['To'] = destinatario

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_domo, passw)
    server.sendmail(email_domo, destinatario, message.as_string())
    server.quit()

