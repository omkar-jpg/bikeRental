from django.db import models
from django.contrib.auth.models import User
from bikes.models import Bikes  # assuming your model is named Bike

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bikes, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')  # or 'Confirmed', 'Completed'

    def __str__(self):
        return f"{self.user.username} - {self.bike.name} ({self.start_date} to {self.end_date})"