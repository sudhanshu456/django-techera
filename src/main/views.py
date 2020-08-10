from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .models import Blogpost

from .forms import BlogpostForm
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,DetailView



class ListBlogPost(ListView):
    template_name='list.html'
    queryset=Blogpost.objects.all()
    
class DetailBlogPost(LoginRequiredMixin,DetailView):
    template_name='detail.html'
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Blogpost,id=id_)

class DeleteBlogPost(LoginRequiredMixin,DeleteView):
    template_name='delete.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Blogpost, id=id_)
    def get_success_url(self):
        return reverse('main:list')

class CreateBlogPost(LoginRequiredMixin,CreateView):
    template_name='create.html'
    form_class=BlogpostForm
    success_url = '/'

class UpdateBlogPost(LoginRequiredMixin,UpdateView):
    template_name='create.html'
    form_class=BlogpostForm
    success_url = '/'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Blogpost, id=id_)


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

