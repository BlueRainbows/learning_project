from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Lesson, Course

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE,
                               default='/users/796d02684eadafba407faf81a4fd697d.png')
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Электронная почта: {self.email}. Телефон: {self.phone}. Город проживания: {self.city}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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
