# db_models/student_db.py
# date created : 28-10-2021
# by : Pawan Bhosle
# updated by : Simran Beig

from config.instance import *

class studentModel(db.Model):
	__tablename__ = 'student'
	member_id = db.Column(db.Integer, primary_key=True)
	member_name = db.Column(db.String(300))
	book_title = db.Column(db.String(400))
	designation = db.Column(db.String(200))
