from rest_framework import serializers

from .models import Product, ProductLine
from ..category.serializers import BrandSerializer, CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = "__all__"
        
class ProductLineSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = ProductLine
        fields = "__all__"