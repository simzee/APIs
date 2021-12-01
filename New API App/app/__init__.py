# third party imports
from flask import Blueprint
from flask_restplus import Api

# local imports
from app.main.controllers.item_controller import api as item_api

blueprint = Blueprint('api', __name__, url_prefix='/store')

api = Api(blueprint, title='Store', version='1.0', description='API web service')

# add namespaces
api.add_namespace(item_api)
