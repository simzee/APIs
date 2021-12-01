import os
from app import blueprint
from app.main import create_app

config_name = os.getenv('FLASK_ENV') or "development"
app = create_app(config_name)
app.register_blueprint(blueprint)
app.app_context().push()

if __name__ == '__main__':
	app.run()
