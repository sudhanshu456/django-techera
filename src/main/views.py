from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Blogpost

def index(request):
    
    return render(request,'test.html')


def data(request):
    queryset=Blogpost.objects.all()
    context={
        'data':queryset,
    }
    return render(request,'home.html',context)



