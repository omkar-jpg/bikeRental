from django.urls import path
from . import views 


urlpatterns = [
    path('<int:bike_id>/', views.book_bike, name='Booking'),
    path('booking-confirmation/<int:booking_id>/',views.booking_confirmation, name=
         'booking_confirmation')
]
