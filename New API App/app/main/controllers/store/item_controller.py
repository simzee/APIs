# third party imports
from flask_restplus import Resource, reqparse

# local imports
from app.main.util.store.items_dto import ItemApi
from app.main.services.store.item_services import get_all_items, add_item, update_item, delete_item

# parsers
add_item_parser = reqparse.RequestParser()
add_item_parser.add_argument('id', type=int)
add_item_parser.add_argument('name', type=str)
add_item_parser.add_argument('price', type=int)
add_item_parser.add_argument('rack', type=str)
add_item_parser.add_argument('quantity', type=int)

update_item_parser = reqparse.RequestParser()
update_item_parser.add_argument('id', type=int)
update_item_parser.add_argument('name', type=str)
update_item_parser.add_argument('price', type=int)
update_item_parser.add_argument('rack', type=str)
update_item_parser.add_argument('quantity', type=int)

delete_item_parser = reqparse.RequestParser()
delete_item_parser.add_argument('id', type=int)
delete_item_parser.add_argument('name', type=str)

# api call
api = ItemApi.api


@api.route('/items', methods=['GET', 'POST', 'PUT', 'DELETE'])
class Items(Resource):
	def get(self):
		"""Fetch all items in the store"""
		return get_all_items()

	@api.expect(add_item_parser, validate=True)
	def post(self):
		"""Add a new item"""
		return add_item(add_item_parser.parse_args())

	@api.expect(update_item_parser, validate=True)
	def put(self):
		"""Update details of an existing item"""
		return update_item(update_item_parser.parse_args())

	@api.expect(delete_item_parser)
	def delete(self):
		"""Delete an existing item"""
		return delete_item(delete_item_parser.parse_args())
