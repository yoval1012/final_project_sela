import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    # Test the index route
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Flask App' in response.data

def test_add_animal(client):
    # Test the add_animal route
    response = client.post('/add_animal', data={'new_animal': 'Lion', 'new_description': 'A powerful predator', 'new_url': 'https://en.wikipedia.org/wiki/Lion'})
    assert response.status_code == 200

    # Verify that the animal was added (you may need to query your MongoDB or database)
    # Example assertion: assert Animal.query.filter_by(name='Lion').first() is not None

def test_remove_animal(client):
    # Test the remove_animal route
    response = client.post('/remove_animal', data={'animal': 'Cat'})
    assert response.status_code == 200

    # Verify that the animal was removed (you may need to query your MongoDB or database)
    # Example assertion: assert Animal.query.filter_by(name='Cat').first() is None

# You can add more test methods for other routes and functions in your app

