from django.urls import path
from rest_framework import routers

from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionView

app_name = SubscriptionConfig.name

urlpatterns = [
    path('subscription', SubscriptionView.as_view(), name='subscription')
]
