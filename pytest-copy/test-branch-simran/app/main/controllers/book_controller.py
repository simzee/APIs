from flask_restplus import Resource, reqparse
from app.main.util.book_dto import Book
from app.main.services.book_services import get_all_book_details, add_book, delete_book,\
	update_existing_book_details, find_book_by_author

api = Book.api
api2 = Book.name_space2

bparser = reqparse.RequestParser()
bparser.add_argument('bid', type=int)
bparser.add_argument('bname', type=str)
bparser.add_argument('author', type=str)
bparser.add_argument('status', type=str)

bparser1 = reqparse.RequestParser()
bparser1.add_argument('bid', type=str)
bparser1.add_argument('bname', type=str)

bparser2 = reqparse.RequestParser()
bparser2.add_argument('bid', type=int)
bparser2.add_argument('bname', type=str)
bparser2.add_argument('status', type=str)

bparser3 = reqparse.RequestParser()
bparser3.add_argument('author', type=str)


@api.route('/admin/book', methods=['GET', 'POST', 'DELETE', 'PUT'])
class AllBooks(Resource):
	# function to get all the available books in the library
	def get(self):
		"""Book Details - By Simran"""
		return get_all_book_details()

	# function to add new books
	@api.expect(bparser, validate=True)
	def post(self):
		"""Add a new book - By Simran"""
		return add_book(bparser.parse_args())

	@api.expect(bparser1)
	def delete(self):
		"""Delete an existing book - By Simran"""
		return delete_book(bparser.parse_args())

	@api.expect(bparser2, validate=True)
	def put(self):
		"""Update details of an existing book - By Simran"""
		return update_existing_book_details(bparser2.parse_args())


@api2.route('/admin/book-author', methods=['GET'])
class BookAuthor(Resource):
	# function to get book by name
	@api.expect(bparser3)
	def get(self):
		"""Find the book by the respective book author - By Simran"""
		return find_book_by_author(bparser3.parse_args())
