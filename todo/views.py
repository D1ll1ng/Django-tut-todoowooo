from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

def signupuser(request):
    if request.method =='GET':
        return render(request, 'todo/signupuser.html', {'form':UserChangeForm})
    else:
        # Create a new user
        user = User.objects.create_user(
            request.POST['username'], 
            request.POST['email'])
        user.save