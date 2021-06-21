from django.db.models.query import QuerySet
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics


from .serializer import *
from .models import *

# class ProductViews(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

class CategoryViews(generics.ListAPIView):
    serializer_class = CategorySerializer()
    queryset = Category.objects.all()


class ProductCardView(generics.ListAPIView):
    queryset = Product.objects.all()
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductCardSerializers(queryset, many=True)
        return Response(serializer.data)     
    
class ProductCartWithEmpty(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    def get(self, request, slug):
        queryset = Product.objects.filter(slug=slug)
        for product in queryset:
            if product.amount > 0:
                queryset = Product.objects.filter(slug=slug)
                serializer_class = ProductCardSerializers(queryset, many=True)
                return Response(serializer_class.data)
            else:
                queryset = Product.objects.filter(slug=slug)
                serializer_class = ProductCardNoAmountSerializers(queryset, many=True)
                return Response(serializer_class.data)

class ProfileViews(generics.ListAPIView):
    queryset = Profile.objects.all()
    def get(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

class ProfileKorzinaViews(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    def get(self, request, pk):
        queryset = Profile.objects.filter(pk=pk)
        serializer = ProfileKorzinaSerializer(queryset, many=True)
        return Response(serializer.data)