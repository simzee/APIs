from app.main.models import book_model
from app.main.util.book_dto import Book
from app.main import db

api = Book.api


def get_all_book_details():
	try:
		get_all_books = book_model.bookModel.query.order_by(book_model.bookModel.bid.asc())
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
		api.abort(500, status='Could not store information')


def add_book(args):
	try:
		data = args
		print(data)
		[print(f'{key} : {data[key]}') for key in data]
		book = book_model.bookModel(bid=data['bid'], bname=data['bname'], author=data['author'], status=data['status'])
		db.session.add(book)
		db.session.commit()
		return {'message': f'{book} was added successfully!'}

	except Exception as e:
		print(e)
		api.abort(500, status='Could not store information')


def delete_book(args):
	try:
		bid = args['bid']
		bname = args['bname']
		bookname = book_model.bookModel.query.filter_by(bid=bid, bname=bname).first()
		db.session.delete(bookname)
		db.session.commit()
		return {'message': f'Book {bookname} was deleted successfully!'}
	except Exception as e:
		print(e)
		api.abort(500, message='Book does not exist')


def update_existing_book_details(args):
	try:
		bid = args['bid']
		print(bid)
		bname = args['bname']
		status = args['status']
		UpdateBook = book_model.bookModel.query.filter_by(bid=bid).first()
		UpdateBook.bid = bid
		UpdateBook.bname = bname
		UpdateBook.status = status
		db.session.add(UpdateBook)
		db.session.commit()
		return {'message': f'Book {UpdateBook} was updated sucessfully!'}
	except Exception as e:
		print(e)
		api.abort(500, status='Could not store information')


def find_book_by_author(args):
	try:
		author = args['author']
		book = book_model.bookModel.query.filter_by(bid=book_model.bookModel.bid, bname=book_model.bookModel.bname, author=author)
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
		api.abort(500, status='Could not store information')
