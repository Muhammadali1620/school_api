from django.db import models

from apps.student_groups.models import StudentGroup

from rest_framework import serializers
from django.contrib.auth import get_user_model


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'

    def validate(self, attrs):
        obj = super().validate(attrs)
        teacher = get_user_model().objects.filter(id=obj['teacher'].id).first()
        if teacher.teacher_groups.exists():
            raise serializers.ValidationError({"teacher": "Teacher doesn't have any groups"})
        return obj

{
    "start_time": "10:00",
    "end_time": "12:00",
    "week_days": [0,2,4],
    "teacher": "1",
    "subject": "1"
}