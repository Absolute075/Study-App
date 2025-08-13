
from django.shortcuts import redirect
from django.urls import reverse

class BlockedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile = getattr(request.user, 'profile', None)
            if profile and profile.is_blocked:
                # Перенаправляем заблокированного пользователя на страницу блокировки
                return redirect(reverse('blocked'))
        response = self.get_response(request)
        return response

