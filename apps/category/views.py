from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Product, Brand
from rest_framework.response import Response
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer

class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()
    
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
        
    