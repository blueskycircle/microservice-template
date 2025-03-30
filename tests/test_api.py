import pytest
from fastapi.testclient import TestClient
from api import app

# pylint: disable=redefined-outer-name
# This disables the redefined-outer-name warning specifically for pytest fixtures

@pytest.fixture
def client():
    """Fixture providing a FastAPI test client."""
    return TestClient(app)


def test_api_exists(client):
    """Test that the API exists and can be invoked."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Welcome to the Math Operations API" in response.json()["message"]


def test_addition_post(client):
    """Test the addition endpoint with POST method."""
    # Test with positive integers
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "addition"
    assert data["a"] == 2
    assert data["b"] == 3
    assert data["result"] == 5

    # Test with negative numbers
    response = client.post("/add", json={"a": -1, "b": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0

    # Test with decimals
    response = client.post("/add", json={"a": 2.5, "b": 3.5})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 6.0


def test_addition_post_precision(client):
    """Test the addition endpoint with floating point precision edge cases."""
    # Test case that would normally have floating point precision issues
    response = client.post("/add", json={"a": -1, "b": 2.3})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 1.3
    
    # Test more precision edge cases
    response = client.post("/add", json={"a": 0.1, "b": 0.2})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0.3
    
    response = client.post("/add", json={"a": 0.1, "b": 0.7})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0.8


def test_subtraction_post(client):
    """Test the subtraction endpoint with POST method."""
    # Test with positive integers
    response = client.post("/subtract", json={"a": 5, "b": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "subtraction"
    assert data["a"] == 5
    assert data["b"] == 3
    assert data["result"] == 2

    # Test with numbers that yield zero
    response = client.post("/subtract", json={"a": 1, "b": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0

    # Test with decimals
    response = client.post("/subtract", json={"a": 10.5, "b": 4.5})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 6.0

    # Test with negative result
    response = client.post("/subtract", json={"a": 3, "b": 7})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == -4


def test_subtraction_post_precision(client):
    """Test the subtraction endpoint with floating point precision edge cases."""
    # Test case that would normally have floating point precision issues
    response = client.post("/subtract", json={"a": 1.3, "b": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0.3
    
    # Test more precision edge cases
    response = client.post("/subtract", json={"a": 0.3, "b": 0.1})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0.2
    
    response = client.post("/subtract", json={"a": 1, "b": 0.7})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0.3


def test_addition_get(client):
    """Test the addition endpoint with GET method."""
    # Test with positive integers
    response = client.get("/add/2/3")
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "addition"
    assert data["a"] == 2
    assert data["b"] == 3
    assert data["result"] == 5

    # Test with negative numbers
    response = client.get("/add/-1/1")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0

    # Test with decimals
    response = client.get("/add/2.5/3.5")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 6.0


def test_addition_get_precision(client):
    """Test the addition GET endpoint with floating point precision edge cases."""
    response = client.get("/add/-1/2.3")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 1.3
    
    response = client.get("/add/0.1/0.2")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0.3


def test_subtraction_get(client):
    """Test the subtraction endpoint with GET method."""
    # Test with positive integers
    response = client.get("/subtract/5/3")
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "subtraction"
    assert data["a"] == 5
    assert data["b"] == 3
    assert data["result"] == 2

    # Test with negative result
    response = client.get("/subtract/3/7")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == -4


def test_subtraction_get_precision(client):
    """Test the subtraction GET endpoint with floating point precision edge cases."""
    response = client.get("/subtract/1.3/1")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0.3
    
    response = client.get("/subtract/1/0.7")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 0.3


def test_invalid_inputs(client):
    """Test error handling for invalid inputs."""
    # Test with non-numeric input for addition
    response = client.get("/add/abc/3")
    assert response.status_code == 422  # FastAPI validation error code

    # Test with missing field in POST request
    response = client.post("/add", json={"a": 5})
    assert response.status_code == 422

    # Test with invalid JSON in POST request
    response = client.post(
        "/add", headers={"Content-Type": "application/json"}, content="invalid json"
    )
    assert response.status_code == 422
