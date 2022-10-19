from django.shortcuts import render,get_object_or_404
from blog.models import post2 , sql_test ,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.utils import timezone
from django.core import serializers
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from blog.forms import CommentForm
from django.contrib import messages

t=timezone.now()

def blog_view(request,cat_name=None):
    posts=post2.objects.filter(status=1,publish_date__lte=t)
    if cat_name:
        posts=posts.filter(category__name=cat_name)    
    #paginators
    posts=Paginator(posts,4)

    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number) 

    except PageNotAnInteger:
        posts=posts.get_page(1)

    except EmptyPage:
        posts=posts.get_page(1)    
    context={'posts': posts}
    
    return render(request,"blog/blog-home.html",context)


def single_view(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"tiket comment successfully") 

        else:
            messages.add_message(request,messages.ERROR,"don't comment submit")          
    post=get_object_or_404(post2,id=pid,status=1,publish_date__lte=t)
    comment=Comment.objects.filter(post=post.id,approved=True)

    post.counted_view+=1       #added counted_view
    post.save()
    form = CommentForm()
    context={'post':post,'comments':comment,'form':form}
    return render(request,"blog/blog-single.html",context)


def test(request):
    posts=post2.objects.filter(publish_date__lte=t)
    context={'posts': posts}
    return render(request,"blog/test.html",context)


def blog_search(request):
    posts=post2.objects.filter(status=1,publish_date__lte=t)
    if request.method=='GET':  
        if s:= request.GET.get('s') :
            posts=posts.filter(content__contains=s)
    context={'posts': posts}
    return render(request,"blog/blog-home.html",context)


#start postgre sql examples

@csrf_exempt
def blog_all_posts(request):
    posts=sql_test.objects.filter()
    posts_serializers=serializers.serialize('json',posts)
    posts_json=json.loads(posts_serializers)
    data=json.dumps(posts_json)
    return HttpResponse(data)


@csrf_exempt
def insert_post(request):
    try:
        f_name_req = request.POST.get('f_name')
        l_name_req = request.POST.get('l_name')
        age_req = request.POST.get('age')
        objs = sql_test(f_name=f_name_req, l_name=l_name_req, age=age_req)
        objs.save()
        return HttpResponse("ok")
    except:
        return HttpResponse("not ok")


@csrf_exempt
def update_post(request):
    try:
        id= request.POST.get('id')
        f_name= request.POST.get('f_name')
        l_name= request.POST.get('l_name')
        age=request.POST.get('age')

        sql_test.objects.filter(id=id).update(f_name=f_name, l_name=l_name,age=age)
        return HttpResponse("update successfully")
    except:
        return HttpResponse("not update")

#end postgre sql examples
    