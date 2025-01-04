from django.db import models

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

