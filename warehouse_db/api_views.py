from rest_framework import viewsets
from . import models
from . import serializers


class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class Stock_On_HandViewset(viewsets.ModelViewSet):
    queryset = models.Stock_On_Hand.objects.all()
    serializer_class = serializers.Stock_On_HandSerializer


