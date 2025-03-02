from django.urls import path
from .views import show_menu

urlpatterns = [
    path('menu/',show_menu)
]