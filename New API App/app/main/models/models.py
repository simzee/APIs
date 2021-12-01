# local imports
from app.main import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class Item(db.Model):
	__tablename__ = 'item'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	price = db.Column(db.Integer, nullable=False)
	rack = db.Column(db.String, nullable=False)
	quantity = db.Column(db.Integer)


class Role(db.Model):
	"""
	Create a Role table
	"""

	__tablename__ = 'roles'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True)
	description = db.Column(db.String(200))
	users = db.relationship('Employee', backref='role', lazy='dynamic')


class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(60), index=True, unique=True)
	username = db.Column(db.String(60), index=True, unique=True)
	first_name = db.Column(db.String(60), index=True)
	last_name = db.Column(db.String(60), index=True)
	password_hash = db.Column(db.String(128))
	item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	@property
	def password(self):
		"""
		Prevent password from being accessed
		"""
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):
		"""
		Set password to a hashed password
		"""
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		"""
		Check if hashed password matches actual password
		"""
		return check_password_hash(self.password_hash, password)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
