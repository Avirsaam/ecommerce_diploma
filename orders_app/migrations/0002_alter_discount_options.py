# Generated by Django 3.2.12 on 2024-04-22 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name': 'Скидки', 'verbose_name_plural': 'Скидки и акции на товары'},
        ),
    ]
