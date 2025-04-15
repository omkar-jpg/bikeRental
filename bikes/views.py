from django.shortcuts import render
from .models import Bikes
import random

def bike_list(request):
    bike = Bikes.objects.all()
    
    # Debugging line: print the bikes to the console
    print("All bikes:", bike)  # Check if you're getting bikes from DB
    
    random_bikes = random.sample(list(bike), 4)
    
    # Debugging line: print the random bikes
    print("Random bikes:", random_bikes)  # Check if 4 bikes are being selected
    
    return render(request, 'home.html', {'random_bikes': random_bikes})

