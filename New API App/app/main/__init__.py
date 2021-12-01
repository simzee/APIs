# local imports
from instance.config import app_config
import os

# third party imports
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate


env = os.environ.get("PYTHON_ENV", "development")

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()


def create_app(self):
	app.config.from_object(app_config[env])
	db.init_app(app)

	with app.app_context():
		db.create_all()

	login_manager.init_app(app)
	login_manager.login_message = "You must be logged in to access this page."
	login_manager.login_view = ".login"

	return app
