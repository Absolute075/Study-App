
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Если создан новый пользователь — создаём профиль
    if created:
        Profile.objects.create(user=instance)
    else:
        # Для существующих пользователей проверяем, есть ли профиль
        Profile.objects.get_or_create(user=instance)


