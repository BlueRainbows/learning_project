from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentViewSet

app_name = UsersConfig.name

course_router = routers.SimpleRouter()
course_router.register(r'user', UserViewSet, basename='user')
course_router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [] + course_router.urls
