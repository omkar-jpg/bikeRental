from django.shortcuts import render
from bikes.models import Bikes

def search_bikes(request):
    location = request.GET.get('places')
    quantity = request.GET.get('quantity', 1)

    try:
        quantity = int(quantity)
    except ValueError:
        quantity = 1

    bikes = Bikes.objects.all()

    if location:
        bikes = bikes.filter(location__iexact=location)
    
    if quantity:
        bikes = bikes.filter(quantity__gte=quantity)

    return render(request, 'bikelist.html', {
        'filtered_bikes': bikes,
        'location': location,
        'quantity': quantity,
    })
