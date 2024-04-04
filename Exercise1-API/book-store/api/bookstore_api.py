import re
from datetime import datetime
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# In-memory database
books = []

def find_book(book_id):
    return next((book for book in books if book['book_id'] == book_id), None)


@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()

    required_fields = ['title', 'author', 'published_date', 'isbn', 'price']
    if not all(field in data for field in required_fields):
        return make_response(
            jsonify({'error': 'Missing required fields'}), 400)

    result = validate(data)
    if result is not None:
        return result

    new_book = {
        'book_id': str(len(books) + 1),
        'title': data['title'],
        'author': data['author'],
        'published_date': data['published_date'],
        'isbn': data['isbn'],
        'price': data['price']
    }

    books.append(new_book)
    return make_response(jsonify(new_book), 201)


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<string:book_id>', methods=['GET'])
def get_single_book(book_id):
    book = find_book(book_id)
    if book is None:
        return make_response(jsonify({'error': 'Book not found'}), 404)
    return jsonify(book)


@app.route('/books/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    book = find_book(book_id)
    if book is None:
        return make_response(jsonify({'error': 'Book not found'}), 404)

    data = request.get_json()

    result = validate(data)
    if result is not None:
        return result

    for field in ['title', 'author', 'published_date', 'isbn', 'price']:
        if field in data:
            book[field] = data[field]
    return jsonify(book)


@app.route('/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if book is None:
        return make_response(jsonify({'error': 'Book not found'}), 404)

    books.remove(book)
    return make_response(
        jsonify({'message': 'Book deleted successfully'}), 204)


def validate(data):

    if 'title' in data and len(data['title']) >= 256:
        return make_response(jsonify({'error': 'Title has to be maximum 255 characters'}), 400)

    if 'author' in data and len(data['author']) >= 256:
        return make_response(jsonify({'error': 'Author has to be maximum 255 characters'}), 400)

    if 'published_date' in data:
        try:
            datetime.strptime(data['published_date'], '%Y-%m-%d')
        except ValueError:
            return make_response(jsonify({'error': 'Invalid Publish Date'}), 400)

    if 'isbn' in data and not re.match(r'^\d{10}$|^\d{13}$', data['isbn']):
        return make_response(jsonify({'error': 'Invalid ISBN'}), 400)

    if 'price' in data:
        try:
            price = float(data['price'])
            if price <= 0:
                raise ValueError()
        except ValueError as e:
            return make_response(jsonify({'error': 'Invalid Price'}), 400)

if __name__ == '__main__':
    app.run(debug=True)
