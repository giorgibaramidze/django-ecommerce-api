import factory
from ..models import Category, Brand

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    name = "test_category"
    
class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
        
    name = "test_brand"
    
    