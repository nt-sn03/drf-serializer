from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    name = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image', 'products')
