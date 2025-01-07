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

        # delete tours
    path('delete_tour/<int:id>/', views.delete_tour, name='delete_tour'),

        # customer page
    path('customer',views.customer),


# ----------------user section---------------


        # user page
    path('user_home',views.user_home),    

        # contact page
    path('contact',views.contact),

        # user tour
    path('user_tour',views.user_tours),

        # user tour details
    path('view_tour/<id>', views.user_tour_details, name='user_tour_details'),



        # logout
    path('logout',views.admin_logout),
    
]