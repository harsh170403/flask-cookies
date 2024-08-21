import pytest
import threading
import time
from http.server import HTTPServer
from app import SimpleHTTPRequestHandler  
import requests 

SERVER_ADDRESS = ('localhost', 8000)

@pytest.fixture(scope='module')
def http_server():
    server = HTTPServer(SERVER_ADDRESS, SimpleHTTPRequestHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    time.sleep(1)  
    yield
    server.shutdown()
    thread.join()

def test_set_cookie(http_server):
    url = f'http://{SERVER_ADDRESS[0]}:{SERVER_ADDRESS[1]}/set_cookie'
    response = requests.get(url)
    assert response.status_code == 200
    assert 'Set-Cookie' in response.headers
    assert response.headers['Set-Cookie'] == 'my_cookie=cookie_value'

def test_get_cookie(http_server):
    
    url = f'http://{SERVER_ADDRESS[0]}:{SERVER_ADDRESS[1]}/set_cookie'
    response = requests.get(url)
    assert response.status_code == 200


    url = f'http://{SERVER_ADDRESS[0]}:{SERVER_ADDRESS[1]}/get_cookie'
    cookies = {'my_cookie': 'cookie_value'}
    response = requests.get(url, cookies=cookies)
    assert response.status_code == 200
    assert 'The value of the cookie is: cookie_value' in response.text

def test_no_cookie(http_server):
    url = f'http://{SERVER_ADDRESS[0]}:{SERVER_ADDRESS[1]}/get_cookie'
    response = requests.get(url)
    assert response.status_code == 200
    assert 'No cookie found' in response.text
