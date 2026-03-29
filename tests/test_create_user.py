
import pytest
from fastapi.testclient import TestClient
from main import app, client

def test_create_user():
    response = client.post("/users", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

def test_create_user_missing_fields():
    response = client.post("/users", json={})
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "name"]
    assert response.json()["detail"][0]["msg"] == "field required"

def test_create_user_invalid_data():
    response = client.post("/users", json={"name": "John Doe", "email": "invalid_email"})
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "email"]
    assert response.json()["detail"][0]["msg"] == "email does not match format"
