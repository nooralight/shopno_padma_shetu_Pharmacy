# Generated by Django 4.1.3 on 2023-01-15 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer_id',
            field=models.BigIntegerField(default=2),
        ),
    ]
