# Generated by Django 4.1.3 on 2023-01-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='shop_name',
            field=models.TextField(max_length=255, unique=True),
        ),
    ]