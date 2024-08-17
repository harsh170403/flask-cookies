import pytest
from app import app  # Replace 'your_flask_app_filename' with the actual name of your app file.

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_set_cookie(client):
    # Send a GET request to the /set_cookie route
    response = client.get('/set_cookie')
    
    # Check if the response has the cookie set
    assert 'my_cookie' in response.headers['Set-Cookie']
    assert response.status_code == 200
    assert b'Cookie is set!' in response.data

def test_get_cookie(client):
    # First, set the cookie by visiting the /set_cookie route
    client.get('/set_cookie')
    
    # Now, get the cookie value by visiting the /get_cookie route
    response = client.get('/get_cookie')
    
    # Check if the correct value is returned
    assert b'The value of the cookie is: cookie_value' in response.data
    assert response.status_code == 200
