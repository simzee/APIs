from app.main.util.resgistration_dto import RegistrationApi
from app.main.services.registration_service import register

api = RegistrationApi.api

@api.route('/Register', methods=['GET', 'POST'])
def registration():
	return register()