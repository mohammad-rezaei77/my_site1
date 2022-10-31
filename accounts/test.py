#views.py File

from django.shortcuts import render, redirect
from .forms import Signupform, Loginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages



def pagelogin(request):
  
    uservalue=''
    passwordvalue=''


    valuenext= request.POST.get('next')

    form= Loginform(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")

        user= authenticate(username=uservalue, password=passwordvalue)
        if user is not None and valuenext=='':
            login(request, user)

            context= {'form': form,
                      'valuenext': valuenext}

    messages.success(request, "You have successfully logged in")
            
    return render(request, 'accounts/Login.html', context)
        
    if user is not None and valuenext !='':
            login(request, user)

    messages.success(request, "You have successfully logged in")

            context= {'form': form,
                      'valuenext': valuenext}
            
            return redirect(valuenext)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'accounts/Login.html', context)

    else:
    
        
        context= {'form': form}
        return render(request, 'accounts/Login.html', context)
