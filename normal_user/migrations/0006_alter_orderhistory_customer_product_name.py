# Generated by Django 4.1.3 on 2023-01-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0005_orderhistory_customer_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory_customer',
            name='product_name',
            field=models.TextField(max_length=255),
        ),
    ]