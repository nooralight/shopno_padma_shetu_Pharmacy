from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    phone = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    isAdmin = models.CharField(default='0' , max_length=2)

    def __str__(self):
        return self.first_name

class Company(models.Model):
    com_name = models.TextField(max_length=255)
    admin_name = models.TextField(max_length=255)
    com_email = models.EmailField(max_length=255,unique=True)
    com_phone = models.TextField(max_length=255)
    tin_no = models.TextField(max_length=255)
    com_address = models.TextField(max_length=255)
    website = models.TextField(max_length=255)
    com_reg_no = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    company_logo = models.TextField(max_length=255)

    def __str__(self):
        return self.com_name

class Seller(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    shop_name = models.TextField(max_length=255,unique=True)
    photo = models.TextField(max_length=255, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True,null=True)
    email = models.EmailField(max_length=255,unique=True)
    phone = models.TextField(max_length=255)
    password = models.TextField(max_length=255)

    def __str__(self):
        return self.shop_name


