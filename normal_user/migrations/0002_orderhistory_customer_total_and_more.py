# Generated by Django 4.1.3 on 2023-01-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory_customer',
            name='total',
            field=models.TextField(default='sdvvsv', max_length=255),
        ),
        migrations.AddField(
            model_name='orderhistory_customer',
            name='verified',
            field=models.CharField(default='Yes', max_length=3),
        ),
    ]
