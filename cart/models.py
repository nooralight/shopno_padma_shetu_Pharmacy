from django.db import models

# Create your models here.
class Cart(models.Model):
    shop_id= models.BigIntegerField()
    product_id = models.BigIntegerField()
    customer_id = models.BigIntegerField()
    product_name = models.TextField(max_length=255)
    quantity = models.TextField(max_length=255)
    total_price = models.TextField(max_length=255)
    prescription = models.TextField(null=True,blank=True)
    order_date =  models.DateTimeField()
    active =  models.CharField(max_length=3,default="Yes")
