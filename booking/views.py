from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking
from bikes.models import Bikes 
from django.contrib.auth.decorators import login_required
from datetime import datetime 

@login_required
def book_bike(request, bike_id):
    bike = get_object_or_404(Bikes, id=bike_id)  # Ensure the 'Bike' model is correctly imported

    # Initialize the form regardless of the request method
    form = BookingForm(request.POST or None)  # Initialize with POST data if available

    if request.method == 'POST':
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.bike = bike
            booking.total_price = 100  # Adjust price logic if needed
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    
    # This return statement is for both GET and invalid POST requests
    return render(request, 'booking.html', {'form': form, 'bike': bike})




# Create your views here.
