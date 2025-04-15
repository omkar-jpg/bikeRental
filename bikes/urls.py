from django.urls import path
from . import views

urlpatterns = [
    path('', views.bike_list, name='bike_list'),  # Show bike list at /home/
]