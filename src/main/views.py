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


## import for api
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer





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




## api concept


@api_view(["GET"])
def apiOverview(request):
    api_urls={
        'list':'/bloglist/',
        'detail':'/blogdetail/<str:pk>/',
        'create': '/blogcreate/',
        'update':'/blogcreate/<str:pk>/',
        'delete':'/blogdelete/<str:pk>/',

    }

    return Response(api_urls)


    
@api_view(['GET'])
def blogList(request):
    posts=Blogpost.objects.all()
    serializers=BlogSerializer(posts,many=True)
    return Response(serializers.data)



@api_view(['GET'])
def blogDetail(request,pk):
    posts=Blogpost.objects.get(id=pk)
    serializers=BlogSerializer(posts,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def blogCreate(request):
    serializers=BlogSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return HttpResponse("error")

@api_view(['GET','POST'])
def blogUpdate(request,pk):
    posts=Blogpost.objects.get(id=pk)
    serializers=BlogSerializer(instance=posts,data=request.data)
    if serializers.is_valid():
        serializers.save()
        
    return Response(serializers.data)




@api_view(['DELETE'])
def blogDelete(request,pk):
    posts=Blogpost.objects.get(id=pk)
    posts.delete() 
    return Response("item deleted ")






##ajax



def createajax(request):
	form = BlogpostForm()
	return render(request, "ajax_create.html", {"form": form})

def ajaxRequest(request):
	if request.method == "POST" and request.is_ajax():
		form = BlogpostForm(request.POST)
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)