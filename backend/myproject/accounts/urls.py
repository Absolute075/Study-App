
from django.urls import path
from .views import blocked_view

urlpatterns = [
    path('blocked/', blocked_view, name='blocked'),
]

