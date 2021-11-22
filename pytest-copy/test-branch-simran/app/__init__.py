from flask import Blueprint
from flask_restplus import Api
from app.main.controllers.book_search_controller import api as book_search
from app.main.controllers.book_controller import api as book_services
from app.main.controllers.bookedByStudent_controller import api as booked_by_student
from app.main.controllers.member_controller import api as member_service

blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='Library', version='1.0', description='API web service')

# adding namespace for swagger
api.add_namespace(book_search)
api.add_namespace(book_services)
api.add_namespace(booked_by_student)
api.add_namespace(member_service)