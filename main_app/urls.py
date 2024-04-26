"""
URL configuration for ecommerce_diploma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
    path('', IndexPageVies.as_view(), name='index_page'),
    path('custom_knitting/', CustomKnittingView.as_view(), name='custom_knitting_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('payment_and_delivery/', PaymentAndDeliveryView.as_view(), name='payment_and_delivery_page'),
    path('contacts/', ContactsPageView.as_view(), name='contacts_page'),
]
