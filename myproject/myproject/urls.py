
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include  # импортируем include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # подключаем маршруты из api/urls.py
]


