from conftest import generate_payload
from constants import *


def test_status_code_201(client):
    payload = generate_payload()

    response = client.post('/books', json=payload)
    assert response.status_code == 201


def test_header_201(client):
    payload = generate_payload()
    response = client.post('/books', json=payload)

    assert CONTENT_TYPE_HEADER in response.headers
    assert response.headers[CONTENT_TYPE_HEADER] == JSON_MEDIA_TYPE


def test_payload_201(client):
    payload = generate_payload()
    response = client.post('/books', json=payload)

    assert response.json[KEY_BOOK_ID] == '11'
    assert response.json[KEY_TITLE] == payload[KEY_TITLE]
    assert response.json[KEY_AUTHOR] == payload[KEY_AUTHOR]
    assert response.json[KEY_PUBLISHED_DATE] == payload[KEY_PUBLISHED_DATE]
    assert response.json[KEY_ISBN] == payload[KEY_ISBN]
    assert response.json[KEY_PRICE] == payload[KEY_PRICE]


def test_missing_title_400(client):
    payload = generate_payload(title=False)
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Missing required fields'


def test_boundary_title_201(client):
    payload = generate_payload()
    payload[KEY_TITLE] = '9XCeicOpZ5asgNzktYP6aAQ4ooaVvPNGbJL8MVTuyc903wMB077JJzuUHptKC2XFHMqudtxLjF8QBdrA3YL7tB5oks2rCxCJCtL1JHueAOSxpW7PGLFhRyNXsYMyY6R7XH0aGOhIPPyalpIVec0sIYgemcyX7n0lq5iGV9Ym6lyeFyqC5GrDOChpnlpqdAkvt7XWcIzANpUW0BcWK9mePuhTeSTIniJPjmXGHboKXCtI8SKNUGCTy1qir5xerxr'
    response = client.post('/books', json=payload)

    assert response.status_code == 201
    assert response.json[KEY_TITLE] == payload[KEY_TITLE]


def test_boundary_title_400(client):
    payload = generate_payload()
    payload[KEY_TITLE] = '19XCeicOpZ5asgNzktYP6aAQ4ooaVvPNGbJL8MVTuyc903wMB077JJzuUHptKC2XFHMqudtxLjF8QBdrA3YL7tB5oks2rCxCJCtL1JHueAOSxpW7PGLFhRyNXsYMyY6R7XH0aGOhIPPyalpIVec0sIYgemcyX7n0lq5iGV9Ym6lyeFyqC5GrDOChpnlpqdAkvt7XWcIzANpUW0BcWK9mePuhTeSTIniJPjmXGHboKXCtI8SKNUGCTy1qir5xerxr'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Title has to be maximum 255 characters'


def test_long_title_400(client):
    payload = generate_payload()
    payload[KEY_TITLE] = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ullamcorper nibh ut dapibus accumsan. Vestibulum fermentum mauris a magna hendrerit, sed vestibulum magna vestibulum. Cras ac fermentum nisi. Vivamus congue est nec lectus ultricies, vitae tincidunt nisi lobortis. Nullam sed fermentum nisi. Fusce semper nulla eu mauris fermentum, ac sollicitudin velit consectetur. Integer vel eros quis velit tempus vehicula. Pellentesque eget purus quis arcu suscipit interdum. Proin in velit quis quam interdum placerat nec vitae libero. Ut viverra orci at eros interdum ultricies. Curabitur dignissim dapibus purus. Integer sed malesuada orci.'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Title has to be maximum 255 characters'


def test_missing_author(client):
    payload = generate_payload(author=False)
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Missing required fields'


def test_boundary_author_201(client):
    payload = generate_payload()
    payload[KEY_AUTHOR] = '9XCeicOpZ5asgNzktYP6aAQ4ooaVvPNGbJL8MVTuyc903wMB077JJzuUHptKC2XFHMqudtxLjF8QBdrA3YL7tB5oks2rCxCJCtL1JHueAOSxpW7PGLFhRyNXsYMyY6R7XH0aGOhIPPyalpIVec0sIYgemcyX7n0lq5iGV9Ym6lyeFyqC5GrDOChpnlpqdAkvt7XWcIzANpUW0BcWK9mePuhTeSTIniJPjmXGHboKXCtI8SKNUGCTy1qir5xerxr'
    response = client.post('/books', json=payload)

    assert response.status_code == 201
    assert response.json[KEY_AUTHOR] == payload[KEY_AUTHOR]


def test_boundary_author_400(client):
    payload = generate_payload()
    payload[KEY_AUTHOR] = '19XCeicOpZ5asgNzktYP6aAQ4ooaVvPNGbJL8MVTuyc903wMB077JJzuUHptKC2XFHMqudtxLjF8QBdrA3YL7tB5oks2rCxCJCtL1JHueAOSxpW7PGLFhRyNXsYMyY6R7XH0aGOhIPPyalpIVec0sIYgemcyX7n0lq5iGV9Ym6lyeFyqC5GrDOChpnlpqdAkvt7XWcIzANpUW0BcWK9mePuhTeSTIniJPjmXGHboKXCtI8SKNUGCTy1qir5xerxr'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Author has to be maximum 255 characters'


def test_long_author(client):
    payload = generate_payload()
    payload[KEY_AUTHOR] = 'Nullam malesuada luctus dolor, vitae mattis tellus eleifend in. Nulla vitae odio vel turpis scelerisque tempus nec in leo. Phasellus nec lorem lobortis, lacinia velit vel, cursus ex. Sed nec enim quis justo vehicula vulputate. Sed nec quam nec mi suscipit pellentesque ut id leo. Donec fringilla neque vitae magna fringilla, nec convallis nunc malesuada. Nullam nec lorem eu felis aliquet ullamcorper a sed arcu. Vivamus nec lectus aliquam, volutpat lacus eu, tempor elit.'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Author has to be maximum 255 characters'


def test_missing_published_date(client):
    payload = generate_payload(published_date=False)
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Missing required fields'


def test_invalid_format_published_date(client):
    payload = generate_payload()
    payload[KEY_PUBLISHED_DATE] = '12-13-2020'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid Publish Date'


def test_invalid_published_date(client):
    payload = generate_payload()
    payload[KEY_PUBLISHED_DATE] = '2020-13-13'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid Publish Date'


def test_missing_isbn(client):
    payload = generate_payload(isbn=False)
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Missing required fields'


def test_invalid_string_isbn(client):
    payload = generate_payload()
    payload[KEY_ISBN] = '97861609-20'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid ISBN'


def test_invalid_shorter_isbn(client):
    payload = generate_payload()
    payload[KEY_ISBN] = '978610'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid ISBN'


def test_invalid_longer_isbn(client):
    payload = generate_payload()
    payload[KEY_ISBN] = '97861609789461'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid ISBN'


def test_missing_price(client):
    payload = generate_payload(price=False)
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Missing required fields'


def test_invalid_string_price(client):
    payload = generate_payload()
    payload[KEY_PRICE] = 'eleven'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid Price'


def test_invalid_negative_price(client):
    payload = generate_payload()
    payload[KEY_PRICE] = '-1'
    response = client.post('/books', json=payload)

    assert response.status_code == 400
    assert response.json['error'] == 'Invalid Price'
