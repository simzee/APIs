from app.main import db


class studentModel(db.Model):
	__tablename__ = 'student'
	member_id = db.Column(db.Integer, primary_key=True)
	member_name = db.Column(db.String(300))
	book_title = db.Column(db.String(400))
	designation = db.Column(db.String(200))
