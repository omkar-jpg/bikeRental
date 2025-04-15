from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm

# Home page view - protected by login_required
@login_required
def home(request):
    return render(request, 'home.html')

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Explicitly set the backend
            user.backend = 'django.contrib.auth.backends.ModelBackend'  
            login(request, user)  # Now Django knows which backend to use

            messages.success(request, 'Signup successful! You are now logged in.')
            return redirect('home')  # Redirect to home after signup
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

# Login view

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home page if already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
