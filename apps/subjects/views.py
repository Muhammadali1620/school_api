from rest_framework.views import APIView
from rest_framework.response import Response

from apps.subjects.models import Subject
from apps.subjects.serializers import SubjectSerializer
from apps.users.permissions import AddSubjectPermission


class SubjectListCreateAPIView(APIView):
    permission_classes = [AddSubjectPermission]

    def get(self, request):
        serializer = SubjectSerializer(Subject.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)