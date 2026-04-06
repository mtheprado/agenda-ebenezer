from http import HTTPStatus

from fastapi.testclient import TestClient

from backend.app import app

client = TestClient(app)


def test_read_root_retorna_ola_mundo():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_read_home_retorna_ola_mundo():
    response = client.get('/home')
    assert response.status_code == HTTPStatus.OK
    assert '<p>Ola mundo!</p>' in response.text
