import factory
from ..models import Product
from apps.category.tests.factories import CategoryFactory, BrandFactory

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    name = "test_product"
    description = "test_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)