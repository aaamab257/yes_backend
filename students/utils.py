from django.core.mail import EmailMessage
import os
import threading

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

class Util:
    @staticmethod
    def send_email(data):
      email = EmailMessage(
        subject=data['subject'],
        body=data['body'],
        from_email=os.environ.get('EMAIL_FROM'),
        to=[data['to_email']]
      )
      EmailThread(email).start()