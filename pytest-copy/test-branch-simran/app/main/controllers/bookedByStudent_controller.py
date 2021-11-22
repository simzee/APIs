from flask_restplus import Resource, reqparse
from app.main.util.member_dto import MemberAdmin
from app.main.services.bookedByStudent_service import all_member_details, member_details_wrt_id, member_details_wrt_designation

api = MemberAdmin.api

# student parser
sparser = reqparse.RequestParser()
sparser.add_argument('member_id', type=int)
sparser.add_argument('member_name', type=str)
sparser.add_argument('book_title', type=str)

sparser1 = reqparse.RequestParser()
sparser1.add_argument('member_id', type=int)
sparser1.add_argument('member_name', type=str)

sparser3 = reqparse.RequestParser()
sparser3.add_argument('designation', type=str)


@api.route('/admin/borrowed-by-member', methods=['GET'])
class BookedByStudents(Resource):
	def get(self):
		"""Member Details - By Simran"""
		return all_member_details()


@api.route('/admin/id-name', methods=['GET'])
class BookedByStudents(Resource):
	@api.expect(sparser1)
	def get(self):
		"""Find the member through their respective id and name - By Simran"""
		return member_details_wrt_id(sparser1.parse_args())


@api.route('/admin/member-designation', methods=['GET'])
class BookedByStudents(Resource):
	@api.expect(sparser3)
	def get(self):
		"""Find the member through their designated post - By Simran"""
		return member_details_wrt_designation(sparser3.parse_args())
