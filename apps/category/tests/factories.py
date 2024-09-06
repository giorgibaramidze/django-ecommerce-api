import factory
from ..models import Category, Brand

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    name = factory.Sequence(lambda n: "category-%d" % n)
    slug = factory.Sequence(lambda n: "category-%d" % n)
    is_active = True
    
class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
        
    name = factory.Sequence(lambda n: "brand_%d" % n)
    
    