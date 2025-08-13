
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.models import User
from .models import ActionLog
from accounts.models import Profile  # <-- правильно импортируем Profile

# ==========================
# Логирование входа/выхода пользователей
# ==========================

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ActionLog.objects.create(
        user=user,
        action_type="login",
        description=f"Пользователь {user.username} вошёл в систему",
        extra_data={"ip": request.META.get('REMOTE_ADDR')}
    )

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ActionLog.objects.create(
        user=user,
        action_type="logout",
        description=f"Пользователь {user.username} вышел из системы",
        extra_data={"ip": request.META.get('REMOTE_ADDR')}
    )

# ==========================
# Логирование создания, изменения и удаления моделей
# ==========================

@receiver(post_save)
def log_model_save(sender, instance, created, **kwargs):
    if sender.__name__ in ["ActionLog", "Profile"]:
        return
    if sender._meta.app_label not in ["logs", "accounts", "myapp"]:  # укажи свои приложения
        return

    ActionLog.objects.create(
        user=getattr(instance, "user", None),
        action_type="create" if created else "update",
        description=f"{'Создан' if created else 'Обновлён'} объект {sender.__name__} (ID: {instance.pk})",
        extra_data={"model": sender.__name__, "id": instance.pk}
    )

@receiver(post_delete)
def log_model_delete(sender, instance, **kwargs):
    if sender.__name__ in ["ActionLog", "Profile"]:
        return
    if sender._meta.app_label not in ["logs", "accounts", "myapp"]:
        return

    ActionLog.objects.create(
        user=getattr(instance, "user", None),
        action_type="delete",
        description=f"Удалён объект {sender.__name__} (ID: {instance.pk})",
        extra_data={"model": sender.__name__, "id": instance.pk}
    )

# ==========================
# Авто-создание профиля для пользователей
# ==========================

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
