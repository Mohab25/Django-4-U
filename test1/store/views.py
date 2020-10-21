from django.shortcuts import render
from .models import Product
from rest_framework import generics 
from .serializers import ProductSerializer

class Latest(generics.ListCreateAPIView):
    queryset = Product.objects.filter(feature__icontains='Latest')
    serializer_class = ProductSerializer

class LatestProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(feature__icontains='Latest')
    serializer_class = ProductSerializer