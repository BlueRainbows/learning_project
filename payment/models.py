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
    payment_course = models.ManyToManyField(Course, verbose_name='Оплаченный курс', **NULLABLE)
    payment_lesson = models.ManyToManyField(Lesson, verbose_name='Оплаченный урок', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма платежа', default=0)
    payment_method = models.CharField(choices=PAYMENT_METHOD, verbose_name='Способ оплаты', **NULLABLE)

    def __str__(self):
        return f'Пользователь: {self.user}. Суммы платежа: {self.payment_amount}.'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
