from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        can_add_attendance = Permission.objects.get(codename='add_attendance')    
        can_view_attendance = Permission.objects.get(codename='view_attendance')
        can_view_student = Permission.objects.get(codename='view_students')

        teacher_group = Group.objects.create(name='teacher',)
        teacher_group.permissions.set([can_add_attendance, can_view_attendance, can_view_student])
        
        admin_group = Group.objects.create(name='admin',)
        admin_group.permissions.set(Permission.objects.exclude(codename=can_add_attendance))
        
        self.stdout.write(self.style.SUCCESS(f"{Group.objects.count()}-groups created"))