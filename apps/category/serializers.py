from rest_framework import serializers

from .models import Brand, Category

class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = ["name"]

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="name")
    class Meta:
        model = Category
        fields = ["category_name"]