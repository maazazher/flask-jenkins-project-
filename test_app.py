import pytest
from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b"Hello, Jenkins!"

def test_add():
    client = app.test_client()
    response = client.get('/add/2/3')
    assert response.data == b"5"

def test_add_negative():
    client = app.test_client()
    response = client.get('/add/-1/1')
    assert response.data == b"0"
