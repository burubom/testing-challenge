import random

from conftest import generate_payload, assert_org_data
from constants import *


def test_update_all_200(client):
    id = get_random_id()
    payload = generate_payload()

    response = client.put('/books/' + id, json=payload)
    assert response.status_code == 200
    assert CONTENT_TYPE_HEADER in response.headers
    assert response.headers[CONTENT_TYPE_HEADER] == JSON_MEDIA_TYPE
    assert response.json[KEY_BOOK_ID] == id
    assert response.json[KEY_TITLE] == payload[KEY_TITLE]
    assert response.json[KEY_AUTHOR] == payload[KEY_AUTHOR]
    assert response.json[KEY_PUBLISHED_DATE] == payload[KEY_PUBLISHED_DATE]
    assert response.json[KEY_ISBN] == payload[KEY_ISBN]
    assert response.json[KEY_PRICE] == payload[KEY_PRICE]




def test_status_code_200(client):
    id = get_random_id()
    payload = generate_payload()
    response = client.put('/books/' + id, json=payload)

    assert response.status_code == 200


def test_header_200(client):
    id = get_random_id()
    payload = generate_payload()
    response = client.put('/books/' + id, json=payload)

    assert CONTENT_TYPE_HEADER in response.headers
    assert response.headers[CONTENT_TYPE_HEADER] == JSON_MEDIA_TYPE


def test_payload_200(client):
    id = get_random_id()
    payload = generate_payload()
    response = client.put('/books/' + id, json=payload)

    assert response.json[KEY_BOOK_ID] == id
    assert response.json[KEY_TITLE] == payload[KEY_TITLE]
    assert response.json[KEY_AUTHOR] == payload[KEY_AUTHOR]
    assert response.json[KEY_PUBLISHED_DATE] == payload[KEY_PUBLISHED_DATE]
    assert response.json[KEY_ISBN] == payload[KEY_ISBN]
    assert response.json[KEY_PRICE] == payload[KEY_PRICE]


def test_boundary_title_200(client):
    payload = {KEY_TITLE: '9XCeicOpZ5asgNzktYP6aAQ4ooaVvPNGbJL8MVTuyc903wMB077JJzuUHptKC2XFHMqudtxLjF8QBdrA3YL7tB5oks2rCxCJCtL1JHueAOSxpW7PGLFhRyNXsYMyY6R7XH0aGOhIPPyalpIVec0sIYgemcyX7n0lq5iGV9Ym6lyeFyqC5GrDOChpnlpqdAkvt7XWcIzANpUW0BcWK9mePuhTeSTIniJPjmXGHboKXCtI8SKNUGCTy1qir5xerxr'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 200
    assert response.json[KEY_TITLE] == payload[KEY_TITLE]


def test_boundary_title_400(client):
    payload = generate_payload()
    payload[KEY_TITLE] = '19XCeicOpZ5asgNzktYP6aAQ4ooaVvPNGbJL8MVTuyc903wMB077JJzuUHptKC2XFHMqudtxLjF8QBdrA3YL7tB5oks2rCxCJCtL1JHueAOSxpW7PGLFhRyNXsYMyY6R7XH0aGOhIPPyalpIVec0sIYgemcyX7n0lq5iGV9Ym6lyeFyqC5GrDOChpnlpqdAkvt7XWcIzANpUW0BcWK9mePuhTeSTIniJPjmXGHboKXCtI8SKNUGCTy1qir5xerxr'
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Title has to be maximum 255 characters'


def test_long_title_400(client):
    payload = {KEY_TITLE: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ullamcorper nibh ut dapibus accumsan. Vestibulum fermentum mauris a magna hendrerit, sed vestibulum magna vestibulum. Cras ac fermentum nisi. Vivamus congue est nec lectus ultricies, vitae tincidunt nisi lobortis. Nullam sed fermentum nisi. Fusce semper nulla eu mauris fermentum, ac sollicitudin velit consectetur. Integer vel eros quis velit tempus vehicula. Pellentesque eget purus quis arcu suscipit interdum. Proin in velit quis quam interdum placerat nec vitae libero. Ut viverra orci at eros interdum ultricies. Curabitur dignissim dapibus purus. Integer sed malesuada orci.'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Title has to be maximum 255 characters'


def test_boundary_author_200(client):
    payload = {KEY_AUTHOR: '9XCeicOpZ5asgNzktYP6aAQ4ooaVvPNGbJL8MVTuyc903wMB077JJzuUHptKC2XFHMqudtxLjF8QBdrA3YL7tB5oks2rCxCJCtL1JHueAOSxpW7PGLFhRyNXsYMyY6R7XH0aGOhIPPyalpIVec0sIYgemcyX7n0lq5iGV9Ym6lyeFyqC5GrDOChpnlpqdAkvt7XWcIzANpUW0BcWK9mePuhTeSTIniJPjmXGHboKXCtI8SKNUGCTy1qir5xerxr'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 200
    assert response.json[KEY_AUTHOR] == payload[KEY_AUTHOR]


def test_boundary_author_400(client):
    payload = {KEY_AUTHOR: '19XCeicOpZ5asgNzktYP6aAQ4ooaVvPNGbJL8MVTuyc903wMB077JJzuUHptKC2XFHMqudtxLjF8QBdrA3YL7tB5oks2rCxCJCtL1JHueAOSxpW7PGLFhRyNXsYMyY6R7XH0aGOhIPPyalpIVec0sIYgemcyX7n0lq5iGV9Ym6lyeFyqC5GrDOChpnlpqdAkvt7XWcIzANpUW0BcWK9mePuhTeSTIniJPjmXGHboKXCtI8SKNUGCTy1qir5xerxr'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Author has to be maximum 255 characters'


def test_long_author_400(client):
    payload = {KEY_AUTHOR: 'Nullam malesuada luctus dolor, vitae mattis tellus eleifend in. Nulla vitae odio vel turpis scelerisque tempus nec in leo. Phasellus nec lorem lobortis, lacinia velit vel, cursus ex. Sed nec enim quis justo vehicula vulputate. Sed nec quam nec mi suscipit pellentesque ut id leo. Donec fringilla neque vitae magna fringilla, nec convallis nunc malesuada. Nullam nec lorem eu felis aliquet ullamcorper a sed arcu. Vivamus nec lectus aliquam, volutpat lacus eu, tempor elit.'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Author has to be maximum 255 characters'


def test_invalid_format_published_date_400(client):
    payload = {KEY_PUBLISHED_DATE: '12-13-2020'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid Publish Date'


def test_invalid_published_date_400(client):
    payload = {KEY_PUBLISHED_DATE: '2020-13-13'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid Publish Date'


def test_invalid_string_isbn_400(client):
    payload = {KEY_ISBN: '7861609-20'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid ISBN'


def test_invalid_shorter_isbn_400(client):
    payload = {KEY_ISBN: '978610'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid ISBN'


def test_invalid_longer_isbn_400(client):
    payload = {KEY_ISBN: '97861609789461'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid ISBN'


def test_invalid_string_price_400(client):
    payload = {KEY_PRICE: 'eleven'}
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid Price'


def test_invalid_negative_price_400(client):
    payload = generate_payload()
    payload[KEY_PRICE] = '-1'
    response = client.put('/books/' + get_random_id(), json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid Price'


def test_update_title_200(client, test_data):
    id = get_random_id()
    payload = generate_payload(author=False, published_date=False, isbn=False, price=False)
    response = client.put('/books/' + id, json=payload)

    assert response.status_code == 200
    assert response.json[KEY_TITLE] == payload[KEY_TITLE]
    assert_org_data(response.json, test_data[int(id) - 1], title=False)


def test_update_author_200(client, test_data):
    id = get_random_id()
    payload = generate_payload(title=False, published_date=False, isbn=False, price=False)
    response = client.put('/books/' + id, json=payload)

    assert response.status_code == 200
    assert response.json[KEY_AUTHOR] == payload[KEY_AUTHOR]
    assert_org_data(response.json, test_data[int(id) - 1], author=False)


def test_update_published_date_200(client, test_data):
    id = get_random_id()
    payload = generate_payload(title=False, author=False, isbn=False, price=False)
    response = client.put('/books/' + id, json=payload)

    assert response.status_code == 200
    assert response.json[KEY_PUBLISHED_DATE] == payload[KEY_PUBLISHED_DATE]
    assert_org_data(response.json, test_data[int(id) - 1], published_date=False)


def test_update_isbn_200(client, test_data):
    id = get_random_id()
    payload = generate_payload(title=False, author=False, published_date=False, price=False)
    response = client.put('/books/' + id, json=payload)

    assert response.status_code == 200
    assert response.json[KEY_ISBN] == payload[KEY_ISBN]
    assert_org_data(response.json, test_data[int(id) - 1], isbn=False)


def test_update_price_200(client, test_data):
    id = get_random_id()
    payload = generate_payload(title=False, author=False, published_date=False, isbn=False)
    response = client.put('/books/' + id, json=payload)

    assert response.status_code == 200
    assert response.json[KEY_PRICE] == payload[KEY_PRICE]
    assert_org_data(response.json, test_data[int(id) - 1], price=False)


def test_empty_body_415(client):
    response = client.put("/books/1")
    assert response.status_code == 415


def get_random_id():
    return str(random.randint(1, 10))
