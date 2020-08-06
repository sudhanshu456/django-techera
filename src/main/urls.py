from django.urls import path

from . import views
urlpatterns = [
    path('list',views.index,name='index'),
    path('',views.data,name='list'),
    path('register',views.register,name='register'),
    path('logout',views.logouts,name='logout'),
    path('login',views.logins,name='login'),
    path('create',views.CreateBlogPost.as_view(),name='create'),
    path('<int:id>/delete/',views.DeleteBlogPost.as_view(), name='delete')
]
