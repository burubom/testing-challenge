from conftest import assert_org_data
from constants import *


def test_http_status_200(client, test_data):
    response = client.get('/books')

    assert response.status_code == 200


def test_header_200(client, test_data):
    response = client.get('/books')

    assert CONTENT_TYPE_HEADER in response.headers
    assert response.headers[CONTENT_TYPE_HEADER] == JSON_MEDIA_TYPE


def test_payload_200(client, test_data):
    response = client.get('/books')

    assert len(response.json) == 10

    idx = 0
    for data in test_data:
        assert_org_data(response.json[idx], test_data[idx])
        idx += 1
