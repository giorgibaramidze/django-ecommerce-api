from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
        
    