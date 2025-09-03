from django.urls import path
from .views import RegisterView, blocked_view

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('blocked/', blocked_view, name='blocked'),
]
