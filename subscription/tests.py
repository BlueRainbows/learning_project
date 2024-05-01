from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course
from users.models import User

USER = {'email': 'Karina@Sapojkina.ru'}

COURSES = {'name_course': 'Python',
           'description_course': 'Основы языка Python'}


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(**USER)
        self.course = Course.objects.create(**COURSES)
        self.client.force_authenticate(user=self.user)

    def test_post_subscription(self):
        """
        Тест добавления подписки к курсу
        """
        url = reverse('subscription:subscription')
        content = {'course_id': self.course.id}
        response = self.client.post(url, content)
        message = response.json()

        # Тест на успешный ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Тест на успешную подписку у пользователя
        self.assertEqual(message['message'], 'подписка добавлена')

        response = self.client.post(url, content)
        message = response.json()

        # Тест на отписку от курса при повторной отправке запроса
        self.assertEqual(message['message'], 'подписка удалена')
