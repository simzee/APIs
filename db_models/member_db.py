# author_name : pawan bhosle
# updated on : 02 November 2021
from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://word:sentence@172.16.2.27:5432/school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class studentModel(db.Model):
	__tablename__ = 'student'
	member_id = db.Column(db.Integer, primary_key=True)
	bid = db.Column(db.Integer)
	member_name = db.Column(db.String(300))
	book_title = db.Column(db.String(400))
	designation = db.Column(db.String(500))

	def __init__(self, member_id, bid, member_name, book_title, designation):
		self.member_id = member_id
		self.bid = bid
		self.member_name = member_name
		self.book_title = book_title
		self.designation = designation

	def __repr__(self):
		return f"<student {self.member_name},{self.book_title}>"
