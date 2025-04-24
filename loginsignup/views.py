from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
from bikes.views import bike_list
from users.models import UserProfile

# Home page view - protected by login_required
@login_required
def home(request):
    return bike_list(request)

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)

            messages.success(request, 'Signup successful! You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {
        'form': form,
        'is_post': request.method == 'POST',
    })

# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if not UserProfile.objects.filter(user=user).exists():
                UserProfile.objects.create(user=user)

            messages.success(request, 'You are now logged in!')
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html', {
        'is_post': request.method == 'POST',
    })

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')
