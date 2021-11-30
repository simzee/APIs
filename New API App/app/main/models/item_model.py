from app.main import db


class Item(db.Model):
	__tablename__ = 'item'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	price = db.Column(db.Integer, nullable=False)
	rack = db.Column(db.String, nullable=False)
	quantity = db.Column(db.Integer, nullable=False)
