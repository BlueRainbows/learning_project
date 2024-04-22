from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters
from users.models import User, Payment
from users.serializers.payment import PaymentSerializer
from users.serializers.user import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('payment_course', 'payment_lesson', 'payment_method')
    ordering_fields = ('payment_data',)
