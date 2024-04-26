# Generated by Django 5.0.4 on 2024-04-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0003_orderdetail_orderitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='address',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='phone',
            field=models.CharField(default=None, max_length=12),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='status',
            field=models.CharField(choices=[('Неоплачен', 'Неоплачен'), ('Оплачен', 'Оплачен'), ('Доставляется', 'Доставляется'), ('Доставлен', 'Доставлен')], max_length=100),
        ),
    ]
