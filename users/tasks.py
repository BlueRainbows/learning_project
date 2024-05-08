from datetime import datetime, timedelta
from calendar import monthrange
from celery import shared_task

from users.models import User


@shared_task(name='check_user_last_login')
def check_user_last_login():
    year = datetime.now().year
    month = datetime.now().month
    days = monthrange(year, month)[1]
    last_date_for_login = datetime.now() - timedelta(days=days)

    users = User.objects.all()
    srp_last_date = last_date_for_login.strftime('%Y-%m-%d')
    date_object_last_date = datetime.strptime(srp_last_date, '%Y-%m-%d').date()

    for user in users:
        if user.last_login is not None:
            srp_last_login = user.last_login.strftime('%Y-%m-%d')
            date_object_last_login = datetime.strptime(srp_last_login, '%Y-%m-%d').date()
            if date_object_last_login <= date_object_last_date:
                user.is_active = False
                user.save()
