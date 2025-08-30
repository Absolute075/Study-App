
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.utils.timezone import now, timedelta
from .models import ActionLog

@staff_member_required
def dashboard_view(request):
    today = now().date()
    dates = [today - timedelta(days=i) for i in range(6, -1, -1)]
    logs_by_date = [ActionLog.objects.filter(timestamp__date=date).count() for date in dates]

    context = {
        'dates': [d.strftime('%d.%m') for d in dates],
        'logs_by_date': logs_by_date,
    }
    return render(request, 'admin/dashboard.html', context)


