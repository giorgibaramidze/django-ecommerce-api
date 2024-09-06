from pytest_factoryboy import register
from rest_framework.test import APIClient
from apps.category.tests.factories import CategoryFactory, BrandFactory
from apps.product.tests.factories import ProductFactory, ProductLineFactory
import pytest

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductLineFactory)

@pytest.fixture
def api_client():
    return APIClient