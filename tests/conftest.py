import pytest


@pytest.fixture(scope="session", autouse=True)
def base_api_url():
    return 'https://petstore.swagger.io/v2/'