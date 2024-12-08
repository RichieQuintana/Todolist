import pytest
from app import create_app
from app.database import db
from app.models import Task

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    with app.test_client() as client:
        yield client

def test_create_task(client):
    response = client.post('/tasks', json={"title": "Test Task", "description": "A test task"})
    assert response.status_code == 201

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
