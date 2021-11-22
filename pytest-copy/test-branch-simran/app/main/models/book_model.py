from app.main import db

class bookModel(db.Model):
	__tablename__ = 'book'
	bid = db.Column(db.Integer, primary_key=True)
	bname = db.Column(db.String, nullable=False)
	author = db.Column(db.String, nullable=False)
	status = db.Column(db.String, nullable=False)