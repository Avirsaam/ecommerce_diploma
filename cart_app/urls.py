from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import *



urlpatterns = [    
    path('', CartDetailsView.as_view(), name='cart_details_page'),
    path('remove_item/<int:product_id>', CartRemoveItemView.as_view(), name='cart_remove_item_page'),
    path('fill_cart/<int:items_count>', FillCartView.as_view(), name='fill_cart'),
    path('clear_cart/', ClearCartView.as_view(), name='clear_cart'),
]