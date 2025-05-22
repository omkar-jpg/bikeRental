from django.urls import path
from . import views 


urlpatterns = [
    path('<int:bike_id>/', views.book_bike, name='Booking'),
    path('booking-confirmation/<int:booking_id>/',views.booking_confirmation, name=
         'booking_confirmation'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
