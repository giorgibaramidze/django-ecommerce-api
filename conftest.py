from pytest_factoryboy import register
from apps.category.tests.factories import CategoryFactory, BrandFactory
from apps.product.tests.factories import ProductFactory


register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)