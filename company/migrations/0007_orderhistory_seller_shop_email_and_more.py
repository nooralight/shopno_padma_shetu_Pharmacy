# Generated by Django 4.1.3 on 2023-02-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_orderhistory_seller_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory_seller',
            name='shop_email',
            field=models.EmailField(default='Something@gmail.com', max_length=255),
        ),
        migrations.AddField(
            model_name='orderhistory_seller',
            name='shop_name',
            field=models.TextField(default='Something', max_length=255),
        ),
        migrations.AddField(
            model_name='orderhistory_seller',
            name='shop_phone',
            field=models.TextField(default='01571238110', max_length=255),
        ),
    ]