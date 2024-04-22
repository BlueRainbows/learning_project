from rest_framework import serializers

from materials.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('course',)
