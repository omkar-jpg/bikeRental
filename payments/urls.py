# payments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('khalti/initiate/<int:booking_id>/', views.khalti_initiate, name='khalti_initiate'),
    path('khalti/verify/', views.khalti_verify, name='khalti_verify'),  # optional, for later
]