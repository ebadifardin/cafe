from django.shortcuts import render
from .models import Catgory
# Create your views here.
def show_catgory(request):
    cate_obj=Catgory.objects.all()
    contaxe={
        "cate":cate_obj
    }
    return render(request,'base.html',contaxe)
