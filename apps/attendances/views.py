import calendar
from django.utils.timezone import now

from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.attendances.models import Attendance
from apps.attendances.serializers import AttendanceSerializer
from apps.users.models import CustomUser
from apps.users.permissions import AddAttendancePermission
from django.shortcuts import get_object_or_404


class AttendanceCreateAPIVew(APIView):
    permission_classes = [AddAttendancePermission]

    def post(self, request):
        if request.user.role == CustomUser.Role.TEACHER:
            if not request.data['student']:
                return Response({'student': 'This field is required'}, status=400)
            group = request.user.teacher_groups.first()
            student = get_object_or_404(get_user_model(), id=request.data['student'])
            if not student in group.students.all():
                return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        request.data['date'] = now().date()
        serializer = AttendanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
    def get(self, request):
        context = {}
        group_id = self.request.GET.get('group_id', '')
        year = self.request.GET.get('year', '')
        month = self.request.GET.get('month', '')

        if month.isdigit() and year.isdigit():
            days = list(range(1, calendar.monthrange(int(year), int(month))[1] + 1))
        else:
            days = []

        if group_id and month.isdigit() and year.isdigit():
            context['students'] = list(get_user_model().objects.filter(student_group_id=group_id
                                                                 ).prefetch_related('student_attendance'
                                                                    ).order_by('first_name'
                                                                        ).values('id', 'first_name', 'last_name'))
            attendances = list(Attendance.objects.filter(student__student_group_id=group_id,
                                                        date__year=year, 
                                                        date__month=month).values())
            for student in context['students']:
                student['attendances'] = []
                for day in days:
                    for attendance in attendances:
                        if attendance['date'].day == day and attendance['student_id'] == student['id']:
                            obj = {'come': attendance['come'], 'rezone': attendance['rezone'], 'day': day}
                            break
                    else:
                        obj = {'come': '', 'rezone': '', 'day': day}
                    student['attendances'].append(obj)
        else:
            context['students'] = []
        
        if request.user.role == CustomUser.Role.TEACHER and group_id.isdigit() and int(group_id) != request.user.teacher_groups.first().id:
            print(group_id)
            print(request.user.teacher_groups.first().id)
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        
        return Response(context, status=200)