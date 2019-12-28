from django.shortcuts import render

# Create your views here.
#from rest_framework import generics
from rest_framework import viewsets


from . import models
from . import serializers

class UserListView(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer