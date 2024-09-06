import factory
from apps.product.models import Product, ProductLine
from apps.category.tests.factories import CategoryFactory, BrandFactory

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    name = factory.Faker("word")
    description = "test_description"
    is_digital = True
    is_active = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    

class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True, min_value=1, max_value=1000)
    sku = factory.Sequence(lambda n: f"SKU-{n}")
    stock_qty = factory.Faker('random_int', min=0, max=100)
    product = factory.SubFactory(ProductFactory)
    is_active = factory.Faker('boolean')