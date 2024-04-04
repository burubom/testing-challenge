import inspect
import json
import string
import sys
import os
import random
import pytest

from constants import *
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.bookstore_api import app, books

DATE_FILE_PATH = 'tests/books.json'

@pytest.fixture
def client():
    with app.test_client() as client:
        json_data = load_data(DATE_FILE_PATH)
        books.clear()
        for data in json_data:
            books.append(data)

        yield client

        client.delete()


@pytest.fixture(scope='session')
def test_data():
    return load_data(DATE_FILE_PATH)


@pytest.fixture(autouse=True, scope='session')
def setup_print():
    print("\n")


def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def generate_payload(title=True, author=True, published_date=True, isbn=True, price=True):
    payload = {}
    if title:
        payload[KEY_TITLE] = 'Title' + ''.join(random.choices(' 0123456789', k=5))
    if author:
        payload[KEY_AUTHOR] = (''.join(random.choices(string.ascii_letters, k=random.randint(3, 5)))
                               + ' ' + ''.join(random.choices(string.ascii_letters, k=random.randint(3, 5))))
    if published_date:
        today = datetime.now().date()
        rand_date = today - timedelta(days=random.randint(1, 36500))
        payload[KEY_PUBLISHED_DATE] = rand_date.strftime('%Y-%m-%d')
    if isbn:
        payload[KEY_ISBN] = ''.join(random.choices('0123456789', k=13))
    if price:
        payload[KEY_PRICE] = round(random.uniform(10, 500), 2)

    print(f'{inspect.stack()[1].function}:{payload}')

    return payload


def assert_org_data(response, org_data, title=True, author=True, published_date=True, isbn=True, price=True):
    assert response[KEY_BOOK_ID] == org_data[KEY_BOOK_ID]

    if title:
        assert response[KEY_TITLE] == org_data[KEY_TITLE]
    if author:
        assert response[KEY_AUTHOR] == org_data[KEY_AUTHOR]
    if published_date:
        assert response[KEY_PUBLISHED_DATE] == org_data[KEY_PUBLISHED_DATE]
    if isbn:
        assert response[KEY_ISBN] == org_data[KEY_ISBN]
    if price:
        assert response[KEY_PRICE] == org_data[KEY_PRICE]
