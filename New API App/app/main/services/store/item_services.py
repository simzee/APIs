# local imports
from app.main.models.item_model import Item
from app.main import db


def get_all_items():
	# import pdb
	# pdb.set_trace()

	get_items = Item.query.order_by(Item.id.asc())

	items = [
		{
			'id': item.id,
			'name': item.name,
			'price': item.price,
			'rack': item.rack,
			'quantity': item.quantity
		} for item in get_items
	]

	all_items = {'All Items': items}
	return all_items


def add_item(args):
	data = args
	item = Item(id=data['id'], name=data['name'], price=data['price'], rack=data['rack'], quantity=data['quantity'])
	db.session.add(item)
	db.session.commit()
	return {'message': f'{item} was added successfully!'}


def update_item(args):
	data = args

	iid = data['id']
	name = data['name']
	price = data['price']
	quantity = data['quantity']

	item_updated = Item.query.filter_by(name=name).first()
	item_updated.id = iid
	item_updated.name = name
	item_updated.price = price
	item_updated.quantity = quantity

	db.session.add(item_updated)
	db.session.commit()

	return {'message': f'{item_updated} updated successfully!'}


def delete_item(args):
	data = args

	iid = data['id']
	name = data['name']

	item_deleted = Item.query.filter_by(id=iid, name=name).first()

	db.session.delete(item_deleted)
	db.session.commit()

	return {'message': f'{item_deleted} is deleted successfully!'}