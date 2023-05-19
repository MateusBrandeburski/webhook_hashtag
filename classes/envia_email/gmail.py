import os
import smtplib
from email.message import EmailMessage

def envia_email():
    #consgiurar email, senha
    EMAIL_ADDRESS = 'mateus@trovale.com.br'
    EMAIL_PASSWORD = ''

    msg = EmailMessage()
    msg['Subject'] = 'WebHooks'
    msg['From'] = 'mateus@trovale.com.br'
    msg['To'] = 'mateus.brandeburski92@gmail.com'
    msg.set_content("receba")


    # Enviar email
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
 
 
 