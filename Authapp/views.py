from functools import reduce
from django.shortcuts import redirect, render
# from django.views import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import logout, authenticate, login

from Authproj import settings

# Create your views here.

def home(request):
        return render(request, "home.html")

def signup(request):
        if request.method == 'POST':
            username = request.POST.get('username-signup')
            email = request.POST.get('email-signup')
            password = request.POST.get('password-signup')
            print(f'this is username: {username}\n email: {email}\n password: {password} \n')
            
            newuser = User.objects.create_user(username, email, password)
            newuser.username = username
            newuser.email = email
            newuser.password = password
            newuser.is_active = False
            messages.success(request, "Account has been created!! ")
        
            subject = 'WELCOME TO DJANGO EMAIL TESTING'
            message = F'Hey {newuser.username} !! \n Welcome to my Django website. \n Thank you for signing up'
            from_email = settings.EMAIL_HOST_USER
            to = [newuser.email]
            send_mail(subject, message, from_email, to)
            return redirect('home')
        return render(request, 'signup.html')

def login1(request):
       if request.method=='POST':
              username = request.POST.get("username-login")
              password = request.POST.get("password-login")

              user = authenticate(username=username, password=password)
              if user is not None:
                     login(request, user)
                     return redirect('home')
              else:
                     messages.error(request, "bad Credentials!")
                     return render(request, 'home.html')
              
       return render(request, 'login.html')

def signout(request):
        logout(request)
        # return redirect('home')
        return render(request, 'home.html')