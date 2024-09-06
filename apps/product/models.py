from django.db import models
from ..category.models import Category, Brand
from mptt.models import TreeForeignKey, MPTTModel

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True) 
    category = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        db_table = "product"
    
    def __str__(self):
        return self.name
