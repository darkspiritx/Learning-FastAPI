
from fastapi.testclient import TestClient
from day6 import app

client = TestClient(app)


def test_get_students():
    response = client.get("/students")

    assert response.status_code == 200
    assert "students" in response.json()
