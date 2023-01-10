from django.db import models

# Create your models here.
class Shop_product(models.Model):
    name = models.TextField(max_length=255)
    brand_name = models.TextField(max_length=255)
    product_photo = models.TextField(max_length=255)
    category = models.TextField(max_length=255)
    #email = models.EmailField(max_length=255,unique=True)
    quantity = models.TextField(max_length=255)
    price = models.TextField(max_length=255)
    shop_id = models.BigIntegerField()
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

    def __str__(self):
        return self.name