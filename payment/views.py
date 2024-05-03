from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView


from django_filters import rest_framework as filters

from payment.models import Payment
from payment.serializers.payment import PaymentSerializer
from payment.services import create_price, create_session


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('payment_course', 'payment_lesson', 'payment_method')
    ordering_fields = ('payment_data',)


class PaymentCreateAPIView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        pk_product = []
        payment = serializer.save(user=self.request.user)
        if payment.payment_course.all():
            for course in payment.payment_course.all():
                pk_product.append(course.product_id)
            product = pk_product[0]
        else:
            for lesson in payment.payment_lesson.all():
                pk_product.append(lesson.product_id)
            product = pk_product[0]
        price = create_price(payment.payment_amount, product)
        session, payment_url = create_session(price)
        payment.payment_session = session
        payment.payment_url = payment_url
        payment.save()
