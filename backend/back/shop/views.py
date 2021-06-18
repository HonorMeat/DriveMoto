from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializer import ProductSerializer
from .models import Product

class ProductViews(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()