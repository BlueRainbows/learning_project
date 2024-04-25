from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters

from payment.models import Payment
from payment.serializers.payment import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('payment_course', 'payment_lesson', 'payment_method')
    ordering_fields = ('payment_data',)

