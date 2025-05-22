from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Models

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='default_profile_pic.png')
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # <--- Added this line
    street_number = models.CharField(max_length = 10) #hello
    zipcode = models.CharField(max_length = 10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length = 50)
    bio = models.TextField(blank=True, null = True)

    def __str__(self):
        return self.user.username   # Return the username associated with the profile for easy identification