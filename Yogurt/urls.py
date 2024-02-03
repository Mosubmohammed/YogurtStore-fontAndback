from .views import *
from django.urls import path 
urlpatterns = [
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('menu/',menu, name='menu'),
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('logout/',logout_user, name='logout'),
    path('product/<int:pk>/',product, name='product'),
    path('register/',register_user, name='register'),
    path('update_user/',update_user, name='update_user'),
    path('update_password/',update_password, name='update_password'),
    ]