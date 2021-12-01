from app.main import db
from flask import render_template, flash, redirect
from app.main.forms.registration_form import RegisterationForm
from app.main.models.models import User


def register():
	form = RegisterationForm()

	if form.validate_on_submit():
		user = User(
			first_name = form.first_name.data,
			last_name = form.last_name.data,
			email = form.email.data,
			username = form.username.data,
			password = form.password.data
		)

		db.session.add(user)
		db.session.commit()
		flash('You have successfully registered! You may now login.')

		return redirect('login.html')

	return render_template('registration.html')