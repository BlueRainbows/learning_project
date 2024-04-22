from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = SerializerMethodField()
    course_lessons = SerializerMethodField()

    def get_course_lessons(self, course):
        course_lessons = Lesson.objects.filter(course=course).values()
        return course_lessons

    def get_count_lessons(self, course):
        count_lessons = Lesson.objects.filter(course=course).count()
        return count_lessons

    class Meta:
        model = Course
        fields = '__all__'
