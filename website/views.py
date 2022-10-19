from django.http import HttpResponseRedirect
from django.shortcuts import render
from website.forms import ContactForm ,NewsletterForm
from blog.models import post2
from django.contrib import messages
from datetime import datetime
t=datetime.now()

def index_view(request):                              
    return render(request,"website/index.html")


def about_view(request):                   
    return render(request,"website/about.html")


def contact_view(request):                            
    if request.method =="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()
            #first_name=form.cleaned_data["name"]
            instance.name = 'ناشناس'
            instance.save()
            messages.add_message(request,messages.SUCCESS,"tiket submit successfully") 
        else:
            messages.add_message(request,messages.ERROR,"didnt submit")
        #f = ContactForm()
    return render(request,"website/contact.html")


def Newsletter_view(request):                                                      
    if request.method =="POST":
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()   
            messages.add_message(request,messages.SUCCESS,"your Email submit successfully")
        else:
            messages.add_message(request,messages.ERROR,"your didnt submit")
    return HttpResponseRedirect("/")