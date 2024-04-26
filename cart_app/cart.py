from catalog_app.models import Product
from django.conf import settings
from decimal import Decimal


class Cart(object):
    def __init__(self, request):    
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)        
        if not cart:    
            self.session[settings.CART_SESSION_ID] = dict()
            cart = self.session[settings.CART_SESSION_ID]
        self.cart = cart
            
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:            
            self.cart[product_id] = {'quantity': 0,
                                    'price': str(product.price_discount),
                                    }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        
    def save(self):
        self.session.modified = True
    
    def remove(self, product):
        product_id = str(product)
        if product_id in self.cart:             
            del self.cart[product_id]
        self.save()
        
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(pk__in=product_ids)
        
        cart = self.cart.copy()
                        
        for product in products:            
            cart[str(product.id)]['product_id'] = product.id
            cart[str(product.id)]['product'] = product.name
            cart[str(product.id)]['image'] = str(product.image)
            
        for item in cart.values():  
            #getcontext().prec = -2
            item['total'] = str(Decimal(item['price']) * item['quantity'])
            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
    
    def get_total_items(self):
        return sum(item['quantity'] for item in self.cart.values())
                
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
       
