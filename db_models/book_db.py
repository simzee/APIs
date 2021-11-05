# author_name : pawan bhosle
# updated on : 02 November 2021
from config.instance import db

class bookModel(db.Model):
	__tablename__ = 'book'
	bid = db.Column(db.Integer, primary_key=True)
	bname = db.Column(db.String, nullable=False)
	author = db.Column(db.String, nullable=False)
	status = db.Column(db.String, nullable=False)

	def __init__(self, bid, bname, author, status):
		self.bid = bid
		self.bname = bname
		self.author = author
		self.status = status

	def __repr__(self):
		return f"<Book-id:{self.bid}, Book-Name:{self.bname}, Book-author:{self.author}, Book-status:{self.status}>"
