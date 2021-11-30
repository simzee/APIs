from instance.config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

env = os.environ.get("PYTHON_ENV", "development")

app = Flask(__name__)
db = SQLAlchemy()


def create_app():
	app.config.from_object(app_config[env])
	db.init_app(app)

	with app.app_context():
		db.create_all()

	return app
