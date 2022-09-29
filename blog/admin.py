from django.contrib import admin
from blog.models import post2,category
# Register your models here.


class Postadmin(admin.ModelAdmin):
    
    date_hierarchy='created_date'
    #fields=('title','content')
    list_display=('title','author','status','counted_view','publish_date','created_date')
    list_filter=('status','author')
    #ordering=['created_date']
    search_fields=['title','content']

admin.site.register(post2,Postadmin)
   
admin.site.register(category)