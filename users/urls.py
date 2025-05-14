from django.urls import path  # Import the path function to define URL patterns
from django.conf import settings  # Import settings to access MEDIA_URL and MEDIA_ROOT
from . import views  # Import views from the current app
from django.conf.urls.static import static  # Import static to serve media files in development

urlpatterns = [
    path('profile/', views.profile_view, name ='profile'),  # URL pattern for the profile view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development
