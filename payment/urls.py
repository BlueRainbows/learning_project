from django.urls import path
from rest_framework import routers

from payment.apps import PaymentConfig
from payment.views import PaymentViewSet

app_name = PaymentConfig.name

course_router = routers.SimpleRouter()
course_router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [] + course_router.urls
