# Generated by Django 5.0.4 on 2024-04-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_course_user_lesson_user_alter_lesson_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='url_course',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на курс'),
        ),
    ]
