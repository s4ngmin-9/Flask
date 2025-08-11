from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from uuid import uuid4

from schemas import BookSchema

# 데이터 저장소 (메모리 내 리스트)
books = {}

blp = Blueprint(
    "Books", __name__, url_prefix="/books", description="Operations on books"
)

@blp.route("/")
class BookList(MethodView):
    @blp.response(200, BookSchema(many=True))
    def get(self):
        # 책 목록 조회
        return list(books.values())

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_book_data):
        # 새로운 책 추가
        book_id = uuid4().hex
        new_book = {**new_book_data, "id": book_id}
        books[book_id] = new_book
        return new_book

@blp.route("/<string:book_id>")
class Book(MethodView):
    @blp.response(200, BookSchema)
    def get(self, book_id):
        # 특정 책 정보를 조회
        try:
            return books[book_id]
        except KeyError:
            abort(404, message="Book not found.")

    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def put(self, book_data, book_id):
        # 특정 책 정보 업데이트
        try:
            book = books[book_id]
            book.update(book_data)
            return book
        except KeyError:
            abort(404, message="Book not found.")

    @blp.response(204)
    def delete(self, book_id):
        # 특정 책 삭제
        try:
            del books[book_id]
            return {"message": "Book deleted."}
        except KeyError:
            abort(404, message="Book not found.")