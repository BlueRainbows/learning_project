# Generated by Django 5.0.4 on 2024-04-25 11:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0002_course_user_lesson_user_alter_lesson_course'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_data', models.DateField(blank=True, null=True, verbose_name='Дата оплаты')),
                ('payment_amount', models.PositiveIntegerField(default=0, verbose_name='Сумма платежа')),
                ('payment_method', models.CharField(blank=True, choices=[('Наличные', 'Оплата наличными'), ('Перевод', 'Перевод на счёт')], null=True, verbose_name='Способ оплаты')),
                ('payment_course', models.ManyToManyField(blank=True, null=True, to='materials.course', verbose_name='Оплаченный курс')),
                ('payment_lesson', models.ManyToManyField(blank=True, null=True, to='materials.lesson', verbose_name='Оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]
