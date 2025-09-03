from django.contrib import admin
from .models import ActionLog

@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "user", "action_type", "description")
    list_filter = ("action_type", "timestamp", "user")
    search_fields = ("description", "extra_data")
    readonly_fields = ("timestamp",)



from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.utils.timezone import now, timedelta
from .models import ActionLog

class CustomAdminSite(admin.AdminSite):
    site_header = "Админка с дашбордом"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return my_urls + urls

    def dashboard_view(self, request):
        # Собираем данные за последние 7 дней по типам действий
        today = now().date()
        dates = [today - timedelta(days=i) for i in range(6, -1, -1)]

        logs_by_date = []
        for date in dates:
            count = ActionLog.objects.filter(timestamp__date=date).count()
            logs_by_date.append(count)

        context = dict(
            self.each_context(request),
            logs_by_date=logs_by_date,
            dates=[d.strftime("%d.%m") for d in dates],
        )
        return TemplateResponse(request, "admin/dashboard.html", context)

# Зарегистрируем новый админ сайт (если используешь кастомный)
admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(ActionLog)
