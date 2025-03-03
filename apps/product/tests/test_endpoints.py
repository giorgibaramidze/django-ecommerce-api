import pytest
import json
import factory
pytestmark = pytest.mark.django_db

class TestProductEndpoints:
    endpoint = '/api/product/'
    
    def test_return_all_products(self, product_factory, api_client):
        product_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4
        
    def test_return_product_by_slug(self, product_factory, api_client):
        obj = product_factory(slug="test-slug")
        response = api_client().get(f"{self.endpoint}{obj.slug}/")
        assert response.status_code == 200
        
    def test_return_product_by_category_slug(self, category_factory, product_factory, api_client):
        obj = category_factory(slug="test-slug")
        product_factory(category=obj)
        response = api_client().get(f"{self.endpoint}category/{obj.slug}/")
        assert response.status_code == 200