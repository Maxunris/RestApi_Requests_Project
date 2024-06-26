from tests.base import add_new_pet, main_headers
from schemas.pet_schema import pet_schema
from jsonschema import validate
from utils.requests_helper import api_request
import pytest

def test_add_new_pet(base_api_url):
    global main_id

    endpoint = "pet"
    payload = add_new_pet()
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "POST", headers=headers, data=payload)

    assert response.status_code == 200
    assert response.json()['status'] == "available"
    validate(response.json(), pet_schema)
    assert response.json()['name'] == "doggie"
    main_id = response.json()['id']


def test_update_pet(base_api_url):
    payload = {"id": main_id, "category": {"id": 0, "name": "string"}, "name": "cat", "photoUrls": ["string"],
               "tags": [{"id": 0, "name": "string"}], "status": "available"}
    endpoint = "pet"
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "PUT", headers=headers, json=payload)
    assert response.status_code == 200
    validate(response.json(), pet_schema)
    assert response.json()['name'] == "cat"


def test_find_pet_by_id(base_api_url):
    endpoint = (f"pet/{main_id}")
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "GET", headers=headers)
    assert response.status_code == 200
    validate(response.json(), pet_schema)
    assert response.json()['id'] == main_id
    assert response.json()['name'] == "cat"


def test_update_with_form_data(base_api_url):
    endpoint = (f"pet/{main_id}")
    payload = {
        'name': 'Marina',
        'status': 'Switty'
    }
    response = api_request(base_api_url, endpoint, "POST", data=payload)
    assert response.status_code == 200
    assert response.json()['message'] == (f'{main_id}')


@pytest.mark.parametrize(
    "params",
    [{'status': 'available'},
     {'status': 'pending'},
     {'status': 'sold'}],
    ids=["available status", "pending status", "sold status"]
)
def test_find_pet_by_status(base_api_url, params):
    endpoint = "pet/findByStatus"
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "GET", params=params, headers=headers)
    assert response.status_code == 200

    for pet in response.json():
        assert pet['status'] == params['status']



def test_delete_pet(base_api_url):
    endpoint = (f"pet/{main_id}")
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "DELETE", headers=headers)
    assert response.status_code == 200
    assert response.json()['message'] == (f'{main_id}')


def test_find_pet_by_id_after_delete(base_api_url):
    endpoint = (f"pet/{main_id}")
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "GET", headers=headers)
    assert response.status_code == 404
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == 'Pet not found'
