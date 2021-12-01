from app.main.util.book_dto import Book
from app.main.models import book_model
from app.main.models import member_model
from app.main import db

api = Book.name_space2


def check_if_book_is_present(args):
	try:
		bname = args['bname']
		book_search1 = book_model.bookModel.query.all()
		for book in book_search1:
			if book.bname == bname:
				print(book.bname)
				results = {'bid': book.bid, 'bname': book.bname, 'status': book.status}
				return {'result': results}
		return {'result': f'{bname} book is not present in the library'}
	except Exception as e:
		print(e)
		api.abort(500, status="could not save information", statusCode="500")


def get_list_of_available_books():
	student = book_model.bookModel.query.all()
	result = []
	results = {}
	for st in student:
		print(len(student))
		if st.status == "a":
			result.append(st.bname)
			results.update({st.bid: st.bname})

	return {'books avialable in the library': results}


def get_list_of_books_not_available():
	book_na = book_model.bookModel.query.all()
	result = {}
	for book in book_na:
		if book.status == "na":
			result.update({book.bid: book.bname})
	return {'not available books': result}


def member_with_book_not_avialable_in_library(args):
	try:
		bid = args['bid']
		book_search = member_model.studentModel.query.filter_by(bid=bid).first()
		results = {'member_name': book_search.member_name}
		return {'result': results}
	except Exception as e:
		print(e)
		api.abort(500, status="could not save information", statusCode="500")


def change_status_of_book(args):
	bid = args['bid']
	status = args['status']
	update_status1 = book_model.bookModel.query.filter_by(bid=bid).first()
	update_status1.status = status
	local_object = db.session.merge(update_status1)
	db.session.add(local_object)
	db.session.commit()
	return {'massage': f'student {update_status1.bname}s status has been modified'}