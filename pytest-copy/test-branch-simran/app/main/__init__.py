from config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy(app)


def create_app(config_name):
	app.config.from_object(app_config[config_name])
	# app.config.from_pyfile('app.config.py')
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://word:sentence@172.16.2.27:5432/school'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	return app
