from django.urls import path
from .views import show_catgory

urlpatterns = [
    path('', show_catgory, name='home'),
    
]