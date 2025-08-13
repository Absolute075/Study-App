
from django.shortcuts import render

def blocked_view(request):
    return render(request, 'accounts/blocked.html')


