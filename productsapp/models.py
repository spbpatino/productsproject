from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=2000)
    product_tags = models.CharField(max_length=2000)
    creation_date = models.DateTimeField('date published')
    #disabled_date = models.DateTimeField('date disabled')
    user = models.ForeignKey(User, on_delete=models.PROTECT)


"""class ProductsImages(models.Model):
    id = models.AutoField(primary_key=True)
    Image = models.CharField(max_length=1500)
    product = models.ForeignKey(Products, on_delete=models.PROTECT)"""

    
class PlatformUser(User):
    identity_card = models.CharField(max_length=20)    
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
