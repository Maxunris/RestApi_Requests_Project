import requests

def api_request(base_api_url, endpoint, method, data=None, params=None, headers=None):
    url = f"{base_api_url}{endpoint}"
    response = requests.request(method, url, data=data, params=params, headers=headers)
    return response
