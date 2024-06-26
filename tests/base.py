import json
def main_headers():
    return {
        'Content-Type': 'application/json'
    }

def add_new_pet():
    return json.dumps({
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    })