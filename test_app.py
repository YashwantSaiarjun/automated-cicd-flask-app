from app import add_numbers, app


def test_add_numbers():
    """Test our simple business logic function."""
    assert add_numbers(2, 3) == 99
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_health_endpoint():
    """Test that the health check returns 200 and correct status."""
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_home_endpoint():
    """Test that the home route returns 200."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200