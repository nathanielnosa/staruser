from django.core.mail import send_mail
from django.conf import settings

def SendMail(email,fullname):
    subject = "welcome to star web"
    message = f'''
            Welcome {fullname}.
            This is a welcome message from the DevOps.
            we want to specially welcome for registring
'''
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email,fullname],
        fail_silently=False,
    )