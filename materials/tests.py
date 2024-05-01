from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course
from users.models import User

COURSES = {'name_course': 'Python',
           'description_course': 'Основы языка Python'}

LESSONS = {'name_lesson': 'Основы языка Python',
           'description_lesson': 'Основные понятия Python разработки'}

USER = {'email': 'Karina@Sapojkina.ru'}


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(**USER)
        self.course = Course.objects.create(**COURSES)
        self.lesson = Lesson.objects.create(**LESSONS, course=self.course, user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_getting_lesson_detail(self):
        """
        Тестирование получения детальной информациии о уроке
        """
        url = reverse('materials:lesson_detail', kwargs={'pk': self.lesson.pk})
        response = self.client.get(url)
        content = response.json()

        # Тест на удачное обращение к уроку
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)

        # Тест на равенство названия урока
        self.assertEqual(
            content.get('name_lesson'), self.lesson.name_lesson)

    def test_creating_lesson(self):
        """
        Тестирование создания урока
        """
        url = reverse('materials:lesson_create')
        data = {'name_lesson': 'C#'}
        response = self.client.post(path=url, data=data, format='json')

        # Тест на удачное создание урока
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED)

        # Тест на колличество уроков
        self.assertEqual(
            Lesson.objects.count(), 2)

        # Тест на прикрепление авторства на урок
        self.assertEqual(
            Lesson.objects.get(name_lesson='C#').user, self.user)

        data = {'name_lesson': 'C#', 'url_lesson': 'https://google.com'}
        response = self.client.post(path=url, data=data, format='json')

        # Тест на ошибку валидации ссылки на урок
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_lesson(self):
        """
        Тестирование изменения урока
        """
        url = reverse('materials:lesson_update', kwargs={'pk': self.lesson.pk})
        data = {'description_lesson': 'Основные понятия Python, синтаксис языка Python'}
        response = self.client.patch(path=url, data=data, format='json')
        content = response.json()

        # Тест на удачное изменение урока
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)

        # Тест на удачное изменение описания урока
        self.assertEqual(
            content.get('description_lesson'), 'Основные понятия Python, синтаксис языка Python')

        data = {'url_lesson': 'https://google.com'}
        response = self.client.patch(path=url, data=data, format='json')

        # Тест на ошибку валидации ссылки на урок
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_lesson(self):
        """
        Тестирование удаление урока
        """
        url = reverse('materials:lesson_destroy', kwargs={'pk': self.lesson.pk})
        response = self.client.delete(path=url)

        # Тест на удачное удаление урока
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT)

    def test_getting_lesson_list(self):
        """
        Тестирование получения списка уроков
        """
        url = reverse('materials:lesson_list')

        response = self.client.get(url)
        content = response.json()

        # Тест на удачное получение списка уроков
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        # Тест на вывод кол-ва уроков
        self.assertEqual(
            content.get('count'), Lesson.objects.all().count()
        )

        # Тест на правильности вывода первого значения списка по названию урока
        self.assertEqual(
            content.get('results')[0].get('name_lesson'),
            Lesson.objects.get(pk=self.lesson.pk).name_lesson)

        # Тест на вывод ошибки при попытке вызова поля несуществующего объекта
        self.assertRaises(
            TypeError,
            Lesson.objects.get(pk=self.lesson.pk).name_lesson,
            'C#'
        )
