from django.shortcuts import render, redirect, get_object_or_404
from .forms import PaymentForm
from .models import Payment
from booking.models import Booking

def make_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.status = 'Paid'  # Simulated
            payment.save()

            booking.status = 'Paid'  # Update booking status if payment is complete
            booking.save()

            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = PaymentForm()

    return render(request, 'make_payment.html', {'form': form, 'booking': booking})
