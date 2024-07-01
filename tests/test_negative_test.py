from tests.base import add_new_pet, main_headers
from utils.requests_helper import api_request
import allure
@allure.title("Add new pet")
def test_add_new_pet_negarive(base_api_url):
    global main_id

    endpoint = "pet"
    payload = add_new_pet()
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "GET", headers=headers, data=payload)
    with allure.step('Status code GET = 405'):
        assert response.status_code == 405
    response = api_request(base_api_url, endpoint, "DELETE", headers=headers, data=payload)
    with allure.step('Status code DELETE = 405'):
        assert response.status_code == 405
    response = api_request(base_api_url, endpoint, "PATCH", headers=headers, data=payload)
    with allure.step('Status code PATCH = 405'):
        assert response.status_code == 405
    response = api_request(base_api_url, endpoint, "POST", headers=headers, data=payload)
    main_id = response.json()['id']


@allure.title("Update pet data")
def test_update_pet(base_api_url):
    payload = {"id": main_id, "category": {"id": 0, "name": "string"}, "name": "cat", "photoUrls": ["string"],
               "tags": [{"id": 0, "name": "string"}], "status": "available"}
    endpoint = "pet"
    headers = main_headers()
    response = api_request(base_api_url, endpoint, "GET", headers=headers, json=payload)
    with allure.step('Status code GET = 405'):
        assert response.status_code == 405
    response = api_request(base_api_url, endpoint, "PATCH", headers=headers, json=payload)
    with allure.step('Status code PATCH = 405'):
        assert response.status_code == 405
    response = api_request(base_api_url, endpoint, "DELETE", headers=headers, json=payload)
    with allure.step('Status code DELETE = 405'):
        assert response.status_code == 405
    response = api_request(base_api_url, endpoint, "PUT")
    with allure.step('Status code Without a body = 415'):
        assert response.status_code == 415
