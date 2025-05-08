from django.urls import path
from . import views

urlpatterns = [
    path('', views.bike_list, name='bike_list'),
    path('bike/<int:bike_id>/rate/', views.rate_bike, name='rate_bike'),
    path('about/', views.aboutus_view, name='aboutus'),
    path('contact/', views.contactus_view, name='contactus'),
]