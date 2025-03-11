from fastapi.testclient import TestClient

from .main import app
from .main import get_db
from .main import TodoItem

client = TestClient(app)

list = [
        TodoItem(id=1,title="Foo1", description="There goes my hero"),
        TodoItem(id=2,title="Foo2", description="Watch him as he goes"),
        TodoItem(id=3,title="Foo3", description="He's ordinary"),
    ]

def mock_db():
    global list
    return list

# Dependency magic: override get_db with mock_db for testing
app.dependency_overrides[get_db] = mock_db

def test_read_list():
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_read_item():
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Foo1"
    assert response.json()["description"] == "There goes my hero"

def test_read_item_not_found():
    response = client.get("/todos/4")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_add_item():
    response = client.get("/todos")
    pre_add = len(response.json())
    response = client.post("/todos", json={"id": 4, "title": "foo4", "description": "Kudos my hero"})
    assert response.status_code == 200
    assert response.json()["id"] == 4
    assert response.json()["title"] == "foo4"
    assert response.json()["description"] == "Kudos my hero"
    response = client.get("/todos")
    assert len(response.json()) == pre_add + 1

def test_delete_item():
    response = client.get("/todos")
    pre_delete = len(response.json())
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}
    response = client.get("/todos/1")
    assert response.status_code == 404
    response = client.get("/todos")
    assert len(response.json()) == pre_delete - 1

def test_search_item():
    response = client.get("/search?keyword=foo")
    assert response.status_code == 200
    assert len(response.json()) == 3
    response = client.get("/search?keyword=foo2")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Foo2"
    response = client.get("/search?keyword=ordinary")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Foo3"