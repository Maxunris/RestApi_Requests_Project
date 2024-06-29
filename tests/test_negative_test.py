from tests.base import add_new_pet, main_headers
from schemas.pet_schema import pet_schema
from jsonschema import validate
from utils.requests_helper import api_request
import pytest

def test_add_new_pet(base_api_url):
    global main_id
