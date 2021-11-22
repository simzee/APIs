from flask_restplus import Resource, reqparse

from app.main.util.book_dto import Book
from app.main.services.book_search_service import check_if_book_is_present, get_list_of_available_books,\
	get_list_of_books_not_available, member_with_book_not_avialable_in_library,\
	change_status_of_book

api = Book.name_space2

par = reqparse.RequestParser()
par.add_argument('bname', type=str)

pars = reqparse.RequestParser()
pars.add_argument('bid', type=int)

pa = reqparse.RequestParser()
pa.add_argument('bid', type=int)
pa.add_argument('status', type=str)

@api.route('/book', methods=['GET', 'POST', 'PUT', 'DELETE'])
class book_search(Resource):
	@api.expect(par)
	def get(self):
		"""To find that the book of the members choice is present in the library or not -by Pawan"""
		return check_if_book_is_present(par.parse_args())

@api.route('/book_avialable', methods=['GET'])
class books(Resource):
	def get(self):
		"""To get the list of books available in the library -by Pawan"""
		return get_list_of_available_books()

@api.route('/books_not_avialable', methods=['GET'])
class book_na(Resource):
	def get(self):
		"""To get the list of books not available in the library -by Pawan"""
		return get_list_of_books_not_available()

@api.route('/books_with_others', methods=['GET'])
class books_with(Resource):
	@api.expect(pars)
	def get(self):
		"""To find the member who has the book that is not available in the library -by Pawan"""
		return member_with_book_not_avialable_in_library(pars.parse_args())

@api.route('/change_status', methods=['put'])
class check(Resource):
	@api.expect(pa, validate=True)
	def put(self):
		"""To change the status of the book so the no one else put a request for the same book -by Pawan"""
		return change_status_of_book(pa.parse_args())

