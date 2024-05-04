from django.db import models

from materials.models import Course, Lesson
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):

    PAYMENT_METHOD = [
        ('Наличные', 'Оплата наличными'),
        ('Перевод', 'Перевод на счёт')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_data = models.DateField(verbose_name='Дата оплаты', **NULLABLE)
    payment_course = models.ForeignKey(Course, verbose_name='Оплаченный курс', on_delete=models.CASCADE, **NULLABLE)
    payment_lesson = models.ForeignKey(Lesson, verbose_name='Оплаченный урок', on_delete=models.CASCADE,  **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма платежа', default=0)
    payment_method = models.CharField(choices=PAYMENT_METHOD, verbose_name='Способ оплаты', **NULLABLE)

    payment_session = models.CharField(max_length=200, verbose_name='Сессия платежа', **NULLABLE)
    payment_url = models.URLField(max_length=400, verbose_name='Ссылка для оплаты', **NULLABLE)

    def __str__(self):
        return f'Пользователь: {self.user}. Суммы платежа: {self.payment_amount}.'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
