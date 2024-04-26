
from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
    path('', NewOrderView.as_view(), name='new_order_page'),
]
