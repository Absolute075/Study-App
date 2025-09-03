
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from logs.views import dashboard_view

@never_cache
def admin_logout_view(request):
    logout(request)
    return redirect('/admin/login/')  # переход на страницу логина в админке

urlpatterns = [
    path('admin/logout/', admin_logout_view, name='admin_logout'),

    # Дашборд в админке
    path('admin/dashboard/', dashboard_view, name='admin-dashboard'),

    # Стандартная админка
    path('admin/', admin.site.urls),

    # Другие маршруты
    path('api/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
]


