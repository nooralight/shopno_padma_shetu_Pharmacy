# Generated by Django 4.1.3 on 2023-01-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_orderhistory_seller_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory_seller',
            name='total_price',
            field=models.TextField(default='svdfbdf'),
        ),
    ]
