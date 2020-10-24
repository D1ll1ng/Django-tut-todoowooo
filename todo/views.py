from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method =='GET':
        return render(request, 'todo/signupuser.html', {'form':UserChangeForm})
    else:
        # Create a new user
        try:
            user = User.objects.create_user(
                request.POST['username'], 
                request.POST['email'])
            user.save
            login(request, user)
            return redirect('currenttodos')

        except IntegrityError:
            return render(request, 'todo/signupuser.html', {'form':UserChangeForm(), 'error': 'U fucking dummy! The username is already taken, man up!'})

def loginuser(request):
    if request.method =='GET':
        return render(request, 'todo/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currenttodos')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

    
def currenttodos(request):
    return render(request, 'todo/currenttodos.html')