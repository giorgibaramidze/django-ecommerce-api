from rest_framework import serializers

from .models import Product, ProductLine
from ..category.serializers import BrandSerializer, CategorySerializer

class ProductLineSerializer(serializers.ModelSerializer):
     class Meta:
        model = ProductLine
        exclude = ["id", "is_active", "product"]

class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source="category.name")
    product_line = ProductLineSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ["id", "name", "slug", "description", "brand_name", "category_name", "product_line"]
        

        
