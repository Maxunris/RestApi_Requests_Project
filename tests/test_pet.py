import pytest
import requests
import json
from tests.base import add_new_pet
from schemas.add_pet_schema import add_pet
from jsonschema import validate


def test_add_new_pet():
    url = 'https://petstore.swagger.io/v2/pet'
    payload = add_new_pet()
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url=url, headers=headers, data=payload)

    print(response.text)
    assert response.status_code == 200
    validate(response.json(), add_pet)



def update_pet():
    pass