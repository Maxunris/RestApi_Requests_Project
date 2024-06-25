import json
def add_new_pet():
    payload = json.dumps({
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

    headers = {
        'Content-Type': 'application/json'
    }
    return payload