from django.core.mail import send_mail
from django.conf import settings

from celery import shared_task


@shared_task
def send_verification_email(email, user_name, verification_code):
    send_mail(
        subject="SBD ANIMAL verification",
        message=f"HI {user_name}\nplease enter {verification_code}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[f"{email}"],
        fail_silently=False,
    )
    return "Done"


@shared_task
def test_email():
    send_mail(
        subject="sbd_animal.",
        message="born again",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=["lux00leo@gmail.com", "dlehdgks103@gmail.com"],
        fail_silently=False,
    )
    return "Mail saved haha"
