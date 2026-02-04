
import pytest
from fastapi.testclient import TestClient
from main import app, client

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []
