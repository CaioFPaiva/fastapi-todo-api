from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_read_task():
    r = client.post("/tasks/", json={"title": "Study Python"})
    assert r.status_code == 201
    created = r.json()
    assert created["title"] == "Study Python"
    r = client.get("/tasks/")
    assert r.status_code == 200
    items = r.json()
    assert any(t["title"] == "Study Python" for t in items)
