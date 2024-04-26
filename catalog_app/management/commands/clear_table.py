from django.core.management.base import BaseCommand
from catalog_app.models import ProductCategory, Product
from random import choice, randint, random, choices
import os

class Command(BaseCommand):
    help = "Удалить записи"
    def add_arguments(self, parser):
        parser.add_argument('table', type=str, help='тип данных')
            
    def handle(self, *args, **kwargs):
        
        table = kwargs['table']
        
        if table == 'products':
            print(f'Deleted {Product.objects.all().delete()} records')
        else:
            print("unknown table")
            
