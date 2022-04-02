import contact
import os
from flask_mail import Message
from contact import app

def send_mail(sender, subject, content):
    msg = Message(subject=subject,
                  body=content, 
                  sender=sender)
    
    msg.add_recipient(os.environ["RECIPIENTS"])

    with app.app_context():
        contact.mail.send(msg)
