from django.db import models

# Create your models here.

class OrderHistory_customer(models.Model):
    purchase_date = models.DateTimeField()
    cart_id = models.BigIntegerField()
