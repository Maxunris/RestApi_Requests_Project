from tests.base import add_new_pet, main_headers
from schemas.add_pet_schema import add_pet
from jsonschema import validate
from utils.requests_helper import api_request


def test_add_new_pet(base_api_url):
    global main_id

    endpoint = "pet"
    payload = add_new_pet()
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "POST", headers=headers, data=payload)

    print(response.text)
    assert response.status_code == 200
    assert response.json()['status'] == "available"
    validate(response.json(), add_pet)

    main_id = response.json()['id']


def test_update_pet(base_api_url):
    payload = {"id": main_id, "category": {"id": 0, "name": "string"}, "name": "cat", "photoUrls": ["string"],
               "tags": [{"id": 0, "name": "string"}], "status": "available"}
    endpoint = "pet"
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "POST", headers=headers, json=payload)
    assert response.status_code == 200
    print(response.text)
    print(payload)
