from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking
from bikes.models import Bikes 
from bikes.views import bike_list
from django.contrib.auth.decorators import login_required
from datetime import timedelta 
import random
from django.http import HttpResponse


@login_required
def book_bike(request, bike_id):
    # Get the specific bike to be booked
    bike = get_object_or_404(Bikes, id=bike_id)

    # Get all bikes and pick 3 random ones for display
    bikes = Bikes.objects.all()
    random_bikes = random.sample(list(bikes), min(3, len(bikes)))

    # Initialize the form (pre-filled with POST data if available)
    form = BookingForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.bike = bike

            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            quantity = form.cleaned_data['quantity']
            
            if quantity > bike.quantity:
                return HttpResponse("Invalid qunatitiy selected.",status=400)

            rental_days = (end_date - start_date).days + 1
            if rental_days <= 0:
                form.add_error('end_date', "End date must be after start date.")
                return render(request, 'booking.html', {
                    'form': form,
                    'bike': bike,
                    'random_bikes': random_bikes,
                })

            booking.total_price = rental_days * quantity * bike.daily_rate
            booking.save()

            bike.quantity -= quantity 
            bike.save()

            return redirect('booking_confirmation', booking_id=booking.id)

    # Render booking page with bike details and random bikes
    return render(request, 'booking.html', {
        'form': form,
        'bike': bike,
        'random_bikes': random_bikes,
    })

from django.shortcuts import render

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})





