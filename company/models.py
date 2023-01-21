from django.db import models

# Create your models here.
class Company_product(models.Model):
    name = models.TextField(max_length=255)
    product_photo = models.TextField(max_length=255)
    category = models.TextField(max_length=255)
    #email = models.EmailField(max_length=255,unique=True)
    price = models.TextField(max_length=255)
    company_id = models.BigIntegerField()
    company_name = models.TextField(max_length=255)
    ##TODO
    generic_name = models.TextField(max_length=255,null=True,blank=True) #Naproxen Sodium 500mg
    ##TODO
    sub_category = models.TextField(max_length=255) #Tablet, Lotion, Tablet pot, Oral Solution, solution, Suspension, Oral Suspension,
    contradiction = models.TextField(max_length=1500,null=True,blank=True)
    pharmacology = models.TextField(max_length=1500,null=True,blank=True)
    interaction = models.TextField(max_length=1500,null=True,blank=True)
    side_effects = models.TextField(max_length=1500,null=True,blank=True)
    pregnancy = models.TextField(max_length=1500,null=True,blank=True)
    warnings = models.TextField(max_length=1500,null=True,blank=True)
    therapeutic = models.TextField(max_length=1500,null=True,blank=True)
    storage_condition = models.TextField(max_length=1500,null=True,blank=True)


class OrderHistory_seller(models.Model):
    company_id = models.BigIntegerField()
    company_name = models.TextField(max_length=255)
    seller_id = models.BigIntegerField()
    product_name = models.TextField(max_length=255)
    quantity = models.TextField(max_length=255)
    verified = models.TextField(max_length=255,default="No")
    order_dt = models.DateTimeField()
    total_price = models.TextField(default="svdfbdf")
    delivered_dt = models.DateTimeField(blank=True, null=True)
    delivered = models.TextField(max_length=20,default="No")
