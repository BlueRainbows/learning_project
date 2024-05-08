from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def add_mailing_task(users_list):
    create_mailing = send_mail(
        subject='Курс обновлен',
        message='Зайдите на сайт чтобы посмотреть обновления в курсе',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=users_list,
        fail_silently=False
    )
