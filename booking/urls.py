from django.urls import path
from . import views 

urlpatterns = [
    path('<int:bike_id>/', views.book_bike, name='Booking'),  # Make sure this matches
]