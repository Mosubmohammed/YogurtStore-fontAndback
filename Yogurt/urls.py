from .views import *
from django.urls import path 
urlpatterns = [
    
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('menu/',menu, name='menu'),
    path('product/<int:pk>/',product, name='product'),
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('logout/',logout_user, name='logout'),
    path('register/',register_user, name='register'),
    path('update_user/',update_user, name='update_user'),
    path('update_info/',update_info, name='update_info'),
    path('update_password/',update_password, name='update_password'),
    path('search/',search, name='search'),
    ]