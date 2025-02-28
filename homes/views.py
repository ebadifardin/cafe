from django.shortcuts import render,redirect
from .models import Catgory,Pool
from .forms import PollCreateForm
# Create your views here.
def show_catgory(request):
    cate_obj=Catgory.objects.all()
    contaxe={
        "cate":cate_obj
    }
    return render(request,'base.html',contaxe)
def post(self,request):
    forms=PollCreateForm(request.POST)
    if forms.is_valid():
        
        Pool.objects.create(name=forms.cleaned_data.get('name'),
                            email=forms.cleaned_data.get('email'),
                            message=forms.cleaned_data.get('message'))
        return redirect ('/')
    return render(request,'base.html')