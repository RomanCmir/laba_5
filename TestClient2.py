from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["username"] == "string"

def test_create_user():
        response = client.post(
"/register/",
json={"username": "test_user", "email": "testuser@example.com",
"full_name": "Test User", "password": "qwerty12345"},
)
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "test_user"
        assert data["email"] == "testuser@example.com"