import email
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from urllib3 import HTTPResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def login_view(request):
    redirect_to = request.GET.get('next', '')
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                
                user = authenticate(request, username=username, password=password)
                if user is not None :
                    login(request,user)
                    if  redirect_to :
                        return redirect(redirect_to,'/')
                    else :
                        return redirect('/')
            else :
                return redirect(redirect_to,'/')
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html',context)
    else :
        return redirect('/')
            

@login_required  
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request): 
    if not request.user.is_authenticated:
        if request.method == 'POST':   
            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('/')
        form = UserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')

