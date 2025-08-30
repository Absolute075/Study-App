from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)       # заголовок задачи
    description = models.TextField(blank=True)     # описание, необязательное
    done = models.BooleanField(default=False)      # выполнена или нет

    def str(self):
        return self.title

    
