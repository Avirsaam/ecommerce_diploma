# Generated by Django 5.0.4 on 2024-04-24 21:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0004_alter_product_rating'),
        ('orders_app', '0002_alter_discount_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Детали заказа',
                'verbose_name_plural': 'Информация о заказе',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders_app.orderdetail')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_app.product')),
            ],
            options={
                'verbose_name': 'Товары в заказе',
                'verbose_name_plural': 'Список товаров по номеру заказа',
            },
        ),
    ]