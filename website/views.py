from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return render(request,"website/index.html")


def blog_view(request):
    return render(request,"blog.html")


def contact_view(request):
    return render(request,"contact.html")
