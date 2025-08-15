
# logs/signals.py
from django.db.models.signals import post_save, post_delete, pre_save
from django.contrib.auth.signals import user_logged_in, user_logged_out, password_change
from django.dispatch import receiver
from django.contrib.auth.models import User
from logs.models import ActionLog


# ===== Логин =====
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ActionLog.objects.create(
        user=user,
        action_type="login",
        description=f"Пользователь {user.username} вошёл в систему"
    )

# ===== Логаут =====
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ActionLog.objects.create(
        user=user,
        action_type="logout",
        description=f"Пользователь {user.username} вышел из системы"
    )

# ===== Создание и изменение пользователя =====
@receiver(post_save, sender=User)
def log_user_create_update(sender, instance, created, **kwargs):
    if created:
        ActionLog.objects.create(
            user=instance,
            action_type="create",
            description=f"Создан новый пользователь: {instance.username}"
        )
    else:
        ActionLog.objects.create(
            user=instance,
            action_type="update",
            description=f"Пользователь {instance.username} был изменён"
        )

# ===== Удаление пользователя =====
@receiver(post_delete, sender=User)
def log_user_delete(sender, instance, **kwargs):
    ActionLog.objects.create(
        user=None,
        action_type="delete",
        description=f"Пользователь {instance.username} был удалён"
    )

# ===== Сброс или изменение пароля =====
@receiver(password_change)
def log_password_change(sender, request, user, **kwargs):
    ActionLog.objects.create(
        user=user,
        action_type="update",
        description=f"Пользователь {user.username} сменил пароль"
    )


