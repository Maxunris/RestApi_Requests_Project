from tests.base import add_new_pet, main_headers
from schemas.pet_schema import pet_schema
from jsonschema import validate
from utils.requests_helper import api_request
import pytest
import allure
@allure.title("Add new pet")
def test_add_new_pet_negarive(base_api_url):
    endpoint = "pet"
    payload = add_new_pet()
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "GET", headers=headers, data=payload)
    with allure.step('Status code=405'):
        assert response.status_code == 405
    response = api_request(base_api_url, endpoint, "DELETE", headers=headers, data=payload)
    with allure.step('Status code=405'):
        assert response.status_code == 405
    response = api_request(base_api_url, endpoint, "PATCH", headers=headers, data=payload)
    with allure.step('Status code=405'):
        assert response.status_code == 405
