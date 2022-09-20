from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>HOME PAGE</h1>')


def blog_view(request):
    return HttpResponse('<h1>blog PAGE</h1>')


def contact_view(request):
    return HttpResponse('<h1>contact PAGE</h1>')
