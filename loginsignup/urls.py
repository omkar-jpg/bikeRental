from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path("account/", include("allauth.urls")), 
    path('', views.login_view, name='login'), 
    path('home/', views.home, name='home'),  
    path('logout/', views.logout_view, name='logout'),

]
