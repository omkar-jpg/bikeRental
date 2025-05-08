import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from booking.models import Booking
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def khalti_initiate(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        amount = int(Decimal(booking.total_price) * 100)  # Convert to paisa

        payload = {
            "return_url": "http://127.0.0.1:8000/payments/khalti/verify/",
            "website_url": "http://127.0.0.1:8000/",
            "amount": amount,
            "purchase_order_id": f"BOOK{booking.id}",
            "purchase_order_name": "Bike Rental",
            "customer_info": {
                "name": f"{request.user.first_name} {request.user.last_name}",
                "email": request.user.email,
                "phone": "9800000000"  # Replace with dynamic phone if available
            }
        }

        headers = {
           "Authorization": f"Key {settings.KHALTI_PUBLIC_KEY}",  # Use test key
            "Content-Type": "application/json"
        }

        response = requests.post("https://dev.khalti.com/api/v2/epayment/initiate/", json=payload, headers=headers)
        data = response.json()

        if response.status_code == 200:
            return redirect(data['payment_url'])
        else:
            return HttpResponse(f"Error: {data}", status=400)

    return render(request, 'payment.html', {"booking": booking})


@csrf_exempt
def khalti_verify(request):
    pidx = request.GET.get('pidx')

    response = requests.post(
        "https://khalti.com/api/v2/epayment/lookup/",
        headers={"Authorization": f"Key 35fe7785748249e4824174b29424f582"},
        json={"pidx": pidx}
    )
    
    print("Status Code:", response.status_code)
    print("Response JSON:", response.text)  # Print raw text in case it's not JSON

    try:
        data = response.json()
    except ValueError:
        return HttpResponse("Failed to parse response from Khalti.", status=400)

    if data.get('status') == "Completed":
        return redirect('home')  # Update this to your actual homepage URL name
    else:
        return HttpResponse(f"Payment failed or pending. Status: {data.get('status', 'No status')}", status=400)
