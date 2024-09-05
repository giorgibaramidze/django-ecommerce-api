from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Brand
from rest_framework.response import Response
from .serializers import CategorySerializer, BrandSerializer
from drf_spectacular.utils import extend_schema

class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
        
    