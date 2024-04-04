import random

from conftest import generate_payload, assert_org_data
from constants import *


def test_status_code_200(client, test_data):
    id = str(random.randint(1, 10))
    response = client.get('/books/' + id)

    assert response.status_code == 200


def test_header_200(client, test_data):
    id = str(random.randint(1, 10))
    response = client.get('/books/' + id)

    assert CONTENT_TYPE_HEADER in response.headers
    assert response.headers[CONTENT_TYPE_HEADER] == JSON_MEDIA_TYPE


def test_payload_200(client, test_data):
    id = str(random.randint(1, 10))
    response = client.get('/books/' + id)

    assert_org_data(response.json, test_data[int(id) - 1])


def test_not_found(client):
    response = client.get('/books/' + 'invalid_id')

    assert response.status_code == 404
    assert response.headers[CONTENT_TYPE_HEADER] == JSON_MEDIA_TYPE
    assert response.json['error'] == 'Book not found'
