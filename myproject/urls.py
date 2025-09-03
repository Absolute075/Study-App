from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout
from django.shortcuts import redirect, render  # Импортируем render
from django.views.decorators.cache import never_cache
from logs.views import dashboard_view

@never_cache
def admin_logout_view(request):
    logout(request)
    return redirect('admin:login')  # редирект на страницу логина

# Убедись, что dashboard view защищено
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def dashboard_view(request):
    return render(request, 'admin/dashboard.html')  # Свой дашборд

urlpatterns = [
    path('admin/logout/', admin_logout_view, name='admin_logout'),  # Логика выхода
    path('admin/dashboard/', dashboard_view, name='admin-dashboard'),  # Дашборд
    path('admin/', admin.site.urls),  # Стандартная админка
    path('api/', include('api.urls')),  # API маршруты
    path('accounts/', include('accounts.urls')),  # Путь для аккаунтов
]
