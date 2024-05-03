from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.pagination import PaginationLesson
from materials.serializers.lesson import LessonSerializer
from materials.services import create_product_lesson
from users.permissions import PermissionModer, PermissionUser


class LessonDetailView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, PermissionUser | PermissionModer]


class LessonListView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PaginationLesson


class LessonCreateView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, PermissionUser & ~PermissionModer]

    def perform_create(self, serializer):
        lesson = serializer.save(user=self.request.user)
        product = create_product_lesson(lesson.name_lesson, lesson.description_lesson)
        lesson.product_id = product
        lesson.save()


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, PermissionUser | PermissionModer]


class LessonDestroyView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~PermissionModer | PermissionUser]
