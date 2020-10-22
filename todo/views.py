from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

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

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')