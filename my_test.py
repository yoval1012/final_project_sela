import pytest
from app import app
import pymongo


# Initialize the Flask app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def test_db():
    client = MongoClient('mongodb://root:3yGWpZ7jeS@34.78.116.136:27017/')
    db = client['test_animals_db']
    yield db
    client.close()

# Test adding a new animal
def test_add_animal(client, test_db):
    # Define the data for the new animal
    new_animal_data = {
        'new_animal': 'Giraffe',
        'new_description': 'A tall African mammal with a long neck.',
        'new_url': 'https://en.wikipedia.org/wiki/Giraffe'
    }

    # Send a POST request to the /add_animal route with the new animal data
    response = client.post('/add_animal', data=new_animal_data, follow_redirects=True)

    # Check if the response status code is 200 (OK) after adding the animal
    assert response.status_code == 200

    # Check if the new animal exists in the test MongoDB database
    added_animal = test_db.animals.find_one({'name': 'Giraffe'})
    assert added_animal is not None
    assert added_animal['name'] == 'Giraffe'
    assert added_animal['description'] == 'A tall African mammal with a long neck.'
    assert added_animal['url'] == 'https://en.wikipedia.org/wiki/Giraffe'
