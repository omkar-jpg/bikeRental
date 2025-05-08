import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from booking.models import Booking
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@login_required
def khalti_initiate(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        amount = int(Decimal(booking.total_price) * 100)

        payload = {
            "return_url": "http://127.0.0.1:8000/payments/khalti/verify/",
            "website_url": "http://127.0.0.1:8000/",
            "amount": amount,
            "purchase_order_id": f"BOOK{booking.id}",
            "purchase_order_name": "Bike Rental",
            "customer_info": {
                "name": f"{request.user.first_name} {request.user.last_name}",
                "email": request.user.email,
                "phone": "9800000000"
            }
        }

        headers = {
            "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post("https://dev.khalti.com/api/v2/epayment/initiate/", json=payload, headers=headers)
        data = response.json()

        if response.status_code == 200 and 'payment_url' in data:
            return redirect(data['payment_url'])
        else:
            return HttpResponse(f"Error: {data}", status=400)

    return render(request, 'payment.html', {"booking": booking})


def khalti_verify(request):
    pidx = request.GET.get('pidx')
    purchase_order_id = request.GET.get('purchase_order_id')  # e.g., BOOK33

    if not pidx or not purchase_order_id:
        return HttpResponse("Missing transaction ID or order ID.", status=400)

    response = requests.post(
        "https://dev.khalti.com/api/v2/epayment/lookup/",
        headers={
            "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
            "Content-Type": "application/json"
        },
        json={"pidx": pidx}
    )

    print("Status Code:", response.status_code)
    print("Response JSON:", response.text)

    try:
        data = response.json()
    except ValueError:
        return HttpResponse("Failed to parse response from Khalti.", status=400)

    if data.get('status') == "Completed":
        # Extract booking ID from purchase_order_id (e.g., "BOOK33" -> 33)
        try:
            booking_id = int(purchase_order_id.replace("BOOK", ""))
            booking = Booking.objects.get(id=booking_id)
            booking.status = "Paid"
            booking.save()
        except Booking.DoesNotExist:
            return HttpResponse("Booking not found.", status=404)
        except Exception as e:
            return HttpResponse(f"Error updating booking: {str(e)}", status=500)

        return redirect('home')  # Or redirect to success page
    else:
        return HttpResponse(f"Payment failed or pending. Status: {data.get('status', 'No status')}", status=400)