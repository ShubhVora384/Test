
import pytest
from fastapi.testclient import TestClient
from main import app, client

def test_update_user():
    user_id = 1
    new_name = "John Doe"
    response = client.put(f"/users/{user_id}", json={"name": new_name})
    assert response.status_code == 200
    assert response.json()["name"] == new_name

def test_update_user_invalid_json():
    user_id = 1
    response = client.put(f"/users/{user_id}", json=None)
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "value is not a valid dict"

def test_update_user_not_found():
    user_id = 999
    response = client.put(f"/users/{user_id}", json={"name": "John Doe"})
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
