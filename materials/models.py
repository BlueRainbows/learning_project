from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name_course = models.CharField(max_length=200, verbose_name='Название курса')
    image_course = models.ImageField(upload_to='courses/', verbose_name='Превью курса', **NULLABLE)
    description_course = models.TextField(verbose_name='Описание курса', **NULLABLE)

    def __str__(self):
        return f'{self.name_course}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=200, verbose_name='Название урока')
    image_lesson = models.ImageField(upload_to='lessons/', verbose_name='Превью урока', **NULLABLE)
    description_lesson = models.TextField(verbose_name='Описание урока', **NULLABLE)
    url_lesson = models.URLField(verbose_name='Ссылка на урок', **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)

    def __str__(self):
        return f'{self.name_lesson}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
