from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, DestroyAPIView

from apps.users import permissions
from apps.users.models import CustomUser
from apps.users.serializers import StudentRegisterSerializer, StudentUpdateSerializer, TeacherRegisterSerializer, TeacherUpdateSerializer 


class StudentRegisterAPIView(APIView):
    permission_classes = [permissions.AddStudentPermission]

    def get(self, request):
        serializer = StudentRegisterSerializer(get_user_model().objects.filter(role=CustomUser.Role.STUDENT), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        request.data['role'] = 3
        serializer = StudentRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    

class RetrieveStudentAPIView(RetrieveAPIView):
    permission_classes = [permissions.ViewStudentPermission]

    queryset = get_user_model().objects.filter(role=CustomUser.Role.STUDENT)
    serializer_class = StudentRegisterSerializer


class UpdateStudentAPIView(UpdateAPIView):
    permission_classes = [permissions.ChangeStudentPermission]

    queryset = get_user_model().objects.filter(role=CustomUser.Role.STUDENT)
    serializer_class = StudentUpdateSerializer


class DeleteStudentAPIView(DestroyAPIView):
    permission_classes = [permissions.DeleteStudentPermission]

    queryset = get_user_model().objects.filter(role=CustomUser.Role.STUDENT)


class TeacherRegisterAPIView(APIView):
    permission_classes = [permissions.AddTeacherPermission]

    def get(self, request):
        serializer = TeacherRegisterSerializer(get_user_model().objects.filter(role=CustomUser.Role.TEACHER), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        request.data['role'] = 2
        serializer = TeacherRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class UpdateTeacherAPIVew(UpdateAPIView):
    permission_classes = [permissions.ChangeTeacherPermission]

    queryset = get_user_model().objects.filter(role=CustomUser.Role.TEACHER)
    serializer_class = TeacherUpdateSerializer


class RetrieveTeacherAPIVew(RetrieveAPIView):
    permission_classes = [permissions.ViewTeacherPermission]

    queryset = get_user_model().objects.filter(role=CustomUser.Role.TEACHER)
    serializer_class = TeacherRegisterSerializer


class DeleteTeacherAPIView(APIView):
    permission_classes = [permissions.DeleteTeacherPermission]

    def get(self, request, pk):
        teacher = get_object_or_404(get_user_model(), pk=pk)
        if teacher.teacher_groups.all().exists():
            print(teacher.teacher_groups.all())
            return Response({'error': 'This teacher has groups.'}, status=400)
        teacher.delete()
        return Response(status=204)