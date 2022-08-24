from app import models, views
from app.models import domo_usuario
from app import app
import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, mensaje, asunto):

    print(destinatario,mensaje,asunto)

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

def enviar_email_cliente(cliente, mensaje, asunto):
    corr_destino = cliente.cli_correo
    
    if(corr_destino == None):
        corr_destino = domo_usuario.get_by_cliente(cliente.cli_id).usr_login
    enviar_email(corr_destino, mensaje, asunto)

def recordatorio():
    lista = models.domo_reserva.get_reservas_today()
    for n in lista:
        cliente = n.get_cliente()
        mensaje = "Recordatorio de que hoy tienes una reserva, con id " + n.rsv_id + " a las " + n.rsv_hora
        enviar_email_cliente(cliente, mensaje, "Recordatorio Reserva")
        
