from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Bikes, BikeRating
from .form import BikeRatingForm
import random

def bike_list(request):
    print("✅ bike_list view triggered!")

    # Retrieve all bikes as a list
    bikes_qs = Bikes.objects.all()
    bikes_list = list(bikes_qs)

    # Select up to 5 random bikes for the featured section
    random_bikes = random.sample(bikes_list, min(5, len(bikes_list)))
    print("Random bikes:", random_bikes)

    # Convert the queryset to a list of dictionaries for JSON serialization
    bikes_data = list(bikes_qs.values(
        'id', 'name', 'location', 'latitude', 'longitude',
        'daily_rate', 'weekly_rate', 'rating', 'quantity'
    ))

    # 🔽 Bikes sorted in ascending order of ratings
    bikes_sorted_by_rating = Bikes.objects.all().order_by('-rating')

    return render(request, 'home.html', {
        'random_bikes': random_bikes,                # For the featured section
        'bikes': bikes_data,                         # For JSON serialization in the template
        'bikes_sorted_by_rating': bikes_sorted_by_rating,  # For display sorted by rating
    })


from django.http import HttpResponse, HttpResponseBadRequest

from django.http import HttpResponse, HttpResponseBadRequest

def rate_bike(request, bike_id):
    bike = get_object_or_404(Bikes, id=bike_id)

    try:
        existing_review = BikeRating.objects.get(bike=bike, user=request.user)
    except BikeRating.DoesNotExist:
        existing_review = None

    if request.method == 'POST':
        form = BikeRatingForm(request.POST, instance=existing_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.bike = bike
            review.user = request.user
            review.save()
            # Return empty response with 204 No Content status
            return HttpResponse(status=204)

        else:
            return HttpResponseBadRequest("Invalid data submitted.")

    return HttpResponseBadRequest("Invalid request method.")


from django.shortcuts import render

def aboutus_view(request):
    return render(request, 'aboutus.html')

def contactus_view(request):
    return render(request, 'contactus.html')