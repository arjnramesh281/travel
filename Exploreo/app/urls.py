from django.urls import path
from . import views

urlpatterns=[

        # login
    path('',views.log),

        # register
    path('registration',views.reg),

        # admin page
    path('admin_home',views.admin_home),

        # tours page
    path('tours',views.tours),    

        # edit tours
    path('edit_tour/<id>',views.edit_tour),

        # customer page
    path('customer',views.customer),


        # user page
    path('user_home',views.user_home),    

        # contact page
    path('contact',views.contact),

        # logout
    path('logout',views.admin_logout),
    
]