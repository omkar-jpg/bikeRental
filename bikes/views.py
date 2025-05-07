from django.shortcuts import render
from .models import Bikes
import random

def bike_list(request):
    print("✅ bike_list view triggered!")

    # Retrieve all bikes as a list
    bikes_qs = Bikes.objects.all()
    bikes_list = list(bikes_qs)

    # Select up to 5 random bikes for the featured section
    random_bikes = random.sample(bikes_list, min(5, len(bikes_list)))
    print("Random bikes:", random_bikes)

    # Convert the queryset to a list of dictionaries for JSON serialization
    bikes_data = list(bikes_qs.values(
        'id', 'name', 'location', 'latitude', 'longitude',
        'daily_rate', 'weekly_rate', 'rating', 'quantity'
    ))

    return render(request, 'home.html', {
        'random_bikes': random_bikes,  # For the featured section
        'bikes': bikes_data,           # For JSON serialization in the template
    })