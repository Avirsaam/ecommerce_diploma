from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .cart import Cart
from catalog_app.models import Product

from random import randint, choice

class CartDetailsView(View):    
    def get(self, request):
        cart = Cart(request)        
        context = {
            "page_title" : "Корзина",
            "cart" : cart
        }        
        return render(request, 'cart_app/cart_details_template.html', context)
    
    def post(self, request, *args, **kwargs):        
        if 'product_id' in request.POST:
            product_id = request.POST['product_id']            
            if 'quantity' in request.POST:                
                try:
                    quantity = int(request.POST['quantity'])
                except:
                    #TODO
                    quantity = 1
            else:
                quantity=1
            
            update = False
            if 'update_quantity' in request.POST:
                update = True                
            
            cart = Cart(request)
            product = get_object_or_404(Product, pk=product_id)
            cart.add(product, quantity, update_quantity=update)
        return redirect(request.META['HTTP_REFERER'])

class CartRemoveItemView(View):
    def get(self, request, product_id):        
        cart = Cart(request)
        cart.remove(product_id)
        return redirect('cart_details_page')

class FillCartView(View):
    def get(self, request, items_count):
        products = Product.objects.all()        
        cart = Cart(request)
        
        for _ in range(items_count):
            cart.add(choice(products), quantity=randint(1,10))        
        
        return redirect('cart_details_page')

class ClearCartView(View):
    def get(self, request):        
        cart = Cart(request)
        cart.clear()
        return redirect('cart_details_page')

