from django.urls import path
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views.course import CourseViewSet
from materials.views.lesson import LessonListView, LessonCreateView, LessonUpdateView, LessonDestroyView, \
    LessonDetailView

app_name = MaterialsConfig.name

course_router = routers.SimpleRouter()
course_router.register(r'course', CourseViewSet, basename='courses')

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/detail/<int:pk>', LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', LessonDestroyView.as_view(), name='lesson_destroy'),
] + course_router.urls
