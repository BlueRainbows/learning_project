from celery import shared_task
from django.core.mail import send_mail

from config import settings
from materials.models import Course
from subscription.models import Subscription


@shared_task
def notify_subscribers_about_course_update(course_id):
    users_list = []
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(course=course)
    if subscriptions.exists():
        for user in subscriptions:
            users_list.append(user.user.email)
    send_mail(
        subject='Курс обновлен',
        message='Зайдите на сайт чтобы посмотреть обновления в курсе',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=users_list,
        fail_silently=False
    )
