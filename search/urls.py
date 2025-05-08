from django.urls import path
from .views import search_bikes

urlpatterns = [
    path('', search_bikes, name='search_bikes'),
]