# author_name : pawan bhosle
# updated_on : 01 November 2021

from flask import request
from namespaces.student_ns import *
from namespaces.book_ns import *
from api_models.member_api_model import a_student
from db_models.member_db import *
from db_models.book_db import *

@name_space.route('/student', methods=['GET', 'POST', 'PUT', 'DELETE'])
class book(Resource):
	def get(self):
		"""To fetch all student requesting for books -by Pawan"""
		try:
			student = studentModel.query.all()
			results = [
				{
					'member_id': stud.member_id,
					'bid': stud.bid,
					'member_name': stud.member_name,
					'book_title': stud.book_title,
					'designation': stud.designation

				} for stud in student
			]
			return {'count': len(results),
			        'student': results}
		except Exception as e:
			print(e)
			name_space.abort(500, status="Could not save information", statusCode="500")

	@api.expect(a_student, validate=True)
	def post(self):
		"""To request for a book -by Pawan"""
		try:
			data = request.get_json()
			[print("distinary is", f'{key}:{data[key]}') for key in data]
			new_student = studentModel(**data)
			db.session.add(new_student)
			db.session.commit()
			return {
				'message': f'student {new_student.member_name} has been successfully added! with book name {new_student.book_title}'}
		except Exception as e:
			print(e)
			name_space.abort(500, status="Could not save information", statusCode="500")

	@api.expect(a_student, validate=True)
	def put(self):
		"""To update your request -by Pawan"""
		try:
			data = request.get_json()
			member_id = args.parse_args()['member_id']
			update_list = studentModel.query.filter_by(member_id=member_id).first()
			update_list.member_id = data['member_id']
			update_list.member_name = data['member_name']
			update_list.book_title = data['book_title']
			update_list.designation = data['designation']
			local_object = db.session.merge(update_list)
			db.session.add(local_object)
			db.session.commit()
			return {'massage': f'studend {update_list.member_name}has been added'}
		except Exception as e:
			print(e)
			name_space.abort(500, status="could not save information", statusCode="500")

	@api.expect(arge, validate=True)
	def delete(self):
		"""to delete your request -by Pawan"""
		try:
			member_id = arge.parse_args()['member_id']
			member_name = arge.parse_args()['member_name']
			student = studentModel.query.filter_by(member_id=member_id).first()
			local_object = db.session.merge(student)
			db.session.delete(local_object)
			db.session.commit()
			return {'result': f'{student.member_name} has been deleted'}
		except Exception as e:
			print(e)
			name_space.abort(500, status="could not save information", statusCode="500")

@name_space.route('/student/student', methods=['GET'])
class select(Resource):
	@api.expect(parser)
	def get(self):
		"""To find the student and book he has -by Pawan"""
		try:
			member_name = parser.parse_args()['member_name']
			# s_title = parser.parse_args()['s_title']
			stud = studentModel.query.filter_by(member_name=member_name).first()
			results = {}
			results['member_id'] = stud.member_id
			results['member_name'] = stud.member_name
			results['book_title'] = stud.book_title
			return {'result': results}
		except Exception as e:
			print(e)
			name_space.abort(500, status="could not save information", statusCode="500")

@name_space2.route('/book', methods=['GET', 'POST', 'PUT', 'DELETE'])
class book_search(Resource):
	@api.expect(par)
	def get(self):
		"""To find that the book of the members choice is present in the library or not -by Pawan"""
		try:
			bname = par.parse_args()['bname']
			book_search1 = bookModel.query.all()
			book_search2 = bookModel.query.filter_by(bname=bname).first()
			for book in book_search1:
				if book.bname == bname:
					print(book.bname)
					results = {}
					results['bid'] = book.bid
					results['bname'] = book.bname
					results['status'] = book.status
					return {'result': results}
			return {'result': f'{bname} book is not present in the library'}

		except Exception as e:
			print(e)
			name_space.abort(500, status="could not save information", statusCode="500")

@name_space2.route('/book_avialable', methods=['GET'])
class books(Resource):
	def get(self):
		"""To get the list of books available in the library -by Pawan"""
		student = bookModel.query.all()
		result = []
		results = {}
		for st in student:
			print(len(student))
			if st.status == "a":
				result.append(st.bname)
				results.update({st.bid: st.bname})

		return {'books avialable in the library': results}

@name_space2.route('/books_not_avialable', methods=['GET'])
class book_na(Resource):
	def get(self):
		"""To get the list of books not available in the library -by Pawan"""
		book_na = bookModel.query.all()
		result = {}
		for book in book_na:
			if book.status == "na":
				result.update({book.bid: book.bname})
		return {'not avialable books': result}

@name_space2.route('/books_with_others', methods=['GET'])
class books_with(Resource):
	@api.expect(pars)
	def get(self):
		"""To find the member who has the book that is not available in the library -by Pawan"""
		try:
			bid = pars.parse_args()['bid']
			book_search = studentModel.query.filter_by(bid=bid).first()
			results = {}
			results['member_name'] = book_search.member_name
			return {'result': results}

		except Exception as e:
			print(e)
			name_space.abort(500, status="could not save information", statusCode="500")

@name_space2.route('/change_status', methods=['put'])
class check(Resource):
	@api.expect(pa, validate=True)
	def put(self):
		"""To chage the status of the book so the no one else put a request for the same book -by Pawan"""
		# data = request.get_json()
		bid = pa.parse_args()['bid']
		status = pa.parse_args()['status']
		update_status1 = bookModel.query.filter_by(bid=bid).first()
		update_status1.status = status
		local_object = db.session.merge(update_status1)
		db.session.add(local_object)
		db.session.commit()
		return {'massage': f'student {update_status1.bname}s status has been modified'}
