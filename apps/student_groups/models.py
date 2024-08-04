from django.db import models
from apps.users.models import CustomUser
from django.conf import settings
from django.core.exceptions import ValidationError
from apps.subjects.models import Subject
from django.contrib.postgres.fields import ArrayField


class StudentGroup(models.Model):
    class WeekDays(models.IntegerChoices):
        mo = 0, 'Monday'
        tu = 1, 'Tuesday'
        we = 2, 'Wednesday'
        th = 3, 'Thursday'
        fr = 4, 'Friday'
        sa = 5, 'Saturday'
        su = 6, 'Sunday'

    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, limit_choices_to={'role': CustomUser.Role.TEACHER.value},
                                related_name='teacher_groups')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name='student_groups')
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_days = ArrayField(base_field=models.PositiveSmallIntegerField(choices=WeekDays.choices))

    created_at = models.DateTimeField(auto_now_add=True)        

    def __str__(self):
        return f'{self.subject.name} ({self.start_time.strftime("%H:%M")}-{self.end_time.strftime("%H:%M")})'