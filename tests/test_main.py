from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_greet():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "Hello from Irmak's Quiz Bot!"}
