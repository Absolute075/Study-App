
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done')       # какие колонки показывать в списке
    list_filter = ('done',)                       # фильтр по статусу задачи
    search_fields = ('title', 'description')     # поиск по заголовку и описанию
    ordering = ('-id',)                           # сортировка — новые задачи сверху

