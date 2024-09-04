from rest_framework import serializers

from .models import Product
from ..category.serializers import BrandSerializer, CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = "__all__"