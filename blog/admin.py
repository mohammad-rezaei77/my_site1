from django.contrib import admin
from blog.models import post2,category,sql_test,Comment 
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class Postadmin(SummernoteModelAdmin):
    
    date_hierarchy='created_date'
    #fields=('title','content')
    list_display=('title','author','status','counted_view','publish_date','created_date')
    list_filter=('status','author')
    #ordering=['created_date']
    search_fields=['title','content']
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','post','approved','created_date')
    list_filter = ('approved','post')
    search_fields = ['name','message']
   



admin.site.register(Comment,CommentAdmin)
admin.site.register(post2,Postadmin) 
admin.site.register(category)
admin.site.register(sql_test)
