from django.urls import path
from rest_framework import routers

from payment.apps import PaymentConfig
from payment.views import PaymentListAPIView, PaymentCreateAPIView

# from payment.views import PaymentViewSet

app_name = PaymentConfig.name

# course_router = routers.SimpleRouter()
# course_router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment_list'),
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    # path('detail/<int:pk>', LessonDetailView.as_view(), name='lesson_detail'),
    # path('update/<int:pk>', LessonUpdateView.as_view(), name='lesson_update'),
    # path('delete/<int:pk>', LessonDestroyView.as_view(), name='lesson_destroy'),
]
# + course_router.urls)
