from django.db import models
from django.contrib.auth.models import User
from booking.models import Booking 

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    payment_id = models.CharField(max_length=100, default="TEMP12345")
    payment_date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits = 10, decimal_places = 2)
    payment_status = models.CharField(max_length = 20, choices = [
        ('Success', 'Success'),
        ('Failed','Failed'),
        ('Pending', 'Pending'),

    ], default = 'Pending')

    def __str__(self):
        return f"payment for {self.booking} - {self.payement_status}"