
# logs/signals.py
from django.db.models.signals import post_save, post_delete, pre_save
from django.contrib.auth.signals import user_logged_in, user_logged_out, password_change
from django.dispatch import receiver
from django.contrib.auth.models import User
from logs.models import ActionLog



# Вход пользователя
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ActionLog.objects.create(
        user=user,
        action_type="login",
        description="Пользователь вошёл в систему"
    )

# Выход пользователя
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ActionLog.objects.create(
        user=user,
        action_type="logout",
        description="Пользователь вышел из системы"
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

# Отслеживание смены пароля
@receiver(pre_save, sender=User)
def log_password_change(sender, instance, **kwargs):
    if instance.pk:  # уже существует в базе
        old_password = User.objects.get(pk=instance.pk).password
        if old_password != instance.password:
            ActionLog.objects.create(
                user=instance,
                action_type="update",
                description="Смена пароля"
            )

