from django.db import models
from django.contrib.auth.models import User
from bikes.models import Bikes  # assuming your model is named Bike

class Booking(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links the booking to a user
    bike = models.ForeignKey(Bikes, on_delete=models.CASCADE)  # Links the booking to a bike
    start_date = models.DateField()  # Start date of the booking
    end_date = models.DateField()  # End date of the booking
    quantity = models.PositiveIntegerField(default=1)  # Number of bikes being rented
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price for the booking
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set creation time
    status = models.CharField(max_length=20, default='Pending')  # Booking status (e.g., Pending, Confirmed)

    def __str__(self):
        return f"{self.user.username} - {self.bike.name} ({self.start_date} to {self.end_date})"