from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return JsonResponse({"error": "Все поля обязательны"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Такой пользователь уже существует"}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return JsonResponse({"message": "Регистрация успешна"}, status=201)

    return JsonResponse({"error": "Метод не разрешён"}, status=405)
