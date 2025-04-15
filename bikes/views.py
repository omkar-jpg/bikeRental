from django.shortcuts import render
from .models import Bikes
import random

def bike_list(request):
    print("✅ bike_list view triggered!")
    bikes = Bikes.objects.all()

    random_bikes = random.sample(list(bikes), min(3, len(bikes)))

    print("Random bikes:", random_bikes) 

    return render(request, 'home.html', {'random_bikes': random_bikes})
