from pkgutil import get_data
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

books = []

@book_blp.route('/')
class BookList(MethodView):
  @book_blp.response(200, BookSchema(many=True))
  def get(self):
    return books
  
  @book_blp.arguments(BookSchema)
  @book_blp.response(201, BookSchema)
  def post(self, new_book):
    new_book['id'] = len(books) + 1
    books.append(get_data)
    return get_data
  
@book_blp.route('/<int:book_id>')
class Book(MethodView):
  @book_blp.response(200, BookSchema)
  def get(self, book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
      abort(404, message="Book not found.")
    return book
  
  @book_blp.arguments(BookSchema)
  @book_blp.response(200, BookSchema)
  def put(self, new_data, book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
      abort(404, message="Book not found.")
    book.update(new_data)
    return book
  
  @book_blp.response(204)
  def delete(self, book_id):
    global books
    books = next ((book for book in books if book['id'] == book_id), None)
    if books is None:
      abort(404, message="Book not found.")
    books = [book for book in books if book['id'] != book_id]
    return ''