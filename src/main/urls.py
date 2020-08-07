from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('list',views.index,name='index'),
    path('',views.data,name='list'),
    path('register',views.register,name='register'),
    path('logout',views.logouts,name='logout'),
    path('login',views.logins,name='login'),
    path('create',views.CreateBlogPost.as_view(),name='create'),
    path('<int:id>/delete/',login_required(views.DeleteBlogPost.as_view()), name='delete'),
    path('<int:id>/update/',login_required(views.UpdateBlogPost.as_view()), name='update'),
]
