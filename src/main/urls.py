from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'main'
urlpatterns = [
    ## API Urls 

    path('overview/',views.apiOverview,name='overview'),
    path('bloglist/',views.blogList,name='blogList'),
    path('blogcreate/',views.blogCreate,name='blogCreate'),
    path('blogupdate/<str:pk>/',views.blogUpdate,name='blogUpdate'),
    path('blogdelete/<str:pk>/',views.blogDelete,name='blogDelete'),
    path('blogdetail/<str:pk>/',views.blogDetail,name='blogDetail'),
    ### ajax blog create post urls
    
    path('ajaxcreate/',views.createajax),  # load the page
    path('ajax-request/',views.ajaxRequest,name='ajax-request'),
    ##########################################################################
   
   
   
   
    path('list',views.index,name='index'),
    path('',views.data,name='list'),
    path('listview',views.ListBlogPost.as_view(),name='listview'),
    path('<int:id>/detailview',views.DetailBlogPost.as_view(),name='detailview'),
    path('register',views.register,name='register'),
    path('logout',views.logouts,name='logout'),
    path('login',views.logins,name='login'),
    path('create',views.CreateBlogPost.as_view(),name='create'),
    path('<int:id>/delete/',views.DeleteBlogPost.as_view(), name='delete'),
    path('<int:id>/update/',views.UpdateBlogPost.as_view(), name='update'),
]

