from django.db import models
from mptt.models import TreeForeignKey, MPTTModel

class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    
    class MPTTMeta:
        order_insertion_by = ["name"]
        
    class Meta:
        db_table = "category"
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = "brand"
    
    def __str__(self):
        return self.name