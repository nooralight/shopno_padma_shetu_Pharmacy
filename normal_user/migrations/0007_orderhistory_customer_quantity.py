# Generated by Django 4.1.3 on 2023-01-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0006_alter_orderhistory_customer_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory_customer',
            name='quantity',
            field=models.TextField(default='sfrs', max_length=255),
        ),
    ]
