from datetime import datetime
from unicodedata import category
from django.shortcuts import render,get_object_or_404
from blog.models import post2
t=datetime.now()

def blog_view(request,cat_name=None):
    posts=post2.objects.filter(status=1,publish_date__lte=t)
    if cat_name:
        posts=posts.filter(category__name=cat_name)    
    context={'posts': posts}
    return render(request,"blog/blog-home.html",context)

def single_view(request,pid):
    post=get_object_or_404(post2,id=pid,status=1,publish_date__lte=t)
    post.counted_view+=1       #added counted_view
    post.save()
    context={'post':post}
    return render(request,"blog/blog-single.html",context)


def test(request):
    posts=post2.objects.filter(publish_date__lte=t)
    context={'posts': posts}
    return render(request,"blog/test.html",context)

