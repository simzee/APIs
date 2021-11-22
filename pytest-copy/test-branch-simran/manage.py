from app import blueprint

import os

from app.main import create_app

config_name = os.getenv('PYTHON_ENV') or "development"
app = create_app(config_name)
app.register_blueprint(blueprint)
app.app_context().push()

if __name__ == '__main__':
	app.run()
