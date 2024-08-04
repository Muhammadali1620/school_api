from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers import CustomUserManager
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class CustomUser(AbstractUser):

    class Role(models.IntegerChoices):
        ADMIN = 1, 'admin'
        TEACHER = 2, 'teacher'
        STUDENT = 3, 'student'
    
    username = None
    objects = CustomUserManager()

    role = models.PositiveSmallIntegerField(choices=Role.choices, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    father_name = models.CharField(max_length=70, blank=True)
    date_of_birth = models.DateField()
    student_group = models.ForeignKey('student_groups.StudentGroup', on_delete=models.PROTECT, blank=True, null=True, related_name='students')
    subject = models.ForeignKey('subjects.Subject', on_delete=models.PROTECT, blank=True, null=True, related_name='teacher')
    salary = models.DecimalField(default=0, max_digits=20, decimal_places=2, help_text='add in UZS',
                                 validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='user/student', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role', 'date_of_birth']
        
    @classmethod
    def get_all_student_in_group(cls, user):
        if not user.teacher_groups:
            return None
        students = []
        for group in user.teacher_groups.all():
            for student in group.students.all():
                students.append(student)
        return students
    
    class Meta:
        ordering = ['-pk']
    
    def __str__(self):
        return f'{self.get_role_display()}: {self.first_name} {self.last_name}'