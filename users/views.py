from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from booking.models import Booking
from bikes.models import BikeRating
# Ensures that only logged-in users can access the profile view
@login_required
def profile_view(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    user_ratings = BikeRating.objects.filter(user=user)
    user_ratings_by_bike = {r.bike.id: r for r in user_ratings}

    # Fetch all bookings made by the user
    booked_bikes = Booking.objects.filter(user=user)  # Fetching all bookings made by the user
    #error handling
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile, user=user)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile, user=user)
    # Render the profile page with form, profile info, bookings, and ratings
    return render(request, 'profile.html', {
    'form': form,
    'profile': profile,
    'user_rentals': booked_bikes,
    'user_profile': profile,
    'user_ratings': user_ratings_by_bike,  # ✅ New line
})

