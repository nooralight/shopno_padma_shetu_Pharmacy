# Generated by Django 4.1.3 on 2023-01-06 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0008_remove_shop_product_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_product',
            name='sub_category',
            field=models.TextField(max_length=255),
        ),
    ]
