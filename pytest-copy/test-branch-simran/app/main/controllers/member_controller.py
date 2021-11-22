from flask_restplus import reqparse, Resource
from flask import request

from app.main.util.member_dto import MemberUser

from app.main.services.member_service import fetch_all_members, request_book,\
	update_request, delete_request, fetch_member_with_book

api = MemberUser.api
a_student = MemberUser.a_student

parser = reqparse.RequestParser()
parser.add_argument('member_name', type=str)
parser.add_argument('book_title', type=str)
parser.add_argument('status', type=str)

args = reqparse.RequestParser()
args.add_argument('member_id', type=int)

arge = reqparse.RequestParser()
arge.add_argument('member_id', type=int)
arge.add_argument('member_name', type=str)

@api.route('/student', methods=['GET', 'POST', 'PUT', 'DELETE'])
class book(Resource):
	def get(self):
		"""To fetch all student requesting for books -by Pawan"""
		return fetch_all_members()

	@api.expect(a_student, validate=True)
	def post(self):
		"""To request for a book -by Pawan"""
		data = request.get_json()
		return request_book(data=data)


	@api.expect(a_student, validate=True)
	def put(self):
		"""To update your request -by Pawan"""
		data = request.get_json()
		return update_request(args.parse_args(), data=data)

	@api.expect(arge, validate=True)
	def delete(self):
		"""to delete your request -by Pawan"""
		return  delete_request(arge.parse_args())

@api.route('/student/student', methods=['GET'])
class select(Resource):
	@api.expect(parser)
	def get(self):
		"""To find the student and book he has -by Pawan"""
		return fetch_member_with_book(parser.parse_args())

