# models/instance.py
# date created : 28-10-2021
# by : Simran Beig
# updated by pawan on 03 November 2021

from flask import Flask
from flask_restplus import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

# Load the development "mode". Use "development" if not specified
env = os.environ.get("PYTHON_ENV", "development")

# Configuration for each environment
# Alternatively use "python-dotenv"
all_environments = {
	"development": {"port": 5000, "debug": True, "swagger-url": "/api/swagger"},
	"production": {"port": 8080, "debug": False, "swagger-url": None}
}

# The config for the current environment
environment_config = all_environments[env]

class Server(object):
	def __init__(self):
		self.app = Flask(__name__)
		self.api = Api(self.app)

	def run(self):
		self.app.run(
			debug=environment_config["debug"],
			port=environment_config["port"]
		)

server = Server()

server.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://word:sentence@172.16.2.27:5432/school'
server.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(server.app)
migrate = Migrate(server.app, db)
