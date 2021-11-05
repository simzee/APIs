# services/student_service.py
# date created : 29-10-2021
# by : Simran Beig

from db_models.student_db import studentModel
from flask_restplus.resource import Resource
from namespaces.student_ns import nstudent, sparser, sparser1, sparser3
from config.instance import server


@nstudent.route('/admin/borrowed-by-member', methods=['GET'])
class BookedByStudents(Resource):
	def get(self):
		"""Member Details - By Simran"""
		try:
			query_member = studentModel.query.order_by(studentModel.member_id.asc())
			result = [
				{
					'Member-id': member.member_id,
					'Member-name': member.member_name,
					'Book-name': member.book_title,
					'Designation': member.designation
				} for member in query_member
			]
			return {'Member-Details': result}
		except Exception as e:
			print(e)
			nstudent.abort(500, status="Error")


@nstudent.route('/admin/id-name', methods=['GET'])
class BookedByStudents(Resource):
	@server.api.expect(sparser1)
	def get(self):
		"""Find the member through their respective id and name - By Simran"""
		try:
			member_id = sparser.parse_args()['member_id']
			member_name = sparser.parse_args()['member_name']
			query_member = studentModel.query.filter_by(member_id=member_id, member_name=member_name).order_by(
				studentModel.member_id.asc())
			if not query_member:
				return {'message': f"No records for student :'{member_name}'"}
			else:
				result = [
					{
						'Member-id': member.member_id,
						'Member-name': member.member_name,
						'Book-name': member.book_title,
						'Designation': member.designation
					} for member in query_member
				]
				return {'Member-Details': result}
		except Exception as e:
			print(e)
			nstudent.abort(500, status="Error")


@nstudent.route('/admin/member-designation', methods=['GET'])
class BookedByStudents(Resource):
	@server.api.expect(sparser3)
	def get(self):
		"""Find the member through their designated post - By Simran"""
		try:
			designation = sparser3.parse_args()['designation']
			query_member = studentModel.query.filter_by(designation=designation).order_by(studentModel.member_id.asc())
			if not query_member:
				return {'message': f"No records for student :'{designation}'"}
			else:
				result = [
					{
						'Member-id': member.member_id,
						'Member-name': member.member_name,
						'Book-name': member.book_title,
						'Designation': member.designation
					} for member in query_member
				]
				return {'Member-Details': result}
		except Exception as e:
			print(e)
			nstudent.abort(500, status="Error")
