from django.shortcuts import render,redirect
from django.contrib import messages

from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .models import Blogpost

from .forms import BlogpostForm
from django.views.generic import CreateView



class CreateBlogPost(CreateView):
    template_name='create.html'
    form_class=BlogpostForm
    success_url = '/'




def index(request):
    
    return render(request,'test.html')


def data(request):
    queryset=Blogpost.objects.all()
    context={
        'data':queryset,
    }
    return render(request,'home.html',context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

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






def logins(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')   
    else:
        return render(request,'login.html')    

