from flask_restplus import fields, Namespace


class Book:
	api = Namespace('Books', description='Book-Api')

	name_space2 = Namespace('Search book', description='school APIs')  # Pawan Bhosle


	bmodel = api.model('Book Model', {
		'bid': fields.Integer(required=True, description='book-id', help='this field cannot be empty'),
		'bname': fields.String(required=True, description='book-name', help='this field cannot be empty'),
		'author': fields.String(required=True, description='Name of the author', help='this field cannot be empty'),
		'status': fields.String(required=True, description='availability of the book', help='this field cannot be empty')
	})

