
from operator import index
from django.urls import path
from blog.views import *
app_name='blog'
urlpatterns = [

    path('',blog_view,name='blog'),
    path('blog/single',single_view,name='single'),

    
]
