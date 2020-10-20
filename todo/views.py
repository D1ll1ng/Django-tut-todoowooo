from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm

def signupuser(request):

    return render(request, 'todo/signupuser.html', {'form':UserChangeForm})
