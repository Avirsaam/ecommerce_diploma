from django.db import models
from gallery_app.models import Image
from django.core.validators import MaxValueValidator
from orders_app.models import Discount
from decimal import Decimal


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(blank=True, verbose_name='Описание категории')
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    
    class Meta:
      verbose_name = 'Категория'
      verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return self.name

class Product(models.Model):
    MAX_RATING = 5
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    description = models.TextField(blank=True, verbose_name='Описание продукта')        
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')
    rating = models.IntegerField(validators=[MaxValueValidator(MAX_RATING)])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    
    class Meta:
      verbose_name = 'Товар'
      verbose_name_plural = 'Товары'
    
    @property
    def isSale(self):        
        #TODO
        return Discount.objects.filter(products=self).all().count() > 0
    
    @property
    def price_discount(self):
        #TODO
        if self.isSale:
          total_discount = Discount.objects.filter(products=self).aggregate(total=models.Sum('discount_value'))                            
          return self.price * total_discount["total"] / 100
        return self.price
    
    def get_rating_stars(self):            
      return [True if i < self.rating else False for i in range(self.MAX_RATING)]

    def __str__(self):
        return self.name