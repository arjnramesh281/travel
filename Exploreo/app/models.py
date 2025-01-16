from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TourPackage(models.Model):

    # Fields     
    package_name = models.CharField(max_length=255)  # Package Name
    destination = models.CharField(max_length=255)  # Destination
    duration_days = models.PositiveIntegerField()  # Duration in days
    price = models.PositiveIntegerField()  # Price
    rating = models.FloatField()  # Rating
    description = models.TextField()  # Description
    image = models.FileField()
    max_capacity = models.PositiveIntegerField()  # Maximum Capacity

    # Dates
    start_date = models.DateField()  # Start Date
    end_date = models.DateField()  # End Date

    # Inclusions
    accommodation = models.BooleanField(default=False)  # Accommodation
    meals = models.BooleanField(default=False)  # Meals
    transport = models.BooleanField(default=False)  # Transport


class Booking(models.Model):
    """Model to store booking information."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')  # Link to the authenticated user
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='bookings')  # Link to the selected package
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    guests = models.PositiveIntegerField()
    preferred_date = models.DateField()
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)