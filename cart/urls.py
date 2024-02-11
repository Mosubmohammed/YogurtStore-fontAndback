from .views import *
from django.urls import path 


urlpatterns = [
    path('',cart_summary,name='cart_summary'),
    path('add/',cart_add,name='cart_add'),
    path('update/',cart_update,name='cart_update'),
    path('delete/',cart_delete,name='cart_delete'),
]