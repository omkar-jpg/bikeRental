from django.shortcuts import render
from bikes.models import Bikes

def search_bikes(request):
    location = request.GET.get('places')
    quantity = request.GET.get('quantity', 1)
    print("Location:", location)  # Debugging

    try:
        quantity = int(quantity)
    except ValueError:
        quantity = 1

    bikes = Bikes.objects.all()

    if location:
        bikes = bikes.filter(location__iexact=location)
    print("Location received from form:", location)  # This will print in the console/log

    return render(request, 'bikelist.html', {
        'filtered_bikes': bikes,
        'location': location,
        'quantity': quantity,
    })