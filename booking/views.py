from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking
from bikes.models import Bikes 
from bikes.views import bike_list
from django.contrib.auth.decorators import login_required
from datetime import timedelta 
import random
from django.http import HttpResponse
from decimal import Decimal

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)  # Get booking or 404
    return render(request, 'booking_confirmation.html', {'booking': booking})  # Render confirmation page

@login_required  # Ensure the user is logged in
def book_bike(request, bike_id):
    bike = get_object_or_404(Bikes, id=bike_id)  # Get the specific bike
    bikes = Bikes.objects.all()  # Retrieve all bikes
    random_bikes = random.sample(list(bikes), min(5, len(bikes)))  # Pick 3 random bikes

    form = BookingForm(request.POST or None)  # Initialize form with POST data if available

    if request.method == 'POST':  # If form is submitted
        print("POST data:", dict(request.POST))
        if form.is_valid():  # Validate form data
            booking = form.save(commit=False)  # Create booking object without saving
            booking.user = request.user  # Assign the logged-in user
            booking.bike = bike  # Assign the selected bike

            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            quantity = form.cleaned_data['quantity']

            if quantity > bike.quantity:  # Check if requested quantity exceeds available bikes
                return HttpResponse("Invalid quantity selected.", status=400)

            rental_days = (end_date - start_date).days + 1  # Calculate rental duration
            if rental_days <= 0:  # Ensure end date is after start date
                form.add_error('end_date', "End date must be after start date.")
                return render(request, 'booking.html', {'form': form, 'bike': bike, 'random_bikes': random_bikes})

            booking.total_price = rental_days * quantity * bike.daily_rate * Decimal('0.80') # Calculate total price
            booking.save()  # Save the booking

            bike.quantity -= quantity  # Update bike availability
            bike.save()  # Save the updated bike

            payment_option = request.POST.get('payment_option')

            if payment_option == 'now':
                return redirect('khalti_initiate', booking_id=booking.id)
               
                
            else:
                 return redirect('booking_confirmation', booking_id=booking.id)
    return render(request, 'booking.html', {'form': form, 'bike': bike, 'random_bikes': random_bikes})

