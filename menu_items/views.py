from django.shortcuts import render
from .models import MenuItem

def show_menu(request):
    menu_obj=MenuItem.objects.all()
    contaxe={
        "menu":menu_obj
    }

    return render(request,"menu.html",contaxe)