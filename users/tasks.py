import logging

from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from users.models import User

logger = logging.getLogger(__name__)


@shared_task()
def check_user_last_login():
    now = timezone.now()
    month_ago = now - relativedelta(months=1)

    qs = User.objects.filter(last_login__lte=month_ago)
    qs = qs.exclude(is_active=False)

    deactivated_users_count = 0
    for user in qs:
        user.is_active = False
        deactivated_users_count += 1

    if deactivated_users_count:
        User.objects.bulk_update(qs, ['is_active'])
        logger.info(f'{deactivated_users_count} deactivated users')
