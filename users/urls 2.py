from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', views.profile_view, name ='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)