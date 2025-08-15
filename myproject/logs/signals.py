
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.models import User
from .models import ActionLog
from accounts.models import Profile


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
    if sender._meta.app_label not in ["logs", "accounts", "myapp"]:
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
        Profile.objects.get_or_create(user=instance)

# ==========================
# Логирование изменений пользователя с историей
# ==========================
@receiver(pre_save, sender=User)
def cache_old_user_data(sender, instance, **kwargs):
    """Сохраняем старые данные пользователя перед сохранением"""
    if instance.pk:
        try:
            old_instance = User.objects.get(pk=instance.pk)
            instance._old_data = {
                "first_name": old_instance.first_name,
                "last_name": old_instance.last_name,
                "email": old_instance.email,
            }
        except User.DoesNotExist:
            instance._old_data = {}
    else:
        instance._old_data = {}

@receiver(post_save, sender=User)
def log_user_update(sender, instance, created, **kwargs):
    """Логируем изменения пользователя после сохранения"""
    if created:
        # уже создаётся профиль и логируется через create_user_profile
        return

    old_data = getattr(instance, "_old_data", {})
    changes = {}
    for field in ["first_name", "last_name", "email"]:
        old_value = old_data.get(field)
        new_value = getattr(instance, field)
        if old_value != new_value:
            changes[field] = {"old": old_value, "new": new_value}

    if changes:
        ActionLog.objects.create(
            user=instance,
            action_type="update",
            description=f"Обновлён пользователь {instance.username}",
            extra_data=changes
        )


