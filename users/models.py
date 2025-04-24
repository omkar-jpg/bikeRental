# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     profile_pic = models.ImageField(upload_to= 'profile_pics/', blank=True, null=True)
#     street_number = models.CharField(max_length = 10)
#     zipcode = models.CharField(max_length = 10)
#     city = models.CharField(max_length=50)
#     country = models.CharField(max_length = 50)
#     bio = models.TextField(blank=True, null = True)

#     def __str__(self):
#         return self.user.username