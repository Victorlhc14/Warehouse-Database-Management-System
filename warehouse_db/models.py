from django.db import models
from datetime import datetime
from django.conf import settings

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    cost = models.IntegerField()
    manufacturer = models.CharField(max_length=100)

class Stock_On_Hand(models.Model):
    time = models.DateTimeField(auto_now=True)
    product1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='producta')
    quantity1 = models.IntegerField()
    product2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productb')
    quantity2 = models.IntegerField()
    product3 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productc')
    quantity3 = models.IntegerField()


