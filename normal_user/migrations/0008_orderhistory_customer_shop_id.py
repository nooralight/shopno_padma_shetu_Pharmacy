# Generated by Django 4.1.3 on 2023-01-17 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0007_orderhistory_customer_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory_customer',
            name='shop_id',
            field=models.BigIntegerField(default=2),
        ),
    ]
