from rest_framework import serializers
from apps.attendances.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        extra_kwargs = {
            'date': {'required': True},
        }


{
    "student":"5"
}