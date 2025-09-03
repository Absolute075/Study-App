
from django.db import models
from django.contrib.auth.models import User

class ActionLog(models.Model):
    ACTION_TYPES = [
        ("create", "Создание"),
        ("update", "Изменение"),
        ("delete", "Удаление"),
        ("login", "Вход"),
        ("logout", "Выход"),
        ("custom", "Другое"),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пользователь")
    action_type = models.CharField(max_length=20, choices=ACTION_TYPES, verbose_name="Тип действия")
    description = models.TextField(verbose_name="Описание")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время")
    extra_data = models.JSONField(null=True, blank=True, verbose_name="Доп. данные")

    class Meta:
        verbose_name = "Лог действия"
        verbose_name_plural = "Логи действий"
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.timestamp} — {self.user} — {self.get_action_type_display()}"

