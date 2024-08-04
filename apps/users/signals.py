from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from apps.users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def post_save_user(instance, created, *args, **kwargs):
    if not created:
        return
    teacher_group = Group.objects.get(name='teacher')
    admin_group = Group.objects.get(name='admin')
    UserModel = get_user_model()
    if instance.role == UserModel.Role.TEACHER:
        instance.groups.set([teacher_group])
    if instance.role == UserModel.Role.ADMIN:
        instance.groups.set([admin_group])