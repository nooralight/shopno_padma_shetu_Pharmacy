# Generated by Django 4.1.3 on 2023-01-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0009_alter_orderhistory_customer_shop_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory_customer',
            name='address',
            field=models.TextField(default='ddd', max_length=255),
        ),
    ]
