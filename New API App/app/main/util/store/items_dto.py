from flask_restplus import fields, Namespace


class ItemApi:
	api = Namespace('Items', description='Item API')

	item_model = api.model('Item-Model', {
		'id': fields.Integer(required=True, description='Item-Id'),
		'name': fields.String(required=True, description='Item-Name'),
		'price': fields.Integer(required=True, description='Item-Price'),
		'rack': fields.String(required=True, description='Rack-name'),
		'quantity_available': fields.Integer(required=True)
	})
