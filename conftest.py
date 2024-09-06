from pytest_factoryboy import register
from apps.category.tests.factories import CategoryFactory, BrandFactory

register(CategoryFactory)
register(BrandFactory)