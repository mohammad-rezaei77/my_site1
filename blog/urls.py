
from operator import index
from django.urls import path ,include
from blog.views import *
app_name='blog'
urlpatterns = [
    #path('',include('website.urls')),
    path('',blog_view,name='blog'),
    path('<int:pid>',single_view,name='single'),
    path('category/<str:cat_name>',blog_view,name='category'),
    path ('search/',blog_search,name='search'),
    path('test',test,name='test'),
    path ('all_posts/' , blog_all_posts , name = 'all_posts'),
    path ('insert_post/' , insert_post ,name = 'insert_post'),
    path ('update_post/' , update_post ,name = 'update_post'),


    
]
