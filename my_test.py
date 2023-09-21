import pytest
from app import app
from pytest_timeout import timeout

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    # Test the '/' route (index route)
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Welcome to the Animal Catalog' in rv.data

def test_add_animal_route(client):
    # Test the '/add_animal' route
    rv = client.get('/add_animal')
    assert rv.status_code == 200
    assert b'Add a New Animal' in rv.data

def test_remove_animal_route(client):
    # Test the '/remove_animal' route
    rv = client.get('/remove_animal')
    assert rv.status_code == 200
    assert b'Remove an Animal' in rv.data

@timeout(10)  # Set the timeout to 10 seconds
def test_my_function():
    # Your test code here
    print("Starting the test")
    # Your test code here
    print("Test completed")


