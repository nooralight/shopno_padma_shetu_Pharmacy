# Generated by Django 4.1.3 on 2023-01-15 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.BigIntegerField()),
                ('product_id', models.BigIntegerField()),
                ('product_name', models.TextField(max_length=255)),
                ('quantity', models.TextField(max_length=255)),
                ('total_price', models.TextField(max_length=255)),
                ('prescription', models.FileField(blank=True, null=True, upload_to='prescriptions/')),
                ('order_date', models.DateTimeField()),
            ],
        ),
    ]
