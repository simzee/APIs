from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class RegisterationForm(FlaskForm):
	first_name = StringField('First-Name')
	last_name = StringField('Last-Name')
	email = StringField('Email')
	username = StringField('username')
	password = PasswordField('password')
	confirm_password = PasswordField('Confirm Password')
