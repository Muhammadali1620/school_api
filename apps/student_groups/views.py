from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.student_groups.models import StudentGroup
from apps.student_groups.serializers import StudentGroupSerializer
from apps.users.permissions import AddStudentGroupPermission, ViewStudentGroupPermission


class ListCreateStudentGroupAPIView(APIView):
    permission_classes = [AddStudentGroupPermission]

    def get(self, request):
        serializer = StudentGroupSerializer(StudentGroup.objects.all(), many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = StudentGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class DeleteStudentUpdateGroupAPIView(APIView):
    permission_classes = [ViewStudentGroupPermission]

    def get(self, request, pk):
        student_group = get_object_or_404(StudentGroup, pk=pk)
        serializer = StudentGroupSerializer(student_group)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        student_group = get_object_or_404(StudentGroup, pk=pk)
        student_group.delete()
        return Response(status=204)

    def patch(self, request, pk):
        student_group = get_object_or_404(StudentGroup, pk=pk)
        serializer = StudentGroupSerializer(student_group, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)