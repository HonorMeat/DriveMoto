from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta: 
        model = Product
        fields = ('category', 'model')


class ProductCardSerializers(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ('category', 'model', 'cost')


class ProductCardNoAmountSerializers(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ('category', 'model', 'empty')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    izbrannye = ProductSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('user', 'avatar')

class ProfileKorzinaSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    izbrannye = ProductSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('user', 'izbrannye')