import pytest
import json
import factory
pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:
    endpoint = '/api/product/'
    
    def test_category_get(self, product_factory, api_client):
        product_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4