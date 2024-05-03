from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_field, extend_schema_serializer, OpenApiParameter
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from materials.serializers.lesson import LessonSerializer
from materials.validators import UrlValidator
from subscription.models import Subscription


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = SerializerMethodField()
    course_lessons = SerializerMethodField()
    current_subscriptions = SerializerMethodField()

    @extend_schema_field(OpenApiTypes.STR)
    def get_current_subscriptions(self, course):
        user = self.context['request'].user
        if Subscription.objects.filter(user=user, course=course):
            current_subscriptions = "Вы подписаны на курс"
        else:
            current_subscriptions = "Вы не подписаны на курс"
        return current_subscriptions

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_course_lessons(self, course):
        course_lessons = Lesson.objects.filter(course=course).values()
        return course_lessons

    @extend_schema_field(OpenApiTypes.INT)
    def get_count_lessons(self, course):
        count_lessons = Lesson.objects.filter(course=course).count()
        return count_lessons

    class Meta:
        model = Course
        fields = '__all__'
        validators = [UrlValidator(field='url_course')]
