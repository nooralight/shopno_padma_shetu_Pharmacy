# Generated by Django 4.1.3 on 2023-01-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_alter_shop_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_product',
            name='descr',
            field=models.TextField(default='fdvdvdfv', max_length=1500),
        ),
    ]