
from operator import index
from xml.etree.ElementInclude import include
from django.urls import path ,include
from blog.views import *
app_name='blog'
urlpatterns = [
    #path('',include('website.urls')),
    path('',blog_view,name='blog'),

    path('<int:pid>',single_view,name='single'),

    path('test',test,name='test')

    
]
