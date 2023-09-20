import pytest
from app import app  # Replace 'your_app_module' with the actual module name where your Flask app is defined

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_syntax(client):
    # Send a GET request to the root URL
    response = client.get('/')
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # You can add more checks as needed for other routes and functionality
