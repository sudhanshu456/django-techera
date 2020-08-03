from django.urls import path

from . import views
urlpatterns = [
    path('list',views.index,name='index'),
    path('',views.data,name='list'),
    path('register',views.register,name='register'),
    path('logout',views.logouts,name='logout'),
    path('login',views.logins,name='login'),
]
