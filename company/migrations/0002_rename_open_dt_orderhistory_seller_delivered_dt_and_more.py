# Generated by Django 4.1.3 on 2023-01-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderhistory_seller',
            old_name='open_dt',
            new_name='delivered_dt',
        ),
        migrations.AddField(
            model_name='orderhistory_seller',
            name='delivered',
            field=models.TextField(default='No', max_length=20),
        ),
    ]
