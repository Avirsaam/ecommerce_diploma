from django.core.management.base import BaseCommand
from catalog_app.models import ProductCategory, Product
from orders_app.models import Discount
from random import choice, randint, random, choices
import os

class Command(BaseCommand):
    help = "Создать скидки и применить их к определенному числу товаров"
    
    # def add_arguments(self, parser):
    #     parser.add_argument('discounts', type=int, help='Количество ссылок')
    #     parser.add_argument('probability', type=int, help='вероятность срабатывания скидки')
    
    def handle(self, *args, **kwargs):
                
        discounts_dict = [
                        {
                            "name": "Товар дня",
                            "discount_size": 0.2,                            
                        },
                        {
                            "name": "Сезонная скидка",
                            "discount_size": 0.3,                            
                        },
                        {
                            "name": "Бесплатная доставка",
                            "discount_size": 0.3,                            
                        }                        
                    ]
        
        for discount_dict in discounts_dict:
            discount = Discount(
                name=discount_dict['name'],
                discount_value=discount_dict['discount_size'] * 100                
            )
            discount.save()
            self.stdout.write(f'{discount}')
            
        
        discounts = Discount.objects.all()
        products = Product.objects.all()
                
        
        for discount in discounts:            
            for product in products:
                if  random() < 0.15:
                    discount.products.add(product)
                    discount.save()
                    
                
        
