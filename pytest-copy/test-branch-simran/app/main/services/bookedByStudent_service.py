from app.main.util.member_dto import MemberAdmin
from app.main.models import member_model

api = MemberAdmin.api

def all_member_details():
	try:
		query_member = member_model.studentModel.query.order_by(member_model.studentModel.member_id.asc())
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
		api.abort(500, status="Error")

def member_details_wrt_id(args):
	try:
		member_id = args['member_id']
		member_name = args['member_name']
		query_member = member_model.studentModel.query.filter_by(member_id=member_id, member_name=member_name).order_by(
			member_model.studentModel.member_id.asc())
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
		api.abort(500, status="Error")

def member_details_wrt_designation(args):
	try:
		designation = args['designation']
		query_member = member_model.studentModel.query.filter_by(designation=designation).order_by(member_model.studentModel.member_id.asc())
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
		api.abort(500, status="Error")