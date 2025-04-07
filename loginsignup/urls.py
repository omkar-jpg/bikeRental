from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path("account/", include("allauth.urls")),  # For Google sign-in
    path('', views.login_view, name='login'),  # Ensure the root URL maps to the login page
    path('home/', views.home, name='home'),  # Ensure this exists for the home page URL
    path('logout/', views.logout_view, name='logout'),

]
