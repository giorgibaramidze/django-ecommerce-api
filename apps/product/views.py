from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from django.db import connection


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.isactive().select_related("brand", "category").prefetch_related("product_line")
    serializer_class = ProductSerializer
    lookup_field = "slug"

    @action(methods=["get"], detail=False, url_path=r"category/(?P<category>\w+)")
    def list_product_by_category(self, request, category=None):
        """
        Endpoint for fetching products by category
        """
        products = self.queryset.filter(category__name=category)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


        
    