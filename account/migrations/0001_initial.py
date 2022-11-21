# Generated by Django 4.1.3 on 2022-11-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_name', models.TextField(max_length=255)),
                ('admin_name', models.TextField(max_length=255)),
                ('com_email', models.EmailField(max_length=255, unique=True)),
                ('com_phone', models.TextField(max_length=255)),
                ('tin_no', models.TextField(max_length=255)),
                ('com_address', models.TextField(max_length=255)),
                ('website', models.TextField(max_length=255)),
                ('com_reg_no', models.TextField(max_length=255)),
                ('password', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=255)),
                ('last_name', models.TextField(max_length=255)),
                ('shop_name', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.TextField(max_length=255)),
                ('password', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=255)),
                ('last_name', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.TextField(max_length=255)),
                ('password', models.TextField(max_length=255)),
                ('isAdmin', models.CharField(default='0', max_length=2)),
            ],
        ),
    ]
