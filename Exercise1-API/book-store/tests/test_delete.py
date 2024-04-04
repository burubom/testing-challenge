import random

from constants import *


def test_status_code_204(client):
    id = str(random.randint(1, 10))
    response = client.delete('/books/' + id)

    assert response.status_code == 204


def test_header_204(client):
    id = str(random.randint(1, 10))
    response = client.delete('/books/' + id)

    assert CONTENT_TYPE_HEADER in response.headers
    assert response.headers[CONTENT_TYPE_HEADER] == JSON_MEDIA_TYPE


def test_payload_204(client):
    id = str(random.randint(1, 10))
    response = client.delete('/books/' + id)

    assert response.text == ''


def test_not_found(client):
    response = client.delete('/books/' + 'invalid_id')

    assert response.status_code == 404
    assert response.headers[CONTENT_TYPE_HEADER] == JSON_MEDIA_TYPE
    assert response.json['error'] == 'Book not found'
