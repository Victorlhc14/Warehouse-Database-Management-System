from django.shortcuts import render
from .permissions import IsOwner


class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]

class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsOwner]

class Stock_On_HandViewset(viewsets.ModelViewSet):
    queryset = models.Stock_On_Hand.objects.all()
    serializer_class = serializers.Stock_On_HandSerializer
    permission_classes = [IsOwner]