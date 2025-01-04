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



def admin_home(request):
    if 'admin' in request.session:
        # Fetch all tour packages
        packages = TourPackage.objects.all()

        # Calculate other data for dashboard overview
        total_bookings = 1234  # Example: Replace with actual calculation
        active_tours = packages.count()  # Total number of active tours
        total_revenue = 45678  # Example: Replace with actual revenue calculation
        customer_rating = 4.8  # Example: Replace with actual rating

        # Pass data to the template
        context = {
            'packages': packages,
            'total_bookings': total_bookings,
            'active_tours': active_tours,
            'total_revenue': total_revenue,
            'customer_rating': customer_rating,
        }

        # Render the dashboard page
        return render(request, 'admin/home.html', context)
    else:
        return redirect(log)  # Redirect to login if not an admin
    

# -----------------add tour----------------

def tours(req):
    if 'admin' in req.session:  # Check if admin is logged in
        if req.method == 'POST':
            # Fetch form data
            package_name = req.POST.get('package_name')
            destination = req.POST.get('destination')
            duration_days = req.POST.get('duration_days')
            price = req.POST.get('price')
            description = req.POST.get('description')
            image = req.FILES.get('image')
            max_capacity = req.POST.get('max_capacity')
            rating = req.POST.get('rating')
            start_date = req.POST.get('start_date')
            end_date = req.POST.get('end_date')

            # Handle checkboxes (convert "on" to True and missing values to False)
            accommodation = req.POST.get('accommodation') == 'on'
            meals = req.POST.get('meals') == 'on'
            transport = req.POST.get('transport') == 'on'

            # Create and save the TourPackage instance
            data = TourPackage(
                package_name=package_name,
                destination=destination,
                duration_days=duration_days,
                price=price,
                rating=rating,
                description=description,
                image=image,
                max_capacity=max_capacity,
                start_date=start_date,
                end_date=end_date,
                accommodation=accommodation,
                meals=meals,
                transport=transport
            )
            data.save()
            return redirect(tours)  # Redirect after saving
        else:
            return render(req, 'admin/tours.html')  # Render the form for GET request
    else:
        return redirect(log)  # Redirect to login if not an admin


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