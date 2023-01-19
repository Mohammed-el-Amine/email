import asyncio
import smtplib
import email
from email.message import EmailMessage
from aiosmtpd.controller import Controller

class MySMTPHandler:
    async def handle_DATA(self, server, envelope):
        message = EmailMessage()
        message.set_content(envelope.original_content.decode().encode('ascii', 'ignore').decode().split("MIME-Version: 1.0")[1])
        message['From'] = envelope.mail_from
        message['To'] = ', '.join(envelope.rcpt_tos)
        message['Subject'] = envelope.original_content.decode().split("Subject: ")[1].split("\n")[0]
        smtp_server = smtplib.SMTP('vps-f9c60122.vps.ovh.net')
        smtp_server.send_message(message)
        smtp_server.quit()
        return '250 OK'


controller = Controller(MySMTPHandler, hostname='146.59.14.191', port=8025)
loop = asyncio.get_event_loop()
controller.start()
print("Je suis connecter à mon server OVH : vps-f9c60122.vps.ovh.net")
loop.run_forever()
