import pytest
import json
from app import app

@pytest.fixture(scope="function")
def client():
    app.config.update({"TESTING": True})
    return app.test_client()

def test_create_client(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "first_name": "Edgar",
        "middle_name": "Mauricio",
        "last_name": "Ceron",
        "email": "maurinin@yahoo.com",
        "zipcode": ""
    }

    url = '/create_user'

    response = client.post(url, data=json.dumps(data), headers=headers)
    print(response)
    assert response.content_type == mimetype
    assert response.json['first_name'] == "Edgar"

def test_add_localization_data(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "first_name": "Edgar",
        "middle_name": "Mauricio",
        "last_name": "Ceron",
        "email": "maurinin@yahoo.com",
        "zipcode": "42733"
    }

    url = '/create_user'

    response = client.post(url, data=json.dumps(data), headers=headers)
    print(response)
    assert response.content_type == mimetype
    assert response.json['country'] == "Taylor"
    assert response.json['city'] == "Elk Horn"

