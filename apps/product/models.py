from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False) 
    
    class Meta:
        db_table = "product"
    
    def __str__(self):
        return self.name
