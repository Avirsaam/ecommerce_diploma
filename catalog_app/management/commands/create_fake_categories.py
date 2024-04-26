from django.core.management.base import BaseCommand
from catalog_app.models import ProductCategory, Product
from random import choice, randint, random, choices
from datetime import date, timedelta


class Command(BaseCommand):
    help = "Категориями товаров"
    
    def handle(self, *args, **kwargs):
                
        LOREM = """Occaecat adipisicing ipsum exercitation non est laboris cillum culpa pariatur. Nostrud mollit dolor aliqua eiusmod proident ad est pariatur reprehenderit irure nostrud voluptate occaecat. Quis sit qui Lorem consequat culpa sint tempor labore commodo velit. Ex culpa labore consequat in sint aliquip commodo. Qui dolor fugiat nulla minim id magna et. Dolor laboris fugiat eiusmod enim proident qui nisi esse elit proident esse magna aliqua proident. Minim consequat incididunt Lorem nostrud magna ut elit consequat fugiat commodo veniam labore amet est.                   Adipisicing in tempor minim cillum est cillum anim reprehenderit culpa dolor ea esse eiusmod consectetur. Ut enim est sunt dolor. Anim do amet nulla exercitation. Ipsum excepteur ad reprehenderit officia enim et sint. Aliqua minim sint ea reprehenderit sint.
            Eu est voluptate mollit sunt commodo mollit enim ut minim amet ullamco incididunt eiusmod nisi. Nisi exercitation do dolore amet nisi fugiat ex do id quis. Elit ullamco esse id veniam ad nostrud irure. Pariatur Lorem fugiat tempor velit irure velit dolor ex. Labore do qui qui magna exercitation veniam eu. Cillum velit consequat tempor ex ea dolore ipsum nisi. Magna irure ut adipisicing voluptate.
            Adipisicing nisi minim labore dolor ea labore dolor. In dolor non elit laborum do quis do dolor Lorem et commodo aliquip. Fugiat deserunt excepteur tempor eu aliquip excepteur ad. Esse pariatur ex ipsum minim cillum nostrud enim voluptate. Excepteur ad Lorem quis dolor excepteur proident pariatur et laboris nisi sit excepteur ad. Officia laborum amet laborum dolore est ullamco aliqua elit nostrud ad. Cupidatat ullamco fugiat reprehenderit culpa ad exercitation.
            """
                
        
        categories = {
            'Пряжа': 'Различные виды пряжи для вязания',
            'Наборы': 'Наборы для вязания, включающие пряжу и инструкции',
            'Книги': 'Книги с описанием моделей и схемами для вязания',
            'Узоры': 'Различные узоры и техники вязания',
            'Спицы': 'Различные виды спиц для вязания',
            'Крючки': 'Различные виды крючков для вязания крючком',
            'Аксессуары': 'Различные аксессуары для вязания, такие как иглы, маркеры и т.д.'
        }
        
        for name, description in categories.items():
            category = ProductCategory(
                name=name,
                description=description,
                image='images/default_category.png',
            )
        
            category.save()
            self.stdout.write(f'{category}')
        
