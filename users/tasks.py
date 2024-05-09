from celery import shared_task
from django.utils import timezone
from dateutil.relativedelta import relativedelta
# from django_celery_beat.models import IntervalSchedule, PeriodicTask

from users.models import User

# schedule, created = IntervalSchedule.objects.get_or_create(
#     every=1,
#     period=IntervalSchedule.DAYS,
# )


@shared_task(name='check_user_last_login')
def check_user_last_login():
    now = timezone.now()
    month_ago = now - relativedelta(months=1)

    qs = User.objects.filter(last_login__lte=month_ago, is_active=True)

    for user in qs:
        user.is_active = False
        user.save()
