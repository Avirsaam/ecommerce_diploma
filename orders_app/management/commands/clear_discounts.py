from django.core.management.base import BaseCommand
from catalog_app.models import ProductCategory, Product
from orders_app.models import Discount
from random import choice, randint, random, choices



class Command(BaseCommand):
    help = "Удаление скидок"
    
    def handle(self, *args, **kwargs):
        Discount.objects.all().delete()
        
        