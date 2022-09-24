from django.contrib import admin
from blog.models import post2
# Register your models here.


class Postadmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    #fields=('title','content')
    list_display=('title','status','counted_view','publish_date','created_date')
    list_filter=('status',)
    #ordering=['created_date']
    search_fields=['title','content']
admin.site.register(post2,Postadmin)