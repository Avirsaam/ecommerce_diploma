from django import template
from catalog_app.models import ProductCategory
from cart_app.cart import Cart

register = template.Library()

@register.simple_tag
def get_all_categories():    
    return ProductCategory.objects.all()

@register.simple_tag
def cart_total_items_tag(request):    
    cart = Cart(request)
    return cart.get_total_items()

