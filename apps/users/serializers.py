from rest_framework import serializers

from django.contrib.auth import get_user_model

from apps.users.models import CustomUser

UserModel = get_user_model()


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'role', 'email', 'first_name', 'last_name', 'father_name', 'date_of_birth', 'student_group', 'image', 'password']
        extra_kwargs = {
            'student_group': {'required': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'first_name', 'last_name', 'father_name', 'date_of_birth', 'student_group', 'image', 'password']
        extra_kwargs = {
            'student_group': {'required': True},
            'password': {'write_only': True}
        }

{
    "password": "qwerty",
    "email": "muhammadali_student1@gmail.com",
    "first_name": "muhammadali",
    "last_name": "mahammadvaliev",
    "student_group": "1",
    "date_of_birth": "2000-1-1"
}


class TeacherRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'role', 'email', 'first_name', 'last_name', 'father_name', 'date_of_birth', 'subject', 'salary', 'image', 'password']
        extra_kwargs = {
            'subject': {'required': True},
            'salary': {'required': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        obj = super().validate(attrs)
        if obj['salary'] <= 0:
            raise serializers.ValidationError({'salary':'A teacher should have a salary'})
        return obj
    
    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)
    

class TeacherUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'first_name', 'last_name', 'father_name', 'date_of_birth', 'subject', 'salary', 'image', 'password']
        extra_kwargs = {
            'subject': {'required': True},
            'salary': {'required': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        obj = super().validate(attrs)
        if obj['salary'] <= 0:
            raise serializers.ValidationError({'salary':'A teacher should have a salary'})
        return obj
    
{
    "password": "qwerty",
    "email": "muhammadali_teacher@gmail.com",
    "first_name": "muhammadali",
    "last_name": "mahammadvaliev",
    "subject": "1",
    "salary":"20000000",
    "date_of_birth": "2000-1-1"
}