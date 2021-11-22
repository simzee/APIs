from app.main.models import member_model
from app.main.util.member_dto import MemberUser
from app.main import db

api = MemberUser.api

def fetch_all_members():
	try:
		student = member_model.studentModel.query.all()
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
		api.abort(500, status="Could not save information", statusCode="500")

def request_book(data):
	try:
		[print("distinary is", f'{key}:{data[key]}') for key in data]
		new_student = member_model.studentModel(**data)
		db.session.add(new_student)
		db.session.commit()
		return {
			'message': f'student {new_student.member_name} has been successfully added! with book name {new_student.book_title}'}
	except Exception as e:
		print(e)
		api.abort(500, status="Could not save information", statusCode="500")

def update_request(args, data):
	try:
		member_id = args['member_id']
		update_list = member_model.studentModel.query.filter_by(member_id=member_id).first()
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
		api.abort(500, status="could not save information", statusCode="500")

def delete_request(args):
	try:
		member_id = args['member_id']
		student = member_model.studentModel.query.filter_by(member_id=member_id).first()
		local_object = db.session.merge(student)
		db.session.delete(local_object)
		db.session.commit()
		return {'result': f'{student.member_name} has been deleted'}
	except Exception as e:
		print(e)
		api.abort(500, status="could not save information", statusCode="500")


def fetch_member_with_book(args):
	try:
		member_name = args['member_name']
		stud = member_model.studentModel.query.filter_by(member_name=member_name).first()
		results = {'member_id': stud.member_id, 'member_name': stud.member_name, 'book_title': stud.book_title}
		return {'result': results}
	except Exception as e:
		print(e)
		api.abort(500, status="could not save information", statusCode="500")