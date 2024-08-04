from django.core.management import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_customuser = ContentType.objects.filter(app_label='users', model='customuser').first()

        #<=========>Students<=========>#
        view_student = Permission.objects.create(
            codename='view_students',
            name='Can view students',
            content_type=user_customuser
        )

        add_student = Permission.objects.create(
            codename='add_students',
            name='Can add students',
            content_type=user_customuser
        )

        change_student = Permission.objects.create(
            codename='change_students',
            name='Can change students',
            content_type=user_customuser
        )

        delete_student = Permission.objects.create(
            codename='delete_students',
            name='Can delete students',
            content_type=user_customuser
        )


        #<=========>Teachers<=========>#
        view_teacher = Permission.objects.create(
            codename='view_teachers',
            name='Can view teachers',
            content_type=user_customuser
        )

        add_teacher = Permission.objects.create(
            codename='add_teachers',
            name='Can add teachers',
            content_type=user_customuser
        )

        change_teacher = Permission.objects.create(
            codename='change_teachers',
            name='Can change teachers',
            content_type=user_customuser
        )

        delete_teacher = Permission.objects.create(
            codename='delete_teachers',
            name='Can delete teachers',
            content_type=user_customuser
        )
        
        self.stdout.write(self.style.SUCCESS(f"8-perms created"))