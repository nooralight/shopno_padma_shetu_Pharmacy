from django.db import models

# Create your models here.

class OrderHistory_customer(models.Model):
    purchase_date = models.DateTimeField()
    cart_id = models.BigIntegerField()
    customer_id = models.BigIntegerField()
    total = models.TextField(max_length=255,default="sdvvsv")
    verified = models.CharField(max_length=3,default="Yes")
