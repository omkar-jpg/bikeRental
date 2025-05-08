from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
# updated
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
    image_2 = models.ImageField(upload_to='bike_image/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='bike_image/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='bike_image/', null=True, blank=True)

    daily_rate = models.DecimalField(max_digits=6, decimal_places=2)
    weekly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    is_available = models.BooleanField(default = True)

    location = models.CharField(max_length=100, blank=True)

    latitude = models.FloatField(default=80)
    longitude = models.FloatField(default=80)

    rating = models.DecimalField(max_digits=2, decimal_places=1, default=Decimal('0.0'))

    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    @property
    def quantity_available(self):
        return self.quantity_in_stock - self.quantity_rented
    
    def update_rating(self):
        ratings = self.bike_ratings.all()
        if ratings:
            self.rating = sum(r.rating for r in ratings)/ ratings.count()
            self.total_ratings = ratings.count()
        else:
            self.rationg = 0
            self.total_ratings = 0
        self.save()    



    def __str__(self):
        return self.name
    
class BikeRating(models.Model):
    bike = models.ForeignKey(Bikes, related_name='bike_ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='bike_ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, f'{i} Stars') for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('bike', 'user')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.bike.update_rating()

    def delete(self, *args, **kwargs):
        bike = self.bike
        super().delete(*args, **kwargs)
        bike.update_rating()

    def __str__(self):
        return f"{self.user.username}'s {self.rating}-star rating for {self.bike.name}"
        
    

