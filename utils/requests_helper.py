import requests


def api_request(base_api_url, endpoint, method, data=None, json=None, params=None, headers=None):
    url = f"{base_api_url}{endpoint}"
    response = requests.request(method, url, data=data, json=json, params=params, headers=headers)
    return response
