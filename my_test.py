import pytest
from app import app, db

@pytest.fixture(scope='module')
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def test_db():
    # Create a temporary test database
    db.create_all()

    yield db

    # Clean up the database after testing
    db.drop_all()

def test_index_route(test_client):
    # Your test code here
    pass

# Other test functions



