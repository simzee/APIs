# services/book_service.py
# date created : 28-10-2021
# by : Simran Beig

from db_models.book_db import bookModel
from flask_restplus import Resource
from config.instance import *
from namespaces.book_ns import nbook, bparser, bparser2, bparser1, bparser3, name_space2


@nbook.route('/admin/book', methods=['GET', 'POST', 'DELETE', 'PUT'])
class AllBooks(Resource):
	# function to get all the available books in the library
	def get(self):
		"""Book Details - By Simran"""
		try:
			get_all_books = bookModel.query.order_by(bookModel.bid.asc())
			books = [
				{
					'bid': book.bid,
					'bname': book.bname,
					'author': book.author,
					'status': book.status
				}
				for book in get_all_books
			]
			return {'books': books}
		except Exception as e:
			print(e)
			nbook.abort(500, status='Could not store information')

	# function to add new books
	@server.api.expect(bparser, validate=True)
	def post(self):
		"""Add a new book - By Simran"""
		try:
			data = bparser.parse_args()
			print(data)
			[print(f'{key} : {data[key]}') for key in data]
			book = bookModel(bid=data['bid'], bname=data['bname'], author=data['author'], status=data['status'])
			db.session.add(book)
			db.session.commit()
			return {'message': f'{book} was added successfully!'}

		except Exception as e:
			print(e)
			nbook.abort(500, status='Could not store information')

	@server.api.expect(bparser1)
	def delete(self):
		"""Delete an existing book - By Simran"""
		try:
			bid = bparser.parse_args()['bid']
			bname = bparser.parse_args()['bname']
			bookname = bookModel.query.filter_by(bid=bid, bname=bname).first()
			db.session.delete(bookname)
			db.session.commit()
			return {'message': f'Book {bookname} was deleted successfully!'}
		except Exception as e:
			print(e)
			nbook.abort(500, message='Book does not exist')

	@server.api.expect(bparser2, validate=True)
	def put(self):
		"""Update details of an existing book - By Simran"""
		try:
			bid = bparser2.parse_args()['bid']
			print(bid)
			bname = bparser2.parse_args()['bname']
			status = bparser2.parse_args()['status']
			UpdateBook = bookModel.query.filter_by(bid=bid).first()
			UpdateBook.bid = bid
			UpdateBook.bname = bname
			UpdateBook.status = status
			db.session.add(UpdateBook)
			db.session.commit()
			return {'message': f'Book {UpdateBook} was updated sucessfully!'}
		except Exception as e:
			print(e)
			nbook.abort(500, status='Could not store information')

@name_space2.route('/admin/book-author', methods=['GET'])
class BookAuthor(Resource):
	# function to get book by name
	@server.api.expect(bparser3)
	def get(self):
		"""Find the book by the respective book author - By Simran"""
		try:
			author = bparser3.parse_args()['author']
			book = bookModel.query.filter_by(bid=bookModel.bid, bname=bookModel.bname, author=author)
			if not book:
				return {'message': f"<No book by '{author}'> is available"}
			else:
				result = [
					{
						'Book-id': b.bid,
						'Book-name': b.bname,
					} for b in book
				]
				return {'Member-Details': result}
		except Exception as e:
			print(e)
			nbook.abort(500, status='Could not store information')
