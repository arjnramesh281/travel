from django.urls import path
from . import views

urlpatterns=[

        # login
    path('',views.log),

        # register
    path('registration',views.reg),

        # admin page
    path('admin_home',views.admin_home),
        # customer page
    path('customer',views.customer),


        # user page
    path('user_home',views.user_home),    

        # logout
    path('logout',views.admin_logout),
    
]