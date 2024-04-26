from django.db import models
from django.contrib import admin

from django.contrib.auth.models import User

class Discount(models.Model):
    name = models.CharField(max_length=100)
    discount_value = models.DecimalField(max_digits=5, decimal_places=2)    
    products = models.ManyToManyField('catalog_app.Product')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} - {self.discount_value}'
    
    class Meta:
      verbose_name = 'Скидки'
      verbose_name_plural = 'Скидки и акции на товары'
      
     

class OrderDetail(models.Model):
    ORDER_STATUS = (
        ('Неоплачен', 'Неоплачен'),
        ('Оплачен', 'Оплачен'),
        ('Доставляется', 'Доставляется'),
        ('Доставлен', 'Доставлен'),
        )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, default=None)
    address = models.CharField(max_length=250, default=None)
    status = models.CharField(choices=ORDER_STATUS, max_length=100, default=ORDER_STATUS[0][0], verbose_name='Статус заказа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')    
    #TODO
    #payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    #детали доставки выделить в отдельную модель с привязкой к пользователю
    
       
    def get_order_items(self):
        return OrderItem.objects.filter(order=self).all()
    
    @admin.display(description='Общая сумма заказа')
    def get_total(self):
        return sum(item.total() for item in self.get_order_items())
    
    def __str__(self):
        return f'{self.user} - {self.created_at}'
    
    class Meta:
      verbose_name = 'Заказ'
      verbose_name_plural = 'Заказы'
    
class OrderItem(models.Model):    
    product = models.ForeignKey('catalog_app.Product', on_delete=models.CASCADE)   
    order =  models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    final_price = models.DecimalField(max_digits=9, decimal_places=2)    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.product}'
    
    def total(self):
        return self.quantity * self.final_price
