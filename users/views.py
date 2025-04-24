from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def profile_view(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile, user=user)
        if form.is_valid():
            # Update user fields
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            # Update profile fields
            form.save()
            return redirect('profile')  # Replace with your profile URL name
    else:
        form = UserProfileForm(instance=profile, user=user)

    return render(request, 'profile.html', {'form': form})
