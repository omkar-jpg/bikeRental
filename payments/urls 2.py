from django.urls import path
from .views import make_payment

urlpatterns = [
    path('pay/<int:booking_id>/', make_payment, name='simulate_payment'),
]
