from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
import os
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.db.models import Q


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
    

# --------------tours------------
def tours(req):
    # tours=Tour.objects.all()
    return render(req,'admin/tours.html',{'tours':tours})


# -------------logout----------------


def admin_logout(req):
    logout(req)
    req.session.flush()
    return redirect(log)


# ----------------user home----------------

def user_home(req):
    if 'user' in req.session:
        return render(req,'user/home.html')

# ---------------- customer ----------------

def customer(req):
    users=User.objects.all()
    return render(req,'admin/customer.html',{'users':users})
    


# -----------------register-------------------
 
def reg(req):
    if req.method=='POST':
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=username,email=email,username=email,password=password)
            data.save()
        except:
            messages.warning(req, " This Email Already In Use.")
            return redirect(reg)
        return redirect(log)
    else:
         return render(req,'user/register.html')
    

    # -----------------contact----------------

def contact(req):
    if 'user' in req.session:
        return render(req,'user/contact.html')
    if 'admin' in req.session:
        return render(req,'admin/contact.html')