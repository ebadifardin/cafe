from django.urls import path
from .views import show_catgory,post

urlpatterns = [
    path('', show_catgory, name='home'),
    path('',post,name='createpoll')
]