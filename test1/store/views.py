from django.shortcuts import render
from .models import Product
from rest_framework import generics 
from .serializers import ProductSerializer

class AllProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Latest(generics.ListCreateAPIView):
    queryset = Product.objects.filter(feature__icontains='Latest')[:6]
    serializer_class = ProductSerializer

class LatestProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(feature__icontains='Latest')
    serializer_class = ProductSerializer

# what i need to do is to create filters to render different resources to 
# different pages, so i have pages for each brand (Samsung, Iphone, .. ), and according
# to the vendor, the filter will take place.. 

class Samsung(generics.ListCreateAPIView):
    queryset = Product.objects.filter(vendor__iexact='Samsung')
    serializer_class = ProductSerializer

class Samsung_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Samsung_Gallery(generics.ListCreateAPIView):
    # this is limited specifically for the gallery items 
    queryset = Product.objects.filter(vendor__iexact='Samsung')[:7]
    serializer_class = ProductSerializer


class Apple(generics.ListCreateAPIView):
    queryset = Product.objects.filter(vendor__iexact='Apple')
    serializer_class = ProductSerializer

class Apple_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Apple_Gallery(generics.ListCreateAPIView):
    # this is limited specifically for the gallery items 
    queryset = Product.objects.filter(vendor__iexact='Apple')[:7]
    serializer_class = ProductSerializer


class Huawei(generics.ListCreateAPIView):
    queryset = Product.objects.filter(vendor__iexact='Huawei')
    serializer_class = ProductSerializer

class Huawei_Gallery(generics.ListCreateAPIView):
    queryset = Product.objects.filter(vendor__iexact='Huawei')[:7]
    serializer_class = ProductSerializer

class Huawei_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

