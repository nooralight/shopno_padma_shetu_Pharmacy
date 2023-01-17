from django.db import models

# Create your models here.

class OrderHistory_customer(models.Model):
    purchase_date = models.DateTimeField()
    cart_id = models.BigIntegerField()
    shop_id = models.BigIntegerField()
    product_name = models.TextField(max_length=255)
    address = models.TextField(max_length=255, default="ddd")
    quantity = models.TextField(max_length=255,default="sfrs")
    customer_id = models.BigIntegerField()
    total = models.TextField(max_length=255)
    verified = models.CharField(max_length=3,default="Yes")
