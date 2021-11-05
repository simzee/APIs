# api_models/book_api_model.py
# date created : 28-10-2021
# by : Simran Beig
# update by pawan on 03 november 2021

from flask_restplus import fields
from namespaces.book_ns import nbook

# book model
bmodel = nbook.model('Book Model', {
	'bid': fields.Integer(required=True, description='book-id', help='this field cannot be empty'),
	'bname': fields.String(required=True, description='book-name', help='this field cannot be empty'),
	'author': fields.String(required=True, description='Name of the author', help='this field cannot be empty'),
	'status': fields.String(required=True, description='availability of the book', help='this field cannot be empty')
})

