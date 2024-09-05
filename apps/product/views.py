from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    
    lookup_field = "slug"
    
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug), many=True)
        return Response(serializer.data)
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @action(methods=["get"], detail=False, url_path=r"category/(?P<category>\w+)")
    def list_product_by_category(self, request, category=None):
        """
        endpoint product by category
        """
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)
        
    