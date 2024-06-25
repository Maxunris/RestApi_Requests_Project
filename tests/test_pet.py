import requests
import pytest
from tests.base import add_new_pet, main_headers, update_pet
from schemas.add_pet_schema import add_pet
from jsonschema import validate
from utils.requests_helper import api_request


def test_add_new_pet(base_api_url):

    endpoint = "pet"
    payload = add_new_pet()
    headers = main_headers()
    response = api_request(base_api_url, endpoint,"POST", headers=headers, data=payload)


    print(response.text)
    assert response.status_code == 200
    assert response.json()['status'] == "available"
    validate(response.json(), add_pet)
    return response.json()['id']
def test_update_pet(base_api_url):
    endpoint = "pet"
    payload = update_pet()
    headers = main_headers()
    response = api_request(base_api_url, endpoint,"POST", headers=headers, data=payload)
    assert response.status_code == 200

