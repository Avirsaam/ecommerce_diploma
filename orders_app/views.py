from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from cart_app.cart import Cart
from catalog_app.models import Product

from .forms import NewOrderForm
from .models import OrderDetail, OrderItem

from decimal import Decimal

class NewOrderView(View):
    def get(self, request):                       
        return render(request, 'orders_app/new_order_template.html', {"form" : NewOrderForm()})
    
    def post(self, request):
        form = NewOrderForm(request.POST)
        new_order = form.save(commit=False)
        new_order.user = request.user
        
        new_order.save()        
        cart = Cart(request)
        for item in cart:
            order_item = OrderItem(
                order=new_order,                
                product=Product.objects.get(pk=item['product_id']),
                quantity=item['quantity'],
                final_price=Decimal(item['price']),
                )
            order_item.save()        
        cart.clear()
        
        context = {
            "page_title":"Заказ сохранён",
            "messages":[f'Заказ номер {new_order.pk} отправлен в обработку']
        }
        return render(request, 'orders_app/order_submitted.html', context)
        
