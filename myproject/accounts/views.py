from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Существующая функция
def blocked_view(request):
    return render(request, 'accounts/blocked.html')


# Новый класс для регистрации через API
@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Пользователь уже существует'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return Response({'message': 'Регистрация прошла успешно'}, status=status.HTTP_201_CREATED)


