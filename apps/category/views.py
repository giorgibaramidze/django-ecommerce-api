from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from rest_framework.response import Response
from .serializers import CategorySerializer

class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()
    
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
        
    