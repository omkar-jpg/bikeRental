
from django.contrib import admin
from django.urls import path, include  # Correctly import include and path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginsignup.urls')),  # Include loginsignup URLs for home, login, signup
]
