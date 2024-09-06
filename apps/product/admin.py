from django.contrib import admin
from .models import Product, ProductLine

class ProductLineInline(admin.TabularInline):
    model = ProductLine

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]
    

admin.site.register(ProductLine)