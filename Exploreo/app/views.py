from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
import os
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

# ----------------login ---------------

def log(req):
    if 'admin' in req.session:
        return redirect(admin_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        print(username+password)
        data=authenticate(username=username,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['admin']=username
                return redirect(admin_home)
            else:
                req.session['user']=username
                return redirect(user_home)
        else:
            messages.warning(req, " Invalid username or password.")
            return redirect(log)
    else:
        return render(req,'login.html')
    
# --------------admin home------------


def admin_home(req):
    if 'admin' in req.session:
        return render(req,'admin/home.html')


# -------------logout----------------


def admin_logout(req):
    logout(req)
    req.session.flush()
    return redirect(log)







# -----------------register-------------------
 
def reg(req):
    if req.method=='POST':
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=username,email=email,username=email,password=password)
            data.save()
            send_mail(
                'Welcome to Exploreo - Your Adventure Awaits!',
                '''Dear {user_name},

            Thank you for joining Exploreo, your gateway to discovering unforgettable travel experiences! 

            We are thrilled to have you as part of our growing community of explorers and adventurers. With Exploreo, you can uncover breathtaking destinations, find the best travel deals, and make your journey truly memorable.

            Here’s what you can do with your account:
            - Browse exclusive travel packages and discounts.
            - Save your favorite destinations for easy planning.
            - Get personalized recommendations based on your preferences.

            We’re here to make your travel dreams come true. If you have any questions or need assistance, feel free to reach out to our support team.

            Pack your bags—your next adventure is just a click away!

            Warm regards,  
            The Exploreo Team

            Your Travel, Your Way.''',
                settings.EMAIL_HOST_USER,
                [email]
            )

        except:
            messages.warning(req, " This Email Already In Use.")
            return redirect(reg)
        return redirect(log)
    else:
         return render(req,'user/register.html')
         

# ----------------user home----------------

def user_home(req):
    if 'user' in req.session:
        return render(req,'user/home.html')