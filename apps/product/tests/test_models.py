from unittest.mock import patch
import pytest
from django.core.exceptions import ValidationError
from django.core import checks
from apps.product.models import OrderField, ProductLine

pytestmark = pytest.mark.django_db

class TestProductModel:
    def test_str_method(self, product_factory):
        obj = product_factory(name="test_product")
        
        assert obj.__str__() == "test_product"
        
class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        obj = product_line_factory(sku="12")
        assert obj.__str__() == "12"
        
    def test_duplicate_order_values(self, product_line_factory, product_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj).clean()
            