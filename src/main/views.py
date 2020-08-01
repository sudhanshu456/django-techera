from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from .models import Blogpost

def index(request):
    
    return render(request,'test.html')


def data(request):
    queryset=Blogpost.objects.all()
    context={
        'data':queryset,
    }
    return render(request,'home.html',context)


def register(request):
    form=UserCreationForm
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    context={'form':form}
    return render(request,'register.html',context)


def logouts(request):
    logout(request)
    return redirect('/')