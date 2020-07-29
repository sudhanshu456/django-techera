from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Blogpost

def index(request):
    return HttpResponse('<h1>hello world</h1>')


def data(request):
    queryset=Blogpost.objects.all()
    context={
        'data':queryset,
    }
    return render(request,'home.html',context)



