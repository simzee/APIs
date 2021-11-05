# api_models/member_api_model.py
# date created : 28-10-2021
# by : Pawan Bhosle

from config.instance import server
from flask_restplus import fields
from namespaces.student_ns import nstudent

a_student = server.api.model('student', {
	'member_id': fields.Integer(required=True, description='student Id', help='This field cannot be empty'),
	'bid': fields.Integer(reuired=True, description='book id', help='this field cannot be empty'),
	'member_name': fields.String(required=True, description='book name', help='This field cannot be empty'),
	'book_title': fields.String(required=True, description='author name', help='This field cannot be empty'),
	'designation': fields.String(requored=True, description="designation", help='this field is required')
})

# date created : 28-10-2021
# by : Simran Beig
smodel = nstudent.model('Student-Model', {
	'member_id': fields.Integer(required=True, description='student id', help='this field cannot be empty'),
	'member_name': fields.String(required=True, description='student name', help='this field cannot be empty'),
	'status': fields.String(descripton='status of the book taken', help='Available or not')
})
