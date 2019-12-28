from rest_framework import serializers
from . import models
from django.conf import settings


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ('product_id', 'description','brand', 'cost', 'manufacturer')

class Stock_On_HandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Stock_On_Hand
        fields = ('time', 'product1', 'quantity1', 'product2', 'quantity2', 'product3', 'quantity3')