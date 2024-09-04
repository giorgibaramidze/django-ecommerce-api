from django.db import models
from mptt.models import TreeForeignKey, MPTTModel

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    
    class MPTTMeta:
        order_insertion_by = ["name"]
        
    class Meta:
        db_table = "category"
    
    def __str__(self):
        return self.name