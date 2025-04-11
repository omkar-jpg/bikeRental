from django.shortcuts import render
from .models import Bike

def home(request):
    bike = Bike.object.all()

    return render(request, 'home.html',{'bikes': bikes})

