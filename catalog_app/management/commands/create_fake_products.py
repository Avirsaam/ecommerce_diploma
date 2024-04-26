from django.core.management.base import BaseCommand
from catalog_app.models import ProductCategory, Product
from random import choice, randint, random, choices
import os

class Command(BaseCommand):
    help = "Наполнить базу товарами"
    
    def handle(self, *args, **kwargs):
                
        LOREM = """Occaecat adipisicing ipsum exercitation non est laboris cillum culpa pariatur. Nostrud mollit dolor aliqua eiusmod proident ad est pariatur reprehenderit irure nostrud voluptate occaecat. Quis sit qui Lorem consequat culpa sint tempor labore commodo velit. Ex culpa labore consequat in sint aliquip commodo. Qui dolor fugiat nulla minim id magna et. Dolor laboris fugiat eiusmod enim proident qui nisi esse elit proident esse magna aliqua proident. Minim consequat incididunt Lorem nostrud magna ut elit consequat fugiat commodo veniam labore amet est.                   Adipisicing in tempor minim cillum est cillum anim reprehenderit culpa dolor ea esse eiusmod consectetur. Ut enim est sunt dolor. Anim do amet nulla exercitation. Ipsum excepteur ad reprehenderit officia enim et sint. Aliqua minim sint ea reprehenderit sint.
            Eu est voluptate mollit sunt commodo mollit enim ut minim amet ullamco incididunt eiusmod nisi. Nisi exercitation do dolore amet nisi fugiat ex do id quis. Elit ullamco esse id veniam ad nostrud irure. Pariatur Lorem fugiat tempor velit irure velit dolor ex. Labore do qui qui magna exercitation veniam eu. Cillum velit consequat tempor ex ea dolore ipsum nisi. Magna irure ut adipisicing voluptate.
            Adipisicing nisi minim labore dolor ea labore dolor. In dolor non elit laborum do quis do dolor Lorem et commodo aliquip. Fugiat deserunt excepteur tempor eu aliquip excepteur ad. Esse pariatur ex ipsum minim cillum nostrud enim voluptate. Excepteur ad Lorem quis dolor excepteur proident pariatur et laboris nisi sit excepteur ad. Officia laborum amet laborum dolore est ullamco aliqua elit nostrud ad. Cupidatat ullamco fugiat reprehenderit culpa ad exercitation.
            """
                
        
        products = {
            'Пряжа': [
                {'название': 'Мериносовая пряжа', 'описание': 'Натуральная мериносовая пряжа разных цветов', 'цена': 500},
                {'название': 'Хлопковая пряжа', 'описание': 'Пряжа из натурального хлопка в мотках', 'цена': 300},
                {'название': 'Альпака', 'описание': 'Пряжа из альпаки, мягкая и теплая', 'цена': 700},
                {'название': 'Шерстяная пряжа', 'описание': 'Пряжа из натуральной шерсти, идеальна для вязания свитеров', 'цена': 450},
                {'название': 'Льняная пряжа', 'описание': 'Пряжа из натурального льна, подходит для вязания летних изделий', 'цена': 350},
                {'название': 'Шелковая пряжа', 'описание': 'Элегантная шелковая пряжа для создания изысканных вещей', 'цена': 800},
                {'название': 'Вискозная пряжа', 'описание': 'Пряжа из вискозного волокна, мягкая и шелковистая на ощупь', 'цена': 550},
                {'название': 'Смесовая пряжа', 'описание': 'Пряжа смешанного состава для разнообразных вязаных изделий', 'цена': 600},
                {'название': 'Полушерстяная пряжа', 'описание': 'Пряжа с добавлением шерсти, комфортная и теплая', 'цена': 480},
                {'название': 'Бамбуковая пряжа', 'описание': 'Экологически чистая бамбуковая пряжа, легкая и приятная к телу', 'цена': 650},
            ],
            'Наборы': [
                {'название': 'Набор для вязания шарфа', 'описание': 'Набор включает пряжу и инструкцию', 'цена': 800},
                {'название': 'Набор для вязания игрушки', 'описание': 'В наборе все необходимое для создания мягкой игрушки', 'цена': 1000},
                {'название': 'Набор для вязания пледа', 'описание': 'В наборе достаточно пряжи для создания теплого пледа', 'цена': 1200},
                {'название': 'Набор для вязания кардигана', 'описание': 'Набор включает пряжу и инструкцию для вязания модного кардигана', 'цена': 1100},
                {'название': 'Набор для вязания сумки', 'описание': 'В наборе все необходимое для создания стильной вязаной сумки', 'цена': 900},
                {'название': 'Набор для вязания шапки', 'описание': 'Набор включает пряжу и инструкцию для вязания модной шапки', 'цена': 750},
                {'название': 'Набор для вязания пинеток', 'описание': 'В наборе все необходимое для создания милых пинеток', 'цена': 600},
                {'название': 'Набор для вязания платья', 'описание': 'Набор включает пряжу и инструкцию для вязания элегантного платья', 'цена': 1300},
                {'название': 'Набор для вязания свитера', 'описание': 'Набор включает пряжу и инструкцию для вязания уютного свитера', 'цена': 950},
                {'название': 'Набор для вязания носков', 'описание': 'В наборе все необходимое для создания теплых носков', 'цена': 700},
            ],
            'Книги': [
                {'название': 'Справочник по вязанию', 'описание': 'Подробное описание различных техник и узоров', 'цена': 600},
                {'название': 'Модели для вязания', 'описание': 'Книга с описанием моделей для вязания', 'цена': 450},
                {'название': 'Вязание для начинающих', 'описание': 'Книга с пошаговыми инструкциями для новичков', 'цена': 550},
                {'название': 'Креативное вязание', 'описание': 'Идеи для творческих проектов и необычных узоров', 'цена': 700},
                {'название': 'Вязание для детей', 'описание': 'Книга с моделями для вязания детской одежды и игрушек', 'цена': 500},
                {'название': 'Мастер-классы по вязанию', 'описание': 'Подробные уроки с фото и описанием шагов', 'цена': 800},
                {'название': 'Журнал вязания', 'описание': 'Журнал с новыми моделями и идеями для вязания', 'цена': 350},
                {'название': 'Книга с ажурными узорами', 'описание': 'Сборник узоров для создания красивых ажурных вещей', 'цена': 650},
                {'название': 'Книга о технике вязания', 'описание': 'Подробное руководство по различным техникам вязания', 'цена': 600},
                {'название': 'Книга о вязаных аксессуарах', 'описание': 'Идеи для создания модных вязаных аксессуаров', 'цена': 550},
            ],
            'Узоры': [
                {'название': 'Косы и плетение', 'описание': 'Сборник узоров для вязания кос и плетения', 'цена': 350},
                {'название': 'Ажурные узоры', 'описание': 'Коллекция узоров для создания ажурных изделий', 'цена': 400},
                {'название': 'Узоры для носков', 'описание': 'Подборка узоров для вязания теплых носков', 'цена': 300},
                {'название': 'Геометрические узоры', 'описание': 'Идеи для вязания изделий с геометрическими узорами', 'цена': 450},
                {'название': 'Акварельные узоры', 'описание': 'Узоры с яркими и красочными цветами, напоминающие акварельные картины', 'цена': 500},
                {'название': 'Узоры для пледов', 'описание': 'Идеи для вязания узоров на пледы и одеяла', 'цена': 380},
                {'название': 'Фэшн-узоры', 'описание': 'Модные узоры для создания стильных вязаных изделий', 'цена': 550},
                {'название': 'Волнообразные узоры', 'описание': 'Узоры, имитирующие волны и океанские волны', 'цена': 420},
                {'название': 'Ромбовые узоры', 'описание': 'Идеи для вязания изделий с ромбовыми узорами', 'цена': 470},
                {'название': 'Узоры для пончо', 'описание': 'Коллекция узоров для создания стильных вязаных пончо', 'цена': 600},
            ],
            'Спицы': [
                {'название': 'Комплект спиц', 'описание': 'Набор из различных размеров спиц', 'цена': 750},
                {'название': 'Деревянные спицы', 'описание': 'Спицы из натурального дерева', 'цена': 900},
                {'название': 'Металлические спицы', 'описание': 'Спицы из легкого металла, прочные и долговечные', 'цена': 600},
                {'название': 'Пластиковые спицы', 'описание': 'Спицы с эргономичными ручками для удобства вязания', 'цена': 550},
                {'название': 'Спицы с покрытием', 'описание': 'Спицы с покрытием от скольжения для легкости вязания', 'цена': 800},
                {'название': 'Прямые спицы', 'описание': 'Спицы для вязания плоских изделий и шарфов', 'цена': 400},
                {'название': 'Круговые спицы', 'описание': 'Спицы для вязания круглых изделий без швов', 'цена': 700},
                {'название': 'Спицы с длинным каблуком', 'описание': 'Спицы с каблуком для вязания крупных изделий', 'цена': 950},
                {'название': 'Мелкие спицы', 'описание': 'Спицы меньшего размера для вязания тонких изделий', 'цена': 500},
                {'название': 'Большие спицы', 'описание': 'Спицы большого размера для вязания плотных изделий', 'цена': 850},
            ],
            'Крючки': [
                {'название': 'Набор крючков', 'описание': 'Набор из крючков разных размеров', 'цена': 550},
                {'название': 'Крючки с пластиковой ручкой', 'описание': 'Удобные крючки с эргономичной ручкой', 'цена': 400},
                {'название': 'Металлические крючки', 'описание': 'Прочные крючки из металла для вязания толстых ниток', 'цена': 600},
                {'название': 'Крючки с деревянной ручкой', 'описание': 'Крючки с натуральной деревянной ручкой для комфортного вязания', 'цена': 450},
                {'название': 'Крючки с крючком', 'описание': 'Крючки с плоским крючком для удобства вязания', 'цена': 500},
                {'название': 'Крючки для крупных ниток', 'описание': 'Крючки для вязания толстых ниток и больших изделий', 'цена': 700},
                {'название': 'Крючки для тонких ниток', 'описание': 'Крючки для вязания тонких ниток и деликатных изделий', 'цена': 450},
                {'название': 'Пластиковые крючки', 'описание': 'Крючки из прочного пластика для долговечного использования', 'цена': 300},
                {'название': 'Эргономичные крючки', 'описание': 'Крючки с резиновой ручкой для удобства вязания', 'цена': 550},
                {'название': 'Крючки с закругленным крючком', 'описание': 'Крючки с закругленным крючком для вязания краев и отделок', 'цена': 400},
            ],
            'Аксессуары': [
                {'название': 'Набор маркеров', 'описание': 'Набор маркеров для отметок в процессе вязания', 'цена': 150},
                {'название': 'Игла для вязания', 'описание': 'Игла для сбора петель и завязывания концов', 'цена': 200},
                {'название': 'Мерительная лента', 'описание': 'Лента для измерения длины и ширины вязаных изделий', 'цена': 100},
                {'название': 'Блокнот для вязания', 'описание': 'Блокнот для записи схем и идей для вязания', 'цена': 80},
                {'название': 'Набор иголок', 'описание': 'Набор иголок для фиксации и сшивания вязаных деталей', 'цена': 120},
                {'название': 'Терка для шерсти', 'описание': 'Терка для снятия катышек и лишней шерсти с вязаных изделий', 'цена': 90},
                {'название': 'Помпон для шапки', 'описание': 'Пушистый помпон для украшения вязаной шапки', 'цена': 70},
                {'название': 'Металлические крючки для маркировки', 'описание': 'Крючки для маркировки и отделения петель в процессе вязания', 'цена': 180},
                {'название': 'Набор для вышивки на вязаных изделиях', 'описание': 'Набор для вышивки узоров и узоров на вязаных изделиях', 'цена': 250},
                {'название': 'Комплект для обработки краев', 'описание': 'Набор инструментов для обработки и закрепления краев вязаных изделий', 'цена': 300},
            ]
        }
        media_dir = 'products'
        image_list = os.listdir(os.path.join('media',media_dir))
        
        for category_name, products_list in products.items():
            for product_dict in products_list:
                category = ProductCategory.objects.filter(name__icontains=category_name).first()
                product = Product(
                    name=product_dict.get('название'),
                    description=product_dict.get('описание'),
                    price=product_dict.get('цена'),
                    category=category,
                    image = os.path.join(media_dir, choice(image_list)),
                    rating=(randint(0,5)),
                    
                )        
                product.save()
                self.stdout.write(f'{product} {product.image}')
        
