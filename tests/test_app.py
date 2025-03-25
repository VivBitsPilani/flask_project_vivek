from app import app
import pytest

# Test client fixture
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Basic route test
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

# Sample test for demonstration
def test_sample_math():
    assert 1 + 1 == 2
