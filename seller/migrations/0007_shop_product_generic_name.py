# Generated by Django 4.1.3 on 2023-01-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_shop_product_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_product',
            name='generic_name',
            field=models.TextField(default='dfbgfbbg', max_length=255),
        ),
    ]
