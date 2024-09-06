from pytest_factoryboy import register
from rest_framework.test import APIClient
from apps.category.tests.factories import CategoryFactory, BrandFactory
from apps.product.tests.factories import ProductFactory
import pytest

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

@pytest.fixture
def api_client():
    return APIClient