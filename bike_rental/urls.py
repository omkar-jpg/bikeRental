
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginsignup.urls')),
    path('home/', include('bikes.urls')),
    path('booking/', include('booking.urls')),
    path('users/', include('users.urls')),
    path('payments/', include('payments.urls')),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)