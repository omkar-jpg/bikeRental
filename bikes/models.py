from django.db import models

class Bikes(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    
    short_description = models.TextField(blank = True)

    category = models.CharField(max_length=50, choices=[
        ('mountain','Mountain'),
        ('city','City'),
        ('electric', 'Electric'),
        ('road','Road'),
        ('hybrid','Hybrid'),
    ])
    
    image = models.ImageField(upload_to = 'bike_image/', null=True, blank=True)

    daily_rate = models.DecimalField(max_digits=6, decimal_places=2)
    weekly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    is_available = models.BooleanField(default = True)

    location = models.CharField(max_length=100, blank=True)

    rating = models.FloatField(default = 0)

    quantitiy_in_stock = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    @property
    def quantity_available(self):
        return self.quantity_in_stock - self.quantity_rented



    def __str__(self):
        return self.name
    

